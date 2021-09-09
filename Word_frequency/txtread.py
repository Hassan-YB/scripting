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

with codecs.open("content.txt",encoding="utf-8") as f1:
        sentences1 = f1.read()
        # sentences = sentences.translate(table)
        sentences1 = re.sub(r"\d+", " ", sentences1)
        # English punctuations
        sentences1 = re.sub(r"""[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]+""", " ", sentences1)
        # Urdu punctuations
        sentences1 = re.sub(r"[:؛؟’‘٭ء،۔]+", " ", sentences1)
        # Arabic numbers
        sentences1 = re.sub(r"[٠‎١‎٢‎٣‎٤‎٥‎٦‎٧‎٨‎٩]+", " ", sentences1)
        sentences1 = re.sub(r"[^\w\s]", " ", sentences1)
        # Remove English characters and numbers.
        sentences1 = re.sub(r"[a-zA-z0-9]+", " ", sentences1)
        # remove multiple spaces.
        sentences1= re.sub(r" +", " ", sentences1)
        words1 = sentences1.split()
        counter = Counter(words1)
        y=dict(counter.most_common())
        text_file = open("Content_list.txt", "w",encoding="utf-8")
        for char in y:
                n = text_file.write(str('%s : %d \n' % (char, y[char])))
        text_file.close()

        count1=Counter(words1)
        count2=list(words)
        for value in list(count1):
                if value in count2:
                        del count1[value]
                                
        y=dict(count1.most_common())
        text_file = open("Result.txt", "w",encoding="utf-8")
        for char in y:
                n = text_file.write(str('%s : %d \n' % (char, y[char])))
        text_file.close()
        f.close()
        f1.close()


        
        

