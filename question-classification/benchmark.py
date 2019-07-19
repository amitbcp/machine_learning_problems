
import pandas as pd
from sklearn.model_selection import  StratifiedShuffleSplit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

from time import time

def load_data(file="questions.txt"):
    df = pd.read_csv(file, sep=",,,", header=None,
                     names=['question', 'label'],engine="python")
    labelled_file = open('questions.txt')
    data = labelled_file.readlines()
    df['label']= df['label'].str.strip()

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=42)
    for train_index, test_index in split.split(df['question'],df['label']):
        X_train,X_test = df['question'][train_index], df['question'][test_index]
        y_train, y_test = df['label'][train_index], df['label'][test_index]


    return X_train,y_train,X_test,y_test


def benchmark(clf,X_train_text,y_train,X_test_text,y_test,tf_idf=False):
    if tf_idf:
        vectorizer =  TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                     stop_words='english')
    else:
        vectorizer = CountVectorizer(analyzer='word',lowercase=True)

    X_train = vectorizer.fit_transform(X_train_text)
    X_test= vectorizer.transform(X_test_text)
    print('_' * 80)
    print("Training: ")
    print(clf)
    t0 = time()
    clf.fit(X_train, y_train)
    train_time = time() - t0
    print("train time: %0.3fs" % train_time)

    t0 = time()
    pred = clf.predict(X_test)
    test_time = time() - t0
    print("test time:  %0.3fs" % test_time)

    score = metrics.accuracy_score(y_test, pred)
    print("accuracy:   %0.3f" % score)


    print("classification report:")
    print(metrics.classification_report(y_test, pred))


    #print("confusion matrix:")
    #print(metrics.confusion_matrix(y_test, pred))

    print()
    clf_descr = str(clf).split('(')[0]
    return vectorizer,clf_descr, score, train_time, test_time


