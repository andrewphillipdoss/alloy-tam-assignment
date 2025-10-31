# Alloy API Integration Assignment

## Overview

This project uses Python3 to simulate a bank’s integration with the Alloy API to evaluate new applicants, validate their data, and process decisions (Approved, Manual Review, or Denied) in sandbox mode.

## Features

- Collects applicant details via console input or default test users.
- Validates console user input with regex to ensure data format integrity.
- Submits data to Alloy’s Sandbox /v1/evaluations endpoint.
- Processes and displays the decision outcome (1 of 3, below): Approved, Manual Review, Denied.
- Masks sensitive data (SSN) for terminal display.

## Setup Instructions

### Clone the Repo!
```
git clone https://github.com/yourusername/alloy-tam-assignment.git
cd alloy-tam-assignment
```
### Setup your Virtual Environment!
```
python3 -m venv venv
source venv/bin/activate
```
### Install Dependencies!
```
pip install -r requirements.txt
```
### Set up environment variables: Add your Alloy credentials to the .env file.
```
ALLOY_WORKFLOW_TOKEN=your_token_here
ALLOY_WORKFLOW_SECRET=your_secret_here
```
### Run the Script
```
python3 main.py
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

## Notes

- This script was built as part of Alloy’s Technical Account Manager work assignment.
- All sensitive credentials are stored locally and excluded from version control.
- Code was both human-written and in collaboration with LLM technology. All comments are human-writen
