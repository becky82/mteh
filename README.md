# More than enough Hanzi (MteH)

**A curated set of ~4,540 simplified Chinese characters for advanced language learners.**  

The **_MteH corpus_** is designed as an "endgame corpus" for advanced students. Basically, if you learn these characters, you're practically "done for life" studying simplified Chinese characters (congratulations!).  Obviously, there are more simplified Chinese characters than this (in proper nouns, scientific terms, chengyu, Chinese history, online usernames, etc.), but at a certain point you've got to draw the line and say "this is my endgame".

Currently, MteH focuses entirely on **simplified Chinese characters**, especially those you’ll encounter in mainland China and in **HSK** exams.

- [MteH corpus (v0.1.3)](./versions/v0.1.3/mteh_v0.1.3.txt) (plain text)
- [Handwriting practice](./versions/v0.1.3) (PDFs to print out)
- [Extra characters](./extra_chars/知有其字.md) (good to know, but not part of MteH)
 
There is also an Anki Deck ([here](./mteh_anki_deck.apkg)) which should already work, but should be thought of as a work-in-progress.  (On a computer, [AnkiDraw](https://ankiweb.net/shared/info/1868980340) allows you to handwrite.  On AnkiDroid, the in-built whiteboard feature enables handwriting.)

---

## Summary

The MteH corpus is built to minimize "missing" characters; any characters not included are extremely rare or niche.  The current update merges the following diverse corpora.  Not all of the characters are included (there are way too many); omitted characters are documented in the [missing chars](./sources/missing_chars_report.md) report).

<div align="left">

| # | Corpus | #chars | Source / Reference |
|---|---------|---------------|--------------------|
| 1 | [HSK 1.0](./sources/HSK1.0) | 2,866 | pre-2010, 11 levels |
| 2 | [HSK 2.0](./sources/HSK2.0) | 2,663 | post-2010, 6 levels |
| 3 | [HSK 3.0](./sources/HSK3.0) | 3,000 | 2021 version 3.0 standards, 9 levels |
| 4 | [HSK 3.1](./sources/HSK3.1) | 3,088 | 2025 version 3.0 standards, 9 levels |
| 5 | [TOCFL](./sources/TOCFL) | 3,027* | Taiwan's TOCFL 3100 + 33 traditional chars |
| 6 | [K-5](./sources/K-5) | 1,817 | K-5 word frequency |
| 7 | [通用规范汉字表](./sources/通用规范汉字表) | 3,500 | Ministry of Education (2013) |
| 8 | [现代汉语常用字表](./sources/现代汉语常用字表) | 3,500 | Ministry of Education (1988) |
| 9 | [普通话水平测试](./sources/普通话水平测试) | 3,788 | Putonghua Proficiency Test for native Mandarin fluency |
| 10 | [Taiwan MoE](./sources/TaiwanMoE) | 4,661* | Taiwan Ministry of Education 常用字 | 
| 11 | [primary school](./sources/primary_school) | 2,468 | China primary schools (2016) |
| 12 | [语文](./sources/语文) | 3,500 | China compulsory education 语文 (2022) |
| 13 | [Singapore](./sources/Singapore_primary_school) | 1,655 | Singapore primary schools (2015) |
| 14 | [age of acquisition](./sources/age_of_acquisition) | 4,237 | Cai et al. (2022) |
| 15 | [psycholinguistic](./sources/psycholinguistic) | 3,253 | Chang et al. (2016) |
| 16 | [Heisig](./sources/Heisig) | 3,018 | Heisig & Richardson, *Remembering Simplified Hanzi* I–II |
| 17 | [Hoenig](./sources/Hoenig) | 2,177 | *Learn & Remember 2,178 Characters and Their Meanings* |
| 18 | [Jun Da](./sources/JunDa) | 4,485* | modern Chinese corpus |
| 19 | [SUBTLEX](./sources/SUBTLEX) | 4,462* | film and TV subtitle corpus |
| 20 | [Tsai](./sources/Tsai) | 4,329* | Usenet newsgroups (1993-1994) |
| 21 | [CKIP](./sources/CKIP) | 3,392* | CKIP (Chinese Knowledge and Information Processing) research group |
| 22 | [Wikipedia](./sources/Wikipedia) | 3,476* | Chinese Wikipedia |
| 23 | [Chinese.SE](./sources/ChineseSE) | 4,525* | Chinese Stack Exchange (Jan 2026) |
| 24 | [classical](./sources/classical) | 1,968* | prior to the end of the Han dynasty |
| 25 | [THUOCL](./sources/THUOCL) | 3,421* | mostly Sogou webpages |
| 26 | [Leeds](./sources/Leeds) | 4,230* | Internet corpus |
| 27 | [BLCU](./sources/BLCU) | 4,445* | "balanced", written Chinese |
| 28 | [LWC](./sources/LWC) | 4,130* | Sina Weibo |
| 29 | [food](./sources/food) | 1,182 | food-related terms |
| 30 | [species](./sources/species) | 4,086 | species names |
| 31 | [Chinese surnames](./sources/surnames) | 1,745 | 1,807 Chinese surnames |
| 32 | [Chinese names](./sources/names) | 2,269 | 1,200,000 Chinese names |
| 33 | [city-geo](./sources/city-geo) | 1,277 | mainland China city terms |
| 34 | [company](./sources/company) | 4,363* | company proper nouns |
| 35 | [med-orgs](./sources/med-orgs) | 4,826 | medical organizations |
| 36 | [MCT](./sources/MCT) | 1,180 | Medical Chinese Test |
| 37 | [BCT](./sources/BCT) | 1,752 | Business Chinese Test |
| 38 | [chengyu convention](./sources/chengyu_convention) | 2,226 | characters in "chengyu convention" chengyu |
| 39 | [Xinhua](./sources/Xinhua) | 5,357 | Xinhua chengyu and xiehouyu |

</div>

Those marked * have extraction steps (documented in their respective readmes), typically this involves the selection of top-N words/characters, conversion from traditional to simplified, or sporadic bugs.

Characters are ordered in **[Unicode order](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-18/#G11620)**, grouping visually or structurally related forms as much as possible.  

MteH also incorporates:  
- Character structure data and character drawings from [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) and [cjkvi-ids](https://github.com/cjkvi/cjkvi-ids)
- Frequency data from [Jun Da’s modern corpus](http://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO)
- Images from [Pexels](https://www.pexels.com/), [Wikimedia](https://commons.wikimedia.org/wiki/Main_Page), etc.

Statistics and debug reports: [missing chars](./sources/missing_chars_report.md); [corpus histogram](./sources/mteh_char_corpus_histogram_full.md); [debug](./debug/debug_report.md); [modifications](./debug/mteh_modification_report.md); [syllables](./debug/mteh_syllables_all_combinations.md).

---

## License

© 2025 Rebecca J. Stones  
Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
