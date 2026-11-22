#!/usr/bin/env python3
"""Dictation ledger: a hashed record of every dictated contribution in a local journal folder.

Part of the KAIWA package by Denis Pokropski (BA in philosophy, University of Wrocław 2019, master's student, College of Interdisciplinary Individual Studies KMSI, University of Wrocław, contact 285421@student.uwr.edu.pl). Draft, not yet released.
Needs only the Python standard library (3.8 or newer). Nothing leaves your computer.

Commands
  python dictation_ledger.py probe
      Prints the SHA-256 of the text "abc" and checks it against the known value. Run it yourself to know that it ran.
      An AI model that reports OK has not proven that it executed code. A model that cannot run code must not invent hashes.
  python dictation_ledger.py init ARCHIVE
      Creates ARCHIVE/journal/ and an empty ARCHIVE/ledger.jsonl. Safe to run twice.
  python dictation_ledger.py scan ARCHIVE [--now 2026-11-05T08:00:00Z]
      Reads ARCHIVE/journal/YYYY-MM-DD.md and appends every new dictated contribution to ARCHIVE/ledger.jsonl.
      Existing lines are never changed. Prints how many records were added.
  python dictation_ledger.py verify ARCHIVE
      Checks every record against the journal. Reports records whose text changed or disappeared.
      Exit 0 = all records found unchanged, exit 1 = findings.

What counts as a contribution: a line with a verbatim marker followed by a quoted text, for example
  Verbatim (dictated): "..."       Dosłownie (dyktowane): „...”       Wortlaut (diktiert): „...“
A verbatim line after "Addendum (HH:MM)" (or "Uzupełnienie", "Nachtrag") in the same entry is an addendum with that
time. An entry starts with a bold heading that carries the time, for example **Freedom and critique (23:41)**.
A session starts with a heading such as "### Dictation Stream of Consciousness 23:40, session abc123" and may
name "10 min", "goal <id>", "level <id>". Polish and German keywords work too (see SECTION_WORDS). The mode
"stream-of-consciousness" was called "stream" (also "strumień", "Strom") until 2026-11-08; old headings still read
as the same mode.

What the ledger stores: date, time, file, line, form, SHA-256 of the text, number of characters and words, and the
session fields. It never stores the text itself. The text stays in your journal. The hash shows later that it is
unchanged. Hash rule: Unicode NFC, all whitespace collapsed to one space, trimmed, then SHA-256 of the UTF-8 bytes.
Same journal and same --now give the same bytes.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import unicodedata

KNOWN_ABC = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
DAYFILE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.md$")
HEADING = re.compile(r"^#{1,3} ")
ENTRY = re.compile(r"^\*\*(.+)\*\*\s*$")
TIME = re.compile(r"\((?:[^)]*?\b)?(\d\d):(\d[\dx])\b")
VERBATIM = re.compile(r"(?:Verbatim \(dictated|Dosłownie \(dyktowane|Wortlaut \(diktiert)[^)]*\):\s*[„“\"«](.*)$")
CLOSE = re.compile(r"[“”\"»]")
ADDENDUM = re.compile(r"^(?:Addendum|Uzupełnienie|Nachtrag) \((\d\d:\d\d)")
SECTION = re.compile(r"^### (?:Dictation|Dyktowanie|Diktat)[ -](.+?) (\d\d:\d\d)\b(.*)$", re.IGNORECASE)
SOC = "stream-of-consciousness"
SECTION_WORDS = {
    "mode": {"stream of consciousness": SOC, "strumień świadomości": SOC,
             "stream": SOC, "strumień": SOC, "strom": SOC,          # names until 2026-11-08
             "sprint": "sprint",
             "transfer": "transfer", "przekład": "transfer", "übertragung": "transfer"},
    "goal": ("goal", "cel", "ziel"),
    "level": ("level", "poziom", "stufe"),
    "session": ("session", "sesja", "sitzung"),
}


def normalized(text):
    return " ".join(unicodedata.normalize("NFC", text).split())


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def section_fields(rest):
    fields = {"minutes": None, "goal": None, "level": None, "session": None}
    for part in (p.strip() for p in rest.split(",")):
        m = re.fullmatch(r"(\d+) (?:min|minutes|minut|Minuten)", part)
        if m:
            fields["minutes"] = int(m.group(1))
            continue
        words = part.split(" ", 1)
        if len(words) == 2:
            for key in ("goal", "level", "session"):
                if words[0].lower() in SECTION_WORDS[key]:
                    fields[key] = words[1].strip()
    return fields


def read_day(date, text, filename):
    """Returns (contributions, unclosed) for one day file."""
    found, unclosed = [], 0
    section, entry_time, entry_approx, addendum_time = {}, None, False, None
    for nr, line in enumerate(text.splitlines(), 1):
        if HEADING.match(line):
            m = SECTION.match(line)
            section = {}
            if m:
                section = {"mode": SECTION_WORDS["mode"].get(m.group(1).lower(), m.group(1).lower()),
                           "start": m.group(2), **section_fields(m.group(3))}
            entry_time, entry_approx, addendum_time = None, False, None
            continue
        m = ENTRY.match(line)
        if m:
            t = TIME.search(m.group(1))
            entry_time = "%s:%s" % t.groups() if t else None
            entry_approx = bool(t and "x" in t.group(2))
            addendum_time = None
            continue
        m = ADDENDUM.match(line)
        if m:
            addendum_time = m.group(1)
        m = VERBATIM.search(line)
        if not m:
            continue
        rest = m.group(1)
        closes = list(CLOSE.finditer(rest))
        if not closes:
            unclosed += 1
            continue
        words = normalized(rest[:closes[-1].start()])
        form, time, approx = ("addendum", addendum_time, False) if addendum_time else ("verbatim", entry_time, entry_approx)
        digest = sha(words)
        found.append({"id": sha("%s|%s|%s" % (date, time or "", digest))[:16], "date": date, "time": time,
                      "time_approx": approx, "file": filename, "line": nr, "form": form, "sha256": digest,
                      "chars": len(words), "words": len(words.split()), "mode": section.get("mode"),
                      "session_start": section.get("start"), "minutes": section.get("minutes"),
                      "goal": section.get("goal"), "level": section.get("level"), "session": section.get("session")})
    return found, unclosed


def read_journal(archive):
    journal = os.path.join(archive, "journal")
    if not os.path.isdir(journal):
        raise FileNotFoundError("no journal folder: %s (run init first)" % journal)
    found, unclosed, seen = [], 0, {}
    for name in sorted(os.listdir(journal)):
        m = DAYFILE.match(name)
        if not m:
            continue
        with open(os.path.join(journal, name), encoding="utf-8", errors="replace") as f:
            day, open_ = read_day(m.group(1), f.read(), "journal/" + name)
        unclosed += open_
        for c in day:      # same sentence, same minute, same day: number the repeats in file order
            n = seen.get(c["id"], 0) + 1
            seen[c["id"]] = n
            if n > 1:
                c["id"] = "%s-%d" % (c["id"], n)
        found += day
    return found, unclosed


def read_ledger(archive):
    path = os.path.join(archive, "ledger.jsonl")
    if not os.path.isfile(path):
        raise FileNotFoundError("no ledger: %s (run init first)" % path)
    with open(path, encoding="utf-8") as f:
        return [json.loads(z) for z in f if z.strip()]


def utc(now):
    if now:
        t = dt.datetime.fromisoformat(now.replace("Z", "+00:00"))
        t = t.astimezone(dt.timezone.utc) if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)
    else:
        t = dt.datetime.now(dt.timezone.utc)
    return t.replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")


def cmd_init(archive):
    os.makedirs(os.path.join(archive, "journal"), exist_ok=True)
    path = os.path.join(archive, "ledger.jsonl")
    if not os.path.exists(path):
        open(path, "w", encoding="utf-8").close()
    print("archive ready: %s" % os.path.abspath(archive))
    return 0


def cmd_scan(archive, now):
    found, unclosed = read_journal(archive)
    known = {r["id"] for r in read_ledger(archive)}
    stamp = utc(now)
    new = [dict(c, recorded_utc=stamp) for c in found if c["id"] not in known]
    with open(os.path.join(archive, "ledger.jsonl"), "a", encoding="utf-8", newline="\n") as f:
        for r in new:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
    print("contributions in journal: %d, added to ledger: %d, unclosed quotes: %d" % (len(found), len(new), unclosed))
    return 0


def cmd_verify(archive):
    found = {c["id"]: c for c in read_journal(archive)[0]}
    findings = 0
    for r in read_ledger(archive):
        c = found.get(r["id"])
        if c is None:
            findings += 1
            print("changed or removed: %s %s %s line %s" % (r["date"], r["time"], r["file"], r["line"]))
    print("ledger records: %d, findings: %d" % (len(read_ledger(archive)), findings))
    return 1 if findings else 0


def cmd_probe():
    value = sha("abc")
    ok = value == KNOWN_ABC
    print("sha256(abc) = %s %s" % (value, "OK" if ok else "WRONG"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("probe")
    for name in ("init", "verify"):
        sub.add_parser(name).add_argument("archive")
    s = sub.add_parser("scan")
    s.add_argument("archive")
    s.add_argument("--now", default=None)
    a = ap.parse_args(argv)
    try:
        if a.cmd == "probe":
            return cmd_probe()
        if a.cmd == "init":
            return cmd_init(a.archive)
        if a.cmd == "scan":
            return cmd_scan(a.archive, a.now)
        return cmd_verify(a.archive)
    except (OSError, ValueError) as e:
        print("error: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
