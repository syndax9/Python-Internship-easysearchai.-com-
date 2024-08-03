# Python-Internship-easysearchai.-com-
Project Overview
1. Introduction
  This project aims to predict California housing prices using features like median income, total rooms, total bedrooms, population, households, and ocean proximity.   It involves data loading, cleaning, exploratory data analysis (EDA), feature engineering, and model training with different algorithms.

2. Data Loading
  Load and inspect the dataset to understand its shape, structure, and basic statistics. Check data types, identify missing values, and compute initial metrics for     numerical features.

3. Data Cleaning
  Handle missing values, particularly in 'total_bedrooms', by removing rows with these values to ensure a clean dataset.

4. Data Splitting
  Separate features (X) from the target variable ('median_house_value', y) and split the data into training and testing sets using an 80-20 ratio.

5. Exploratory Data Analysis (EDA)
  Visualize feature distributions and relationships using histograms and heatmaps to understand feature correlations with the target variable.

6. Data Transformation
  Normalize feature distributions with logarithmic transformations on features like 'total_rooms' and 'total_bedrooms'. Apply one-hot encoding to categorical       
  features like 'ocean_proximity' and create new features like 'bedroom_ratio' and 'household_rooms'.

7. Model Training and Evaluation
  Linear Regression: Standardize features, train the model, and evaluate performance using metrics like Mean Squared Error (MSE) and R2 Score, with visualizations   
                     comparing actual vs. predicted values.
  Random Forest Regressor: Standardize features, train the model, and compare performance metrics with Linear Regression.
8. Model Comparison
  Compare both models based on train and test accuracy, MSE, and R2 Score using scatter plots and bar graphs to evaluate effectiveness.
