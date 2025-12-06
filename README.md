# More than enough Hanzi (MteH)

**A curated set of ~4,270 simplified Chinese characters for advanced language learners.**  

The **_MteH corpus_** is designed as an "endgame corpus" for advanced students. Basically, if you learn these characters, you're practically "done for life" studying simplified Chinese characters (congratulations!).  Obviously, there are more simplified Chinese characters than this (in proper nouns, scientific terms, chengyu, Chinese history, online usernames, etc.), but at a certain point you've got to draw the line and say "this is my endgame".

Currently, MteH focuses entirely on **simplified Chinese characters**, especially those you’ll encounter in mainland China and in **HSK** exams.

- [MteH corpus (v0.1.2)](./versions/v0.1.2/mteh_v0.1.2.txt) (plain text)
- [Handwriting practice](./versions/v0.1.2) (PDFs to print out)
- [Extra characters](./extra_chars/characters-to-know-exist.md) (good to know, but not part of MteH)
    - [Repeated-component characters](./extra_chars/repeated_components.md)
    - [Periodic table of the elements](./extra_chars/periodic_table.md)
    - [Province abbreviations](./extra_chars/province_abbreviations.md)
    - [Characters/words using or related to 虫](./extra_chars/虫.md) (insects; lower life forms)
    - [Characters/words using or related to 鸟](./extra_chars/鸟.md) (birds)
    - [Characters/words using or related to 鱼](./extra_chars/鱼.md) (fish)
    - [Characters/words using or related to 木](./extra_chars/木.md) (trees; wood)
 
There is also an Anki Deck ([here](./mteh_anki_deck.apkg)) which should already work, but should be thought of as a work-in-progress.  (On a computer, [AnkiDraw](https://ankiweb.net/shared/info/1868980340) allows you to handwrite.)

---

## Summary

The MteH corpus is built to minimize "missing" characters; any characters not included are extremely rare or niche.  The initial version (v0.1.1) merges the following corpora:

<div align="left">

| # | Corpus | #chars | #used | Source / Reference |
|---|---------|---------------|--------------------|--------------------|
| 1 | [HSK 1.0](./sources/HSK1.0) | 2,866 | 2,866 | pre-2010, 11 levels |
| 2 | [HSK 2.0](./sources/HSK2.0) | 2,663 | 2,663 | post-2010, 6 levels |
| 3 | [HSK 3.0](./sources/HSK3.0) | 3,000 | 3,000 | 2021 version, 9 levels |
| 4 | [TOCFL](./sources/TOCFL) | 3,027* | 2,998 | Taiwan's TOCFL 3100 + 33 traditional chars |
| 5 | [K-5](./sources/K-5) | 1,817 | 1,816 | K-5 word frequency |
| 6 | [通用规范汉字表](./sources/%E9%80%9A%E7%94%A8%E8%A7%84%E8%8C%83%E6%B1%89%E5%AD%97%E8%A1%A8) | 3,500 | 3,500 | Ministry of Education (2013) |
| 7 | [现代汉语常用字表](./sources/%E7%8E%B0%E4%BB%A3%E6%B1%89%E8%AF%AD%E5%B8%B8%E7%94%A8%E5%AD%97%E8%A1%A8) | 3,500 | 3,498 | Ministry of Education (1988) |
| 8 | [primary school](./sources/primary_school) | 2,468 | 2,467 | China primary schools (2016) |
| 9 | [Singapore](./sources/Singapore_primary_school) | 1,655 | 1,655 | Singapore primary schools (2015) |
| 10 | [Heisig](./sources/Heisig) | 3,018 | 3,018 | Heisig & Richardson, *Remembering Simplified Hanzi* I–II |
| 11 | [Hoenig](./sources/Hoenig) | 2,177 | 2,151 | *Learn & Remember 2,178 Characters and Their Meanings* |
| 12 | [Jun Da](./sources/JunDa) | 4,485* | 4,100 | modern Chinese corpus |
| 13 | [SUBTLEX](./sources/SUBTLEX) | 4,462* | 4,034 | film and TV subtitle corpus |
| 14 | [Tsai](./sources/Tsai) | 4,329* | 3,872 | Usenet newsgroups (1993-1994) |
| 15 | [Wikipedia](./sources/Wikipedia) | 3,476* | 3,196 | Chinese Wikipedia |
| 16 | [classical](./sources/classical) | 1,968* | 1,840 | prior to the end of the Han dynasty |
| 17 | [THUOCL](./sources/THUOCL) | 3,421* | 3,156 | mostly Sogou webpages |
| 18 | [Leeds](./sources/Leeds) | 4,230* | 3,984 | Internet corpus |
| 19 | [BLCU](./sources/BLCU) | 4,445* | 4,013 | "balanced", written Chinese |
| 20 | [LWC](./sources/LWC) | 4,130* | 3,863 | Sina Weibo |
| 21 | [food](./sources/food) | 1,182 | 1,093 | food-related terms |
| 22 | [species](./sources/species) | 4,086 | 3,121 | species names |
| 23 | [Chinese surnames](./sources/surnames) | 1,745 | 1,539 | 1,807 Chinese surnames |
| 24 | [Chinese names](./sources/names) | 2,269 | 1,948 | 1,200,000 Chinese names |
| 25 | [city-geo](./sources/city-geo) | 1,277 | 1,116 | mainland China city terms |
| 26 | [company](./sources/company) | 4,363* | 3,554 | company proper nouns |
| 27 | [med-orgs](./sources/med-orgs) | 4,826 | 3,633 | medical organizations |

</div>

Those marked * have extraction steps (documented in their respective readmes): selection of top-N words/characters, conversion from traditional to simplified.

Characters are ordered in **[Unicode order](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-18/#G11620)** (excluding variants), grouping visually or structurally related forms as much as possible.  

MteH also incorporates:  
- Character structure data and character drawings from [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) and [cjkvi-ids](https://github.com/cjkvi/cjkvi-ids)
- Frequency data from [Jun Da’s modern corpus](http://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO)
- Images from [Pexels](https://www.pexels.com/), [Wikimedia](https://commons.wikimedia.org/wiki/Main_Page), etc.

Statistics and debug reports: [missing chars](./sources/missing_chars_report.md); [corpus histogram](./sources/mteh_char_corpus_histogram_full.md); [debug](./debug/debug_report.md); [modifications](./debug/mteh_modification_report.md); [syllables](./debug/mteh_syllables_all_combinations.md).

---

## License

© 2025 Rebecca J. Stones  
Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
