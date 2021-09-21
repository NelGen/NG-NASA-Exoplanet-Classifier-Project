# Kepler Exoplanet Classifier


## Business Case:
* Analyze features affecting disposition of Kepler objects.

## Goal:
* Generate model to predict if a Kepler object is likely to be a confirmed planet or false positive.

## Sources:

* NASA Exoplanet Exploration Information - https://exoplanets.nasa.gov/
* NASA Exoplanet Archive and Databases - https://exoplanetarchive.ipac.caltech.edu/

## Strategies

1. Identify and remove confounding variables.
    i. Database contains features likely to affect both independent and target variable.
    ii. Other features likely to have been engineered from these confounding variables.
2. Maximize accuracy during model training.
    i. As a mock business case, well founded arguments can be made towards minimizing either type I or type II errors.
       Maximizing accuracy stikes balance between the two.
    ii. Using robust scaling methods helps reduce impact of substantial number of outliers found in the dataset

## Findings

* For this dataset, the best performing model was built using a Random Forest Classifier and achieved 97% accuracy on test data.

* Some important features in determining classification included:
    1. Planetary Radius
    !(https://github.com/NelGen/NG-NASA-Exoplanet-Classifier-Project/blob/main/Images/Planetary_radius_feature.PNG)
    2. Distance from Star
    !(https://github.com/NelGen/NG-NASA-Exoplanet-Classifier-Project/blob/main/Images/Distance_from_star_feature.PNG)
    3. Count of Planets in the system
    !(https://github.com/NelGen/NG-NASA-Exoplanet-Classifier-Project/blob/main/Images/Planet_count_feature.PNG)
    
## Predictions

* Passing through 1,589 candidates from the dataset:
    1. 57% are likely to be confirmed
    2. 43% are likely to be false positives

* Assuming the preference is to locate possible confirmed planets, I would recommend resources be directed towards confirming the 57% of candidates here first.

## Improvements and Possible Next Steps

* Further developing knowledge on the subject matter will help with removing additional confounding variables, improving the use and efficacy of the model.

* Adapting for use with other missions such as K2 or TESS.

* Tuning to help discover possible habitable planets.
        