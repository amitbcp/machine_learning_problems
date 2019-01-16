import gensim
import os
import re
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim.models.doc2vec import TaggedDocument


def get_doc_list(folder_name):
    doc_list = []
    file_list = [folder_name + '/' + name for name in os.listdir(folder_name) if name.endswith('txt')]
    for file in file_list:
        st = open(file, 'r').read()
        doc_list.append(st)
    print('Found %s documents under the dir %s .....' % (len(file_list), folder_name))
    return doc_list


def get_doc(folder_name):
    doc_list = get_doc_list(folder_name)
    tokenizer = RegexpTokenizer(r'\w+')
    en_stop = get_stop_words('en')
    p_stemmer = PorterStemmer()

    taggeddoc = []

    texts = []
    for index, i in enumerate(doc_list):
        # for tagged doc
        wordslist = []
        tagslist = []

        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)

        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in en_stop]

        # remove numbers
        number_tokens = [re.sub(r'[\d]', ' ', i) for i in stopped_tokens]
        number_tokens = ' '.join(number_tokens).split()

        # stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in number_tokens]
        # remove empty
        length_tokens = [i for i in stemmed_tokens if len(i) > 1]
        # add tokens to list
        texts.append(length_tokens)

        td = TaggedDocument(gensim.utils.to_unicode(str.encode(' '.join(stemmed_tokens))).split(), str(index))
        taggeddoc.append(td)

    return taggeddoc