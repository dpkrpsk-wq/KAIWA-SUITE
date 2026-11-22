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
signal #FFED00 (yellow) only as stripes and patches, never as the background of the whole frame,
tunnel core #07080C,
green state #3FB97A only in the small square at the bottom right.

The KAIWA, warp mode mark: a dark tile with rounded corners (radius 15 percent of the side). On it a tunnel of six nested ellipses with uneven gaps and varying line weight, with a dark core. An octopus swims towards the tunnel: a body with fins pointing at the tunnel, six arms with round tips trailing behind, one eye. Behind the octopus two pale copies as an echo. At the bottom right of the tile a small square (state indicator).

Warp mode motion: the octopus swims along a straight line at 35 degrees up and to the right, towards the tunnel. The echo follows at fixed distances. The ellipses of the tunnel come closer in steps, without smooth blur. At the end the octopus enters the dark core. In the last second the frame holds on the still mark in the centre, with free space around it (at least a quarter of the side of the mark).

Signal stripes: parallel #FFED00 stripes at 35 degrees, hard edges, fixed widths.

Show no letters or lettering in the image. Do not rotate, stretch or recolour the mark.
```

## Episode field

```text
Episode topic: [one sentence on what this video shows]
Background: [paper #F1EFE9 | ink #14171F]
Colour mode of the mark: [black and white (default) | spectrum | SHIFT]
```

The spectrum and SHIFT modes have their own colours for stripes, rings and echo. List: `design/logo/themes.json`. In the spectrum and SHIFT modes the square is #14171F and shows no state.

## After generating

- Add the lettering KAIWA SUITE (capitals) and the episode number in editing, not in the generator. That way the letters match the system.
- Check every colour in the list on the first and the last frame.
- Compare the mark on the last frame with `design/logo/kaiwa-icon.svg`. If the shape differs, generate the video again or end it with the mark file.

| Name | Hex | Use in the video |
|---|---|---|
| `tinte` (ink) | #14171F | dark background, shapes on the light background |
| `papier` (paper) | #F1EFE9 | light background, shapes on the dark background |
| `signal` | #FFED00 | stripes at 35 degrees |
| core | #07080C | centre of the tunnel |
| `status-aktiv` | #3FB97A | state square, black and white mode only |
