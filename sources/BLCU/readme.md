The Beijing Language and Culture University (BLCU) corpus is a 15-billion character "balanced" word corpus from a variety of written sources.  The relevant paper is:

> 荀恩东, 饶高琦, 肖晓悦, 臧娇娇, *大数据背景下 BCC 语料库的研制*, 语料库语言学, 2016 ([pdf](https://bcc.blcu.edu.cn/downloads/papers/%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%83%8C%E6%99%AF%E4%B8%8BBCC%E8%AF%AD%E6%96%99%E5%BA%93%E7%9A%84%E7%A0%94%E5%88%B6_%E8%8D%80%E6%81%A9%E4%B8%9C.pdf)).

The data used was from [Pleco Forums](https://www.plecoforums.com/threads/word-frequency-list-based-on-a-15-billion-character-corpus-bcc-blcu-chinese-corpus.5859/), and in particular the "global" corpus.

The top 30000 "words" from this corpus were used, all the Chinese characters therein where extracted, and [OpenCC](https://github.com/BYVoid/OpenCC) was used to convert the traditional characters to simplified characters.  We obtain a list of 4445 characters, of which the following characters (432) were excluded from MteH v0.1.1:

> 藩 岚 雯 毓 禺 霖 忒 谟 侬 绫 镕 钊 陇 琛 倭 敕 幡 俾 剌 钵 铢 渭 迥 噶 淄 踞 谑 诃 铎 踵 瘢 豢 汶 衹 饬 栩 曦 梓 嗖 浚 奂 傩 沂 嵋 瑾 沓 蛊 璐 晏 漳 琏 褚 煜 祯 湍 钡 涸 欤 颍 邯 俸 鸾 谀 岐 猓 蔷 恚 锵 寰 唷 诰 诙 罡 胤 嫔 坂 町 瓒 髯 瞠 酰 筱 甬 郸 穑 呷 伫 岬 鳎 岱 芮 赈 鞑 谌 徨 橹 鳗 颔 匝 喏 曜 渥 苓 馀 畹 胫 銮 嘤 隽 鹄 萱 啵 蠡 胭 谡 荨 澹 纭 潞 郅 宓 蟠 濮 蟮 蓟 圩 诿 氲 铠 叵 饕 睢 迩 榭 娑 洌 浜 忻 唑 诒 麾 氐 冽 宸 谝 耄 俑 沱 缜 酚 纾 椤 荩 庑 庋 邺 燮 墒 醯 诤 砷 唏 泾 芷 妫 苷 袂 涞 飧 迳 鋈 凇 芪 觯 鞯 肽 钰 僮 龇 绾 疸 烨 罄 咣 郏 艮 搽 寮 谖 虻 埽 绻 淼 蠹 樽 诮 犷 詈 竦 诨 铰 鸬 螨 洹 俪 痿 瘙 衲 罅 笥 鹗 爻 崴 酢 阈 苁 嗲 哂 飨 娣 薏 鍪 刈 嗪 茯 嵘 怼 昕 咩 髡 砺 佘 弑 慵 潍 帼 魑 醛 剐 呤 铉 骶 峁 渌 厝 硒 硎 煨 甑 炜 笕 浔 耦 遨 绦 龉 嬷 笫 痤 莆 诓 婕 稹 蹴 镏 羯 鲂 匦 酆 蚨 蚴 媸 诖 庾 饧 镉 饔 腱 鲆 砝 颞 瘛 涫 臁 吡 玮 羟 虼 遴 岢 髁 芾 鲎 髋 胍 铵 枰 畲 芏 芎 噱 龆 芄 雒 钒 谠 萸 妗 踔 嘌 饩 蠓 鄣 瓯 缦 濉 殇 卟 杷 袢 黾 枋 餮 乜 堋 髂 缁 醚 搿 卮 苄 芰 趸 蠊 枇 崾 硪 郴 疝 膈 乇 炝 硐 钪 仟 笱 粳 茱 愀 蛘 晟 厍 洙 鞒 睇 钼 钅 觳 鄄 蔻 钕 灞 俅 隳 芊 艽 甙 杓 疃 嬖 哌 婧 缇 窨 炅 莪 隹 辊 酐 逑 噻 鬟 缡 岣 薅 谂 鄹 郜 叻 吖 砼 枨 珉 赟 (Non Jun Da chars: 刂 咗 嚟 伱 旻 妳 屌 啫 嚒 丶 亍 喆 艹 犤 啲 旳 囧 嘢 咁 啱 佢 堃 焗 攰 玥 揾 璟 垺 冇 犦 哋 罒 囖 騒 嘅 浐 喺 糸)

The remaining 4013 characters were included in MteH v0.1.1.
