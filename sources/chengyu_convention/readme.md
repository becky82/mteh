In 2015, there was a TV show called 《中国成语大会》 "chengyu convention".  I was unable to find the original source for these lists of characters, but it is available online via unofficial sources.

We download the list of "chengyu convention" chengyu: three levels, `chengyu_convention_level1.txt`, `chengyu_convention_level2.txt`, and `chengyu_convention_level3.txt`; we also merge them and sort by Unicode `cat chengyu_convention_level1.txt chengyu_convention_level2.txt chengyu_convention_level3.txt | sort -u` to give `chengyu_convention_chengyu.txt`.  We then extract all the characters using `grep -oP '[\p{Han}]' chengyu_convention_chengyu.txt | sort -u`, giving 2,226 characters as in `chengyu_convention_chars.txt`.

