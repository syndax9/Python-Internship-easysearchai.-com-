# Python-Internship-easysearchai.-com-
# Project Overview
## 1. Introduction
  This project aims to predict California housing prices using features like median income, total rooms, total bedrooms, population, households, and ocean  proximity.   It involves data loading, cleaning, exploratory data analysis (EDA), feature engineering, and model training with different algorithms.

## 2. Data Loading
  Load and inspect the dataset to understand its shape, structure, and basic statistics. Check data types, identify missing values, and compute initial metrics for numerical features.

## 3. Data Cleaning
  Handle missing values, particularly in 'total_bedrooms', by removing rows with these values to ensure a clean dataset.

## 4. Data Splitting
  Separate features (X) from the target variable ('median_house_value', y) and split the data into training and testing sets using an 80-20 ratio.

## 5. Exploratory Data Analysis (EDA)
  Visualize feature distributions and relationships using histograms and heatmaps to understand feature correlations with the target variable.

## 6. Data Transformation
  Normalize feature distributions with logarithmic transformations on features like 'total_rooms' and 'total_bedrooms'. Apply one-hot encoding to categorical      features like 'ocean_proximity' and create new features like 'bedroom_ratio' and 'household_rooms'.

## 7. Model Training and Evaluation
  Linear Regression: Standardize features, train the model, and evaluate performance using metrics like Mean Squared Error (MSE) and R2 Score, with visualizations   comparing actual vs. predicted values.
  Random Forest Regressor: Standardize features, train the model, and compare performance metrics with Linear Regression.
## 8. Model Comparison
  Compare both models based on train and test accuracy, MSE, and R2 Score using scatter plots and bar graphs to evaluate effectiveness.

# Instructions on how to set up and run the model training script

To set up and run the Flask API you’ve created locally, follow these steps:

## 1. Install Python and Pip
Verify Python Installation: Ensure Python is installed by checking the version with python --version or python3 --version in your terminal or command prompt.
Install Pip: Pip is usually included with Python. Verify by running pip --version. If not installed, download and install it from the Python website.

## 2. Install Flask and Dependencies
Open Terminal/Command Prompt: Access your command line interface.
Install Flask and Numpy: Run the command pip install Flask numpy to install Flask and NumPy. Ensure these libraries are installed to support your Flask application.

## 3. Save Your Flask Application
Create a Python File: Open a text editor or Integrated Development Environment (IDE).
Paste the Code: Copy the provided Flask code into a new file and save it as app.py (or another name of your choice).

## 4. Save Your Model
Ensure Model File Exists: Place your model.pkl file in the same directory as app.py. This file is necessary for loading the model in your Flask application.

## 5. Run the Flask Application
Navigate to the Project Directory: Use cd to change to the directory where app.py is located.
Start the Flask Server: Run python app.py or python3 app.py in the terminal. This command starts the Flask development server and makes your API accessible locally.

## 6. Test the API
Access the API: Open a web browser or use an API testing tool like Postman to interact with your API.

Health Check: Visit http://127.0.0.1:8000/health to check if the server is running.
Prediction Endpoint: Use Postman or curl to make POST requests to http://127.0.0.1:8000/predict with JSON data containing the features key.
Model Info: Access http://127.0.0.1:8000/model-info to view model information.

## 7. Handle Errors
Check for Errors: If you encounter errors, check the terminal output where the Flask server is running. The error messages can help identify issues with code execution or missing files.
## 8. Stop the Flask Server
Terminate Server: To stop the server, return to the terminal where Flask is running and press Ctrl + C.
By following these steps, you'll be able to set up, run, and test your Flask API locally.
