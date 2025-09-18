import pandas as pd

df = pd.read_csv('cleaned_coffee_survey.csv')

#Age and cups

print(df.groupby('age')['cups'].mean())

#Age and Caffeine

print(df.groupby('age')['caffeine'].value_counts())

#Age and Strength

print(df.groupby('age')['strength'].value_counts())

#Gender and Average daily consumption

print(df.groupby(['gender'])['cups'].mean())

#Work situations and responses

print(df['wfh'].value_counts())

#Work Situations and average coffee consumption
print(df.groupby('wfh')['cups'].mean())

#Employment status and coffee consumption
print(df.groupby('employment_status')['cups'].mean())
