The SUBTLEX dataset is provided by the paper Qing Cai and Marc Brysbaert, "SUBTLEX-CH: Chinese Word and Character Frequencies Based on Film Subtitles", PLoS One, 2010.  It can be downloaded from [here](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010729).

The file SUBTLEX-CH-CHR contains character frequencies, but is encoded using GBK.  By opening the raw file in the Firefox browser, and copy/pasting the result to a text file, we can obtain a Unicode version of the SUBTLEX-CH-CHR.

From the top-4500 characters in SUBTLEX-CH-CHR, [OpenCC](https://github.com/BYVoid/OpenCC) was used to identify traditional characters and convert them to simplified.  It found the following characters (38):

> 乾 來 傢 內 凱 勛 吳 唸 噓 夥 孫 屍 張 後 徵 徹 捱 摺 於 朧 東 濃 煥 癒 竊 給 練 臺 菸 蝦 錫 鍔 鎬 鑽 餌 魯 鯊 鯨

This left 4462 unique characters, of which the following (428) were not included in MteH v0.1.1:

> 玑 藩 雯 瑛 忒 谟 侬 绫 琛 幡 俾 剌 哝 钵 珂 哧 迥 蹑 谑 诃 铎 攫 踵 臆 汶 惴 栩 曦 梓 嗖 奂 瑾 沓 蛊 璐 辘 嗳 湍 钡 涸 亘 筵 犊 扈 谀 岐 蔷 皑 锵 鹳 睽 寰 恣 诙 娓 坂 町 瘠
啜 龛 瞠 筱 轶 麝 湮 呷 岬 啾 岱 盂 芮 闩 铿 牒 鞑 袤 徨 髻 嗬 谄 翱 蓿 鳗 濑 砥 咂 匝 喏 蛰 璜 渥 靼 罔 匍 祗 馀 胫 熠 沅 镭 嘤 瞑 宕 戾 隽 啵 胭 褛 倌 荨 飕 螳 蟠 匐 祐 蜃 褴 蓟 杳 诿 簪 夙 铠 叵 泯 鬃 垠 榭 舐 麾 冽 摈 箔 咝 怏 砧 俑 沱 缜 鹫 瘴 酚 孛 憩 啮 畿 骁 蚱 蹶 啕 燮 觐 晔 砷 唏 缥 刍 嶙 呓 峋 掇 嬴 肽 恸 儆 觎 罄 咣 缈 荻 艮 搽 柩 笞 殒 觊 颧 昱 垩 樽 啐 榉 暹 骛 犷 獠 诨 铰 犟 螨 蜇 钍 痿 犄 饯 馥 鲟 绉 搡 崴 孑 麋 铤 锷 嗲 胛 噘 霰 揄 娣 薏 咿 嗪 轱 咩 苣 盥 弑 怩 讴 慵 杵 诌 胴 钴 醛 剐 燧 铉 忸 锃 蜊 绌 肓 莅 裱 靥 渚 痨 篾 遨 痂 绦 俎 氩 烃 嬷 肱 鸢 砣 诓 姘 婕 砒 羯 浃 褓 仃 泷 俳 孱 屐 掮 鸨 哐 腱 襁 嗄 苜 砝 颞 忤 吡 缛 羟 聒 髋 铵 蹼 鳕 噱 鲶 抻 阡 稔 佻 藿 绱 锶 酩 恹 篑 肼 讧 靛 侩 莜 莴 逖 绔 鳟 纰 桉 髂 醚 蜍 钹 纨 牦 锒 趸 芫 擤 鬣 堀 鳏 疝 揶 囹 螈 膈 赅 桡 疖 栀 槲 硷 圄 掴 貉 擀 茱 晟 鲱 徉 洙 锆 蹚 矬 糅 蔻 镫 螯 哞 徜 萘 噌 楸 蜉 铍 荽 傧 哌 呒 缇 蝣 嚯 噻 沆 泔 蓼 癔 泮 醍 醐 杪 猡 鲔 莳 菪 蝾 莨 尻 袴 娈 鲭 珉 荜 铊 玟 鲻 钸 祂 铪 肏 郇 讬 睪 荳 (Non Jun Da chars: 呎 吔 隠 嗞 円 菈 焗 戸 妳 槃 値 巻 彛 蟌 嘢 媞 屌 喆 呯 嘚 渋 晙 沢 牠 咲 卍 吋 旻 穂 艹 甁 嗙 跩 玆 屄 澪 囧 呣 恵)

The remaining 4034 characters were included in MteH v0.1.1.
