import urllib
import glob
import urllib.request
import json
import re
import os.path


from os import read
from bs4 import BeautifulSoup

INITIAL_ID = 30005
LAST_ID = 30015

def dowload_all_page():
    for i in range(INITIAL_ID,LAST_ID):
        link = 'http://echecs.asso.fr/FicheTournoi.aspx?Ref='+str(i)+''
        page = urllib.request.urlopen(link)
        soup = BeautifulSoup(page.read(), 'html.parser')
        file = open("sample/tournoi"+str(i)+".html","w",encoding="utf8", errors='ignore')
        file.write(str(soup))
        file.close()

def scraping_all_page():
    dictTournoi = {}
    id = INITIAL_ID
    for chemin in glob.glob("sample/*"):
        basename = os.path.splitext(os.path.basename(chemin))
        print(basename)
        file = open(chemin, encoding="utf8", errors='ignore')
        soup = BeautifulSoup(file.read(), 'html.parser')
        file.close
        allTd = soup.find_all("td")
        text = []
        for word in allTd:
            text.append(word.text)
        text = list(filter(None,text))
        dict = {}
        for word in text:
            if len(word)==0:
                print(word)
            else :
                if word is not text[-1]:
                    if ':' in word:
                        inext = text.index(word)+1
                        word = word.strip(':')
                        dict[word]= text[inext]
        
        dictTournoi[id] = dict
        id += 1

    out_file = open("JSON.json", "w", encoding="utf-8") 
    json.dump(dictTournoi, out_file, indent = 4, sort_keys = False, ensure_ascii=False) 
    out_file.close()

dowload_all_page()
scraping_all_page()
