[Jun Da's modern corpus](https://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=MO) was the source of `JunDa_modern_chars_original_order.txt`.  The top 4500 were extracted and sorted according to Unicode using `head -n 4500 JunDa_modern_chars_original_order.txt | sort -u`, giving `JunDa_modern_top4500_unicode_order.txt`.  [OpenCC](https://github.com/BYVoid/OpenCC) was used to identify traditional characters via the command `paste JunDa_modern_top4500_unicode_order.txt <(opencc -c t2s.json -i JunDa_modern_top4500_unicode_order.txt) | awk '$1 != $2 {print $1}'`, which listed 15 characters:

> 乾 後 徵 捱 摺 於 榘 經 與 藥 這 過 醫 體 麽

We keep 乾 (it's used in simplified Chinese, e.g. 乾隆), and manually delete the other characters, giving `JunDa_modern_top4500_simplified_unicode_order.txt` (4486 chars).
