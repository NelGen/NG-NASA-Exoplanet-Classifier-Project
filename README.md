# Kepler Exoplanet Classifier


## Business Case:
* Analyze features affecting disposition of Kepler objects.

## Goal:
* Generate model to accurately predict if a Kepler object is likely to be a confirmed planet or false positive.

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