# !/usr/bin/env python
# encoding: utf-8

"""

Natural Language Processing Toolkit learning

@author: Jessie

@email: jessie.JNing@gmail.com
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


sentence = "At eight o'clock on Thursday morning. Arthur didn't feel very good."

# Tokenize sentence and words
sent_tokens = nltk.sent_tokenize(sentence)
#print sent_tokens
#["At eight o'clock on Thursday morning.", "Arthur didn't feel very good."]

word_tokens = nltk.word_tokenize(sentence)
#print word_tokens
# ['At', 'eight', "o'clock", 'on', 'Thursday', 'morning', '.', 'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']

# filter stop words
stop_word = set(stopwords.words("English"))

filter_sentense = filter(lambda x:x not in stop_word, word_tokens)
#print filter_sentense
# ['At', 'eight', "o'clock", 'Thursday', 'morning', '.', 'Arthur', "n't", 'feel', 'good', '.']

# words stemming
ps = PorterStemmer()
simi_words = ["python", "pythoner", "pythoning"]
stem_words = map(lambda x:ps.stem(x), simi_words)
#print stem_words
# [u'python', u'python', u'python']


# part of speech tagging
tagged = nltk.pos_tag(word_tokens)
#print tagged
# [('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'), ('Thursday', 'NNP'), ('morning', 'NN'), ('.', '.'), ('Arthur', 'NNP'), ('did', 'VBD'), ("n't", 'RB'), ('feel', 'VB'), ('very', 'RB'), ('good', 'JJ'), ('.', '.')]

# chunking: find out the chunks in the sentence based on the defined pattern
chunk_gram = "NP:{<VB.?>*<NN.?>}"
chunk_parser = nltk.RegexpParser(chunk_gram)
chunked = chunk_parser.parse(tagged)

# name entity recognition

name_entity = nltk.ne_chunk(tagged)
#name_entity.draw()

# convert the plural noun into singular
lemmatizer = WordNetLemmatizer()
raw_word = ["cats", "geese", "knives", "matrices", "media"]
lemma_word = map(lambda x:lemmatizer.lemmatize(x), raw_word)
#print lemma_word
# [u'cat', u'goose', u'knife', u'matrix', u'medium']

raw_word = ["better", "best", "runner"]
lemma_word = map(lambda x:lemmatizer.lemmatize(x, pos="a"), raw_word)
#print lemma_word
# [u'good', 'best', 'runner']

syns = wordnet.synsets("program")
word_syns = syns[0]
#print word_syns.name(), word_syns.definition(), word_syns.examples()
# plan.n.01 a series of steps to be carried out or goals to be accomplished [u'they drew up a six-step plan', u'they discussed plans for a new bond issue']


word1 = wordnet.synset("ship.n.01")
word2 = wordnet.synset("boat.n.01")
#print word1.lemmas()[0].name(), word2.lemmas()[0].name(), word1.wup_similarity(word2)
# Lemma('ship.n.01.ship') Lemma('boat.n.01.boat') 0.909090909091


