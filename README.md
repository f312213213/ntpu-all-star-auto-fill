# NTPU all star auto filling

這是一個用 python 寫的程式，用來將參賽者的報名資料從 google 表單上傳至投票網站的 firebase 資料庫。

處理內容包含基本資料與一張照片。

較為麻煩的是照片的部分， google 表單內的照片會以檔案形式存放在雲端硬碟裡，需要先下載到畚箕裡再繼續上傳，而一般的爬蟲也沒辦法直接抓，因此就需要再研究 google api。