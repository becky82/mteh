The SUBTLEX dataset is provided by the paper Qing Cai and Marc Brysbaert, "SUBTLEX-CH: Chinese Word and Character Frequencies Based on Film Subtitles", PLoS One, 2010.  It can be downloaded from [here](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010729).

The file SUBTLEX-CH-CHR contains character frequencies, but is encoded using GBK.  By opening the raw file in the Firefox browser, and copy/pasting the result to a text file, we can obtain a Unicode version of the SUBTLEX-CH-CHR.

From the top-4500 characters in SUBTLEX-CH-CHR, [OpenCC](https://github.com/BYVoid/OpenCC) was used to identify traditional characters and convert them to simplified.  It found the following characters (38):

> 乾 來 傢 內 凱 勛 吳 唸 噓 夥 孫 屍 張 後 徵 徹 捱 摺 於 朧 東 濃 煥 癒 竊 給 練 臺 菸 蝦 錫 鍔 鎬 鑽 餌 魯 鯊 鯨

This left 4462 unique characters, namely `SUBTLEX_chars_top4500_simplified_unicode_order.txt`.

The remaining 4034 characters were included in MteH v0.1.1.
