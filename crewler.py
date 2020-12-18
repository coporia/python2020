# 抓取網頁原始碼
import urllib.request as req
url="https://www.ptt.cc/bbs/PokeMon/index.html"
#模仿使用者,建立一個request物件
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
    #解析原始碼
    import bs4
    root=bs4.BeautifulSoup(data ,"html.parser")
    # print(root.title.string)
    titles=root.find_all("div", class_="title") #尋找標籤class=tile的"div"標籤
    for title in titles:
        if title.a != None:
            print(title.a.string)