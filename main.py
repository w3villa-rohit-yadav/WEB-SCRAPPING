import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/s?k=bike"
proxies = {
    "http" : "http://181.10.736.783"
}
response = requests.get(url, proxies=proxies)
soup = BeautifulSoup(response.text , "html.parser")
# print(soup.find_all(class_="KzDlHZ"))
for data in soup.find_all(class_="a-size-base-plus a-color-base a-text-normal") :
    print(data.text)
for data in soup.find_all(class_="a-price-whole") :
    print(data.text)

