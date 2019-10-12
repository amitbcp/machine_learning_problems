## Table Of Contents
- [Classify the Lunar Rock](#classify-the-lunar-rock)
  - [Data:](#data)
  - [Data Description:](#data-description)
  - [Evaluation Metric :](#evaluation-metric)
  - [Leader Board Rank :](#leader-board-rank)
  - [Solution Approach](#solution-approach)
    - [Binary Image Classification](#binary-image-classification)
    - [Binary Image Classification with Data Augmentation](#binary-image-classification-with-data-augmentation)
    - [Binary Image Classification with Transfer Learning](#binary-image-classification-with-transfer-learning)
      - [Observations](#observations)

# Classify the Lunar Rock

This challenge is powered by DataQuest & Hackerearth. [Challenge Link](https://www.hackerearth.com/challenges/competitive/lunar-rock-hackerearth-data-science-competition/)

Lunar landings by renowned space stations across the world have yielded an abundance of new scientific data on the Moon. The various experiments placed on the surface provided information on seismic, gravitational, and other lunar characteristics. But perhaps the most dramatic result of the missions was returning a total of more than 800 pounds of lunar rock and soil for analysis on Earth. These samples of the Moon offered a deeper appreciation of the evolution of our nearest planetary neighbor.

Imagine you have been called by one of the largest space stations in the world (XYZ) space station and you are requested to make a Machine Learning model which classifies the different rocks present on the moon's surface. The purpose of this is to make the research process a lot easier. This will reduce the human effort of doing a monotonous task. There are basically two types of rocks to be classified:

1. Small Rocks
2. Large Rocks

## Data:
You can find the dataset [here](http://hck.re/kkBIfM). On Furher exploration it's found that the data is a subset of a Artificial Lunar Landscape Dataset. It's available [here](https://www.kaggle.com/romainpessia/artificial-lunar-rocky-landscape-dataset).

## Data Description:
The data folder consists of 2 folders and 2 CSV files

* train - Contains 5999 ‘Small Rock’ images & 5999 ‘Large Rock’ images
* test  - Contains 7534 images
* train.csv - 11999 x 2 (including the headers) consists of image ID and the  true label for each image in the train folder
* test.csv - Contains the image id for the images present in test folder for which the true label needs to be predicted
* sample_submission:

```
Image_File,Class
clean0001.png,Large
ground0002.png,Small
ground0003.png,Small
ground0004.png,Small
```

## Evaluation Metric :

*Note*: To avoid any discrepancies in the scoring, ensure all the index column ('Image_File') values in submitted file match the values in 'test.csv' provided.

## Leader Board Rank :

* Public Leaderboard : 40th Rank
* Private Leaderboard :
* Total participants : 1902


## Solution Approach

Three different approaches which were tried for the challenge. The images were 480 X 720 which was resized to 480 X 480 to feed to the network. The image also had the following characteristics :

* Red Color Specified Sky
* Green Color was mainly for Caters
* Blue color for Rocks/boulders

### Binary Image Classification
The pipeline flow is as described :

* Loading Images using ImageGenerator.
* Since we don't have a separate validation dataset,we split the training data validation.
* We scale the image by dividing it by 255.
* Two models architectures were tested while training.
* The final layer had 1 node with Sigmoid for prediction.
* The **Binary Cross Entropy** loss was used for the model design.
* Thresholds was tweaked to make predictions to improve F1 Score.
* With the result, the model was re-trained with the entire training data.
* The final model was used for submission.

### Binary Image Classification with Data Augmentation

The [above](#binary-image-classification) pipeline resulted in high F1 scores. Though some extent of overfitting was visible.

To address the same, image augmentation was used. Though the selection of augmentation parameters were limited based on the nature of the image.

The following techniques were used for augmentation :

1. Horizontal Flip
2. Vertical Flip
3. Rotation by 45 degree


All the above menthods, don't change the nature of the image like brightness/shear etc. This makes the model to avoid biasness like, only if rocks are present on the left/right side , detect that as a Large Rock.

### Binary Image Classification with Transfer Learning

Transfer Learning was used to experiment with the pipeline flow and see if it adds any difference as for other Image Classification problems.

Though the hypothesis was :

1. Pre-trained models should give poor results.
2. As the first layers capture simple featuers like line/edges/corners/circles
3. Layers to the end of the network capture Patterns and shapes.
4. Since the given the images dont have a lot of complex shapes and patters along with RGB colour specifically, the pre-trained model might perform poorly.


#### Observations

1. Pre-trained VGG-16 model with last 4 layers trainable + 2 Dense Layers, was not classifying all images as **Small**.
2. pre-trained VGG-16 model with last 2 layers trainable + 2 Dense Layers was also classifying all images as **Small**.
3. VGG-16 with all the layers freezed + 2 Dense Layers , showed high performance equivalent to the other two approaches.


The observations validate our hypothesis that the last layers of the pre-trained network are not usefull in this case.
