'''This class is to handle file operations and text operations'''

import smart_open
import csv

def disclosure_files(file_name):

    with smart_open.smart_open(file_name, encoding="ISO-8859-1") as f:
        for i,line in enumerate(f):
            #print(line)
            name = "disclosure/"+str(i)+".txt"
            with open(name, "wb") as disclosure:
                disclosure.write(line)


if __name__=='__main__':
    disclosure_files('disclosures_cleaned.csv')
