import requests

# Paste your Watson Machine Learning service apikey here
# Use the rest of the code sample as written
apikey = "5dImTj6rX5qDBUCXYoSKFu8FxI4ASGh_6ZpV7ER7WUBe"

# Get an IAM token from IBM Cloud
url = "https://us-south.ml.cloud.ibm.com"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
IBM_cloud_IAM_uid = "2206933d-fea8-44fb-8957-a56ad5f0595a"
IBM_cloud_IAM_pwd = "ac1a3950-f51b-4bfb-b573-8ceed31338f9"
response = requests.post(url, headers=headers, data=data, auth=(IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd))
print(response)
iam_token = response.json()["access_token"]
print(iam_token)
