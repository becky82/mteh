The 3500 most frequent characters were sourced from [Jun Da's modern corpus](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO).

- The character 於 [#2025] is normally the traditional character for 于 [#40], so it was excluded;
- The character 麽 [#2725] is normally the traditional character for 么 [#63], so it was excluded;
- The character 後 [#2131] is normally the traditional character for 后 [#48], so it was excluded.

The least frequent character we include in MteH v0.1.1 is 萃, which occured 1032 times within Jun Da's 193504018 character corpus, or in other words, it occurs once every 187504 characters.

The threshold 3500 is fairly arbitrary, so to get an idea of what this omits, the first 200 characters in Jun Da's corpus that is not in MteH v0.1.1 are the following:

> 於 玑 後 藩 岚 麽 雯 毓 瑛 禺 霖 忒 谟 焘 侬 绫 镕 钊 伢 陇 琛 倭 鞅 敕 幡 祺 俾 聿 剌 顼 哝 钵 铢 俟 胥 醫 渭 珂 哧 迥 噶 淄 踞 韬 蹑 谑 诃 铎 荀 攫 踵 臆 瘢 豢 汶 惴 桢 藥 衹 饬 栩 曦 梓 嗖 浚 荃 汾 奂 傩 沂 嵋 瑾 赓 佚 沓 蛊 璐 晏 漳 琏 辘 僭 褚 煜 骥 嗳 祯 湍 轲 钡 箓 涸 亘 筵 欤 颍 稷 恻 邯 珥 俸 鸾 犊 扈 鋆 谀 岐 猓 蔷 遽 恚 皑 锵 簌 鹳 睽 寰 唷 诰 恣 婵 蹙 诙 罡 胤 皋 嫔 娓 坂 町 瘠 啜 瓒 龛 髯 瞠 潼 酰 筱 甬 淞 蕙 郸 轶 荪 麝 醮 湮 穑 呷 萼 伫 岬 鳎 啾 徇 徵 岱 邙 恫 怆 桀 盂 桧 芮 闩 铿 窠 牒 赈 嗫 鞑 袤 谌 徨 橹 嵇 圪 髻 嗬 辎 谄 蛐 鹞 翱 蓿 鳗 鲇 這 嚅 颔 黜 黠 濑 洵 砥 咂 匝 偃 淙

Some characters were manually excluded, despite being relatively high up in Jun Da's corpus.

Another frequency list I've used is from [HanziCraft](https://hanzicraft.com/lists/frequency) which appears to be a modified version of Jun Da's modern corpus.  For the 3500 characters relevant to MteH v0.1.1, HanziCraft adds 乓, 匾, 吝, 揖, 觑, 贻 not present in Jun Da's corpus (all included in MteH v0.1.1).  It also removes 彷, 後, 於 which are seldom-to-never used as simplified characters (not included in MteH v0.1.1), and also 甚, 著, 藉, 覆 but these are commonly used in simplified words like 甚至, 著名, 狼藉, 覆盖, respectively, so they are included in MteH v0.1.1.
