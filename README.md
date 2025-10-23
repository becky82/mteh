# More than enough Hanzi (MteH)

**A curated set of ~4270 simplified Chinese characters for advanced language learners.**  

This simplified Chinese character corpus is intended to make a suitable "endgame corpus" for advanced students.  Basically, if you learn these characters, you're practically "done for life" studying simplified Chinese characters (congratulations!).  Obviously, there are more simplified Chinese characters than this (in proper nouns, scientific terms, chengyu, Chinese history, online usernames, etc.), but at a certain point you've got to draw the line and say "this is my endgame".

For the time being, the MteH corpus only contains simplified Chinese characters, and in particular those you might encounter while living in mainland China or when taking an HSK exam.

Included in this project are [pdfs designed for handwriting practice](https://github.com/becky82/mteh/tree/main/versions/v0.1.1).

## Method

The MteH corpus is designed to have no "missing" characters: all the characters not in this corpus are necessarily very rare, and likely very niche.  To this end, the MteH corpus merges the following corpora:

1. all [2905 characters](https://github.com/becky82/mteh/tree/main/sources/HSK1.0) from the HSK 1.0 syllabus (before 2010; 11 levels);
1. all [2663 characters](https://github.com/becky82/mteh/tree/main/sources/HSK2.0) from the HSK 2.0 syllabus (after 2010; 6 levels);
1. all [3000 characters](https://github.com/becky82/mteh/tree/main/sources/HSK3.0) from the HSK 3.0 syllabus (introduced 2021; 9 levels);
1. the [3018 characters](https://github.com/becky82/mteh/tree/main/sources/Heisig) from Heisig and Richardson's *Remembering Simplified Hanzi 1* and *Remembering Simplified Hanzi 2*;
1. the [2501 characters](https://github.com/becky82/mteh/tree/main/sources/TOCFL) extracted from the [Taiwanese TOCFL vocabulary](https://www.roc-taiwan.org/at_de/post/634.html);
1. the top [3500 characters](https://github.com/becky82/mteh/tree/main/sources/JunDa) from [Jun Da's modern corpus](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO), along with HanziCraft's frequency database;
1. the top [3500 characters](https://github.com/becky82/mteh/tree/main/sources/SUBTLEX) from the SUBTLEX character dataset;
1. the [1817 characters](https://github.com/becky82/mteh/blob/main/sources/K-5) extracted from the K-5 Word Frequency Dictionary;
1. [3654 characters](https://github.com/becky82/mteh/tree/main/sources/Leeds) extracted from the top 20000 words from the Leeds Chinese corpus by Serge Sharo;
1. [3699 characters](https://github.com/becky82/mteh/tree/main/sources/BLCU) extracted from the top 20000 words from the BLCU "global" corpus, by Xun Endong et al.;
1. [3393 characters](https://github.com/becky82/mteh/tree/main/sources/LWC) extracted from the top 20000 words from the [LWC corpus](https://lwc.daanvanesch.nl/openaccess.php);
1. [3500 characters](https://github.com/becky82/mteh/tree/main/sources/Wikipedia) extracted from a [Chinese Wikipedia corpus](https://czielinski.github.io/hanzifreq/hanzifreq/output/frequencies.html);
1. the [3500 characters](https://github.com/becky82/mteh/tree/main/sources/%E9%80%9A%E7%94%A8%E8%A7%84%E8%8C%83%E6%B1%89%E5%AD%97%E8%A1%A8) listed as 一级字表 (level 1) in the Chinese Ministry for Education's 《通用规范汉字表》 (2013);
1. the [3500 characters](https://github.com/becky82/mteh/tree/main/sources/%E7%8E%B0%E4%BB%A3%E6%B1%89%E8%AF%AD%E5%B8%B8%E7%94%A8%E5%AD%97%E8%A1%A8) in the Chinese Ministry for Education's 《现代汉语常用字表》 (1988);
1. the [2480 characters](https://github.com/becky82/mteh/tree/main/sources/primary_school) listed as for Chinese primary school children (2016);
1. [286 characters](https://github.com/becky82/mteh/tree/main/sources/surnames) from the top-300 Chinese surnames, as in the [ChineseNames](https://psychbruce.github.io/ChineseNames/) package.

The characters are ordered in [unicode order](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-18/#G11620) so that characters with similar components are grouped together as much as possible (excluding some variant characters).

This project includes character structure data from the [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) project, licensed under an MIT License, and character frequency data from Jun Da's [modern corpus]( http://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO).

## License

© 2025 Rebecca J. Stones.  This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
