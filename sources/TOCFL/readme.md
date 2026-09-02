Taiwan's TOCFL has a list of 3100 traditional characters, which we souce from [Github](https://github.com/PSeitz/tocfl/tree/main) (named `Chinese_Character_List_111-09-20.xlsx`), who reports sourcing it from [this official source](https://coct.naer.edu.tw/download/tech_report/) although that link seems broken now.  We save the original character list as `TOCFL_chars_original.txt`.  In this file, there are these lines:

    台／臺
    裡／裏
    真／眞
    床／牀
    雞／鷄
    麵／麪
    著／着
    朵／朶
    煙／烟
    舉／擧
    污／汙
    卻／却
    值／値
    強／强
    群／羣
    躲／躱
    濕／溼
    抬／擡
    妝／粧
    峰／峯
    晒／曬
    慎／愼
    飢／饑
    啟／啓
    脣／唇
    痴／癡
    鉢／缽
    蹤／踪
    豔／艷
    傭／佣
    舖／鋪
    薦／荐
    鑑／鑒

So this results in 3133 traditional characters in total.  We use the command `sed 's|／|\n|g' TOCFL_chars_original.txt | opencc -c t2s.json | sort -u` to convert the traditional characters to simplified using [OpenCC](https://github.com/BYVoid/OpenCC).  These characters mapped to duplicate simplified characters (206 traditional -> 100 simplified):

    后: 後, 后
    台: 台, 臺, 颱
    家: 家, 傢
    几: 幾, 几 
    里: 裡, 裏, 里
    出: 出, 齣
    只: 只, 隻
    念: 念, 唸
    面: 面, 麵, 麪
    真: 真, 眞
    钟: 鐘, 鍾
    回: 回, 迴
    床: 床, 牀
    系: 係, 系, 繫
    准: 準, 准
    鸡: 雞, 鷄
    向: 向, 嚮
    局: 局, 侷
    表: 表, 錶
    喂: 喂, 餵
    游: 游, 遊
    发: 發, 髮
    周: 週, 周
    折: 折, 摺
    注: 注, 註
    舍: 舍, 捨
    干: 乾, 幹
    酸: 酸, 痠
    板: 闆, 板
    签: 簽, 籤
    布: 布, 佈
    烟: 煙, 烟, 菸
    污: 污, 汙
    困: 困, 睏
    并: 並, 併
    制: 制, 製
    幸: 幸, 倖
    却: 卻, 却
    强: 強, 强
    复: 復, 複
    须: 須, 鬚
    群: 群, 羣
    历: 曆, 歷
    湿: 濕, 溼
    丑: 醜, 丑
    松: 鬆, 松
    脏: 髒, 臟
    志: 志, 誌
    冲: 沖, 衝
    彩: 彩, 綵
    采: 採, 采
    恶: 惡, 噁
    叹: 嘆, 歎
    尝: 嘗, 嚐
    赞: 讚, 贊
    巨: 巨, 鉅
    伙: 伙, 夥
    凶: 兇, 凶
    划: 划, 劃
    托: 托, 託
    占: 佔, 占
    佛: 佛, 彿
    谷: 谷, 穀
    刮: 刮, 颳
    卷: 卷, 捲
    胡: 胡, 鬍
    致: 致, 緻
    峰: 峰, 峯
    晒: 晒, 曬
    症: 症, 癥
    斗: 鬥, 斗
    欲: 欲, 慾
    愈: 愈, 癒
    迹: 跡, 蹟
    尽: 盡, 儘
    征: 徵, 征
    获: 獲, 穫
    扎: 扎, 紮
    泛: 泛, 氾
    范: 范, 範
    秘: 祕, 秘
    饥: 飢, 饑
    启: 啟, 啓
    梁: 梁, 樑
    唇: 脣, 唇
    雇: 雇, 僱
    汇: 匯, 彙
    痴: 痴, 癡
    钵: 鉢, 缽
    蒙: 蒙, 濛, 矇
    荡: 蕩, 盪
    踪: 蹤, 踪
    苏: 蘇, 甦
    艳: 豔, 艷
    奸: 奸, 姦
    佣: 傭, 佣
    哗: 嘩, 譁
    弥: 彌, 瀰
    荐: 薦, 荐
    鉴: 鑑, 鑒

Thus we obtain a list of 3100 + 33 - 106 = 3027 distinct simplified characters, saved in `TOCFL_simplified_chars_unicode_order.txt` (3027 chars).
