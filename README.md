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

<details>
<summary>Example grader output (click to expand)</summary>

```
Grade: A-

Category Grades:

| Category                       | Grade |
|--------------------------------|-------|
| Scholarly rigor & attribution  | A+    |
| Translation quality & voice    | A     |
| Editorial transparency         | A     |
| Typography & design            | A-    |
| Front/back matter completeness | A-    |
| Internal structure & pacing    | B     |
| Calculation tables clarity     | C+    |
| Overall                        | A-    |

Strengths:
1. The attribution argument is the document's standout contribution.
   The Translator's Introduction makes a careful, well-sourced case
   that English-language sources have systematically misattributed
   this text to Honma Munehisa...

2. Transparency of method is exemplary. The document is consistently
   honest about what it is and isn't...

Weaknesses:
1. Chapter 7 calculation tables are the weakest section (C+).
   Sections 7.3.2 through 7.3.6 are repetitive and hard to follow...

2. Excessive white space / short chapters (B-). Multiple chapters
   end with over half a page blank...

Summary: The document is publishable as-is. The weaknesses are real
but none are disqualifying — they're the kind of refinements that
separate a strong first edition from a polished second edition.
```

This feedback led directly to restructuring Chapter 7.3 (summary table + appendix), fixing orphaned headings, and multiple rounds of content restoration.

</details>

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

### Confidence Assessment

**Headings, labels, and key terms (high confidence).** Section markers (三十八ヶ条, 十五ヶ条), diagram labels (天明古米, 中星, 天井, 底直), and recurring trading terms (順来, 逢来, 強気, 弱気, 禁判) are written larger and more carefully in the manuscript and can be read reliably.

**Overall structure and teachings (high confidence).** The text is internally self-consistent in ways that would be very unlikely if the translation were substantially wrong. The preface introduces yin-yang cosmology; the trading rules operationalize it; the Middle Star system quantifies it; the Grand Diagram synthesizes it; the Four Virtues provide the discipline to execute it. Each piece refers back to the others. Key terms (中星, 強気/弱気) appear consistently across multiple contexts with the same meaning. If the characters were being badly misread, this coherence would break down.

**Flowing cursive prose (moderate confidence).** The body text in dense passages — the calculation tables, the 38 provisions, the afterword — is read with less certainty. Many individual characters are identified by context and plausibility rather than confident visual recognition. The transcription files record confidence levels (HIGH/MEDIUM/LOW) for this reason.

**Specific numerical figures (moderate-low confidence).** The calculation tables contain figures that are difficult to read in the cursive script, and the manuscript's accounting method connecting the figures across stages is not fully transparent.

### Research Context: Why This Is Novel

As of early 2026, this project represents a genuinely novel workflow in the field of AI-assisted classical Japanese translation. Here's why:

**No published end-to-end pipeline exists for this task.** The academic literature on AI translation of classical Japanese focuses on either (a) OCR/kuzushiji recognition (CODH's KuroNet/Miwo) or (b) LLM translation of already-transcribed classical text (the CODH Tsukushi Project, the MITRA Buddhist text project). Nobody has published an end-to-end pipeline that goes directly from Edo-period cursive manuscript images to a publication-ready English translation with a full audit trail.

**The current generation of models is untested on classical Japanese.** The formal academic benchmarks that exist (the Genji ambiguity test, the Kanbun-LM evaluation, the PoetMT benchmark) all tested models from 2023-2024 — GPT-4 era. Claude Opus 4.6, GPT-5.x, and Gemini 3.x have not been rigorously evaluated on classical Japanese. The CODH Tsukushi Project rated Claude Sonnet 4.5 highest among all tested models for classical Japanese text interaction, but did not test Opus 4.6. Our project is, as far as we can determine, one of the first to apply Opus 4.6's multimodal capabilities directly to Edo-period kuzushiji manuscripts.

**Claude Opus 4.6 reads the manuscript images directly.** Most existing workflows use a dedicated OCR tool (KuroNet, Miwo) for character recognition, then feed the recognized text to an LLM for translation. Our workflow skips the OCR step — Claude reads the cursive script directly from the IIIF page images. This is possible because of Opus 4.6's multimodal capabilities, which combine visual character recognition with contextual language understanding in a single pass. The tradeoff is lower character-level accuracy than dedicated OCR tools on clean printed text, but potentially better performance on damaged or ambiguous manuscript pages where context helps.

**The transcription-then-translation separation is methodologically significant.** Our initial approach (Phase 1) had Claude translate directly from images, conflating character recognition and meaning interpretation. When we separated these into explicit stages — transcription with confidence levels, then translation from transcription — the results became more consistent and, critically, auditable. A reader can check the transcription against the original image, then check the translation against the transcription. This separation has been discussed in the literature (e.g., the CODH Tsukushi pipeline) but not, to our knowledge, implemented as an open-source audit trail for a complete book-length translation.

**The adversarial grading loop has no direct precedent in translation work.** Using an independent, context-free LLM instance to grade the output — inspired by GANs — proved remarkably effective at catching failure modes that the production instance couldn't self-detect: fabricated content, arithmetic errors, misattributed sources, and editorial paraphrase presented as translation. This technique is applicable to any AI-assisted translation project and, to our knowledge, has not been formally described in the translation studies literature.

**Key references for the research context:**
- Clanuwat et al., "Deep Learning for Classical Japanese Literature" (2018) — KuroNet, Kuzushiji-MNIST
- Kitamoto et al., CODH Tsukushi Project — LLM interaction with classical Japanese texts
- Wang et al., "Kanbun-LM" (ACL 2023) — Classical Chinese to kanbun parallel dataset
- Nehrdich, "MITRA: A Parallel Corpus for Buddhist Chinese" (2025) — LLM evaluation for Buddhist texts
- De Wolf, "Can ChatGPT Translate Literary Japanese?" (2023) — The Genji ambiguity test
- Miwo app (CODH) — Kuzushiji OCR, 3.4M+ images processed

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

Copyright (c) 2026 Zach Booth. All rights reserved.

**Translation, transcription, and LaTeX source** (this repository): Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International). You may read, study, fork, and build on this work for non-commercial purposes, provided you credit the original and share derivatives under the same terms.

**The compiled book** (PDF / printed editions): All rights reserved. Commercial distribution of the finished book is exclusively authorized by the copyright holder.

**Source manuscript images**: Provided under Kyoto University's free-with-attribution license (二次利用自由・所蔵表示). See [reuse policy](https://rmda.kulib.kyoto-u.ac.jp/reuse). All manuscript images courtesy of the Main Library, Kyoto University (所蔵：京都大学附属図書館).
