'''Implementation of Doc2vec'''



import gensim
import os
import collections
import smart_open
import random
import zipfile
import glob
import sys


def read_corpus(directory, tokens_only=False):
    shakelist = glob.glob(directory, recursive=True)
    for file in shakelist:
        #print("File Name - {}".format(file))
        with smart_open.smart_open(file, encoding="utf-8") as f:
            yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(f.read()), [file])


            '''for i, line in enumerate(f):
                if tokens_only:
                    yield gensim.utils.simple_preprocess(line)
                else:
                    # For training data, add tags
                    yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])'''

def doc2vec(documents):
    '''Traning Doc2Vec model'''
    print("Training Model...")
    print("Size of Documents - {}".format(len(documents)))
    model = gensim.models.doc2vec.Doc2Vec(size=300,dm=0,iter =100, min_count=2,  window=10 ,alpha= 0.02, min_alpha=0.002,workers=3)
    model.build_vocab(documents)
    model.train(documents, total_examples=model.corpus_count, epochs=model.iter)
    model.save('trained.model')
    model.save_word2vec_format('trained.word2vec')
    #:wq
    # model.iter
    # start training
    '''for epoch in range(200):
        model.train(documents)
        model.alpha -= 0.002  # decrease the learning rate
        model.min_alpha = model.alpha  # fix the learning rate, no decay
        if epoch % 20 == 0:
            print('Now training epoch %s' % epoch)
            model.save('trained.model')
            model.save_word2vec_format('trained.word2vec')
    #model.train(documents, total_examples=model.corpus_count, epochs=model.iter)'''

    return model


def build_model():
    print("In Model Building")
    documents = list(read_corpus('internal/paragraph_split_l1/*.txt'))
    model =  doc2vec(documents)
    #Write Test Cases


def test_doc2_vec():
    print("Sanity Checks ..")
    model = gensim.models.Doc2Vec.load('trained.model')
    #docvecs = model.docvecs
    #documents = list(read_corpus('shakespeare/*.txt'))
    documents = list(read_corpus('internal/paragraph_split_l1/*.txt'))
    # print (docvecs[str(3)])
    # shows the similar words
    # print(model.most_similar('Against acquaintance, kindred and allies'))

    # Pick a random document from the test corpus and infer a vector from the model
    #doc_id = random.randint(0, len(documents))
    #doc_id=100
    #inferred_vector = model.infer_vector(documents[doc_id].words)
    #sims = model.docvecs.most_similar([inferred_vector], topn=5)

    # Compare and print the most/median/least similar documents from the train corpus
    #print('Test Document ({}): «{}»\n'.format(doc_id, ' '.join(documents[doc_id].words)))
    #print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
    #for label, index in [('MOST', 0), ('MEDIAN', len(sims) // 2), ('LEAST', len(sims) - 1)]:
        #print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(documents[sims[index][0]].words)))
    #for i in range(5):
        #print(u'%s %s: «%s»\n' % (i, sims[i], ' '.join(documents[sims[i][0]].words)))

    with smart_open.smart_open('templates.csv', encoding="utf-8") as f:
        for _, line in enumerate(f):
            tokens = gensim.utils.simple_preprocess(line)
            print("Tokens :: ", ' '.join(tokens))
            new_vector = model.infer_vector(tokens)
            sims = model.docvecs.most_similar([new_vector])  # gives you top 10 document tags and their cosine similarity
            for i in range(5):
                #print("Document {}  : {} \nContent {} ".format(i, sims[i][0], ' '.join(documents[i].words)))
                with smart_open.smart_open(sims[i][0], encoding="utf-8") as para:
                    print("Document : {}".format(para.read()))
                #print("Document : {}".format(' '.join(documents[i].words)))
            print("-"*25)



    '''tokens = "we remain focused on long term".split()
    print("Tokens :: ", tokens)
    new_vector = model.infer_vector(tokens)
    sims = model.docvecs.most_similar([new_vector])  # gives you top 10 document tags and their cosine similarity

    for i in range(5):
        print(u'%s %s: «%s»\n' % (i, sims[i][0], ' '.join(documents[i].words)))'''









if __name__ == "__main__":
    print("In Main Function")
    test_doc2_vec()

