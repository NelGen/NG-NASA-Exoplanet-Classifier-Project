import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle # this is for scripting

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
# Linear Models
from sklearn.metrics import mean_squared_error, mean_squared_log_error
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

# Classification Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import plot_confusion_matrix, classification_report




# Scalers
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer

# Categorical Create Dummies
from sklearn.preprocessing import OneHotEncoder



# Warnings Off
import warnings
warnings.filterwarnings('ignore')



# Classification Models
def run_class_model(model, X_train, y_train, X_test, y_test):

    # fitting
    model.fit(X_train, y_train)

    # predictions
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)
    
    # Classification Reports
    print('********************************************************\n')
    print('\033[1m' +'     Classification Report: Train\n' +'\033[0m')
    print(classification_report(y_train, y_hat_train))
    print('********************************************************\n')
    print('\033[1m' +'     Classification Report: Test\n' +'\033[0m')
    print(classification_report(y_test, y_hat_test))
    print('********************************************************\n')
    
    # Confusion Matrices
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(18, 6))

    plot_confusion_matrix(model, X_train, y_train, ax=ax0,cmap=plt.cm.Blues);
    plot_confusion_matrix(model, X_test, y_test, ax=ax1,cmap=plt.cm.Greens);

    ax0.title.set_text('Train Confusion Matrix');
    ax1.title.set_text('Test Confusion Matrix');
    
    return model # return the model object


# Linear Models
def run_linear_model(model, X_train, y_train, X_test, y_test):
    # fitting
    model.fit(X_train, y_train)

    # predictions
    y_hat_train = model.predict(X_train)
    y_hat_test = model.predict(X_test)
    
    # Metrics
    print("Train RSquared:", model.score(X_train,y_train))
    print("Test RSquared:", model.score(X_test,y_test))
    print("Train RMSE:", mean_squared_error(y_train,y_hat_train))
    print("Test RMSE:", mean_squared_error(y_test,y_hat_test))
    
    return model
