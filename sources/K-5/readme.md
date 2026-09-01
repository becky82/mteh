The file `K-5 Word Frequency Dictionary Bands XLS format.xls` was originally sourced from `mandarininstitute.org`, but this link seems broken now.  The word list is stored in `K5_words_original_order.txt` (3349 words), after correcting the "lookalike character" 丟 [#2851] to 丢.

The command `grep -oP '[\p{Han}]' K5_words_original_order.txt | sort -u` was used to extract the characters therein, giving `K5_chars_unicode_order.txt` (1817 chars).
