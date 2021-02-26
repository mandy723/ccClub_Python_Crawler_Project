from django.shortcuts import render
import csv

def post(request):

    if request.method == "POST":        #如果是以POST的方式才處理
        GETEPS = request.POST['PEPS']  # 取得表單輸入資料
        GETyield = request.POST['Pyield']
        GETcash = request.POST['Pcash']
        GETstock = request.POST['Pstock']
        GETbata = request.POST['Pbata']
        GETday = request.POST['Pday'] #填權息天數
        GETpercent = request.POST['Ppercent'] #填權息成功率
        GETover = request.POST['Pover'] #三大法人買賣超

        #存取已輸入之權重
        PEPS = GETEPS; Pyield = GETyield; Pcash = GETcash; Pstock = GETstock; Pbata = GETbata
        Pday = GETday; Ppercent = GETpercent; Pover = GETover

        with open('/Users/shuminyang/Desktop/ccProject/Rank2.csv', encoding='utf-8-sig', newline='') as csvfile:
            rows = csv.DictReader(csvfile)
            tree = []
            results = []
            weights = [int(GETEPS), int(GETyield), int(GETcash), int(GETstock),int(GETbata),int(GETday),int(GETpercent),int(GETover)]

            for row in rows:
                tree.append(row['名稱'])
                total = float(row['EPS'])*weights[0] + float(row['DividendYield'])*weights[1] + float(row['CashDividend'])*weights[2] + float(row['StockDividend'])*weights[3] + float(row['beta值'])*weights[4] + float(row['十年填權息平均天數'])*weights[5] + float(row['十年填權息成功率'])*weights[6] + float(row['三大法人買賣超'])*weights[7]
                results.append(total)
            dictionary = dict(zip(tree, results))
            tree = sorted(dictionary.items(), key=lambda d: d[1])

        with open('/Users/shuminyang/Desktop/ccProject/Average_final.csv', encoding='utf-8-sig', newline='') as csvfile:  # 依權重算完的結果產出輸出資料
            d = [] #一次性讀取完所有 Average_final 的資料存到此 list
            rows = csv.DictReader(csvfile)
            for row in rows:
                d.append(row)

            for d1 in d:
                for key, value in d1.items():
                    if key not in ["名稱", "代號"] and len(value) >= 1:
                        d1[key] = round(float(value), 2)

            lst = []
            for (x, y) in tree[0:100]:
                for d1 in d:
                    if d1["名稱"] == x:
                        lst.append(d1)
                        d1["名次"] = tree.index((x, y))+1
                        break

    else:

        with open('/Users/shuminyang/Desktop/ccProject/Rank2.csv', encoding='utf-8-sig', newline='') as csvfile:
            rows = csv.DictReader(csvfile)
            tree = []
            results = []

            for row in rows:
                tree.append(row['名稱'])
                total = float(row['EPS']) + float(row['DividendYield']) + float(row['CashDividend']) + float(row['StockDividend']) + float(row['beta值']) + float(row['十年填權息平均天數']) + float(row['十年填權息成功率']) + float(row['三大法人買賣超'])
                results.append(total)
            dictionary = dict(zip(tree, results))
            tree = sorted(dictionary.items(), key=lambda d: d[1])

        with open('/Users/shuminyang/Desktop/ccProject/Average_final.csv', encoding='utf-8-sig', newline='') as csvfile:  # 依權重算完的結果產出輸出資料
            d = [] #一次性讀取完所有 Average_final 的資料存到此 list
            rows = csv.DictReader(csvfile)
            for row in rows:
                d.append(row)
            for d1 in d:
                for key, value in d1.items():
                    if key not in ["名稱", "代號"] and len(value) >= 1:
                        d1[key] = round(float(value), 2)
            lst = []
            for (x, y) in tree[0:100]:
                for d1 in d:
                    if d1["名稱"] == x:
                        lst.append(d1)
                        d1["名次"] = tree.index((x, y)) + 1
                        break
        mess = "表單資料尚未送出!"
        PEPS = 1; Pyield = 1; Pcash = 1; Pstock = 1; Pbata = 1; Pday = 1; Ppercent = 1; Pover = 1
    return render(request,"hello_django.html",locals())


"""
#select
        post = request.POST
        #input_content = post.get('input_content')
        input_cityid = post.get('PEPS', 0)
        # print(input_cityid)
        # print(input_content)
        city = "1"
        if input_cityid == '0':
            city = "1"
            #params = ('%' + input_content + '%')
            #cursor = connection.cursor()
            #cursor.execute(
                #"SELECT *  FROM `event` where eventTilte like %s", params)
        else:
            if input_cityid == '1':
                city = "2"
            elif input_cityid == '2':
                city = "3"
            elif input_cityid == '3':
                city = "4"
            elif input_cityid == '4':
                city = "5"
            elif input_cityid == '5':
                city = "6"
            elif input_cityid == '6':
                city = "7"
            elif input_cityid == '7':
                city = "8"
            params = ('%' + city + '%')
            cursor = connection.cursor()
            cursor.execute(
                "SELECT *  FROM `event` where eventTilte like %s and eventAddress like %s", params)
        event_list = cursor.fetchall()
        cursor.close()
        content = {'event_list': event_list, 'input_cityid': input_cityid}
"""