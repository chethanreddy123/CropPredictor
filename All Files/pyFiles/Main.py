from sklearn.tree import DecisionTreeClassifier
import pandas as pd
df=pd.read_csv('Crop_recommendation.csv')
Input_set=df.drop(columns=['label'])
Output_set=df['label']
Model= DecisionTreeClassifier()
Model.fit(Input_set,Output_set)
Machine_Predictions=Model.predict([[90,42,43,20.87974371,82.00274423,6.502985292,202.9355362]])
print(Machine_Predictions)
