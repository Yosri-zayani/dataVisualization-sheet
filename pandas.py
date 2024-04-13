# Load CSV data
import pandas as pd
df_can = pd.read_csv('data.csv')

# Handling Missing Values
df_can.dropna()  # Drop rows with missing values
df_can.fillna(0)  # Fill missing values with a specified value

# Removing Duplicates
df_can.drop_duplicates()  # Remove duplicate rows

# Renaming Columns
df_can.rename(columns={'Age': 'Years'})  # Rename one or more columns

# Selecting Columns
df_can['Age']  # Select a single column
df_can[['Name', 'Age']]  # Select multiple columns

# Filtering Rows
df_can[df_can['Age'] > 30]  # Filter rows based on a condition

# Applying Functions to Columns
df_can['Age'].apply(lambda x: x + 1)  # Apply a function to transform values in a column

# Creating New Columns
df_can['Total'] = df_can['Quantity'] * df_can['Price']  # Create a new column with values derived from existing ones

# Grouping and Aggregating
df_can.groupby('Category').agg({'Total': 'mean'})  # Group rows by a column and apply aggregate functions

# Sorting Rows
df_can.sort_values('Date', ascending=True)  # Sort rows based on a column

# Displaying First n Rows
df_can.head(3)  # Show the first n rows of the DataFrame

# Displaying Last n Rows
df_can.tail(3)  # Show the last n rows of the DataFrame

# Checking for Null Values
df_can.isnull()  # Check for null values in the DataFrame

# Selecting Rows by Index
df_can.iloc[3]  # Select rows based on integer index
df_can.iloc[2:5]  # Select rows in a specified range

# Selecting Rows by Label
df_can.loc['Label']  # Select rows based on label/index name
df_can.loc['Age':'Quantity']  # Select rows in a specified label/index range

# Summary Statistics
df_can.describe()  # Generates descriptive statistics for numerical columns
