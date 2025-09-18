import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('cleaned_coffee_survey.csv')

#Daily Coffee Consumption by Age Group

modified_age_order = ['<18 years old', '18-24 years old', '25-34 years old', '35-44 years old','45-54 years old', '55-64 years old',
 '>65 years old']
df['age'] = pd.Categorical(df['age'], categories=modified_age_order, ordered=True)
average_consumption_age = df.groupby('age')[['cups']].mean()

#Visual
fig, (ax1,ax2) = plt.subplots(2, figsize = (10,8), gridspec_kw = {'height_ratios' : [3,1]})
sns.barplot(x='age', y='cups', data=df, palette='dark', order=modified_age_order, ax = ax1)
ax1.set_title('Average Daily Consumption by Age')
ax1.set_xlabel('Age')
ax1.set_ylabel('Cups')

#Table
cell_text = df.groupby('age')[['cups']].mean().values.round(3)
row_labels = df.groupby('age')[['cups']].mean().index.tolist()
column_labels = ['Average Daily Consumption (Cups)']
ax2.axis('off')
table = ax2.table(cellText= cell_text, rowLabels=row_labels, colLabels=column_labels,)
table.scale(1,2)
plt.tight_layout()
plt.show()


#Type of coffe consumption based on age

caff_level_age = df[['age', 'caffeine']].value_counts().reset_index(name='count')
#Visual
fig, (ax1,ax2) = plt.subplots(2, figsize = (14,10), gridspec_kw = {'height_ratios' : [4,1]})
sns.barplot( x='age', y='count',data=caff_level_age,hue='caffeine', palette='dark',order= modified_age_order, ax = ax1)
ax1.set_title('Caffeine Level Counts by Age')
ax1.set_xlabel('Age')
ax1.set_ylabel('Count')
ax1.tick_params(axis = 'x', rotation = 20)
ax1.legend(title = 'Caffeine Level')

#Pivot dataframe
pivoted_caff_level_age = caff_level_age.pivot(index='age', columns='caffeine', values='count')
pivoted_caff_level_age = pivoted_caff_level_age.reindex(modified_age_order)

#Table
cell_text = pivoted_caff_level_age.values.astype(int)
row_labels = pivoted_caff_level_age.index.tolist()
column_labels = pivoted_caff_level_age.columns.tolist()

ax2.axis('off')
table = ax2.table(cellText= cell_text, rowLabels=row_labels, colLabels=column_labels)
table.scale(1,2)
plt.tight_layout()
plt.show()


#Coffee strength based on age

strength_by_age = df.groupby(['age', 'strength']).size().reset_index(name ='count')

#Visual
fig, (ax1,ax2) = plt.subplots(2, figsize = (14,10), gridspec_kw = {'height_ratios' : [4,1]})
sns.barplot(x='age', y='count', data=strength_by_age, hue ='strength', palette='dark', order=modified_age_order, ax = ax1)
ax1.legend(title = 'Coffee Strength')
ax1.set_title('Coffee Strength Preferences by Age')
ax1.set_xlabel('Age')
ax1.set_ylabel('Count')
ax1.tick_params(axis = 'x', rotation=20)

#Pivot Dataframe
reformatted_cell_text = strength_by_age.pivot(index = 'age', columns = 'strength', values = 'count')
reformatted_cell_text = reformatted_cell_text.reindex(modified_age_order)

#Table
cell_text = reformatted_cell_text.values.astype(int)
row_labels = reformatted_cell_text.index.tolist()
column_labels = reformatted_cell_text.columns.tolist()
ax2.axis('off')
table = ax2.table(cellText= cell_text, rowLabels=row_labels, colLabels=column_labels)
table.scale(1,2)
plt.tight_layout()
plt.show()


#Average daily coffee consumption by gender

gender_subset = df[df['gender'].isin(['Male', 'Female'])]
average_by_gender = gender_subset.groupby('gender')['cups'].mean().reset_index()

#Visual
fig, (ax1,ax2) = plt.subplots(2, figsize = (14,10), gridspec_kw = {'height_ratios' : [3,1]})
sns.barplot(x='gender', y='cups', data= gender_subset, palette= "dark", ax = ax1)
ax1.set_xlabel('Gender')
ax1.set_ylabel('Cups')
ax1.set_title('Average Daily Coffee Consumption by Gender')

#Table
cell_text = average_by_gender['cups'].values.round(3).astype(str).reshape(-1,1)
column_labels = ['Average Daily Consumption (Cups)']
row_labels= average_by_gender['gender'].tolist()
ax2.axis('off')
table = ax2.table(cellText= cell_text, rowLabels=row_labels, colLabels=column_labels)
table.scale(1,2)
plt.tight_layout()
plt.show()


# Where people most often drink coffee

wfh_counts = df['wfh'].value_counts()
labels = wfh_counts.index.tolist()
colors = sns.color_palette("dark",len(labels))

plt.pie(wfh_counts, labels=labels, colors=colors, autopct='%1.1f%%', textprops= {"color" : "black"} )
plt.axis('equal')
plt.title('Where people most often drink coffee')
plt.show()


#Average cups of coffee by location

avg_cups = df.groupby('wfh')['cups'].mean().reset_index()
avg_cups['cups'] = avg_cups['cups'].round(3)

#Visual
fig, (ax1,ax2) = plt.subplots(2, figsize = (14,10), gridspec_kw = {'height_ratios' : [2,1]})
sns.barplot(x='wfh', y='cups', data=avg_cups, palette='dark', ax = ax1)
ax1.set_title('Average Cups of Coffee by Work Location')
ax1.set_xlabel("Work Location")
ax1.set_ylabel('Cups')

#Table
cell_text = avg_cups['cups'].values.reshape(-1,1)
row_labels = avg_cups['wfh'].tolist()
column_labels = ['Average Daily Consumption (Cups)']
ax2.axis('off')
table = ax2.table(cellText=cell_text, rowLabels= row_labels, colLabels= column_labels, cellLoc= 'center', bbox = (0, 0.2, 1, 0.7))
plt.tight_layout()
plt.show()


#Average daily coffee consumption by employment status:

mean_employment_status = df.groupby('employment_status')[['cups']].mean().reset_index()

#Visual
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=( 10,8), gridspec_kw= {'height_ratios': [3,1]})
sns.barplot(data = mean_employment_status, x ='employment_status', y='cups', palette="dark", ax = ax1)
ax1.set_title('Average Coffee Consumption by Employment Status')
ax1.set_xlabel("Employment Status")
ax1.set_ylabel("Cups of Coffee")
ax1.tick_params(axis = 'x', rotation = 45)

#Table
cell_text = [[f'{value:.3f}'] for value in mean_employment_status['cups']]
row_values = mean_employment_status['employment_status'].tolist()
column_values = ['Average Daily Coffee Consumption (Cups)']
ax2.axis('off')
table = ax2.table( cellText=cell_text, rowLabels= row_values, colLabels=column_values, loc='center')
table.scale(1,2)
plt.tight_layout()
plt.show()
