import requests
import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

tag = st.selectbox('choose a topics',['love','humor','life','books']) 
generate = st.button("Generate CSC")
url = f"https://quotes.toscrape.com/tag/{tag}/"
st.write(url)
res= requests.get(url)
st.write(res)
conten= BeautifulSoup(res.content ,'html')
quotes = conten.find_all('div',class_ = 'quote')
#st.write(quotes)
#st.code(conten)
quotes_file = []
for quote in quotes:
    text= quote.find('span',class_='text').text
    author= quote.find('small', class_= 'author').text
    link = quote.find('a')
    st.success(text)
    st.write(author)
    st.markdown(f"<a href='https://quotes.toscrape.com{link['href']}/'>{author}</a>", unsafe_allow_html=True)
    #st.code(f"https://quotes.toscrap.com{link['href']}")
    #https://quotes.toscrape.com/author/Andre-Gide/
    quotes_file.append([text,author,link['href']])

if generate:
    try:
        df = pd.DataFrame(quotes_file)
        df.to_csv('quotes.csv', index=False,header=['Quotes','Author','Link'],encoding='cp1252')
    except:
        st.write('Loading....')