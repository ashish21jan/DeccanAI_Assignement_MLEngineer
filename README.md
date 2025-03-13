How to Run This Project
This repository demonstrates a house price prediction model deployed as a simple REST API. Below are the quick steps to set up, run, and test the project on your local machine.

1. Install Dependencies
Make sure you have Python 3.7+ installed.
Create a virtual environment (recommended).

and then use the command:
pip install -r requirements.txt

2. Run the API Locally
Ensure the file finalized_model.pkl is present in the project folder.
Start the API server:

python Deployment_Model.py

By default, the API will run on http://127.0.0.1:5000.

3. Test the API
Use an HTTP client such as Postman, cURL, or any REST tool to send a POST request to:

http://127.0.0.1:5000/predict

Make sure to provide JSON data in the body (e.g., a “features” array) according to the model’s expected input structure.

4. (Optional) Docker Usage
If you wish to containerize the application:

Build the Image (in the same directory as your Dockerfile):

docker build -t house-price-api 

Run the Container:
docker run -p 5000:5000 house-price-api

Your API will be available at http://127.0.0.1:5000.

That’s it! You can now send requests to the /predict endpoint to get house price predictions. If you have any questions or issues, please feel free to open an issue in the repository.
