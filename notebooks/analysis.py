import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#load the dataset
df = pd.read_csv("Tech_Use_Stress_Wellness.csv")

#find the shape and data types
print(df.shape)
print(df.info())

#viewing the first 5 rows
print(df.head())

# Summary statistics
print(df.describe())

# Check missing values
print(df.isna().sum())

# Compare Work Related Hours with Stress Levels
plt.figure(figsize=(10, 6))
sns.scatterplot(data = df, x='work_related_hours', y='stress_level')
plt.title('Work Related Hours vs Stress Levels')
plt.xlabel('Work Related Hours')
plt.ylabel('Stress Levels')
plt.show()

# Compare Daily Screen Time Hours with Sleep hours
plt.figure(figsize=(10,6))
sns.scatterplot(data = df, x='daily_screen_time_hours', y='sleep_duration_hours')
plt.title('Daily Screen Time Hours vs Sleep Duration Hours')
plt.xlabel('Daily Screen Time Hours')
plt.ylabel('Sleep Duration Hours')
plt.show()

# Compare Social Media Hours with Mood rating
plt.figure(figsize=(10,6))
sns.histplot(data=df, x="social_media_hours", kde=True)
plt.title('Social Media Hours vs Mood Rating')
plt.xlabel('Social Media Hours')
plt.ylabel('Mood Rating')
plt.show()