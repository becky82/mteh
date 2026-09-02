[Jun Da's modern corpus](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO) was the source of `JunDa_modern_chars_original_order.txt`.  The top 5000 were extracted and sorted according to Unicode using `head -n 5000 JunDa_modern_chars_original_order.txt | sort -u`, giving `JunDa_modern_top5000_unicode_order.txt` (5000 chars).  The command `cat JunDa_modern_top5000_unicode_order.txt | opencc -c t2s | sort -u` (which uses [OpenCC](https://github.com/BYVoid/OpenCC)) removes what it considers non-simplified characters

> 乾 夥 後 徵 捱 摺 於 榘 種 結 經 腎 與 藥 虛 補 視 變 質 這 過 醫 鏡 長 間 陰 陽 類 體 麽 黃

giving `JunDa_modern_top5000_simplified_unicode_order.txt` (4969 chars).
