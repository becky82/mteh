[THUOCL](https://github.com/thunlp/THUOCL) (Tsinghua University Open Chinese Lexicon) is a Chinese word frequency corpus.  It enumerates the number of times words appear within documents sourced from CSDN博客 (blogs; 3,785,976 docs), 新浪新闻 (news 8,421,097), and 搜狗语料 (Chinese text corpus; 729,008,561 webpages), totally 741 million documents.

We select the words that occur in 7410 documents (i.e., at least 1 in 100000 documents), and extract the characters therein.  Traditional characters were converted to simplified using [OpenCC](https://github.com/yichen0831/opencc-python).  This gave a list of 1923 characters.

The characters (26) excluded from MteH v0.1.1 are:

> 俪啫岚栩汶沓炔禺糌耦茭茼莴薏蛳蜇讴豉踵蹴酚醛铤鳕鸰鹡

The remaining 1897 characters are included in MteH v0.1.1.
