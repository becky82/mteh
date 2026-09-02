This corpus is the data for the paper:

> Chang, YN., Hsu, CH., Tsai, JL. et al. A psycholinguistic database for traditional Chinese character naming. Behav Res 48, 112–122 (2016). https://doi.org/10.3758/s13428-014-0559-7

Which is a list of traditional characters `psycholinguistic_original.txt` (3314 chars).  We convert the characters to simplified using `opencc -c t2s.json -i psycholinguistic_original.txt | sort -u` (which uses [OpenCC](https://github.com/BYVoid/OpenCC)), giving `psycholinguistic_simplified_unicode_order.txt` (3255 chars), and the characters `蹻 紬` were manually deleted, leaving 3253 chars,
