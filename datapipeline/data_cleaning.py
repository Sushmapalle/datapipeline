 
import pandas as pd  # Import the pandas library

# Step 1: Load the raw dataset
data = pd.read_csv('Electric_Vehicle_Population_Data.csv')  # Read the CSV file into a DataFrame

# Step 2: Drop missing values
cleaned_data = data.dropna()  # Remove rows with missing (empty) values

# Step 3: Save the cleaned dataset
cleaned_data.to_csv('cleaned_data.csv', index=False)  # Save the cleaned data to a new file

print("Data cleaning complete. Cleaned data saved to 'cleaned_data.csv'")
