import os
import pandas as pd
from numpy import sqrt
from numpy import argmax
from sklearn import metrics
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import ExtraTreesClassifier,RandomForestClassifier, BaggingClassifier,AdaBoostClassifier,GradientBoostingClassifier,GradientBoostingRegressor,VotingClassifier
from sklearn.model_selection import train_test_split,cross_val_score
from feature_selector import FeatureSelector
import matplotlib
df = pd.read_csv('afterAll.csv')

Y = df['death']
X = df.drop('death',axis=1).reset_index(drop=True)

fs = FeatureSelector(data=X,labels =Y)
fs.identify_all(selection_params={'missing_threshold': 0.3,'correlation_threshold':0.95,'task': 'regression','eval_metric':'auc','cumulative_importance':0.95})
#fs.identify_collinear(correlation_threshold=0.98, one_hot=False)
nowX = fs.remove(methods='all',keep_one_hot=False)
##train_X, test_X, train_y, test_y = train_test_split(X, Y, test_size = 0.2,random_state=42)
print(nowX)

nowX.to_csv('afterfs2.csv',index=False)


#train_X,train_y=SMOTE().fit_resample(train_X,train_y)
