# Identify Question Type

Given a question, the aim is to identify the category it belongs to. The four categories to handle for this assignment are : Who, What, When, Affirmation(yes/no).
Label any sentence that does not fall in any of the above four as "Unknown" type.

### Requirements for running `benchmark.py` , `build_model.py` and `test_model.py`:
Python packages :
> python >= 3.6 \
> numpy==1.13.1\
> pandas==0.22.0\
> scikit_learn==0.19.1\
> sklearn-crfsuite==0.3.6\
> argparse\
> pickle\
> os

# Requirements installation
>pip install -r requirements.txt 

## For Model building 
> python build_model.py

This would print the statistics of the various models and the final ensemble model.

>train time: 1.059s\
>test time:  0.047s\
>accuracy:   0.964\
>classification report:


Type |precision | recall     | f1-score | support
--------- |--------- | ---------- | ------- | --------
affirmation|   1.00   |   0.90    |  0.95   |     31
unknown| 0.95  |    0.95   |   0.95   |     81
what |      0.96   |   0.98  |    0.97  |     183
when   |    0.96   |   0.79  |    0.87   |     29
who   |    0.98  |    1.00  |    0.99  |     121
avg / total   |    0.96  |    0.96   |   0.96   |    445


## For Testing
> python test_model.py  -q "Are you hungry ?"

You need to pass your question with `-q` argument from terminal/command prompt . And output is printed at terminal/cmd like this -\
`Question : <User Query>`\
`Type : <Answer>`

