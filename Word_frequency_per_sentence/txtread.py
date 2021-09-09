from __future__ import unicode_literals
import codecs
from collections import Counter
import re

with codecs.open("stopwords.txt", encoding="utf-8") as f:
        sentences = f.read()
        # sentences = sentences.translate(table)
        sentences = re.sub(r"\d+", " ", sentences)
        # English punctuations
        sentences = re.sub(r"""[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]+""", " ", sentences)
        # Urdu punctuations
        sentences = re.sub(r"[:؛؟’‘٭ء،۔]+", " ", sentences)
        # Arabic numbers
        sentences = re.sub(r"[٠‎١‎٢‎٣‎٤‎٥‎٦‎٧‎٨‎٩]+", " ", sentences)
        sentences = re.sub(r"[^\w\s]", " ", sentences)
        # Remove English characters and numbers.
        sentences = re.sub(r"[a-zA-z0-9]+", " ", sentences)
        # remove multiple spaces.
        sentences = re.sub(r" +", " ", sentences)
        words = sentences.split()
        counter = Counter(words)
        y=dict(counter.most_common())
        text_file = open("stopwords_list.txt", "w",encoding="utf-8")
        for char in y:
                n = text_file.write(str('%s : %d \n' % (char, y[char])))
        text_file.close()

with codecs.open("sample.txt",encoding="utf-8") as f1:
        sentences1 = f1.read()
        # sentences = sentences.translate(table)
        sentences1 = re.sub(r"\d+", " ", sentences1)
        sentences = re.sub(r"[^\w\s]", " ", sentences)
        # remove multiple spaces.
        sentences1= re.sub(r" +", " ", sentences1)
        sentences1 = re.split(r"۔+", sentences1)
        word1=Counter(sentences1)
        count2=list(words)
        i=0
        for value in list(sentences1):
                sentences1[i]=value.split()
                i=i+1
        text_file = open("Deletedwords_list.txt", "w",encoding="utf-8")        
        for value in list(sentences1):
                for value2 in value:
                        if value2 in count2:
                                n = text_file.write(str('%s  \n' % (value2))) 
                                value.remove(value2) 
        text_file.close()
        text_file = open("Result.txt", "w",encoding="utf-8")   
        i=1    
        for value in list(sentences1):
                counter=Counter(value)
                y=dict(counter.most_common()) 
                n = text_file.write(str('\nSentence : %d \n' % (i)))
                for char in y:
                        n = text_file.write(str('%s : %d \t' % (char, y[char])))
                i=i+1
        text_file.close()




        
        

