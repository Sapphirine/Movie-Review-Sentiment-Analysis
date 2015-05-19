import collections
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.classify import DecisionTreeClassifier
from nltk.corpus import CategorizedPlaintextCorpusReader
from sklearn import svm
from sklearn.svm import LinearSVC
import string
from tabulate import tabulate

corpus_root1='/Users/tianhan/Dropbox/Advanced_big_data_Project/aclImdb/train'
train=CategorizedPlaintextCorpusReader(corpus_root1,r'(pos|neg)/.*\.txt',cat_pattern=r'(pos|neg)/.*\.txt')
corpus_root2='/Users/tianhan/Dropbox/Advanced_big_data_Project/aclImdb/test'
test=CategorizedPlaintextCorpusReader(corpus_root2,r'(pos|neg)/.*\.txt',cat_pattern=r'(pos|neg)/.*\.txt')

def evaluate_classifier_Naive(featx):
    
    train_negids = train.fileids('neg')
    train_posids = train.fileids('pos')
    test_negids = test.fileids('neg')
    test_posids = test.fileids('pos')
    train_negfeats = [(featx(train.words(fileids=[f])), 'neg') for f in train_negids]
    train_posfeats = [(featx(train.words(fileids=[f])), 'pos') for f in train_posids]
    test_negfeats = [(featx(test.words(fileids=[f])), 'neg') for f in test_negids]
    test_posfeats = [(featx(test.words(fileids=[f])), 'pos') for f in test_posids]
    trainfeats = train_negfeats + train_posfeats
    testfeats = test_negfeats + test_posfeats

    Naive_classifier = NaiveBayesClassifier.train(trainfeats)
    refsets = collections.defaultdict(set)
    testsets_Naive = collections.defaultdict(set)

    for i, (feats, label) in enumerate(testfeats):
            refsets[label].add(i)           
            observed_Naive = Naive_classifier.classify(feats)
            testsets_Naive[observed_Naive].add(i)
            
    accuracy1 = nltk.classify.util.accuracy(Naive_classifier, testfeats)  
    pos_precision1 = nltk.metrics.precision(refsets['pos'], testsets_Naive['pos'])
    pos_recall1 = nltk.metrics.recall(refsets['pos'], testsets_Naive['pos'])
    neg_precision1 = nltk.metrics.precision(refsets['neg'], testsets_Naive['neg'])
    neg_recall1 = nltk.metrics.recall(refsets['neg'], testsets_Naive['neg'])

    Naive_classifier.show_most_informative_features(50)

    return(['NaiveBayes',accuracy1,pos_precision1,pos_recall1,neg_precision1,neg_recall1])
 
def evaluate_classifier_SVM(featx):

    train_negids = train.fileids('neg')
    train_posids = train.fileids('pos')
    test_negids = test.fileids('neg')
    test_posids = test.fileids('pos')
    train_negfeats = [(featx(train.words(fileids=[f])), 'neg') for f in train_negids]
    train_posfeats = [(featx(train.words(fileids=[f])), 'pos') for f in train_posids]
    test_negfeats = [(featx(test.words(fileids=[f])), 'neg') for f in test_negids]
    test_posfeats = [(featx(test.words(fileids=[f])), 'pos') for f in test_posids]
    trainfeats = train_negfeats + train_posfeats
    testfeats = test_negfeats + test_posfeats

    classifier = nltk.classify.SklearnClassifier(LinearSVC())
    SVM_classifier = classifier.train(trainfeats)
    refsets = collections.defaultdict(set)
    testsets_SVM = collections.defaultdict(set)

    for i, (feats, label) in enumerate(testfeats):
            refsets[label].add(i)           
            observed_SVM = classifier.classify(feats)
            testsets_SVM[observed_SVM].add(i)

    accuracy2 = nltk.classify.util.accuracy(classifier, testfeats)  
    pos_precision2 = nltk.metrics.precision(refsets['pos'], testsets_SVM['pos'])
    pos_recall2 = nltk.metrics.recall(refsets['pos'], testsets_SVM['pos'])
    neg_precision2 = nltk.metrics.precision(refsets['neg'], testsets_SVM['neg'])
    neg_recall2 = nltk.metrics.recall(refsets['neg'], testsets_SVM['neg'])

    return(['SVM',accuracy2,pos_precision2,pos_recall2,neg_precision2,neg_recall2])

def evaluate_classifier_Decision(featx):

    train_negids = train.fileids('neg')
    train_posids = train.fileids('pos')
    test_negids = test.fileids('neg')
    test_posids = test.fileids('pos')
    train_negfeats = [(featx(train.words(fileids=[f])), 'neg') for f in train_negids]
    train_posfeats = [(featx(train.words(fileids=[f])), 'pos') for f in train_posids]
    test_negfeats = [(featx(test.words(fileids=[f])), 'neg') for f in test_negids]
    test_posfeats = [(featx(test.words(fileids=[f])), 'pos') for f in test_posids]
    trainfeats = train_negfeats + train_posfeats
    testfeats = test_negfeats + test_posfeats

    train_negcutoff = len(train_negfeats)*1/100
    train_poscutoff = len(train_posfeats)*1/100
    trainfeats_Decision = train_negfeats[:train_negcutoff] + train_posfeats[:train_poscutoff]
    DecisionTree_classifier = DecisionTreeClassifier.train(trainfeats_Decision)
    refsets = collections.defaultdict(set)
    testsets_Decision = collections.defaultdict(set)

    for i, (feats, label) in enumerate(testfeats):
            refsets[label].add(i)           
            observed_Decision = DecisionTree_classifier.classify(feats)
            testsets_Decision[observed_Decision].add(i)

    accuracy3 = nltk.classify.util.accuracy(DecisionTree_classifier, testfeats)  
    pos_precision3 = nltk.metrics.precision(refsets['pos'], testsets_Decision['pos'])
    pos_recall3 = nltk.metrics.recall(refsets['pos'], testsets_Decision['pos'])
    neg_precision3 = nltk.metrics.precision(refsets['neg'], testsets_Decision['neg'])
    neg_recall3 = nltk.metrics.recall(refsets['neg'], testsets_Decision['neg'])

    return(['DecisionTree',accuracy3,pos_precision3,pos_recall3,neg_precision3,neg_recall3])

def word_feats(words):
    return dict([(word, True) for word in words])

table1 = []
table1.append(evaluate_classifier_Naive(word_feats))
table1.append(evaluate_classifier_SVM(word_feats))
table1.append(evaluate_classifier_Decision(word_feats))
 
print('Single word features:')
print(tabulate(table1, headers=["Classifier","Accuracy","Positive precision", "Positive recall", "Negative precision", "Negative recall"]))
               
import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

def bigram_word_feats(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    words_nopunc = [word for word in words if word not in string.punctuation]
    bigram_finder = BigramCollocationFinder.from_words(words_nopunc)
    bigrams = bigram_finder.nbest(score_fn, n)
    return dict([(ngram, True) for ngram in itertools.chain(words_nopunc, bigrams)])

table2 = []
table2.append(evaluate_classifier_Naive(bigram_word_feats))
table2.append(evaluate_classifier_SVM(bigram_word_feats))
table2.append(evaluate_classifier_Decision(bigram_word_feats))
 
print('Bigram word features:')
print(tabulate(table2, headers=["Classifier","Accuracy","Positive precision", "Positive recall", "Negative precision", "Negative recall"]))
               
