import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the dataset (correct method for Excel)
df = pd.read_excel(r"D:\OneDrive\Desktop\numpy\indian_employee_data.xlsx")

# Display first 5 rows
print(df.head())

# Check missing values
print('\nMissing values in each column:')
print(df.isnull().sum())


# Replace missing values with mean salary
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

df.replace([np.inf, -np.inf], np.nan, inplace=True)

df.fillna(df.select_dtypes(include=[np.number]).mean(), inplace=True)

df.drop_duplicates(inplace=True)

df['Salary'] = np.where(df['Salary'] < 0, df['Salary'].mean(), df['Salary'])

salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# remove rows where salary is too high
df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]
df.to_csv('cleaned_indian_emplyee_Data.csv', index=False)

print('Data cleaned completed! saved as "cleaned_indian_emplyee_Data.csv"')

# i want to visulize the data so i will use matplotlib and seaborn

# Visualizing the cleaned data
plt.figure(figsize=(10, 6))
# Histogram of Salary
# Creates a histogram of the Salary column in your DataFrame df.
# bins=30: Splits the salary values into 30 intervals (bars).
# color='blue': Sets the bar color to blue.
# alpha=0.7: Sets the transparency level of the bars (1 is solid, 0 is fully transparent). So 0.7 means slightly see-through.


plt.hist(df['Salary'], bins=30, color='blue', alpha=0.7)
# Add a vertical line for the mean salary
plt.title('Salary Distribution')

# Add a vertical line for the mean salary
plt.xlabel('Salary')

plt.ylabel('Frequency')
# Adds a background grid to the plot for better visual clarity.
plt.grid(True)
plt.show()

# Creates a new figure (plot canvas) with width 8 inches and height 5 inches.Creates a new figure (plot canvas) with width 8 inches and height 5 inches.

plt.figure(figsize=(8, 5))
# Boxplot of Salary by Department
plt.boxplot(df['Salary'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Box Plot of Salary')
plt.xlabel('Salary')
plt.show()