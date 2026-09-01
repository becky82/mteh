The SUBTLEX dataset is provided as supplementary data for the paper:

> Qing Cai and Marc Brysbaert, "SUBTLEX-CH: Chinese Word and Character Frequencies Based on Film Subtitles", PLoS One, 2010.

It can be downloaded from [here](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010729).

The file `SUBTLEX-CH-CHR` therein contains character frequencies, but is encoded using GBK (not Unicode).  By opening the raw file in the Firefox browser, and copy/pasting the result to a text file, we can obtain a Unicode version, namely `SUBTLEX-CH-CHR_converted_to_unicode.txt`.  The top-4500 characters were extracted using `tail -n +4 SUBTLEX-CH-CHR_converted_to_unicode.txt | head -n 4500 | cut -f1 | sort -u`, giving `SUBTLEX_chars_top4500_unicode_order.txt`

[OpenCC](https://github.com/BYVoid/OpenCC) was used to identify traditional characters via the command `paste SUBTLEX_chars_top4500_unicode_order.txt <(opencc -c t2s.json -i SUBTLEX_chars_top4500_unicode_order.txt) | awk '$1 != $2 {print $1}'`.  It found the following characters (38):

> 乾 來 傢 內 凱 勛 吳 唸 噓 夥 孫 屍 張 後 徵 徹 捱 摺 於 朧 東 濃 煥 癒 竊 給 練 臺 菸 蝦 錫 鍔 鎬 鑽 餌 魯 鯊 鯨

These were removed using `opencc -c t2s.json -i SUBTLEX_chars_top4500_unicode_order.txt | sort -u` but 乾 (as in 乾隆) and 噓 (as in “嘘”了一声) are also simplified characters, so they were manually added back in.

This left 4464 unique characters, as in `SUBTLEX_chars_top4500_simplified_unicode_order.txt`.
