import requests

# Specify the URL of your FastAPI endpoint
url = ""  # Update with your actual endpoint URL

# Specify the file you want to upload
file_path = "./dataset/heart_10.csv"  # Update with the path to your CSV file

# Open the file
with open(file_path, "rb") as file:
    files = {"file": file}

    # Send the POST request with the file
    response = requests.post(url, files=files)

# Print the response
print(response)
