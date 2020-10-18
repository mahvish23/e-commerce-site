def get_price(url):
    import requests
    from bs4 import BeautifulSoup
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    if "www.flipkart.com"  in url:
        d= soup.find("div",{'class':'_1vC4OE _3qQ9m1'}).get_text()
        n=soup.find("span",{'class':'_35KyD6'}).get_text()
        price=(d[1:])
    
    elif "amazon.in" in url:
        headers = {'User-Agent':'Monzilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


        tag_name = "span"
        query = {"class": "a-size-medium a-color-price priceBlockBuyingPriceString", "id": "priceblock_ourprice"}
        response = requests.get(url, headers=headers)
        content = response.text
        soup = BeautifulSoup(content,"html.parser")
        price =soup.find_all(tag_name, query)[0].get_text().replace(",","")
        price=price[2:len(price)-3]
        print(price)
        n=soup.find("span",{"class":"a-size-large"}).get_text().strip()
        
   
    print(price)
    p=(price,n)
    
    return(p)
