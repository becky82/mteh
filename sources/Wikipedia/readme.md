A top-10000 most frequenct Chinese character list for Wikipedia (2015) was downloaded from [Chinese Character Frequencies](https://czielinski.github.io/hanzifreq/hanzifreq/output/frequencies.html) (which was generated using [hanzifreq](https://github.com/czielinski/hanzifreq)), giving `Wikipedia_chars_frequency_order.txt` (10000 chars).

We use `opencc -c t2s.json -i Wikipedia_chars_frequency_order.txt | perl -CSD -lane 'print "$F[0] $F[1]" if $F[0] =~ /^[\x{4E00}-\x{9FFF}]$/' | awk '{count[$1]+=$2} END {for (c in count) print c, count[c]}' | sort -k2,2nr` (which uses [OpenCC](https://github.com/BYVoid/OpenCC)) to convert to simplified, giving `Wikipedia_chars_frequency_order_simplified.txt` (7599 chars).

Then we select the top-5000 characters using `head -n 5000 Wikipedia_chars_frequency_order_simplified.txt | awk '{print $1}' | LC_ALL=C sort -u`, giving `Wikipedia_chars_top5000_unicode_order.txt` (5000 chars).
