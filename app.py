from flask import Flask, render_template, request
import requests, os, re
from dotenv import load_dotenv

app = Flask(__name__) # initialize Flask app, set to default
load_dotenv()

# set token and secret from .env
token = os.getenv("ALLOY_WORKFLOW_TOKEN")
secret = os.getenv("ALLOY_WORKFLOW_SECRET")

def validate_input(value: str, input_type: str) -> bool: # -> is sugar to highlight what type is returned
    # regex patterns for input validation
    patterns = {
        "birth_date": r"^(?:[-+]\d{2})?(?:\d{4}(?!\d{2}\b))(?:(-?)(?:(?:0[1-9]|1[0-2])(?:\1(?:[12]\d|0[1-9]|3[01]))?|W(?:[0-4]\d|5[0-2])(?:-?[1-7])?|(?:00[1-9]|0[1-9]\d|[12]\d{2}|3(?:[0-5]\d|6[1-6])))(?![T]$|[T][\d]+Z$)(?:[T\s](?:(?:(?:[01]\d|2[0-3])(?:(:?)[0-5]\d)?|24:?00)(?:[.,]\d+(?!:))?)(?:\2[0-5]\d(?:[.,]\d+)?)?(?:Z|(?:[+-])(?:[01]\d|2[0-3])(?::?[0-5]\d)?)?)?)?$",
        "ssn": r"^\d{9}$",
        "email_address": r'^(([^ \s"(),.:;<>@[\]]+(\.[^ \s"(),.:;<>@[\]]+)*)|(".+"))@(([^ \s"(),.:;<>@[\]]+\.)+[^ \s"(),.:;<>@[\]]{2,})$',
        "address_state": r"^[A-Z]{2}$",
        "address_postal_code": r"^\d{5}(-\d{4})?$",
        "address_country_code": r"^US$"
    }

    pattern = patterns.get(input_type) # set pattern as proper regex for input data
    if not pattern:
        return True  # no pattern to check, so always valid

    flags = 0 # flag allows us, in this case, to ignore the case of email
    if input_type == "email_address":
        flags = re.IGNORECASE

    return bool(re.match(pattern, value.strip(), flags)) # matches value to regex, includes flags, forces boolean


@app.route("/", methods=["GET", "POST"]) # decorator to call the index function when the URL is visited via either GET or POST
def index():
    # post request is called on a form submit
    if request.method == "POST":
        # sets form data to payload for posting to alloy API. request.form.get is a Flask-specific method
        payload = {
            "name_first": request.form.get("first_name"),
            "name_last": request.form.get("last_name"),
            "birth_date": request.form.get("birth_date"),
            "ssn": request.form.get("ssn"),
            "email_address": request.form.get("email"),
            "address_line_1": request.form.get("address_line_1"),
            "address_line_2": request.form.get("address_line_2"),
            "address_city": request.form.get("city"),
            "address_state": request.form.get("state"),
            "address_postal_code": request.form.get("zip_code"),
            "address_country_code": "US",
        }

        # init empty list for tracking multiple form field format errors
        errors = []

        # loop through payload and validate each input, append to errors if exists
        for key, value in payload.items():
            if not validate_input(value, key):
                errors.append(str(key).replace("_", " ").upper()+" is an invalid format")

        # if any errors exist, set message to disply them, as a warning
        if errors:
            return render_template("index.html", message="<br>".join(errors), alert_class="warning")

        # post JSON payload to alloy API. requests.POST returns a response object
        response = requests.post(
            "https://sandbox.alloy.co/v1/evaluations/",
            auth=(token, secret),
            json=payload
        )
        # handle outcomes. message and alert_class are veraibles for index.html, passed with render_template
        try:
            data = response.json() #.json() converts json to python dict
            outcome = data.get("summary").get("outcome") #.get() is a safe dict call (won't return error if value is empty)
            if outcome == "Approved":
                message = "Congratulations! You are approved."
                alert_class = "success"
            elif outcome == "Denied":
                message = "Unfortunately, we cannot approve your application at this time."
                alert_class = "danger"
            elif outcome == "Manual Review":
                message = "Your application is under review. Please wait for further updates."
                alert_class = "warning"
            else:
                message = "Unexpected outcome: " + outcome 
                alert_class = "info"
            return render_template("index.html", message=message, alert_class=alert_class)
        except Exception:
            # error handling for general errors
            return render_template("index.html", message="Error parsing response", alert_class="danger")

    return render_template("index.html") # renders on intial load from URL visit Get request
    
if __name__ == "__main__":
    app.run(debug=True)
