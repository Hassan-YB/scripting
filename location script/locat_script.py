from __future__ import unicode_literals
import codecs
from collections import Counter
import re

with codecs.open("intent_find_by_location.txt", encoding="utf-8") as f0:
        with codecs.open("words.txt", encoding="utf-8") as f1:
                with codecs.open("out_location.txt","w", encoding="utf-8") as f2:
                        sentences_lines=f0.read().splitlines()
                        lines=f1.read().splitlines()
                        for sentences in sentences_lines:     
                                for words in lines:
                                        text = re.sub(r'\[(.*?)\]',"["+str(words)+"]", sentences)
                                        f2.write(text)
                                        f2.write("\n")
                                #f2.write("\n")
                        f2.close()



