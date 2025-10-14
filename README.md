# More than enough Hanzi (MteH)

**A curated set of ~4300 simplified Chinese characters for advanced language learners.**  

This simplified Chinese character corpus is intended to make a suitable "endgame corpus" for advanced students.  Basically, if you learn these characters, you're practically "done for life" studying simplified Chinese characters (congratulations!).  Obviously, there are more simplified Chinese characters than this (in proper nouns, scientific terms, chengyu, Chinese history, etc.), but at a certain point you've got to draw the line and say "this is my endgame".

## Method

The MteH corpus is designed to have no "missing" characters: all the characters not in this corpus are necessarily very rare, and likely very niche.  To this end, the MteH corpus merges the following 17 corpora:

1. all 2905 characters from the HSK 1.0 syllabus (before 2010; 11 levels);
2. all 2663 characters from the HSK 2.0 syllabus (after 2010; 6 levels);
3. all 3000 characters from the HSK 3.0 syllabus (introduced 2021; 9 levels);
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

The original author (Rebecca J. Stones) has manually checked every single character.  The following characters were manually removed (some are not simplified Mandarin characters, and some were too rare, and didn't make the final cut): 乜亍仄伢伫佘佚侬俸俾倭偃僖冇冼剌匝厝叻吋吖吡呎呣咣咤咩唏唑唷啵啶喆喏嗬嗲嗳嘤噶噻囡圩圻坂垭埕埗埚埤埼堀堃夔夥妤姝姣婕婧嫔嬛嬷宕宸寮寰尻屌岐岘岙岚岣岬岱峁峪崁崧嵋嵺巽帼幡庾弁弋徨徵忒恁慵憩懋揆摺敕斛於旻昕昱昶晏晟暹曜曦杩枋枰栾桢梓棣椤楮榭槃槭樽檎檗忻歆毓氐氹汴汶汾沂沅沱泗泾洙洮洵浚浜浠浼涔淄淞淦渚渥渭溴滘滢漳潍潞潟潲潼澍澶濂濑濠濮瀹灏灞炅炜烃烨焘煜燊燮爻猷玑玟玮珂珉珪琛琮琰瑄瑛瑾璁璐璜璟甬町畈畑畿疃瘛皋睇瞑矽砷硒硪磡礅祇祐祚祯祺禺秕稔稷竜竦筠筱粳绫缁缇罡羟羧羯翊肽胤胥脩臧艄艮芊芪芮芷芾苓苣苫苷苻茛茱荀荃荻莆莒莘莪菀菅萩萱萼蒐蒴蓟蓼蔷蔺蔻蕙薏薨薹藜藩蝽螯蟮衢衲褚谌谝谟豉蹇轲轶辻迺邨邬邯郅郜郴郸鄞鄢鄱酚酰醚醛鋈钊钡钰钵钼铉铎铵锷镓镕闾陂陇隍隳隽雉雯霏霖霰靼鞅鞑鞯颍飧飨餮饕馀馥骞鳎鳚鹛麝麽麾黜鼩.

The characters are primarily ordered in [unicode order](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-18/#G11620) so that characters with similar components are grouped together as much as possible.  The only exceptions are variant characters, which were reordered to be adjacent.
