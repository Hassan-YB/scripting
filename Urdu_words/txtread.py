from __future__ import unicode_literals
import codecs
from collections import Counter
import re

with codecs.open("stopwords.txt", encoding="utf-8") as f:
        sentences = f.read()
        print(sentences)
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
        print(counter)

