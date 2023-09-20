import requests
import smtplib
from bs4 import BeautifulSoup

product_endpoint = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8"
}

desired_price = 100.00

response = requests.get(url=product_endpoint, headers= header)
content = response.text

soup = BeautifulSoup(content, "html.parser")

#product price
prices = soup.select(".a-price .a-offscreen")
price_list = [price.getText() for price in prices]
product_price = price_list[0]
print(product_price)

#product name
p_names = soup.select("#productTitle", class_="product-title-word-break")
product_list = [name.getText() for name in p_names]
product = product_list[0]


#converting the prize in float
main_price = float(product_price.replace("$", ""))
print(main_price)


#Sending mail when the selling price is the desired price 

if main_price <= desired_price:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("{sender}", "{key}")
    message = f"Subject: Amazon\n\nHurray!\n\nThe Price of {product} is now {product_price}\n\nNow you can buy it by clicking the link below\n\n {product_endpoint}".encode("utf-8")
    s.sendmail("{sender}", "{reciever}", message)
    print("mail sent")
    s.quit()
else:
    print("Current price is higher than the desired price")
