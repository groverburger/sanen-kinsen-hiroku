# Sanen Kinsen Hiroku (三猿金泉秘録)

**The First English Translation of the Three Monkeys Gold Spring Secret Record**

An Edo-period Japanese manuscript on the art of rice market speculation, attributed to Ushida Gonzaburō (牛田権三郎), revised by Narukawa Takenosuke (鳴川猛之助). Translated directly from the 1851 manuscript held at Kyoto University (Record ID: [RB00012360](https://rmda.kulib.kyoto-u.ac.jp/item/rb00012360)).

Edited and produced by Zach Booth. Translated with AI assistance (Claude Opus 4.6, Anthropic).

## Why This Translation Exists

For thirty-five years, English-language traders have searched for this text under the wrong name, attributed to the wrong author. The *Sanen Kinsen Hiroku* has been consistently misattributed to Honma Munehisa of Sakata in Western trading literature, beginning with Steve Nison's *Japanese Candlestick Charting Techniques* (1991). Two English books have been published under variations of this text's title. Neither translates it — both render a separate body of trading maxims from the Honma/Sakata tradition while putting Ushida's title on the cover.

In Japanese scholarship, the authorship is unambiguous: the National Diet Library, CiNii, Kyoto University's digital archive, and sources from Honma's own hometown all attribute the *Sanen Kinsen Hiroku* to Ushida Gonzaburō. The confusion exists almost exclusively in English.

This project produces the first English translation of the actual text, from an identified manuscript with real provenance.

## How the Translation Was Produced

### Methodology

The translation was produced using [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Anthropic's CLI agent) powered by **Claude Opus 4.6**, which has strong multimodal capabilities for reading historical Japanese cursive script (草書/kuzushiji).

The workflow evolved through two phases:

**Phase 1: Direct translation.** Claude Opus 4.6 read each manuscript page image and produced English translations directly. This yielded usable drafts but conflated two distinct tasks — character recognition and meaning interpretation — making errors difficult to trace and audit.

**Phase 2: Transcription then translation.** We separated the process into two explicit stages:

1. **Transcription** (`./transcription/`): Claude reads each manuscript page and outputs the Japanese characters it can identify, with confidence levels (HIGH/MEDIUM/LOW) for each reading. Illegible characters are marked rather than guessed.
2. **Translation** (`./translation/`): Working from the transcription (not directly from the images), Claude produces English translations. This makes every editorial decision traceable — a reader can check the transcription against the original image, then check the translation against the transcription.

This separation produced more consistent, more auditable results. When a translation error is found, you can determine whether the problem was a misread character or a misinterpreted meaning.

### Adversarial Grading (GAN-Inspired Iteration)

To improve quality iteratively, we used a technique inspired by Generative Adversarial Networks (GANs) from the 2010s deep learning era: a separate, context-free Claude Opus 4.6 instance grades the work using the prompt:

> "Grade ./sanen-kinsen-hiroku.pdf (and the LaTeX source document) as a standalone document"

This external reviewer has no knowledge of our process, goals, or prior conversations — it evaluates the output cold, as a reader would. Its feedback is then incorporated by the production instance (Claude Code), creating an iterative improvement loop:

1. **Generator** (Claude Code): produces the translation and LaTeX document
2. **Discriminator** (independent Claude instance): grades the output, identifies weaknesses
3. **Iteration**: the generator incorporates the feedback and resubmits

This cycle was repeated multiple times, catching fabricated content, arithmetic errors, misattributions, bibliography inaccuracies, layout problems, and omitted source material that the production instance had missed. The technique proved remarkably effective at surfacing blind spots.

### What Claude Opus 4.6 Does Well

- **Reading kuzushiji**: Claude Opus 4.6 can read Edo-period cursive Japanese script directly from manuscript images with reasonable accuracy, identifying kanji, kana, and structural elements (section markers, diagram labels, numerical tables).
- **Bilingual apparatus**: Consistent inline glossing of Japanese terms with kanji, romanization, and English throughout.
- **Scholarly footnotes**: Contextualizing Edo-period concepts for modern readers (e.g., connecting the three-phase decline pattern to Dow Theory, identifying the Zhou Dunyi cosmological framework).
- **LaTeX typesetting**: Professional book production with XeLaTeX, including CJK font handling, figure placement, and cross-references.

### What Required Human Judgment

- **Editorial decisions**: What to include, what to summarize, how to structure chapters, when to admit uncertainty.
- **Accuracy verification**: Checking AI-generated translations against the manuscript images, catching fabricated content and arithmetic that didn't add up.
- **Attribution research**: The misattribution story required independent research into Nison's books, Japanese library catalogs, and the Honma/Ushida distinction.
- **Source identification**: Finding the manuscript in Kyoto University's digital archive and recognizing its significance.

## Repository Structure

```
sanen-kinsen-hiroku.tex    # LaTeX source (compile with XeLaTeX)
original-manuscript/       # 33 page scans from Kyoto University RMDA
  page_00001.jpg           #   (RB00012360, Tanimura Collection)
  ...
  page_00033.jpg
transcription/             # Character-by-character Japanese transcription
  CONVENTIONS.md           #   with confidence levels (HIGH/MEDIUM/LOW)
  pages_01-02.md
  ...
translation/               # English translation (from transcription)
  pages_01-02_cover_and_title.md
  ...
diagrams/                  # Cleaned-up crops of manuscript diagrams
  fig1_tree_positions.png
  fig2_tree_scaling.png
  diagram_three_levels.png
  diagram_grand_chart.png
```

## Building the PDF

Requires XeLaTeX with the following fonts installed:
- Noto Serif / Noto Serif Bold / Noto Serif Italic / Noto Serif Bold Italic
- Noto Serif JP
- Noto Sans JP (used as Japanese bold fallback)

```bash
xelatex sanen-kinsen-hiroku.tex
xelatex sanen-kinsen-hiroku.tex  # twice for cross-references
```

## Source Manuscript

**Record**: 校正三猿金泉秘録 (Kōsei Sanen Kinsen Hiroku)
**Record ID**: RB00012360
**Collection**: Tanimura Collection (谷村文庫), Main Library, Kyoto University
**Date**: Kaei 4 (嘉永四年五月廿日; 1851)
**Publisher**: Kōmondō (好問堂蔵版), Igarashi-tsu (五十嵐津)
**Digital Archive**: https://rmda.kulib.kyoto-u.ac.jp/item/rb00012360
**License**: Free with Attribution (二次利用自由・所蔵表示)

All manuscript images courtesy of the Main Library, Kyoto University.
所蔵：京都大学附属図書館

## License

The source manuscript images are provided under Kyoto University's free-with-attribution license. See [reuse policy](https://rmda.kulib.kyoto-u.ac.jp/reuse).
