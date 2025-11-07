Chinese surname frequences are part of the R package [ChineseNames](https://psychbruce.github.io/ChineseNames/), which were sourced via [Github](https://github.com/psychbruce/ChineseNames/blob/main/data-csv/familyname.csv)  The relevant citation here is:

> Bao, H. W. S. (2021). ChineseNames: Chinese Name Database 1930-2008. https://doi.org/10.32614/CRAN.package.ChineseNames 

The dataset is described as:

> It contains nationwide frequency statistics of almost all Chinese surnames and given-name characters, which have covered about 1.2 billion Han Chinese population (96.8% of the Han Chinese population born from 1930 to 2008 and still alive in 2008, i.e., the living household-registered population).

The file `familyname.csv` contains 1806 surnames (63 of which are 2-character surnames: 欧阳, 上官, 皇甫, 令狐, 司徒, ...), from which we obtain 1745 unique characters.  The following characters (206) are excluded from MteH v0.1.1:

> 於 藩 岚 雯 瑛 霖 侬 钊 陇 琛 祺 剌 顼 俟 胥 珂 铎 荀 汶 曦 梓 奂 瑾 沓 璐 晏 褚 筵 俸 扈 岐 婵 罡 皋 啜 筱 郸 桀 芮 谌 嵇 闾 熠 隽 萱 胭 澹 郅 弋 宓 蟠 濮 臧 霭 睢 忻 宸 栾 晁 孛 骁 莘 芷 掇 嬴 苻 钰 斛 烨 弁 郏 骈 寮 淼 淦 苫 滢 锟 馥 邝 姣 晗 恽 霰 贲 昕 佘 翦 讴 郧 铉 峁 骞 杲 莅 羿 炜 弭 俎 隗 婕 泷 庾 蒯 辇 玮 蹇 钤 苌 琰 雒 莒 穰 谯 钏 旃 邬 鄯 姒 笪 菅 乜 鄢 蔺 笮 郓 焱 雎 笱 晟 颛 厍 轸 薜 柘 聃 綦 芊 亓 钭 婧 陟 冼 邰 逯 鄞 庹 甯 泮 逄 楮 殳 肜 姝 邳 璩 苒 訾 蘧 阚 缑 戢 芈 哓 郜 葸 佴 隰 昃 呙 剡 仵 昝 郗 貊 迮 镡 琚 茆 蓁 郤 郄 邴 邾 鬲 仝 瘳 茌 郇 眭 郐 仉 贠 蒉 稂 祃 翚 轷 (Non Jun Da chars: 缐 璟 撖 喆 玥 垚 禚 犇)

The remaining characters (1539) are included in MteH v0.1.1.
