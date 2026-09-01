[Chinese Knowledge and Information Processing](https://ckip.iis.sinica.edu.tw/) (CKIP) is:

> The CKIP (Chinese Knowledge and Information Processing) group is a research team formed by the Institute of Information Science and the Institute of Linguistics of Academia Sinica in 1986. Its purpose is to establish a fundamental research environment for Chinese natural language processing.

The file `CKIP_traditional.txt` is the vocab list (20769 traditional Chinese words) posted in the discussion for the Wikipedia page [Appendix:Mandarin Frequency lists](https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists).  We use the command `opencc -c t2s -i CKIP_traditional.txt | grep -oP '[\p{Han}]' | sort -u` (which uses [OpenCC](https://github.com/BYVoid/OpenCC)) to extract the characters and convert them to simplified, giving `CKIP_chars_unicode_order.txt` (3392 total).
