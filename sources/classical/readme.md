We use a classical Chinese frequency list posted by user [叫我小山 at Chinese-Forums](https://www.chinese-forums.com/forums/topic/62647-classical-chinese-frequency-list/), who writes:

> This list was generated from all the texts of the "Pre-Qin and Han" category of the ctext.org website, which includes all of the Classical Chinese corpus prior to the end of the Han dynasty (220 AD). It consists of a base file of 12,236,622 characters. I took this massive data file (5,609 pages!) and sorted it using a character frequency counter online. This method found approximately 14,000 unique characters. After cleaning the data for non-Chinese characters (, . ? ! 1 @ # [ 。、) and etc., I was left with a frequency-sorted list of 13,673 unique characters.

We extract the characters using `awk -F'\t' '$1 ~ /^[一-龥]$/ {print $1}' "Classical Chinese Frequency List.txt"`, giving `classical_original_order.txt` (12403 chars).

The command `head -n 2000 classical_original_order.txt | opencc -c t2s.json | grep -o . | sort -u` (which uses [OpenCC](https://github.com/BYVoid/OpenCC)) was used to select the top-2000 characters, convert to simplified, and sort and remove duplicates, which reduced the number of characters by 63 - 31 = 32:

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

This resulted in `classical_top2000_simplified_unicode_order.txt` (1968 chars).
