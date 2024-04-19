
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a DataFrame
df = pd.read_csv(r"C:\Users\AliWH\Desktop\AI og data\Lektion 4\recipeData.csv\recipeData.csv", encoding='latin1')  # Replace "your_dataset.csv" with the path to your dataset file

# Find out how many columns the dataset contains
num_columns = df.shape[1]
print("Number of columns:", num_columns)

# Find out the column names in the dataset and convert them into a Python list
column_names = df.columns.tolist()
print("Column names:", column_names)

# Get the data type for each column
column_data_types = df.dtypes
print(column_data_types)

# Find out how many rows (instances) there are in the DataFrame
num_rows = df.shape[0]
print("Number of rows:", num_rows)


# Printing some useful information about the index and columns of the DataFrame
print("\nDataFrame information:")
df.info()

# Printing summary statistics for any numeric columns of the DataFrame
print("\nSummary statistics:")
print(df.describe())

#Checking for null values

print(df.isna().sum())

#Removing Null values
print(df.shape)
clean_df = df.dropna()  # Drop all rows with null!
print(clean_df.shape)


clean_df = df.dropna(axis=1)  # Drop columns with NA values
print(clean_df.shape)  # We have lost one column. The rows stay the same.

#The methods above returns a copy of the DataFrame with the NA rows/columns removed. 
#If you want to modify (mutate) the DataFrame directly, pass in inplace=True.
# >>> df.dropna(inplace=True)
# >>> print(df.shape) 
# (414, 12)


#Plotting

# # Plot histograms for numerical variables
# numerical_variables = df.select_dtypes(include=['int64', 'float64']).columns  # Select numerical columns
# for column in numerical_variables:
#     plt.figure(figsize=(8, 6))
#     sns.histplot(df[column], kde=True)
#     plt.title(f'Histogram of {column}')
#     plt.xlabel(column)
#     plt.ylabel('Frequency')
#     plt.show()
