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

The process of model training and evaluation involves selecting appropriate machine learning algorithms, training them on the dataset, and assessing their performance using various metrics. This project utilizes two models: Linear Regression and Random Forest Regressor. Here's a detailed explanation of the steps involved:

## 1. Linear Regression Model
Feature Scaling: Before training, the features are standardized using StandardScaler. This involves rescaling the features so that they have a mean of zero and a standard deviation of one. Standardization is crucial for algorithms like Linear Regression, which are sensitive to the scale of the data.

Model Training: The Linear Regression model is trained on the scaled training data (X_train_s). The model learns the relationships between the features and the target variable (median_house_value) by minimizing the residual sum of squares between the observed targets and the predicted targets.

Predictions and Evaluation: The trained model is used to make predictions on the scaled test data (X_test_s). 

The performance of the model is evaluated using metrics such as:
Mean Squared Error (MSE): Measures the average of the squares of the errors, providing a sense of how far off predictions are from actual values.
R2 Score: Indicates the proportion of the variance in the dependent variable that is predictable from the independent variables. A higher R2 score signifies a better fit.
Visualization: The actual vs. predicted values are visualized using scatter plots, allowing for a visual assessment of the model's performance. A diagonal line representing perfect prediction is included for reference.
## 2. Random Forest Regressor
Model Training: The Random Forest Regressor is trained on the same standardized features. This ensemble learning method combines multiple decision trees, each trained on a random subset of the data, to improve prediction accuracy and control overfitting.

Predictions and Evaluation: The model's predictions on the test set are evaluated similarly to the Linear Regression model. The same metrics (MSE and R2 Score) are used to assess its performance.

Visualization: Like the Linear Regression model, the actual vs. predicted values are plotted to visualize the model's accuracy.
## 3. Model Comparison
The performance of the Linear Regression and Random Forest Regressor models is compared using their evaluation metrics. This comparison helps determine which 
model is more accurate and reliable for predicting housing prices.

Evaluation Metrics:
Train Accuracy: The accuracy of the model on the training dataset.
Test Accuracy: The accuracy of the model on the testing dataset.
Mean Squared Error (MSE): Lower values indicate better accuracy.
R2 Score: A higher score closer to 1 indicates a better fit.

The Random Forest Regressor generally outperforms the Linear Regression model in this project, as indicated by its higher R2 score and lower MSE. The final chosen model, in this case, Random Forest, is saved for future use, indicating that it has been deemed the more accurate and robust model for predicting California housing prices.


# Instructions on how to set up and run API locally

## 1. Install Required Packages
Objective: Ensure that you have all the necessary software libraries installed to run the Flask application.

Steps:

Check Python Installation: Verify that Python is installed on your system. You can do this by opening a terminal or command prompt and typing python --version. If Python is not installed, download and install it from the official Python website.

Install Flask: Flask is a lightweight web framework used to build web applications. You need Flask to create and run the web server for your application.

Install NumPy: NumPy is a library for numerical operations in Python. It is used to handle and manipulate arrays, which are essential for processing features and making predictions.

Ensure Pickle is Available: Pickle is part of Python's standard library, so you don't need to install it separately. It's used for serializing and deserializing Python objects, which is necessary for loading the trained machine learning model.

Use a Package Manager: Use a package manager like pip to install Flask and NumPy. You can do this by running the appropriate commands in your terminal or command prompt.

## 2. Save Your Model
Objective: Ensure that your trained machine learning model is correctly saved and accessible for your Flask application.

Steps:

Train and Save the Model: You should have already trained a machine learning model using a library like Scikit-Learn, TensorFlow, or PyTorch. Once trained, save the model to a file using serialization methods such as pickle.

File Naming and Location: Save the serialized model file with a clear name (e.g., model.pkl). Ensure this file is placed in the same directory as your Flask application code, or adjust the file path in your code to match its location.

Verify Model File: Confirm that the model file exists and is not corrupted. You can check this by attempting to load the file in a Python script or interactive session.

## 3. Create the Flask Application
Objective: Set up the Flask application by creating and configuring the necessary Python file.

Steps:

Create a New Python File: Open your preferred text editor or Integrated Development Environment (IDE). Create a new file named app.py or another name of your choice.

Paste Application Code: Copy the provided Flask application code into this file. This code defines the routes and logic for your web server, including endpoints for health checks, predictions, and model information.

Understand the Structure: Familiarize yourself with the structure of the Flask application. This includes understanding how the routes are defined, how the model is loaded, and how predictions are made based on incoming requests.

Save the File: Save the file in the directory where you intend to run your Flask server.

## 4. Run the Flask Application
Objective: Start the Flask development server to make the application accessible and operational.

Steps:

Open Terminal or Command Prompt: Access your command line interface, which is where you will run the Flask server.

Navigate to the Project Directory: Change the directory to where your app.py file is located. Use commands like cd (change directory) to navigate.

Start the Flask Server: Execute the command to run the Flask application. This will start the development server and make your application available at a local URL.

Verify Server Start: Check the terminal or command prompt output for messages indicating that the Flask server is running. Typically, you will see a message with the URL where the server is accessible, such as http://127.0.0.1:8000.

By following these detailed steps, you'll be able to set up, configure, and run your Flask application, ensuring that all components are correctly installed and operational.
