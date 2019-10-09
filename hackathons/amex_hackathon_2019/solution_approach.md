## Contents
- [Solution Approach](#solution-approach)
  - [Data Imputation](#data-imputation)
  - [Feature Creation](#feature-creation)
      - [Campaign Based Features](#campaign-based-features)
      - [Coupon Based Features](#coupon-based-features)
      - [Redemption based features](#redemption-based-features)
      - [Item based features](#item-based-features)
      - [Customer Purchasing Power based features](#customer-purchasing-power-based-features)
  - [Feature Selection](#feature-selection)
  - [Model Training](#model-training)
  - [Ensembling](#ensembling)
  - [Submission](#submission)

# Solution Approach

The given dataset has been described in the [README.md](). The major challenge for the Hackathon was creating features to train a model. The approach has been divided into the following sections.



## Data Imputation

Missing data points were imputed in the  **Customer Demographics** only.

1. 50% of the customers did not have any demographic details
2. Categorical Values were present like Single/Married , Age-Range
3. Many of the fields were missing among the customers which were custom imputed.

Details can be review in _____________________

## Feature Creation

The most challenging aspect of the Hackathon was to create feature by linnking the various data sources. The following features were created for testing Hypothesis.

1. **Campaign based features**
2. **Coupon based features**
3. **Redemption based features**
4. **Item based features**
5. **Customer Purchasing Power based features**

#### Campaign Based Features

These features were created from the Campaign Data. The features are described as below :

1. Campaign Duration - Number of Days the Campaign was running.
2. Campaign Month - Months during which the Campaign was running.
3. Campaign Weekends - Number of Weekends the Campaign was running.

#### Coupon Based Features

#### Redemption based features

These features were created from the **Item Data**. These were mapped to Customer Transaction & Coupon Item Mapping, to generate the following features :

1. XYZ
2. XYZ
3. ABC

#### Item based features

These features were created from the **Item Data**. These were mapped to Customer Transaction & Coupon Item Mapping, to generate the following features :

1. XYZ
2. XYZ
3. ABC

#### Customer Purchasing Power based features

## Feature Selection

Based on multiple evaluations we found the following features **did not** much value to the model performance:

1. Customer Demographics
2. Item-Coupon group features : Distribution Count of Categories/Brands per Coupon ID
3. Item-Campaign group features : Distribution Count of Categories/Brands per Campaign ID

All the other featrues were included.

## Model Training

The following models where experimented with during the event.

1. LightGBM
2. XGBoost
3. Neural Networks


## Ensembling

MLExtend ensemble pipeline was experimented with but was not finally used.

## Submission

The final submission was done using LightGBM.