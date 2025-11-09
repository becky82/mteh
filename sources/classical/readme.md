We use a classical Chinese frequency list posted by user [叫我小山 at Chinese-Forums](https://www.chinese-forums.com/forums/topic/62647-classical-chinese-frequency-list/), who writes:

> This list was generated from all the texts of the "Pre-Qin and Han" category of the ctext.org website, which includes all of the Classical Chinese corpus prior to the end of the Han dynasty (220 AD). It consists of a base file of 12,236,622 characters. I took this massive data file (5,609 pages!) and sorted it using a character frequency counter online. This method found approximately 14,000 unique characters. After cleaning the data for non-Chinese characters (, . ? ! 1 @ # [ 。、) and etc., I was left with a frequency-sorted list of 13,673 unique characters.

From the top 2000 characters therein, we use [OpenCC](https://github.com/BYVoid/OpenCC) to convert traditional characters to simplified:

    丑: 丑醜
    于: 于於
    云: 云雲
    仆: 仆僕
    从: 从從
    余: 余餘
    修: 修脩
    冲: 沖衝
    历: 曆歷
    发: 發髮
    台: 台臺
    后: 后後
    复: 復複
    宁: 寧甯
    尸: 尸屍
    巨: 巨鉅
    干: 乾干幹
    并: 並并
    征: 征徵
    御: 御禦
    愿: 愿願
    斗: 斗鬥
    无: 无無
    游: 游遊
    系: 系繫
    虫: 虫蟲
    谷: 穀谷
    逾: 踰逾
    里: 裏里
    钟: 鍾鐘
    饥: 飢饑

Since multiple traditional characters can map to the same simplified character, this reduced the number of characters by 63 - 31 = 32, leaving 1968 chraracters.  The characters (128) not included in MteH v0.1.1 are:

> 藩 陇 鞅 敕 俟 胥 渭 荀 佚 蛊 晏 僭 轲 颍 稷 邯 鸾 谀 岐 遽 恣 皋 郸 徇 桀 谄 黜 偃 闾 罔 旌 戾 蠡 弋 祐 夙 臧 睢 纣 栾 歆 翊 燔 刍 觯 绾 斛 弁 雉 佗 笞 囿 辔 佞 麋 恽 飨 贲 胪 僖 郢 髡 弑 骞 骊 醴 耦 爰 俎 隗 歙 豕 杼 荥 壅 蹇 闳 恂 郦 雒 莒 穰 圜 巽 曷 驷 醢 诎 掾 廪 颛 繇 轸 寤 雠 筮 嬖 缯 陟 薨 哙 彘 訾 徼 谿 谮 柰 圉 豨 雩 郤 阼 邾 菑 荅 酎 迺 筭 艸 (Non Jun Da chars: 賔 糸 埶 皃 痺 彊 鴈 畤 卬)

The remaining 1840 characters are included in MteH v0.1.1.
