import requests
import json

# Sample API endpoint URLs
get_url = "https://jsonplaceholder.typicode.com/todos/1"
post_url = "https://jsonplaceholder.typicode.com/posts"

# Function to make a GET request and print the JSON response
def get_sample_json():
    response = requests.get(get_url)
    if response.status_code == 200:
        data = response.json()
        print("GET Response:")
        print(json.dumps(data, indent=2))
    else:
        print(f"Error: {response.status_code}")

# Function to make a POST request with JSON data and print the JSON response
def post_sample_json():
    # Sample JSON data for POST request
    post_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(post_url, json=post_data)
    if response.status_code == 201:
        data = response.json()
        print("POST Response:")
        print(json.dumps(data, indent=2))
    else:
        print(f"Error: {response.status_code}")

# Main execution
if __name__ == "__main__":
    print("Making a GET request...")
    get_sample_json()

    print("\nMaking a POST request...")
    post_sample_json()
