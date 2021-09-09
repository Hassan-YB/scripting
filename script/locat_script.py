from __future__ import unicode_literals
import codecs
from collections import Counter
import re

with codecs.open("location_cuisine_price_intent.txt", encoding="utf-8") as f0:
        with codecs.open("words.txt", encoding="utf-8") as f1:
                with codecs.open("out_location_cuisine_price_intent.txt","w", encoding="utf-8") as f2:
                        sentences_lines=f0.read().splitlines()
                        lines=f1.read().splitlines()
                        for sentences in sentences_lines:
                                result=re.search(r'\[(.*?)\]',sentences)
                                for words in lines:
                                        # next_word=list_of_words[list_of_words.index("location")+1]    
                                        # for words in lines:
                                        text = re.sub(str(result.group(1)),str(words), sentences)
                                        f2.write(text)
                                        f2.write("\n")
                                #f2.write("\n")
                        f2.close()
                                



