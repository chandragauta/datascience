from bs4 import BeautifulSoup
import requests
import smtplib
def main():
    soup = lovely_soup('https://recycledrobot.co.uk')
    #soup = lovely_soup('https://www.publictv.com.np/news/40481')
    print(soup)

def lovely_soup(url):
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'})
    #return BeautifulSoup(r.content, 'lxml')
    ghol = BeautifulSoup(r.content, 'html5lib')
    ghol1= ghol.find('p',class_ ='title is-size-4-desktop is-size-6-touch').text[1:]
    #ghol1= ghol.find('h1').text
    return ghol1


if __name__ == "__main__":
    main()