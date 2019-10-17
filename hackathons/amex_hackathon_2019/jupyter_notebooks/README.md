# AmExpert2019
https://datahack.analyticsvidhya.com/contest/amexpert-2019-machine-learning-hackathon/



* Download the data from the above link, and unzip. 

* Ensure 2 folders are created: test_data and training_data.

* Run 'src/DataCleaningAndBaseline.ipynb' to load and clean the raw data. It saves the cleaned_data to 'src/cleaned_data'.

* Run 'src/FeatureExtraction.ipynb' to load clean_data and create features that would be saved in different files (based on primary key) in 'src/feature_set' directory.
** The files directly under 'src/feature_set' directory contain encoded features that can be directly passed to models.
** The files under 'src/feature_set/experimental' directory contain intermediatory features that cannot be. directly passed to models, but might be used later to create more features and provide a much more convenient human-readble format.

* Run 'src/ModelTraining' to load fetaures from the above directory and create a training set and test-set to pass to models (Logistic Regression and Random Forest have already been provided).
** The model is trained, cross-validated, confusion metrics and auc-scores are extracted, and feature_importance histogram is plotted.


