# Note
 
- 一開始的想法是移除大於target的數，但是在處理數列的
  1. 複製
  2. 刪除
  3. index 
    
    有點麻煩所以直接改用暴力解(雙重迴圈)。<br>

- 第一個測資過了但Wrong Answer好幾次分別因為
  1. 0+0=0
  2. 負數
  3. len()<br>

- 之後有一個極大的陣列, 時間直接出局了。<br>
偷看一下hint，發現應該用減法然後用.index()找的速度快很多。<br>
  - 途中又錯了一次因為忘記要把.index()的 start 改為i + 1

不過這仍然還算是暴力解。O()應該還是平方

---
大神們(官方?)的解法是走List的途中順便直接把數字跟index相反存進一個List(Hash Table)，之後直接用index找相減的數字。記憶體用量差不多但速度快到不行...
  - List只走一次
---

