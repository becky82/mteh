The HSK1.0 syllabus 《汉语水平词汇与汉字等级大纲》 lists the Chinese HSK words in the 1.0 standards.  I sourced it from https://gjxy.gpnu.edu.cn/info/1141/1373.htm (uploaded as HSK1.0standards_汉语水平词汇与汉字等级大纲.txt).  The words split into these levels:

- 甲 (basic) levels 1, 2, 3 (1033 words)
- 乙 (elementary) levels 3, 4, 5 (+2018 words [3051 total]) [yes, they overlap]
- 丙 (intermediate) levels 6, 7, 8 (+2202 words [5253 total])
- 丁 (advanced) levels 9, 10, 11 (+3568 words [8821 total])

From here we run into three issues:

1. There are duplicate words in these files:

`一 一下 上 下 两 中 为 之 了 人家 代 任 会 传 信 倒 假 偏 光 关 冲 净 分 分子 划 别 到底 刺 刻 副 包 单 即使 卷 双 反 只 叫 可以 同 吐 呀 呆 哄 哪 啊 喂 回 圈 土 在 地 地方 堆 处 多 头 奔 好 如 学 对 封 将 就 尽 差 帮 干 并 应 张 弹 当 往 得 怕 怪 成 所 才 扒 打 批 把 报 担 拾 挑 挨 挺 排 摊 支 散 数 方 晃 本 来 架 棒 横 次 正 死 每 毒 毛 气 活 滴 灰 炸 点 理 生 画 白 盘 盛 直 省 看 着 硬 种子 空 站 端 等 精神 结 结果 缝 背 能 节 花 落 行 要 觉 角 该 谈话 费 足 距离 转 转动 过 过去 还 遍 道 那 那么 里 重 量 钉 锁 镇 长 闷 陆 除 难 露 非 面 顶 顺 鼓`

2. Some "words" are actually multiple words separated by `/`:

```
*** 甲
法语/法文
连…都/也…
米/公尺
那里/那儿
日语/日文
外语/外文
星期日/星期天
英语/英文
早晨/早上
这里/这儿

*** 乙
阿拉伯语/阿拉伯文
报道/报导
伯父/伯伯
成分/成份
从不/没
德语/德文
胳膊/胳臂
京剧/京戏
老大妈/大妈
老大娘/大娘
老大爷/大爷
礼拜天/礼拜日
利害/厉害
热水瓶/暖水瓶
人才/人材
手绢/手帕
吸烟/抽烟
想像/想象
照片/相片

*** 丙
订婚/定婚
俄语/俄文
身份/身分
账/帐

*** 丁
订购/定购
订货/定货
订阅/定阅
含义/涵义
…来看/…来讲
薪金/薪水
押韵/压韵
赢利/盈利
```

3. Some of the "words" are grammar structures:

```
*** 甲
除了…以外
从…到…
从…起
…得很…
…分之…
…极了…
连…都/也…
一边…一边…
一…就…
…之间…

*** 乙
边…边…
从…出发
当…的时候
…的话…
非…不可
既…也…
既…又…
一…也…
一方面…一方面…
越…越…
越来越…

*** 丙
不是…而是…
不是…就是
到…为止
对…来说
就是…也…
拿…来说
一面…一面
愈…愈…

*** 丁
从…看来
非…才
…来看/…来讲
连…带…
一会儿…会儿…
```

(And there's also punctuation which needs to be accounted for.)

After editing to ensure there's one word per line, then removing duplicates, we get:

- 甲 levels 1, 2, 3 (1005 words)
- 乙 levels 3, 4, 5 (+1971 words [2976 total])
- 丙 levels 6, 7, 8 (+2125 words [5101 total])
- 丁 levels 9, 10, 11 (+3551 words [8652 total])

And if we extract the characters from these words

- 甲 levels 1, 2, 3 (800 words)
- 乙 levels 3, 4, 5 (+804 words [1604 total])
- 丙 levels 6, 7, 8 (+592 words [2196 total])
- 丁 levels 9, 10, 11 (+670 words [2866 total])

The 2866 characters are in HSK1.0_characters.txt.

It turns out I have an old version of the HSK1.0 character list, and I forget where it came from; I call it HSK1.0_characters_mysterious_old_version.txt.  It has these characters `侯冀冯刘匈卢吕吴咋哩啥喧嗓埃埔孟宋岳崔彭戈曹朱桔欧殷沈沪浙淮潘澳秦粤耿聂萨葛蒋袁赫赵邓邢郭陕魏` (+47) but not these characters `啰嗡帕暄涵蔓账镑` (-8); total 2905.


