import requests # to send request to Alloy API
import os # to fetch .env
from dotenv import load_dotenv # to load .env for keys
import re # for input validation
import json # to package for payload

##API Keys##
load_dotenv()
token = os.getenv("ALLOY_WORKFLOW_TOKEN")
secret = os.getenv("ALLOY_WORKFLOW_SECRET")

# a function to validate each input to ensure it hits a regex and will not throw an error
def validate_input(value: str, input_type: str) -> bool: 
    # regex patterns
    patterns = {
        "SSN": r"^\d{9}$",
        "EMAIL": r'^(([^ \s"(),.:;<>@[\]]+(\.[^ \s"(),.:;<>@[\]]+)*)|(".+"))@(([^ \s"(),.:;<>@[\]]+\.)+[^ \s"(),.:;<>@[\]]{2,})$',
        "DATE": r"^(?:[-+]\d{2})?(?:\d{4}(?!\d{2}\b))(?:(-?)(?:(?:0[1-9]|1[0-2])(?:\1(?:[12]\d|0[1-9]|3[01]))?|W(?:[0-4]\d|5[0-2])(?:-?[1-7])?|(?:00[1-9]|0[1-9]\d|[12]\d{2}|3(?:[0-5]\d|6[1-6])))(?![T]$|[T][\d]+Z$)(?:[T\s](?:(?:(?:[01]\d|2[0-3])(?:(:?)[0-5]\d)?|24:?00)(?:[.,]\d+(?!:))?)(?:\2[0-5]\d(?:[.,]\d+)?)?(?:Z|(?:[+-])(?:[01]\d|2[0-3])(?::?[0-5]\d)?)?)?)?$",
        "STATE": r"^[A-Z]{2}$",
        "ZIP": r"^\d{5}(-\d{4})?$",
        "COUNTRY": r"^US$"
    }

    pattern = patterns.get(input_type.upper()) # set pattern as proper type for input data
    if not pattern:
        return True  # no pattern to check, so always valid

    flags = 0
    if input_type.upper() == "EMAIL":
        flags = re.IGNORECASE

    return bool(re.match(pattern, value.strip(), flags)) # matches value to regex, includes flags, forces boolean

# a function to hide PII data
def mask(value: str, keep: int = 4) -> str:
    length = len(value)
    if length <= keep:
        return value
    hidden_part = "*" * (length - keep)
    visible_part = value[-keep:] # python slice to include the last quanity of variables set to keep
    return hidden_part + visible_part

test_users = {
    "percy": {
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
        },
    "roger": {
        "name_first": "Roger", 
        "name_last": "Review",
        "birth_date": "1995-04-20",
        "ssn": "123456789",
        "email_address": "rogerrealty@rogerrealty.com",
        "address_line_1": "456 Main St",
        "address_line_2": "",
        "address_city": "Boseman",
        "address_state": "MT",
        "address_postal_code": "59715",
        "address_country_code": "US"
        },
    "darryl": {
        "name_first": "Darryl", 
        "name_last": "Deny",
        "birth_date": "1948-06-04",
        "ssn": "987654321",
        "email_address": "discretedarryl@moveyourmoney.com",
        "address_line_1": "4021 Flatlands Avenue",
        "address_line_2": "",
        "address_city": "Brooklyn",
        "address_state": "NY",
        "address_postal_code": "11234",
        "address_country_code": "US"
        }
}

# process default test data
def test_inputs():
    while True:
        choose_data = input(
            "Please select test applicant:\n"
            "1) Percy 'The Perfect' Priest\n"
            "2) 'Risky' Roger Review\n"
            "3) Darryl 'The Dastardly' Deny\n"
            "Choose '1', '2', or '3': "
        ).strip()

        if choose_data == '1':
            print ("You chose:\n")
            print(json.dumps(test_users["percy"], indent=2))
            print('\n')
            return test_users["percy"]
        elif choose_data == '2':
            print ("You chose:\n")
            print(json.dumps(test_users["roger"], indent=2))
            print('\n')
            return test_users["roger"]
        elif choose_data == '3':
            print ("You chose:\n")
            print(json.dumps(test_users["darryl"], indent=2))
            print('\n')
            return test_users["darryl"]
        else:
            print("Invalid input. Please enter '1', '2', or '3'.\n")

    
