from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re
import numpy as np
from pprint import pprint
from collections import Counter
from cltk.tokenize.sentence import TokenizeSentence
import dataExtraction.datapreprocessing.parser as parser
import dataExtraction.datapreprocessing.stopword as stopword
import dataExtraction.clustering.labeling as label


stop=stopword.stopwords()
stemmer=parser.Stemmer()
exclude = set(string.punctuation)
#lemma = WordNetLemmatizer()
vectorizer = TfidfVectorizer(stop_words=stop)


# Cleaning the text sentences so that punctuation marks, stop words & digits are removed
def clean(str):
    stop_free = " ".join([i for i in str if i not in stop])
    #punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    #normalized = " ".join(lemma.lemmatize(word) for word in stop_free.split())
    stemm_line=" ".join(stemmer.stem_word(word) for word in stop_free.split())
    y = stemm_line.split()
    return y

def train_data(data_list):
    train_clean_sentences = []
    for key,line in sorted(data_list.items()):
        tokenizer = TokenizeSentence('bengali')
        bengali_text_tokenize = tokenizer.tokenize(line)
        #print(bengali_text_tokenize)
        cleaned = clean(bengali_text_tokenize)
        cleaned = ' '.join(cleaned)
        print(key,cleaned)
        train_clean_sentences.append(cleaned)

    X = vectorizer.fit_transform(train_clean_sentences)

    # Creating true labels for 30 training sentences
    #y_train = np.zeros(30)
    #y_train[10:20] = 1
    #y_train[20:30] = 2
    y_train=label.labeling(train_clean_sentences)

    # Clustering the document with KNN classifier
    modelknn = KNeighborsClassifier(n_neighbors=5)
    modelknn.fit(X, y_train)

    # Clustering the training 30 sentences with K-means technique
    modelkmeans = KMeans(n_clusters=3, init='k-means++', max_iter=200, n_init=100)
    modelkmeans.fit(X)
    return modelknn,modelkmeans

def test_model(modelknn,modelkmeans,test_data):
    test_clean_sentences = []
    for key, line in sorted(test_data.items()):
        tokenizer = TokenizeSentence('bengali')
        bengali_text_tokenize = tokenizer.tokenize(line)
        # print(bengali_text_tokenize)
        cleaned = clean(bengali_text_tokenize)
        cleaned = ' '.join(cleaned)
        print(key, cleaned)
        test_clean_sentences.append(cleaned)

    Test = vectorizer.transform(test_clean_sentences)

    true_test_labels = ['none', 'name', 'organization']
    predicted_labels_knn = modelknn.predict(Test)
    predicted_labels_kmeans = modelkmeans.predict(Test)

    for i in range(len(test_clean_sentences)):
        print(test_clean_sentences[i],':', true_test_labels[np.int(predicted_labels_knn[i])])
        print(test_clean_sentences[i],':', true_test_labels[np.int(predicted_labels_kmeans[i])])








































