This bot searches for,
1.  hotels at a location supports tier 1 and tier 2 cities
2.  cuisine of choice, you can choose from Chinese, Mexican, Italian, American, North Indian, Sounth Indian 
3.  you can give budget constraints

Some examples are as follows:
```
User: Hello!
Bot: Hi there! How may I help you?
User: I’m hungry. Looking out for some good restaurants
Bot: In what location?
User: in mubaim
Bot: Sorry, didn’t find any such location. Can you please tell again?
User: in Mumbai
Bot: What kind of cuisine would you like to have?
1. Chinese
2. Mexican
3. Italian
4. American
5. Thai
6. North Indian
User: american
Bot: What's the average budget for two people?
1. Lesser than Rs. 300
2. Rs. 300 to 700
3. More than 700
User: <300
Bot: Showing you top rated restaurants:
1. Restaurant 1 in Area 1. And the average price for two people here is: XXX
Rs
2. Restaurant 1 in Area 1. And the average price for two people here is: XXX
Rs
3. .
4. .
5. .
Bot: Should I send you details of all the restaurants on email?
User: yes. Please
Bot: To what email id should I send it to?
User: jddk.2jmd@kdl.co.in
Bot: Sent. Bon Appetit!
```

```
User: Hello!
Bot: Hi there! How may I help you?
User: I’m hungry. Looking out for some good chinese restaurants in chandigarh
Bot: What's the average budget for two people?
1. Lesser than Rs. 300
2. Rs. 300 to 700
3. More than 700
User: <300
Bot: Showing you top rated restaurants:
1. Restaurant 1 in Area 1. And the average price for two people here is: XXX
Rs
2. Restaurant 1 in Area 1. And the average price for two people here is: XXX
Rs
3. .
4. .
5. .
Bot: Should I send you details of all the restaurants on email?
User: no. thanks
Bot: Okay. Bon Appetit!
```


### Installation

Download this repo and cd into the folder

Install the dependencies
```sh
$ pip install -r requirements.txt
```
Install the spacy en library
```sh
$ pip install ‘rasa[spacy]’ 
$ python -m spacy download en_core_web_md
$ python -m spacy link en_core_web_md en 
```

### Training the RASA 

In order to train RASA NLU, run the following command

```sh
$ rasa train nlu
```

In order to train RASA CORE, run the following command

```sh
$ rasa train core
```

In order to train RASA, run the following command

```sh
$ rasa train
```

### Running the RASA on commandline

In order to run rasa action server, execute
```sh
$ rasa run actions
```


In order to run rasa at commandline, execute
```sh
$ rasa shell
```