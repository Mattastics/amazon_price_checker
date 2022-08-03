from bs4 import BeautifulSoup
import requests
import smtplib

HEADERS = {"Accept-Language": "en-US,en;q=0.9",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                         "101.0.4951.67 Safari/537.36"}

URL = "https://www.amazon.com/dp/B08BY1JWHG/?coliid=I3I18RJTIDVI4H&colid=3W1VRL70OXCLJ&psc=1&ref_=lv_ov_lig_dp_it"

BUY_PRICE = 55

USER = "***********@gmail.com"
PASSWORD = "*****************"

response = requests.get(
    url=URL, headers=HEADERS)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
item = soup.find(class_="a-size-large product-title-word-break").getText()
price_list = soup.find(class_="a-offscreen").getText().split("$")
price = float(price_list[1])


if price < BUY_PRICE:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=USER, password=PASSWORD)
    connection.sendmail(from_addr=USER,
                        to_addrs=USER,
                        msg=f"Subject:Price Drop on {item}! \n \n {item} is on sale for"
                            f" {price} at {URL}!")
