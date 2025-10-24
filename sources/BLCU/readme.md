The Beijing Language and Culture University (BLCU) corpus is a 15-billion character "balanced" word corpus from a variety of written sources.

The relevant paper is:

> 荀恩东, 饶高琦, 肖晓悦, 臧娇娇, *大数据背景下 BCC 语料库的研制*, 语料库语言学, 2016 ([pdf](https://bcc.blcu.edu.cn/downloads/papers/%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%83%8C%E6%99%AF%E4%B8%8BBCC%E8%AF%AD%E6%96%99%E5%BA%93%E7%9A%84%E7%A0%94%E5%88%B6_%E8%8D%80%E6%81%A9%E4%B8%9C.pdf)).

The data used was from [Pleco Forums](https://www.plecoforums.com/threads/word-frequency-list-based-on-a-15-billion-character-corpus-bcc-blcu-chinese-corpus.5859/), and in particular the "global" corpus.

The top 20000 "words" from this corpus were used, and all the Chinese characters therein where extracted.  After removing traditional characters, we obtain a list of 3699 characters of which of which 3615 were included in MteH v0.1.1; these characters (81) were removed:

> 乜 亍 侬 俸 俾 倭 冇 厝 叻 吖 咩 唑 唷 啵 喆 嗲 嘤 噶 噻 坂 屌 岚 岣 峁 嵋 徨 忒 忻 晏 晟 曦 枰 椤 榭 氐 洙 浚 漳 灞 玮 琛 疃 瘛 睇 硒 硪 禺 竦 缁 罡 羯 肽 胤 芪 芾 莪 蟮 衲 谌 谝 邯 郅 郸 酚 酰 醛 鋈 钡 钵 钼 铉 隳 雯 霖 鞑 鞯 颍 飧 飨 饕 鳎
