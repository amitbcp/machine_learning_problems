#Identify Question Type

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

## For Testing
> python test_model.py  -q "Are you hungry ?"

You need to pass your question with `-q` argument from terminal/command prompt . And output is printed at terminal/cmd like this -\
`Question Type : <User Query>`\
`Type : <Answer>`

