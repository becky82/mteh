This corpus was generated from the [Chinese Stack Exchange](https://chinese.stackexchange.com/) data dump:

> Chinese Language Stack Exchange  
> Last uploaded: Jan 05, 2026  
> File size: 39.1 MB 

The command `cat Comments.xml Posts.xml | opencc -c t2s | grep -oP '\p{Han}' | sort | uniq -c | sort -nr | awk '{print $2 " " $1}'` (which uses [OpenCC](https://github.com/BYVoid/OpenCC)) was used on the .xml files to give a character frequency table `ChineseSE_frequency_order.txt` (10597 chars).  The command `head -n 5000 ChineseSE_frequency_order.txt | awk '{print $1}' | sort` was used to get the top 5000 characters.  These were manually removed:

> 䟠 㧡 㧡 㗎 䄏 㳄 㠯 㧯 䟠 㞢 𫗪 𠮶 𠮶 𠮶 々 〻 〇 〡 不 ⺈ ⺍ ⺗ ⺝ 爫 ⺷ ⺼ ⻍

giving `ChineseSE_5000_chars_unicode_order.txt` (4973 chars).
