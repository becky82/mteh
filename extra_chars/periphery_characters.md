# Characters on the periphery of MteH

This document is aimed at giving an idea of what characters are close to inclusion into MteH, but didn't make the final cut.

## Character lists

### Non-MteH characters in Jun Da corpus

The top-200 characters from the [Jun Da modern corpus](../mteh/tree/main/sources/JunDa) missing from MteH v0.1.1 are:

> 於玑後藩岚麽雯毓瑛禺霖忒谟焘侬绫镕钊伢陇琛倭鞅敕幡祺俾聿剌顼哝钵铢俟胥醫渭珂哧迥噶淄踞韬蹑谑诃铎荀攫踵臆瘢豢汶惴桢藥衹饬栩曦梓嗖浚荃汾奂傩沂嵋瑾赓佚沓蛊璐晏漳琏辘僭褚煜骥嗳祯湍轲钡箓涸亘筵欤颍稷恻邯珥俸鸾犊扈鋆谀岐猓蔷遽恚皑锵簌鹳睽寰唷诰恣婵蹙诙罡胤皋嫔娓坂町瘠啜瓒龛髯瞠潼酰筱甬淞蕙郸轶荪麝醮湮穑呷萼伫岬鳎啾徇徵岱邙恫怆桀盂桧芮闩铿窠牒赈嗫鞑袤谌徨橹嵇圪髻嗬辎谄蛐鹞翱蓿鳗鲇這嚅颔黜黠濑洵砥咂匝偃淙

The character 淙 is #4172 in Jun Da's modern corpus; it occurred 474 times in a corpus of 193,504,018 characters, or about 2 or 3 times per 1 million characters.

### Non-MteH characters in N corpora

At the time of writing, there are 20 corpora, the non-MteH characters in N corpora (as N varies) are as follows:

- 8: 於
- 7: 岚禺雯
- 6: 忒曦藩霖
- 5: 侬琛祺麽
- 4: 夥婕寰徨徵忻晏晟梓毓汶洙瑛筱羯臧蔷蕙醛
- 3: 佘俸俾倭冼厝唷喆噶囡坂妳嫔宸寮屌岐岱弋後懋摺敕旻昱昶曜沂浚浜漳濂炜煜玑玮珉琮瑄璐璟甬筠胤胥芮芷苓荀莘萱褚谌谟邯郸酚钊钰铉铎陇隽馥

Any simplified character not listed above is either in MteH v0.1.1, or not present in 18+ (out of 20) corpora.

## Why haven't some characters been added to MteH?

First of all, some characters like

> 後藥

are traditional-only, while MteH is a simplified character corpus, so they are excluded from MteH.  Characters like these:

> 於麽夥徵

are rarely used as simplified characters, but are common as traditional characters.  The enumeration algorithms used to generate corpora likely don't have the ability to tell if such characters are being used as a traditional character, or one of the rare cases when it's used as a simplified character, and thus likely vastly overestimate their frequency as simplified characters.

Some characters are not used in standard Mandarin used in mainland China, the language you get on HSK exams:

> 侬伢妳

Some characters are discussed as [characters to know exist](../extra_chars/characters-to-know-exist.md), so they are not needed in MteH:

> 陇桢梓蛊鹳鳎桧蛐鹞鳗鲇

And some characters have since been added to MteH v0.1.1.  At the time of writing, these have been added:

> 倭冽擤杵焱皑箔螯闩鳗

At the time of writing, adding/removing characters from MteH v0.1.1 is an in-progress project.
