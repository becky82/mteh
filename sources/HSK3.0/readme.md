The HSK3.0 syllabus follows the official standards ([pdf](http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202103/W020210329527301787356.pdf)); a version with the watermark removed was [posted on Reddit](www.reddit.com/r/ChineseLanguage/comments/mji9tz/heres_a_version_of_that_hsk_30_standards_pdf_with/) ([pdf](https://ia803408.us.archive.org/28/items/chinese-standards-no-watermark/Chinese_standards_no_watermark.pdf)).

The number of words are:

- level 1: 500 words
- level 2: +772 words [1272 total];
- level 3: +973 words [2245 total];
- level 4: +1000 words [3245 total];
- level 5: +1071 words [4316 total];
- level 6: +1140 words [5456 total];
- level 7-9: +5636 words [11092 total].

For the HSK3.0, there are separate word and character lists.  The number of characters in the character lists are:

- level 1: 300 words
- level 2: +300 words [600 total];
- level 3: +300 words [900 total];
- level 4: +300 words [1200 total];
- level 5: +300 words [1500 total];
- level 6: +300 words [1800 total];
- level 7-9: +1200 words [3000 total].

These HSK7-9 characters (29) do not appear in the word lists:

> 冯 刘 吕 吴 唐 孔 孟 宋 州 曹 杭 欧 沪 洲 浙 浦 淮 渝 潘 澳 秦 粤 蜀 袁 赵 邓 郭 韩 魏

All 3000 characters are included in the MteH corpus.

This is a relatively new corpus (at the time of writing), and there are multiple sources for the vocabulary and characters:

- https://github.com/ivankra/hsk30
- https://github.com/drkameleon/complete-hsk-vocabulary
- https://github.com/krmanik/HSK-3.0
- https://github.com/tonghuikang/HSK-3.0-words-list
- https://github.com/elkmovie/hsk30

Many of them used OCR of the above pdfs to obtain the vocabulary lists, which may result in bugs, but we can cross-check them against each other to debug.  Nowadays all the OCR bugs seem to have been weeded out.

When working with HSK3.0 data sets, we need to be careful:

1. Some words are like this:

```
爸爸|爸
弟弟|弟
哥哥|哥
姐姐|姐
零|〇
妈妈|妈
妹妹|妹
有时候|有时
那时候|那时
这时候|这时
```

2. Some are like this:

```
第（第二）
们（朋友们）
有（一）些
子（桌子）
家（科学家）
老（老王）
头（里头）
小（小王）
有（一）点儿
初（初一）
化（现代化）
性（积极性）
员（服务员）
者（志愿者）
差（一）点儿
品（工艺品）
好（不）容易
界（文艺界）
力（影响力）
长（秘书长）
族（上班族）
度（知名度）
非（非金属）
感（责任感）
率（成功率）
茅台（酒）
业（服务业）
```

3. And these two are like this:

```
…极了
…分之…
```

4. There are duplicates (e.g., 一下儿 is both a HSK1 word [#434] and a HSK5 word [#893]):

`一下儿 一会儿 下 且 两 为 之 了 任 会 传 信 倒 倒车 像 关 冲 出口 分 划 则 别 刻 副 卡 卷 只 叫 吐 命 哄 哪 啊 喂 回 圈 土 地 地方 地道 多 大意 头 好 实在 对 封 尽 局 干 并 应 当 待 得 怕 怪 成 成年 所 扇 才 打 批 把 报 担 拧 挑 挺 排 支 散 料 晃 本 横 次 正 毛 涨 火 炸 牛 生 痛 白 盘 省 看 着 码 种 空 站 等 签 米 精神 系 结 结果 编辑 缝 老 背 节 花 落 蒙 行 要 该 调 转 转动 过 过去 还 那 重 长 闷 露 首 麻`

5. Then there's 儿话音 (-儿 suffix) which is mostly optional.

(And there's also punctuation which needs to be accounted for.)

----

There are also handwriting lists, but those characters are all in the HSK character lists:

|               | HSK1       | HSK2       | HSK3       | HSK4       | HSK5       | HSK6       | HSK7-9       |
|---------------|------------|------------|------------|------------|------------|------------|--------------|
| Elementary    | 273        | 24         | 3          | 0          | 0          | 0          | 0            |
| Intermediate  | 27         | 262        | 67         | 26         | 12         | 6          | 0            |
| Advanced      | 0          | 12         | 220        | 161        | 87         | 20         | 0            |

