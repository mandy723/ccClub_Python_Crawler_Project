# 無尾熊存股法-挑選適合長抱的尤加利樹  (Ref.[PPT](https://drive.google.com/file/d/1NW5nBBQinVo4j0_WFGjpFUUFkPRvsOo8/view?usp=sharing))
> Join the [ccClub Python Study Group](https://www.ccclub.io) and completed this project with other members

The project was about creating a web page which automatically crawls and analysis database from the other stock market web and provides stock ranking according to the user-determined weights of each index.

（使用者可在此網站上自行決定股票各項指標之權重，找出合適的前100名推薦存股）

## 實作方式主要為兩大部分：
### [資料處理]
- 利用 Python+Selenium 至[台灣股市資訊網](https://goodinfo.tw/StockInfo/index.asp)爬取最近10年的各項股票指標資料
- 使用 Panda 套件整理上述資料，再使用一套分析方法計算出所有股票在各項指標的分數，並匯出成 CSV 檔供 Django 使用
### [HTML顯示]
以下步驟皆在 Django 內完成：
- 在 "templates > hello_django.html" 檔案，完成 HTML 之 UI 顯示（含使用者輸入畫面、輸出結果畫面）
- 在 "musics > views.py" 檔案，使用 post 方式獲取使用者在前端所選取的各項指標權重，再與 Panda 算出之相對應的股票指標分數做加權運算
- 即算出「權重值 * 指標分數」，最後以加權平均數為排名輸出最推薦的前一百名股票到 HTML

## 待優化：
### [爬蟲]
能因應股市資料的變動設定工作排程定期抓取最新數據更新於網頁

### [網頁]
- 可篩選特定欄位（例如：只顯示特定股價範圍的股票）
- 點選網頁表格的各項指標名稱，可以升降序排序
- 網頁 UI 的優化
