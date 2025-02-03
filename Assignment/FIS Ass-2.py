#API Automation
#On the following endpoint - api.coindesk.com/v1/bpi/currentprice.json, automate the following
#1. Send the GET request
#2. Verify the response contains
#a. There are 3 BPI -i. USD ii. GBP iii. EUR
#b. The GBP ‘description’ equals ‘British Pound Sterling’.

import requests
import json


def test_coindesk01():
    # Send GET request
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    # Need to verify response status code
    assert response.status_code == 200, "Failed to fetch data from API"

    # Parse JSON response
    data = response.json()

    #2a: Verify the presence of 3 BPIs - USD, GBP, EUR
    bpi = data.get("bpi", {})
    assert "USD" in bpi, "USD currency not found in response"
    assert "GBP" in bpi, "GBP currency not found in response"
    assert "EUR" in bpi, "EUR currency not found in response"

    # 2b: Verify GBP description is 'British Pound Sterling'
    assert bpi["GBP"].get("description") == "British Pound Sterling", "GBP description mismatch"

    print("All tests passed successfully!!!")


# Run the test
if __name__ == "__main__":
    test_coindesk01()