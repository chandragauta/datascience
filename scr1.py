import requests
from bs4 import BeautifulSoup
import smtplib
import time
while True:
    re = requests.get('https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')
    res = re.content
    soup = BeautifulSoup(res,'html')
    price = float(soup.find('p',class_='price_color').text[1:])
    if price < 60:
        smt = smtplib.SMTP('smtp.gmail.com',587)
        smt.ehlo()
        smt.starttls()
        smt.login('moon0411134@gmail.com','cabhhotenhzkdaps')
        smt.sendmail('moon0411134@gmail.com',
                    'moon0411134@gmail.com',
                    f"subject:price notifier\n\n hI PRICE IS DROP TO {price},buy it")
    smt.quit()
    time.sleep(24*60*60)
