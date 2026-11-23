# Design Specification

## Canvas

- 16:9 widescreen, 13.333 × 7.5 in.
- Side margins 0.6 in. Title band 1.1 in high. Body follows a 12-column grid with at least 0.3 in gutters.
- One idea per slide. If a slide needs more than six bullet rows, split it.

## Typography

- Slide title 28–36 pt, bold, written as a conclusion rather than a label.
- Body 18–24 pt. Captions and sources 10–12 pt.
- Use at most two font families. Chinese usually needs an explicit CJK fallback such as Microsoft YaHei or Source Han Sans; English can use Aptos or Arial.
- Keep a single size for the same role across the whole deck.

## Color

- White or very light gray background.
- One primary color, one accent color, two neutrals. Avoid more than four hues.
- Solid fills only. No gradients, 3D bevels, glow, or decorative shadows.
- Encode meaning consistently: the same color never changes meaning between slides.

## Text blocks

- Maximum six lines per text box and about 40 Chinese characters per line.
- Prefer short phrases over full sentences in bullets.
- Leave at least 0.2 in padding inside every shape. Never let text touch a border.

## Charts and tables

- No 3D charts, no pie charts with more than five slices.
- Sort bars by value unless the order carries meaning. Label values directly instead of relying on a legend where possible.
- Keep units in the chart title. Round consistently; do not mix 12.3% and 12%.
- Tables: header row filled with primary color, alternating light row fills, right-align numbers.

## Images

- Use raster images at least 1600 px wide for a full slide, 600 px for a half slide.
- Crop to content. Remove watermarks and unrelated UI chrome before placing.
- Do not stretch images beyond their original aspect ratio.

## Standard page types

Cover, agenda, section divider, content, comparison, data, process, summary, closing. Reuse the same master for each type so the deck reads as one document.

## Failure modes to avoid

- Title smaller than body text.
- Bullet lists longer than six items.
- Icons used as decoration without carrying information.
- Numbers without a source or unit.
- A final slide that says only "Thank you" instead of restating the conclusion.
