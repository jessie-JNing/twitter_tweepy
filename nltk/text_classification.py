# !/usr/bin/env python
# encoding: utf-8

"""
Text classification with movie review data in nltk

@author: Jessie

@email: jessie.JNing@gmail.com
"""

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = map(lambda x:x.lower(), movie_reviews.words())
all_words = nltk.FreqDist(all_words)
#print all_words.most_common(10)

#print all_words.keys()[:20]
# [u'sucess', u'sonja', u'askew', u'woods', u'spiders', u'bazooms', u'hanging', u'francesca', u'comically', u'localized', u'disobeying', u'hennings', u'canet', u'scold', u'originality', u'caned', u'rickman', u'slothful', u'wracked', u'stipulate']


def find_features(document):
    words = set(document)
    features = {}
    for w in all_words.keys()[:2000]:
        features[w] = (w in words)
    return features

#print find_features(movie_reviews.words("neg/cv000_29416.txt"))
# [(u',', 77717), (u'the', 76529), (u'.', 65876), (u'a', 38106), (u'and', 35576), (u'of', 34123), (u'to', 31937), (u"'", 30585), (u'is', 25195), (u'in', 21822)]


featuresets = [(find_features(rev), cat) for (rev, cat) in documents]
