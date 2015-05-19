import collections
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import CategorizedPlaintextCorpusReader
import string

import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

corpus_root1='/Users/tianhan/Dropbox/Advanced_big_data_Project/aclImdb/train'
train=CategorizedPlaintextCorpusReader(corpus_root1,r'(pos|neg)/.*\.txt',cat_pattern=r'(pos|neg)/.*\.txt')

def bigram_word_feats(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    words_nopunc = [word for word in words if word not in string.punctuation]
    bigram_finder = BigramCollocationFinder.from_words(words_nopunc)
    bigrams = bigram_finder.nbest(score_fn, n)
    return dict([(ngram, True) for ngram in itertools.chain(words_nopunc, bigrams)])

f = open('/Users/tianhan/Dropbox/Advanced_big_data_Project/aclImdb/test/neg/0_2.txt','r')
newreview = f.read()

def classify_newreview(newreview):
    train_negids = train.fileids('neg')
    train_posids = train.fileids('pos')
    train_negfeats = [(bigram_word_feats(train.words(fileids=[f])), 'neg') for f in train_negids]   
    train_posfeats = [(bigram_word_feats(train.words(fileids=[f])), 'pos') for f in train_posids]
    trainfeats = train_negfeats + train_posfeats
    classifier = NaiveBayesClassifier.train(trainfeats)
 
    feats = bigram_word_feats(newreview)
    label = classifier.classify(feats)
    print label

classify_newreview(newreview)








