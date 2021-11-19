import urllib
import glob
import urllib.request
import json

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
    for chemin in glob.glob("sample/*"):
        file = open(chemin, encoding="utf8", errors='ignore')
        soup = BeautifulSoup(file.read(), 'html.parser')
        file.close
        allTd = soup.find_all("td")
        
        text = []
        for word in allTd:
            text.append(word.text)

        print(text)
        dict1 = {}
        text = list(filter(None,text))
        for word in text:
            if len(word)==0:
                print(word)
            else :
                if word is not text[-1]:
                    if ':' in word:
                        print(word)
                        inext = text.index(word)+1
                        word = word.strip(':')
                        dict1[word]= text[inext]

        print(dict1)

        out_file = open("test1.json", "w", encoding="utf-8") 
        json.dump(dict1, out_file, indent = 4, sort_keys = False, ensure_ascii=False) 
        out_file.close()



dowload_all_page()
scraping_all_page()

"""file = open("Fédération Française des Échecs.html")
soup = BeautifulSoup(file.read(), 'html.parser')

#print(str(soup))

print(soup.find_all('td'))

text = get_paragraphs_BP3(str(soup))

dict1 = {}

text = list(filter(None,text))

for word in text:
    if len(word)==0:
        print(word)
    else :
        if word is not text[-1]:
            if ':' in word:
                inext = text.index(word)+1
                word = word.strip(':')
                dict1[word]= text[inext]
print(dict1)

    

out_file = open("test1.json", "w") 
json.dump(dict1, out_file, indent = 4, sort_keys = False, ensure_ascii=False) 
out_file.close()"""