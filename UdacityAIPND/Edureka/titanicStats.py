import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

original_df = pd.read_csv('titanic.csv')
print("Number of Passangers in original data",len(original_df.index),original_df.shape)
# print(original_df.head())
print("\n")
# # =========================================Data Wrangling====================================================
# print number of Passangers having NaN at any place
print(original_df.isnull())
# print number of Passangers having NaN in each column at any place (Summing the Data)
print(original_df.isnull().sum())
# # Removing Passangers which have age as null. As age is very important feature.
# print(original_df[pd.notnull(original_df['Age'])])
age_wrangled_df = original_df[pd.notnull(original_df['Age'])]
print("Number of Passangers in Age Wrangled data",len(age_wrangled_df.index))
embark_wrangled_df = age_wrangled_df[pd.notnull(age_wrangled_df['Embarked'])]
print("Number of Passangers in Age and Embark Wrangled data",len(embark_wrangled_df.index))

# # Grouping data by Gender
print("================Group Data By Gender===================")
gender_data = embark_wrangled_df.groupby('Sex', as_index = False)
gender_data_male = gender_data.get_group('male')
gender_data_female = gender_data.get_group('female')
print("Male "+str(len(gender_data_male.index))+" Female "+str(len(gender_data_female.index)))

print("Total Survived ===> "+str(embark_wrangled_df['Survived'].sum()))
print("Total Male Survived ===> "+str(gender_data_male['Survived'].sum()))
print("Total Female Survived ===> "+str(gender_data_female['Survived'].sum()))

# # Survival Rate = Total Successful Save/Total Number in Sample List
print("Total Survival Rate ==> "+str((embark_wrangled_df['Survived'].mean())*100)+"%")
print("Male Survival Rate ===> "+str((gender_data_male['Survived'].mean())*100)+"%")
print("Female Survival Rate ===> "+str((gender_data_female['Survived'].mean())*100)+"%")

# # ===========Mean Data By Gender=========
gender_mean_data = gender_data.mean()
print(gender_mean_data)
# # ===========Gender Data Count===========
print(gender_data['PassengerId'].count()) 



