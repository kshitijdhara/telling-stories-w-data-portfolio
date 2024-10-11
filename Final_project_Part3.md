---
title: Final_project_Part_3
layout: template
filename: Final_project_Part3.md
---
## Final Project Part 3

### Name: Kshitij Dhara
### Andrew ID: kdhara

---
- [The final data story](#the-final-data-story)
    - [Shorthand Preview Link](#shorthand-preview-link)
  - [Changes made since Part II](#changes-made-since-part-ii)
  - [Design Decisions and Observations](#design-decisions-and-observations)
  - [Key Features](#key-features)
  - [The audience](#the-audience)
  - [Final thoughts](#final-thoughts)

# The final data story

### [Shorthand Preview Link](https://preview.shorthand.com/AeYnmeJcNEMe7KOQ)

## Changes made since Part II
1. The chart being used to show top 10 names over time was logically wrong as it was calculating the top 10 names in the dataset and then plotting the line chart to show how their count varied over time. What I wanted to show was the top ten names each year. This way I wanted to show how a name moved up/down in ranks over the year and it's respective count for that year. This was particularly interesting because I was able to analyse if there were any new names that were more influential or not.
2. The second change was the gender neutrality chart. Based on the feedback given by the professor I made changes to better reflect how gender specific names started to become more gender neutral. With the new chart I was able to appeal to a newer audience which was people who were changing their genders.
3. The chart on depicting naming conventions per ethinicity was too cluttered and it was hard to interpret, adding a slider to select the number of names to check per ethinicity was a valuable feedback that I recieved. In addition to the above, I also encoporated the top name parameter from the chart mentioned above to get the most influential name in a particular ethinicity.
4. Depicting the impact of pop culture and other societal changes on naming schemes was a bit difficult hence I figured to create a word cloud for it. Additionally, I also researched about different trends during that time and mentioned them alongside the wordcloud to show why the names were so widely used. This also gave me a chance to connect with the audience by asking them which movie influenced a name in a way  that it become the top name
5. I was confused on how to implement forecasting for this dataset as tableau prompted an error stating that the date range was too small, hence I wrote a simple python script to use linear regression to analyse which names will rise to be top 10 in the year of 2015.
    ```python
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
    ```

6. The dataset consisted of duplicates and was hampering the accuracy of the charts hence I also performed some data preprocessing on the dataset before using it to create visualizations
   ```python
   import pandas as pd

    # Load the CSV file
    df = pd.read_csv('NYC_baby_names.csv')

    # Standardize the 'NM' column to lowercase
    df['NM'] = df['NM'].str.lower()

    # Group by all columns except 'CNT', sum the counts
    df = df.groupby(['BRTH_YR', 'GNDR', 'ETHCTY', 'NM', 'RNK'], as_index=False)['CNT'].sum()

    # Save the modified DataFrame to a new CSV file
    df.to_csv('modified_NYC_baby_names.csv', index=False)

   ```
7. Earlier I was struggling with my call to action, as the topic that I had chosen was not conventional and hence didn't have a significant importance, which is when I realised that a person's name is the identity of a person, it defines them and hence that should be my call to action. I should ask the audience on how they think their name has shaped their life?

## Design Decisions and Observations
Chose a color scheme that enhances readability and emphasizes key data points
Prioritized interactive elements to engage users and allow for deeper exploration
Balanced text and visuals to maintain user interest and convey information effectively
Learned the importance of data preprocessing for accurate visualizations
Discovered the challenge and importance of making complex data accessible to a diverse audience

## Key Features
Interactive name explorer
Gender neutrality heatmap
Ethnicity-based naming trends visualization
Cultural influence timeline
Name forecasting for 2015
Fun facts and short quizzes to keep the audience engaged

## The audience

- Expectant parents interested in name trends
- Sociologists and cultural researchers
- NYC residents curious about demographic shifts
- Data enthusiasts interested in name statistics
- People interested in changing their names
- And lastly, our Telling Stories with Data Class!

## Final thoughts
The project provides a comprehensive exploration of baby name trends in New York City from 2011 to 2014, highlighting the diversity and cultural influences in naming choices. By incorporating user feedback and enhancing data visualization, the project offered a more engaging and informative experience for its audience.

The project's progress was really amazing and the changes that can be seen is mostly because of thing learnt during the class which when encoporated increased the engagement and will to listen to the presentations in a way information sharing was efficient.