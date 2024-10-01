import requests
import json
import logging
import os
from Utils.data_generator import *
from dotenv import load_dotenv
# import os
# Load .env file
load_dotenv()

class RegisterationLoginAPIPage():
    def post_request_and_get_response(self,name,job):
        url = "https://reqres.in/api/users"
        payload = {
            "name": name,
            "job": job
        }

        # Send the POST request
        response = requests.post(url, json=payload)

        # Check the response status
        assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"
        logging.info(response.json())
        return response

    def verify_response(self,response,name,job):
        response_json = response.json()
        # Validate response JSON
        logging.info(response_json["name"])
        assert response_json["name"] == name, "Name does not match"
        logging.info(response_json["job"])
        assert response_json["job"] == job, "Job does not match"
        logging.info(response_json["id"])
        assert "id" in response_json, "ID not present in the response"
        logging.info(response_json["createdAt"])
        assert "createdAt" in response_json, "createdAt timestamp not present in the response"

    def get_request_and_get_response(self,url):
        url = "https://reqres.in/api/users"
        # Send the POST request
        response = requests.get(url)

        # Check the response status
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        logging.info(response.json())
        return response.json()

    def post_request_register_and_validate_response(self,test_data):
        url = os.getenv("API_URL")
        # (url=os.getenv('URL'))
        # global test_data
        # test_data = generate_user_data()
        headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=E3DF9240EE99810FCF17F38B64FF615D'
    }
        payload = {
            "customer.firstName": test_data["username"],
            "customer.lastName": test_data["username"],
            "customer.address.street": test_data["username"],
            "customer.address.city": test_data["username"],
            "customer.address.state": test_data["username"],
            "customer.address.zipCode": "1231231",
            "customer.phoneNumber": "",
            "customer.ssn": "12312",
            "customer.username": test_data["username"],
            "customer.password": test_data["password"],
            "repeatedPassword": test_data["password"]
        }
        print(payload)
        # Send the POST request
        response = requests.post(url,headers=headers, json=payload)
        # Verify if the word "Welcome" appears in the response
        logging.info(response.text)
        assert "Welcome" in response.text, "The word 'Welcome' was not found in the response"

    def post_request_login_and_validate_response(self,test_data):
        url = os.getenv("API_URL")
        headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=E3DF9240EE99810FCF17F38B64FF615D'
    }
        payload = f'username={test_data['username']}&password={test_data["password"]}'
        print(payload)
        # Send the POST request
        response = requests.post(url,headers=headers, json=payload)
        # Verify if the word "Welcome" appears in the response
        logging.info(response.text)
        assert "Welcome" in response.text, "The word 'Welcome' was not found in the response"