# prompt data input from user
def collect_inputs():

    print("---Application Information---")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    while True: # use while True to validate inputs with regexes. if valid, move one, if not, prompt the user to try again
        birth_date = input("Date of Birth (YYYY-MM-DD): ").strip()
        if validate_input(birth_date, "DATE"):
            break
        print("Invalid Date Format. Try again.")
    while True:
        ssn = input("SSN (9 digits, no dashes): ").strip()
        if validate_input(ssn, "SSN"):
            break
        print("Invalid SSN. Try again.")
    while True:
        email = input("Email Address: ").strip()
        if validate_input(email, "EMAIL"):
            break
        print("Invalid Email Format. Try again.")

    print("---Address Information---")
    address_line_1 = input("Address Line 1: ").strip()
    address_line_2 = input("Address Line 2 (optional): ").strip()
    city = input("City: ").strip()
    while True:
        state = input("State (2 letters, e.g. NY): ").strip().upper()
        if validate_input(state, "STATE"):
            break
        print("Invalid State Format. Try again.")
    while True:
        zip_code = input("Zip Code: ").strip()
        if validate_input(zip_code, "ZIP"):
            break
        print("Invalid Zip Code Format. Try again.")
    country = "US" # hardcode to US

    # print entered data to console
    print("\nYou entered:")
    print(first_name, last_name, birth_date, mask(ssn), email)
    print(address_line_1, address_line_2, city, state, zip_code, country)

    return {
        "name_first": first_name,
        "name_last": last_name,
        "birth_date": birth_date,
        "ssn": ssn,
        "email_address": email,
        "address_line_1": address_line_1,
        "address_line_2": address_line_2,
        "address_city": city,
        "address_state": state,
        "address_postal_code": zip_code,
        "address_country_code": country
    }

def submit(payload):
    response = requests.post(
        "https://sandbox.alloy.co/v1/evaluations/",
        auth=(token, secret),
        headers={"Content-Type": "application/json"},
        json=payload, # send data here
        timeout=20 # give timeout delay
    )

    print("Status code:", response.status_code)

    try:
        data = response.json()
        # Pretty-print the full JSON response
        #print(json.dumps(data, indent=2))

        # --- Handle Alloy's decision logic ---
        summary = data.get("summary", {})
        outcome = summary.get("outcome")

        if outcome == "Approved":
            print("Congratulations! You are approved.")
        elif outcome == "Manual Review":
            print("Your application is under review. Please wait for further updates.")
        elif outcome == "Denied": # note, the instructions say "Deny" is the outcome, but it appears to be "Denied"
            print("Unfortunately, we cannot approve your application at this time.")
        else:
            print("Unexpected outcome:", outcome)
    except Exception as e:
        print("Error processing response:", e)
        print("Raw response text:", response.text)
        
def main():
    while True:
        choose_method = input(
            "Do you wish to use default test data, or manual entry?\n"
            "1) Default test\n"
            "2) Manual entry\n"
            "Select '1' or '2':\n\n "
        ).strip()

        if choose_method == '1':
            payload = test_inputs()       # assuming this provides default data
            break
        elif choose_method == '2':
            payload = collect_inputs()    # assuming this collects manual input
            break
        else:
            print("Invalid input. Please enter '1' or '2'.\n")

    while True:
        send_data = input("Do you wish to send this data in a request? (Y / N)\n  ").strip().upper()

        if send_data == "Y":
            if not token or not secret:
                raise SystemExit(
                "Missing Alloy credentials. Set ALLOY_WORKFLOW_TOKEN and ALLOY_WORKFLOW_SECRET in your .env"
                )
            
            submit(payload)
            break  # exits the loop after submission
        elif send_data == "N":
            print("Request canceled.")
            break  # exits the loop gracefully
        else:
            print("Invalid input. Please enter 'Y' or 'N'.\n")

if __name__ == "__main__":
    main()