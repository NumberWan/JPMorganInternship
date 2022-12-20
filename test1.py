import os
import pandas as pd
import datetime
from sklearn.preprocessing import normalize
import matplotlib as plt
import optuna
from optuna.integration.keras import KerasPruningCallback
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from scipy.stats import zscore
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.callbacks import EarlyStopping
from sklearn import preprocessing
import keras
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score
from imblearn.over_sampling import SMOTE
import tensorflow as tf
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier,RandomForestClassifier, BaggingClassifier,AdaBoostClassifier,GradientBoostingClassifier,GradientBoostingRegressor,VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split,cross_val_score
from focal_loss import BinaryFocalLoss
def to_xy(df, target):
    result = []
    for x in df.columns:
        if x != target:
            result.append(x)
    # find out the type of the target column.  Is it really this hard? :(
    target_type = df[target].dtypes
    target_type = target_type[0] if hasattr(target_type, '__iter__') else target_type


    return df.as_matrix(result).astype(np.float32), df.as_matrix([target]).astype(np.float32)

    # Encode to int for classification, float otherwise. TensorFlow likes 32 bits.


df = pd.read_csv('afterAll.csv')

Y = df['death']
X = df.drop('death',axis=1)
# define the method
rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=40)
# fit the model
rfe.fit(X, Y)
# transform the data
X, Y = rfe.transform(X, Y)
print(X)
print(Y)
print("N_features %s" % rfe.n_features_)
print("Support is %s" % rfe.support_)
print("Ranking %s" % rfe.ranking_)
print("Grid Scores %s" % rfe.grid_scores_)