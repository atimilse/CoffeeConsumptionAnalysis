import pandas as pd

#Load data
df = pd.read_csv('/Users/atimil/Downloads/coffee_survey.csv')

#Initial column Check
print(df.columns)

#Keep relevant columns
keep_columns = [
    'cups','caffeine', 'strength', 'age', 'gender',
    'employment_status', 'wfh' ]
df = df[keep_columns]

# Check any for nulls, as well as unique values
print(f"unique values for cups include {df['cups'].unique()}")
print(f"unique values for caffeine include {df['caffeine'].unique()}")
print(f"unique values for strength includes {df['strength'].unique()}")
print(f"unique values for age includes {df['age'].unique()}")
print(f"unique values for gender includes {df['gender'].unique()}")
print(f"unique values for employment status includes {df['employment_status'].unique()}")
print(f"unique values for wfh includes {df['wfh'].unique()}")

#Convert to numeric and handle missing values
df['cups'] = df['cups'].replace({'Less than 1' : 0.5 ,
                                 'More than 4' : 5})
df['cups'] = pd.to_numeric(df['cups'], errors='coerce')
df = df[df['cups'] != 0]
df['cups'] = df['cups'].fillna(df['cups'].mean())

#Standardize gender for easier analysis
df['gender'] = df['gender'].replace({
    'Prefer not to say': 'Not specified',
    'Other (please specify)': 'Other'
}).fillna('Not specified')

#Clean employment status
df['employment_status'] = df['employment_status'].replace({
    'na': 'Not specified'
}).fillna('Not specified')

#Clean Work-from-home status
df['wfh'] = df['wfh'].replace({
    'I primarily work from home': 'Work from home',
    'I primarily work in person': 'Work in person',
    'I split time between home and workplace': 'Hybrid',
}).fillna('Not specified')

#Clean strength
strength_map = {
    'Somewhat light': 'Light',
    'Weak': 'Light',
    'Somewhat strong': 'Strong',
    'Very strong': 'Strong',
    'Medium': 'Medium'
}
df['strength'] = df['strength'].replace(strength_map).fillna('Not specified')

#Clean caffeine levels
df['caffeine'] = df['caffeine'].fillna('Not Specified')

#Export cleaned data
df.to_csv('cleaned_coffee_survey.csv', index=False)