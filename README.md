# Alloy API Integration Assignment

## Overview

This project uses Python3 to simulate a bank’s integration with the Alloy API to evaluate new applicants, validate their data, and process decisions (Approved, Manual Review, or Denied) in sandbox mode.

This tool can be accessed via a Command Line interface or a Web Interface. 

## Features

- Collects applicant details via console input or default test users for CLI, or offers web form interface.
- Validates user input with regex to ensure data format integrity.
- Submits data to Alloy’s Sandbox /v1/evaluations endpoint.
- Processes and displays the decision outcome (1 of 3, below): Approved, Manual Review, Denied.

## Requirements

- Python 3.8+
- Flask
- requests
- python-dotenv

## Project Structure
```
├── app.py
├── main.py
├── get_parameters.py
├── requirements.txt
├── .env
├── README.md
└── templates
    └── index.html
```

## Setup Instructions

### Clone the Repo!
```
$ git clone https://github.com/andrewphillipdoss/alloy-tam-assignment.git
$ cd alloy-tam-assignment
```
### Setup your Virtual Environment!
```
$ python3 -m venv venv
$ source venv/bin/activate
```
### Install Dependencies!
```
$ pip install -r requirements.txt
```
### Set up environment variables 

First, Add your Alloy credentials to your local .env file (reference env.example).
```
ALLOY_WORKFLOW_TOKEN="your_token_here"
ALLOY_WORKFLOW_SECRET="your_secret_here"
```
### Run the Script - Option 1 - Command Line Interface
```
$ python3 main.py
```

## Example Run - Command Line Interface

First, you are prompted to select from the options of default user entries or a manual entry

```
$ python3 app.py
Do you wish to use default test data, or manual entry?
1) Default test
2) Manual entry
Select '1' or '2':
```

Let's go with default users for this example. Say we select '1'. We will then be prompted:
```
Please select test applicant:
1) Percy 'The Perfect' Priest
2) 'Risky' Roger Review
3) Darryl 'The Dastardly' Deny
Choose '1', '2', or '3': 
```

Each of these cases is an example of an Approve, Manual Review, or Deny outcome. Once we select a user (say, 1 for example), we are shown the data, and asked if we are ready to send a request:
```
You chose:

{
  "name_first": "Percy",
  "name_last": "Priest",
  "birth_date": "1970-01-01",
  "ssn": "777777777",
  "email_address": "percyisperfect@gmail.com",
  "address_line_1": "12345 Sunset Blvd",
  "address_line_2": "",
  "address_city": "Los Angeles",
  "address_state": "CA",
  "address_postal_code": "90210",
  "address_country_code": "US"
}


Do you wish to send this data in a request? (Y / N)
```

We can choose 'Y', and see our outcome!
```
Status code: 201
Congratulations! You are approved.
```

## Run the Script - Option 2 - Web Interface
```
$ python3 app.py
```

## Example Run - Web Interface

You will see the below when you run the above script. Once the development server is running, visit http://127.0.0.1:5000 in your web browser to use the web app. 

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 311-457-223
 ```

## Notes

- This script was built as part of Alloy’s Technical Account Manager work assignment.
- All sensitive credentials are stored locally and excluded from version control.
- Code was both human-written and in collaboration with LLM technology. All comments are human-written.

