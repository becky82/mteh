Chih-Hao Tsai has a [Chinese character corpus](https://technology.chtsai.org/charfreq/) sourced from Usenet newsgroups during 1993-1994; we use the [1994 version](https://technology.chtsai.org/charfreq/94charfreq.html), as in `Tsai_chars_frequency_order.txt` (13053 chars).  It includes both simplified and traditional characters.

We use the command `opencc -c t2s.json -i Tsai_chars_frequency_order.txt | awk '{count[$1]+=$2} END {for (c in count) print c, count[c]}' | sort -k2,2nr` (which uses [OpenCC](https://github.com/BYVoid/OpenCC) to convert to simplified) to convert to simplified, giving `Tsai_chars_frequency_order_simplified.txt` (12748 chars).  Then we select the top-5000 characters using `head -n 5000 Tsai_chars_frequency_order_simplified.txt | awk '{print $1}' | LC_ALL=C sort -u`, giving `Tsai_chars_top5000_unicode_order.txt` (5000 chars).

Then we manually delete

> 㐷 㑩 䜣 兀 𨱍 𪱷 𪸩 𫉄 𫚖 𫜬 𫟻 𫟼

The character 兀 (U+FA0C, which we delete) was counted separately to 兀 (U+5140) in the original dataset.  This left 4988 characters.
