import re
import json
# import urllib

from os import read
from boilerpy3.filters import LabelToContentFilter
from bs4 import BeautifulSoup
from boilerpy3 import extractors


def get_paragraphs_BP3(str_text):
  BP_extractor = extractors.DefaultExtractor()    
  text_det = BP_extractor.get_content(str_text)
  return re.split("\n",text_det)

file = open("Fédération Française des Échecs.html")
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
out_file.close()