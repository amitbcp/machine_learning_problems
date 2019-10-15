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
  - [Team](#team)

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

These features were created from the coupon to item mapping Data. The features are described as below :

1. Mean Coupon Price: Average price of items covered by a coupon.
2. Std mean Coupon Price: Standard Deviation of price across items covered by a coupon.
3. Average Std Deviation: Average of Standard Deviation in price of items  covered by a coupon

* Items based features were used for creating these features.

#### Redemption based features

These features were created from the **Item Data**. These were mapped to Customer Transaction & Coupon Item Mapping, to generate the following features :

1. XYZ
2. XYZ
3. ABC

#### Item based features

These features were created from the **Item Data**. These were mapped to Customer Transaction & Coupon Item Mapping, to generate the following features :

1. Mean Item Cost Price: Mean Cost price of each item.
2. Standard deviation of cost price: Standard Deviation of cost price of each item.
3. Latest Cost price: Latest cost price of an item.
4. Price Range: Price range of each item

* Cost price of an item was computed using customer_transaction_data table. Assuming selling_price to be the price at which an item was sold, we computed cost price of an item in a transaction by adding total discounts to the selling price and dividing the sum by quantity for that particular transaction. So, the Mean Item Cost Price feature becomes the average of these cost prices of an item across all it's transactions.

#### Customer Purchasing Power based features

These features were created by combining user details with other tables:

1. coupon user common items: Count of Common items between a user and and a coupon
2. coupon user common items ratio: Ratio of coupon user common items to the number of items a user is interested in
3. coupon user common brands: Count of Common brands between a user and and a coupon
4. coupon user common brands ratio: Ratio of coupon user common brands to the number of brands a user is interested in
5. coupon user common categories: Count of Common categories between a user and and a coupon
6. coupon user common categories ratio: Ratio of coupon user common categories to the number of items a user is interested in
7. coupon user common items with discount: Intersection of items a user availed coupon discount on and items covered by a coupon
8. coupon user common items with discount ratio: Ratio of coupon user common items to the number of items a user is interested in

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

## Team

The team who worked for the hackathon are  :

1. [Ishant Wankhede](https://github.com/IshantWankhede)
2. [Pranshu Anand](https://github.com/pranshu-anand)
3. [Ruhama Ahale]()
4. [Shivam Singla](https://github.com/smatrix017)
5. [Keshav Kumar](https://github.com/keshav787)
6. [Amit Agarwal](https://github.com/amitbcp)