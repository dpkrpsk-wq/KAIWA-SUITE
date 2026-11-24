# KAIWA SUITE: prompt block for 10 second videos (Gemini)

Paste this text into Gemini for every video in the series. The fixed part keeps the look of the series. The episode field describes what happens in one video. The values come from `design/design-system/tokens.css`, `design/logo/themes.json` and the logo description in the KAIWA SUITE design system (Claude Design).

## Fixed part (paste)

```text
A 10 second video, one continuous shot without cuts, no speech.
Format: 16:9, 1920 x 1080. Portrait variant: 9:16, 1080 x 1920.

Style: flat graphics, sharp edges, hard shapes. No gradients, no blur, no soft shadows, no light effects, no texture. Shadows only as a hard 6 px offset down and to the right, in the text colour.

Colours (hex), only these:
background #F1EFE9 (paper) or #14171F (ink),
shapes and lines #14171F on the light background, #F1EFE9 on the dark background,
signal #FFED00 (yellow) only as stripes, patches and the square in the mark, never as the background of the whole frame,
green state #3FB97A only in the small square of the mark, and only when a state is shown.

The KAIWA "K." mark: a dark tile with rounded corners (radius 15 percent of the side). On it a large letter K with straight, hard edges in #F1EFE9, and at the foot of the K, to the right of its leg, a small yellow square #FFED00 (state indicator). Nothing else is on the tile.

Motion: the K holds still. The square appears with a hard cut, then switches on and off twice with hard cuts, without fading. The stripes at 35 degrees run once across the frame from left to right in steps, without smooth blur. In the last second the frame holds on the still mark in the centre, with free space around it (at least a quarter of the side of the mark).

Signal stripes: parallel #FFED00 stripes at 35 degrees, hard edges, fixed widths.

Show no letters or lettering in the image. Do not rotate, stretch or recolour the mark.
```

## Episode field

```text
Episode topic: [one sentence on what this video shows]
Background: [paper #F1EFE9 | ink #14171F]
Colour mode of the mark: [black and white (default) | spectrum | SHIFT]
```

The spectrum and SHIFT modes have their own colours for the horizontal stripes of the tile. List: `design/logo/themes.json`. In the spectrum and SHIFT modes the K and the square are #14171F and the square shows no state.

## After generating

- Add the lettering KAIWA SUITE (capitals) and the episode number in editing, not in the generator. That way the letters match the system.
- Check every colour in the list on the first and the last frame.
- Compare the mark on the last frame with `design/logo/kaiwa-icon.svg`. If the shape differs, generate the video again or end it with the mark file.

| Name | Hex | Use in the video |
|---|---|---|
| `tinte` (ink) | #14171F | dark background, shapes on the light background |
| `papier` (paper) | #F1EFE9 | light background, shapes on the dark background |
| `signal` | #FFED00 | stripes at 35 degrees |
| `status-aktiv` | #3FB97A | state square, black and white mode only, only when a state is shown |
