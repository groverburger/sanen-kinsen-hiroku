# Transcription Conventions

This folder contains a character-level transcription (翻刻, *honkoku*) of the
manuscript images in `../original-manuscript/`. Each file corresponds to one or
more page-images and records the Japanese text as read from the cursive script,
with confidence annotations.

## Purpose

This transcription serves as the auditable intermediate step between the
manuscript images and the English translation in `../translation/`. Any reading
of the original that informs the English text should be traceable to a specific
line here.

## Page numbering

"Page" numbers refer to image file numbers (`page_00001.jpg` = page 1, etc.).
Each image except the cover and back cover shows a two-page spread (right page
and left page of the open book). Within each file, text is presented in reading
order: right page first, then left page; within each page, columns are read
right to left, top to bottom.

## Confidence markup

| Markup | Meaning |
|--------|---------|
| 米 | Confident reading |
| 米(?) | Best-guess reading; character is plausible but not certain |
| [米/来] | Two or more equally plausible readings |
| □ | Illegible character (shape visible but unreadable) |
| ■ | Missing or destroyed (paper damaged, text lost) |
| (...) | Omitted passage (e.g., repeated text, standard colophon) |
| 〈note〉 | Inline editorial note about the reading |

## Confidence ratings

Each section is tagged with an overall confidence level:

- **HIGH** — Characters are clearly legible in the image; reading is
  unambiguous.
- **MEDIUM** — Most characters legible; some require contextual inference or
  are partially obscured. Reasonable readers might disagree on 1-3 characters.
- **LOW** — Significant portions are in dense cursive, damaged, or faded.
  The transcription is a best-effort reconstruction. Multiple alternative
  readings are possible.

## Text formatting

- Section headers visible in the manuscript (often in larger characters or
  with circle markers ◯) are set on their own line and prefixed with `###`.
- Red-ink annotations or markings in the original are noted as
  `〈red ink〉` or `〈red circle marker〉`.
- Kundoku reading marks (返り点, 送り仮名) visible in the manuscript are
  noted where they affect the reading but are not individually transcribed.
- Modern punctuation (、。) is added for readability; the original manuscript
  has none.

## Relationship to other folders

- `../original-manuscript/page_XXXXX.jpg` — source image for each transcription
- `../translation/pages_XX-XX.md` — English translation derived from this transcription
- `../sanen-kinsen-hiroku.tex` — final typeset edition
