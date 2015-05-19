import collections
from collections import deque
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import CategorizedPlaintextCorpusReader
from nltk.corpus import PlaintextCorpusReader
from sklearn import svm
from sklearn.svm import LinearSVC

import string
import csv

corpus_root1='/Users/tianhan/Dropbox/Advanced_big_data_Project/aclImdb/train'
train=CategorizedPlaintextCorpusReader(corpus_root1,r'(pos|neg)/.*\.txt',cat_pattern=r'(pos|neg)/.*\.txt')
corpus_root2='/Users/tianhan/Documents/ColumbiaU/Spring15/Adv_Big_Data_Analytics/Project/Reviews'
test=PlaintextCorpusReader(corpus_root2,'.*\.txt')

def classify(featx):
    train_negids = train.fileids('neg')
    train_posids = train.fileids('pos')
    train_negfeats = [(featx(train.words(fileids=[f])), 'neg') for f in train_negids]
    train_posfeats = [(featx(train.words(fileids=[f])), 'pos') for f in train_posids]
    test_feats = [(featx(test.words(fileids=[f]))) for f in test._fileids]
    trainfeats = train_negfeats + train_posfeats
    NaiveBayes_classifier = NaiveBayesClassifier.train(trainfeats)
    classifier = nltk.classify.SklearnClassifier(LinearSVC())
    SVM_classifier = classifier.train(trainfeats)
    testsets = collections.defaultdict(set)
    labelallNaiveBayes = list()
    labelallSVM = list()

    for i, feats in enumerate(test_feats):
            observed = NaiveBayes_classifier.classify(feats)
            labelallNaiveBayes.append(observed)
            
    for i, feats in enumerate(test_feats):
            observed = classifier.classify(feats)
            labelallSVM.append(observed)
            
    with open('/Users/tianhan/Documents/ColumbiaU/Spring15/Adv_Big_Data_Analytics/Project/criticsnew.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['critic','date','fresh','imdb','original_score','publication','quote','review_date','rt_id','title','label_NaiveBayes','label_SVM'])
        with open('/Users/tianhan/Documents/ColumbiaU/Spring15/Adv_Big_Data_Analytics/Project/critics.csv','rU') as readfile: # input csv file
            reader = csv.reader(readfile, delimiter=',')
            next(reader) # Ignore first row

            for row in reader:
                row[10]=labelallNaiveBayes.pop(0)
                row[11]=labelallSVM.pop(0)              
                writer.writerow(row)
            
    #print classifier.most_informative_features()
    NaiveBayes_classifier.show_most_informative_features(50)


def word_feats(words):
    return dict([(word, True) for word in words])

classify(word_feats)

import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

def bigram_word_feats(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    words_nopunc = [word for word in words if word not in string.punctuation]
    bigram_finder = BigramCollocationFinder.from_words(words_nopunc)
    bigrams = bigram_finder.nbest(score_fn, n)
    return dict([(ngram, True) for ngram in itertools.chain(words_nopunc, bigrams)])

classify(bigram_word_feats)

