The Beijing Language and Culture University (BLCU) corpus is a 15-billion character "balanced" word corpus from a variety of written sources.  The relevant paper is:

> 荀恩东, 饶高琦, 肖晓悦, 臧娇娇, *大数据背景下 BCC 语料库的研制*, 语料库语言学, 2016 ([pdf](https://bcc.blcu.edu.cn/downloads/papers/%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%83%8C%E6%99%AF%E4%B8%8BBCC%E8%AF%AD%E6%96%99%E5%BA%93%E7%9A%84%E7%A0%94%E5%88%B6_%E8%8D%80%E6%81%A9%E4%B8%9C.pdf)).

The data used was from [Pleco Forums](https://www.plecoforums.com/threads/word-frequency-list-based-on-a-15-billion-character-corpus-bcc-blcu-chinese-corpus.5859/), and in particular the "global" corpus `global_wordfreq.release_UTF-8.txt`.

We use `opencc -c t2s -i global_wordfreq.release_UTF-8.txt | perl -CSD -lane '$w=$F[0]; $n=$F[1]; $count{$_}+=$n for $w=~/\p{Han}/g; END { print "$_\t$count{$_}" for sort { $count{$b}<=>$count{$a} } keys %count }'` (which uses [OpenCC](https://github.com/BYVoid/OpenCC)) to generate a character frequency table, namely `BLCU_chars_frequency_order.txt` (12220 chars).

We then use `head -n 5000 BLCU_chars_frequency_order.txt | awk '{print $1}' | sort -u` to get the top-5000 characters from this set, giving `BLCU_6000_chars_unicode_order.txt` (5000 chars).
