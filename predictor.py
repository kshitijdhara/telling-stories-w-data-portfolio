import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data
df = pd.read_csv('modified_NYC_baby_names.csv')

# Prepare the data for modeling
# Filter relevant columns and ensure data types are correct
df = df[['BRTH_YR', 'NM', 'CNT']]
df['CNT'] = df['CNT'].astype(int)

# Group by name and year to get total counts per year
grouped = df.groupby(['NM', 'BRTH_YR']).sum().reset_index()

# Create a dictionary to store predictions
predictions = []

# Iterate over each unique name to fit a model and predict
for name in grouped['NM'].unique():
    # Filter data for each name
    name_data = grouped[grouped['NM'] == name]
    
    # Prepare X (years) and y (counts)
    X = name_data['BRTH_YR'].values.reshape(-1, 1)
    y = name_data['CNT'].values
    
    # Check if there's enough data to fit a model
    if len(X) > 1:
        # Fit a linear regression model
        model = LinearRegression()
        model.fit(X, y)
        
        # Predict for 2015
        prediction_2015 = model.predict(np.array([[2015]]))[0]
        
        # Store the prediction in a list of dictionaries
        predictions.append({'NM': name, 'BRTH_YR': 2015, 'Predicted_CNT': prediction_2015})

# Convert predictions to a DataFrame
predictions_df = pd.DataFrame(predictions)

# Merge predictions with original data
combined_df = pd.concat([df, predictions_df.rename(columns={'Predicted_CNT': 'CNT'})], ignore_index=True)

# Save combined data to a new CSV file
combined_df.to_csv('predicted_NYC_baby_names_2015.csv', index=False)

print("Predictions saved to predicted_NYC_baby_names_2015.csv")