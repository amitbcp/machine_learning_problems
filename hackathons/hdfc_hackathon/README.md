# HDFC ML Hackathon 2019 #

This hackathon was conducted by HDFC on HackerEarth in September 2019. [Hackathon Link](https://www.hackerearth.com/challenges/hiring/hdfc-bank-ml-hiring-challenge-2019/?utm_source=website&utm_medium=widget&utm_campaign=live-widget)

## Problem Statement ##

Given a customer details/portfolio features as annonymised features, the bank wants to analyse a Risk Analysis Score for the customer to decide if a customer will default a loan or not. Based on this the bank plans to improve it's loan sanctioning.

The following things have been taken into consideration while generating customer features.
  1. Customer Demographics.
  2. Whether, customer is new customer.
  3. Last Loan details of the customer.
  4. Customer Transanctions in the past.
  5. Volume of Transactiob & recency.

## Solution Approach ##

The given dataset had 2936 features with the following behaviour :
  1. Numerical Features with positive & negative range of values.
  2. The continous numerical features were not normalised in the data.
  3. Categorical Features were present with indication 0-1 values.
  4. The dataset had many missing values both on feature level & customer level.
  5. The dataset was skewed. Only 5% True Labels
  6. Col1 was customer_id & Col2 was the target variable.

### Our Approach ###

On intial data exploration the following observations were recorded :
  1. Missing Values : A large number of columns had more tha 60% missing values
  2. Missing Customer Details : A large number of customers had more than 50% of the features as NaN/Null/Blank

Since imputation for such dataset leads to excessive data extrapolation, the features were dropped based on a Threshold of missing values.

#### Feature Selection ####

1. Co-relation was computed for the features. Multiple Thresholds were evaluated to  drop features with co-relation above Threshold.
2. Dropping Features which had a Missing Values above a certain Threshold.
3. Feature Importance was computed using Random Forest. Features with importance above a certain Threshold was included.

The above techniques were used to reduce the dimensionality of the data before tranining the model. The features selected above were then merged(union) and intersected(common features) and pushed through the model for Evaluation.

#### Modelling ####

A couple of modelling techniques was tried along with Hyper Parameter Tuning.

1. RandomForest
2. XGBoost
3. CatBoost
4. LightGBM
5. Neural Network
6. Ensembling of Results

### Rank ###

**Public Leader Board** : 50th Rank

**Private Leader Board** : 6th Rank

**Score** :

## Project Layout ##

The project is divided into the following section :

1. common : Contains Config & Utility Scripts
2. evaluation.py : Includes function to evaluate and generate submission file
3. models.py : Includes functions for the different models explored
4. train.py : Includes functions for training different models
5. data_loader.py : Includes functions to read input data and feature selection

## Team

The team who worked for the hackathon are  :

1. [Amit Agarwal](https://github.com/amitbcp)
2. [Ishant Wankhede](https://github.com/IshantWankhede)
3. [Keshav Kumar](https://github.com/keshav787)
4. [Pranshu Anand](https://github.com/pranshu-anand)
5. [Shivam Singla](https://github.com/smatrix017)
