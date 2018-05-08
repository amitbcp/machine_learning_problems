import os
import pickle
import argparse
from sklearn.feature_extraction.text import CountVectorizer

def load_model(model_name):
    model_file = os.path.join(os.getcwd(),model_name+'.pkl')
    with open(model_file, 'rb') as f:
        model = pickle.load(f)
    return model

parser = argparse.ArgumentParser(description='Your Question : ')
parser.add_argument('-q','--query', help='Please enter your question',
                    default='What time will the school bus arrive')

args = vars(parser.parse_args())

model = load_model(model_name='ensembel_model')
vectorizer = load_model(model_name='count_vector')
#vectorizer = CountVectorizer(analyzer='word',lowercase=True)
text = args['query']
query =  vectorizer.transform([text])
pred = model.predict(query)
print("Question : {}".format(text))
print('Type : {} '.format(pred[0]))