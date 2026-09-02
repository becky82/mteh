Chinese surname frequences are part of the R package [ChineseNames](https://psychbruce.github.io/ChineseNames/), which were sourced via [Github](https://github.com/psychbruce/ChineseNames/blob/main/data-csv/familyname.csv)  The relevant citation here is:

> Bao, H. W. S. (2021). ChineseNames: Chinese Name Database 1930-2008. https://doi.org/10.32614/CRAN.package.ChineseNames 

The dataset is described as:

> It contains nationwide frequency statistics of almost all Chinese surnames and given-name characters, which have covered about 1.2 billion Han Chinese population (96.8% of the Han Chinese population born from 1930 to 2008 and still alive in 2008, i.e., the living household-registered population).

The file `familyname.csv` contains 1806 surnames (63 of which are 2-character surnames: 欧阳, 上官, 皇甫, 令狐, 司徒, ...), from which we use `tail -n +2 familyname.csv | cut -d',' -f1 | perl -CSD -nE 'say for /\p{Han}/g' | LC_ALL=C sort -u > familyname_chars_unicode_order.txt` to extract all the characters, given in `surname_all_chars_unicode_order.txt` (1745 chars).
