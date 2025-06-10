import requests

access_token = "YOUR_ACCESS_TOKEN"
org_id = "YOUR_ORG_ID"
file_path = "contacts.csv"
upload_url = "https://workdrive.zoho.com/api/v1/upload?parent_id=YOUR_FOLDER_ID"

headers = {
    "Authorization": f"Zoho-oauthtoken {access_token}",
    "X-WORKDRIVE-ORG": org_id
}

files = {
    'content': open(file_path, 'rb')
}

response = requests.post(upload_url, headers=headers, files=files)

print(response.status_code)
print(response.json())