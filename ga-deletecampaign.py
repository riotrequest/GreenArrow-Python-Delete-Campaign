import requests

def delete_campaign(api_url, api_key, campaign_id):
    """
    Deletes a campaign from GreenArrow Studio using the specified API URL, API key, and campaign ID.
    """
    # Construct the full URL with the campaign ID
    full_url = f"{api_url}/v2/campaigns/{campaign_id}"

    # Headers including the Authorization
    headers = {
        "Authorization": f"Basic {api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        # Sending the DELETE request
        response = requests.delete(full_url, headers=headers)

        # Checking the response
        if response.status_code == 200:
            print("Campaign successfully deleted.")
            print(response.json())
        else:
            print("Failed to delete the campaign.")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
    except requests.RequestException as e:
        print("An error occurred while making the request:", e)

# API details
base_api_url = "http://example.com/ga/api"
api_key = "API_KEY_HERE_FROM_WEB_UI"

# Prompting for campaign ID
campaign_id = input("Enter the campaign ID to delete: ")

# Validating if the input is a number
if campaign_id.isdigit():
    campaign_id = int(campaign_id)
    # Call the function to delete the campaign
    delete_campaign(base_api_url, api_key, campaign_id)
else:
    print("Invalid campaign ID. Please enter a numeric value.")
