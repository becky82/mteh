# More than enough Hanzi (MteH)

**A curated set of ~4300 simplified Chinese characters for Chinese language learners.**  

---

## Purpose

This simplified character corpus is intended to be a set of simplified Chinese characters which will make a good "finishing line" for advanced students.  Basically, if you learn these characters, you're practically "done" studying simplified Chinese characters.

## Construction

This list of characters merges the following corpora:

1. HSK 1.0 (2905 characters);
2. HSK 2.0 (2663 characters);
3. HSK 3.0 (3000 characters);
4. Heisig and Richardson's *Remembering Simplified Hanzi 1* and *Remembering Simplified Hanzi 2* (3018 characters);
5. the [Taiwanese TOCFL vocabulary list](https://www.roc-taiwan.org/at_de/post/634.html) (extracted from 7989 simplified-character words; 妳 and 牠 were excluded);
6. the top 3500 characters from [Jun Da's modern corpus](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO) (後 was excluded);
7. the top 3500 characters from [the SUBTLEX character dataset](https://doi.org/10.1371/journal.pone.0010729) (妳, 後, 菈, and 円 were excluded);
10. the top 3500 characters from [HanziCraft's frequency database](https://hanzicraft.com/lists/frequency) (後 and 於 were excluded);
11. K-5 Word Frequency Dictionary (originally sourced from `mandarininstitute.org` but this link is broken now), which contains 3349 words from which 1817 characters were extracted;
12. the top 20000 words from the Leeds Chinese corpus (originally sourced from `corpus.leeds.ac.uk` but this link is broken now), which contained 3655 characters;
13. the top 20000 words from the BLCU "global" corpus (sourced from [Pleco Forums](http://www.plecoforums.com/threads/word-frequency-list-based-on-a-15-billion-character-corpus-bcc-blcu-chinese-corpus.5859/)), which contained 3917 characters, and after filtering we obtained 3700 characters (excluded characters include 丶, 亞, 伱, 佢, 來, 係, 個, 們, 備, 傳, ...);
15. the top 20000 words from the [Leiden Weibo Corpus](http://lwc.daanvanesch.nl/openaccess.php), which contained 3585 characters, and after filtering we obtained 3393 characters (excluded characters include 丶, 來, 係, 個, 們, 備, 傷, 內, 兩, ...);
16. the [Chinese Wikipedia corpus](https://czielinski.github.io/hanzifreq/hanzifreq/output/frequencies.html), which contained 10000 characters, and after filtering there were 6694, of which the top 3500 characters were selected (excluded characters include 國, 為, 會, 學, 時, 電, 後, 動, 與, 區, ...);
17. the 3500 characters listed as 一级字表 (level 1) in the Chinese Ministry for Education's [《通用规范汉字表》](http://www.moe.gov.cn/jyb_sjzl/ziliao/A19/201306/t20130601_186002.html) (sourced from [Wikisource](zh.wikisource.org/wiki/%E9%80%9A%E7%94%A8%E8%A7%84%E8%8C%83%E6%B1%89%E5%AD%97%E8%A1%A8));
18. the 3500 characters in Chinese Ministry for Education's 《现代汉语常用字表》 (1988) (sourced from [Wikisource](https://en.wikisource.org/wiki/Translation:List_of_Frequently_Used_Characters_in_Modern_Chinese));
19. the 2480 characters listed as for Chinese primary school children (2016) (sourced from [Sohu](https://www.sohu.com/a/62481121_101008));
20. the 300 most common Chinese surnames, based on Chinese census data (c. 2018) (sourced from [Sina](https://news.sina.cn/2018-04-08/detail-ifyuwqez6882483.d.html); there was one two-character surname 欧阳, and the characters 薄 and 路 appear twice in Sina's list; all these characters were included).

The original author (Rebecca J. Stones) has manually checked every single character.  Some characters were manually removed (some are not simplified Mandarin characters, and some were simply too rare to include)  : 冇 (U+5187) 吋 (U+540B) 呎 (U+544E) 呣 (U+5463) 啰 (U+5570) 喆 (U+5586) 埗 (U+57D7) 埼 (U+57FC) 堃 (U+5803) 嬛 (U+5B1B) 屌 (U+5C4C) 崁 (U+5D01) 嵺 (U+5D7A) 旻 (U+65FB) 昇 (U+6607) 槃 (U+69C3) 欸 (U+6B38) 氹 (U+6C39) 滘 (U+6ED8) 潟 (U+6F5F) 燊 (U+71CA) 珪 (U+73EA) 瑄 (U+7444) 璟 (U+749F) 畑 (U+7551) 瞭 (U+77AD) 磡 (U+78E1) 祇 (U+7947) 祐 (U+7950) 竜 (U+7ADC) 脩 (U+8129) 萩 (U+8429) 蒐 (U+8490) 辻 (U+8FBB) 迺 (U+8FFA) 邨 (U+90A8) 镕 (U+9555) 鳚 (U+9CDA) 鼩 (U+9F29).
