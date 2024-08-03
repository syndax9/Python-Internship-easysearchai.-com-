# Python-Internship-easysearchai.-com-
## Project Overview
### 1. Introduction
  This project aims to predict California housing prices using features like median income, total rooms, total bedrooms, population, households, and ocean  proximity.   It involves data loading, cleaning, exploratory data analysis (EDA), feature engineering, and model training with different algorithms.

### 2. Data Loading
  Load and inspect the dataset to understand its shape, structure, and basic statistics. Check data types, identify missing values, and compute initial metrics for numerical features.

### 3. Data Cleaning
  Handle missing values, particularly in 'total_bedrooms', by removing rows with these values to ensure a clean dataset.

### 4. Data Splitting
  Separate features (X) from the target variable ('median_house_value', y) and split the data into training and testing sets using an 80-20 ratio.

### 5. Exploratory Data Analysis (EDA)
  Visualize feature distributions and relationships using histograms and heatmaps to understand feature correlations with the target variable.

### 6. Data Transformation
  Normalize feature distributions with logarithmic transformations on features like 'total_rooms' and 'total_bedrooms'. Apply one-hot encoding to categorical      features like 'ocean_proximity' and create new features like 'bedroom_ratio' and 'household_rooms'.

### 7. Model Training and Evaluation
  Linear Regression: Standardize features, train the model, and evaluate performance using metrics like Mean Squared Error (MSE) and R2 Score, with visualizations   comparing actual vs. predicted values.
  Random Forest Regressor: Standardize features, train the model, and compare performance metrics with Linear Regression.
### 8. Model Comparison
  Compare both models based on train and test accuracy, MSE, and R2 Score using scatter plots and bar graphs to evaluate effectiveness.

## Instructions on how to set up and run the model training script

### 1. Prepare Your Environment
Ensure Python is Installed: Verify the Python version with python --version or python3 --version. Install Python if needed.
Install Required Libraries: Install necessary libraries such as numpy and pickle. Run pip install numpy if they are not already installed.

### 2. Load the Saved Model
Place the Model File: Ensure the model.pkl file is in the directory from where you will be running your application.
Load the Model: Use Python to load the model using pickle. This step involves writing a script that loads the model file into memory.

### 3. Prepare the Input Data
Format the Data: Ensure the input data matches the format expected by the model. This typically involves preparing a list or array of feature values.
Data Preprocessing: Apply any necessary preprocessing steps (e.g., scaling, normalization) to the input data as done during the model training.

### 4. Make Predictions
Predict Using the Model: Use the loaded model to make predictions on your input data. Pass the preprocessed features to the model’s predict method.

### 5. Integrate with Other Applications
Develop Integration Code: Write code in your application to use the model for making predictions. 
This involves:
Loading the model (using the pickle module).
Preprocessing input data.
Passing the data to the model.
Handling and using the model's predictions.

### 6. Test Predictions
Run Predictions: Test your application with various input data to ensure that the model provides accurate predictions and integrates well with your application.

### 7. Error Handling
Handle Errors: Implement error handling for issues such as file not found, corrupted model files, or incorrect input data formats. This ensures your application can manage exceptions gracefully.


## Instructions on how to set up and run the API Locally 

To set up and run the Flask API you’ve created locally, follow these steps:

### 1. Install Python and Pip
Verify Python Installation: Ensure Python is installed by checking the version with python --version or python3 --version in your terminal or command prompt.
Install Pip: Pip is usually included with Python. Verify by running pip --version. If not installed, download and install it from the Python website.

### 2. Install Flask and Dependencies
Open Terminal/Command Prompt: Access your command line interface.
Install Flask and Numpy: Run the command pip install Flask numpy to install Flask and NumPy. Ensure these libraries are installed to support your Flask application.

### 3. Save Your Flask Application
Create a Python File: Open a text editor or Integrated Development Environment (IDE).
Paste the Code: Copy the provided Flask code into a new file and save it as app.py (or another name of your choice).

### 4. Save Your Model
Ensure Model File Exists: Place your model.pkl file in the same directory as app.py. This file is necessary for loading the model in your Flask application.

### 5. Run the Flask Application
Navigate to the Project Directory: Use cd to change to the directory where app.py is located.
Start the Flask Server: Run python app.py or python3 app.py in the terminal. This command starts the Flask development server and makes your API accessible locally.

### 6. Test the API
Access the API: Open a web browser or use an API testing tool like Postman to interact with your API.

Health Check: Visit http://127.0.0.1:8000/health to check if the server is running.
Prediction Endpoint: Use Postman or curl to make POST requests to http://127.0.0.1:8000/predict with JSON data containing the features key.
Model Info: Access http://127.0.0.1:8000/model-info to view model information.

### 7. Handle Errors
Check for Errors: If you encounter errors, check the terminal output where the Flask server is running. The error messages can help identify issues with code execution or missing files.

### 8. Stop the Flask Server
Terminate Server: To stop the server, return to the terminal where Flask is running and press Ctrl + C.

## Documentation of the API endpoints

### Overview
This Flask application provides an API for making predictions using a pre-trained machine learning model. It includes endpoints for health checks, predictions, and model information. The application handles errors gracefully and validates input to ensure robustness.

### Components
Flask App Initialization

app = Flask(__name__): Initializes the Flask application instance.
Model Loading

The model is loaded from a file named model.pkl using pickle.
Error handling is included to manage:
FileNotFoundError: Raised if the model file does not exist.
pickle.UnpicklingError: Raised if there is an issue loading the model.

Endpoints

### /health
Method: GET
Description: Provides a health check endpoint to verify if the API is up and running.
Response: Returns a JSON object with a message indicating the API status, with a status code of 200.

### /predict
Method: POST
Description: Accepts JSON input for making predictions using the loaded model.

Request:
Content-Type: Application/json
Payload: Must include a features key with a list of numerical values (integers or floats).

Validation:
Ensures the request is in JSON format.
Checks if the features key is present and if its value is a list of numbers.

Error Handling:
Returns an error if the request is not in JSON format, the features key is missing, or if the value is not a list of numbers.
Handles ValueError and TypeError specifically, returning appropriate error messages.
Catches and handles any other exceptions, returning a generic error message with a status code of 500.
Response: Returns a JSON object with the prediction result or an error message.

### /model-info
Method: GET
Description: Provides information about the model's performance and characteristics.
Response: Returns a JSON object with details including:
Training data accuracy
Test data accuracy
Mean Squared Error (MSE)
R2 Score
Model description (a Forest Regressor or Random Forest Regression)
Error Handling

Model Loading Errors: Ensures the model file exists and is correctly loaded.
Request Errors: Validates request format and content, returning specific error messages for invalid requests.
General Errors: Catches unforeseen errors and provides a generic error response.
Running the Application

Command: app.run(debug=True, port=8000)
Description: Starts the Flask application in debug mode on port 8000.
This documentation outlines the structure, functionality, and error handling mechanisms of the Flask application, providing a comprehensive guide for understanding and using the API.

### Example Postman collection for testing the API

For API status: http://127.0.0.1:8000/health

For prediction: http://127.0.0.1:5000/predict

Example:

json input:
{
  "features" : [1.00895849, -0.81719509, -0.28350497,  0.50138838,  0.0471463 , 0.29577485,  0.20170303,  0.9585843 , -0.88880219,  1.45563404, -0.01564507, -0.35155493, -0.38278521, -0.85343965,  0.31153227]
}

output: 188385.02

For Model Information: http://127.0.0.1:5000/model-info
