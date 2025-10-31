# Alloy API Integration Assignment

## Overview

This project uses Python3 to simulate a bank’s integration with the Alloy API to evaluate new applicants, validate their data, and process decisions (Approved, Manual Review, or Denied) in sandbox mode.

## Features

- Collects applicant details via console input or default test users.
- Validates console user input with regex to ensure data format integrity.
- Submits data to Alloy’s Sandbox /v1/evaluations endpoint.
- Processes and displays the decision outcome (1 of 3, below): Approved, Manual Review, Denied.
- Masks sensitive data (SSN) for terminal display.

## Requirements

- Python 3.8+
- requests
- python-dotenv

## Setup Instructions

### Clone the Repo!
```
$ git clone https://github.com/yourusername/alloy-tam-assignment.git
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
### Run the Script
```
$ python3 app.py
```
## Requirements

- Python 3.8 or higher (codes uses type hints that are on the relatively newer side, 3.8 is a safe modern baseline)
- Internet connection (for Alloy API)
- Alloy sandbox credentials (token & secret, add these to your .env file)

## Project Structure
```
├── app.py
├── get_parameters.py
├── requirements.txt
├── .env
└── README.md
```

## Example Run

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





## Notes

- This script was built as part of Alloy’s Technical Account Manager work assignment.
- All sensitive credentials are stored locally and excluded from version control.
- Code was both human-written and in collaboration with LLM technology. All comments are human-written
