import requests

# The URL to access the local server
link = 'https://127.0.0.1:2999/liveclientdata/allgamedata'

try:
    # Disable SSL verification for local development (this can be a security risk for production)
    response = requests.get(link, verify=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the text from the response
        web_content = response.text

        # Save the text to a file
        with open('local_gamedata.txt', 'w', encoding='utf-8') as file:
            file.write(web_content)

        print("Data successfully downloaded and saved to 'local_gamedata.txt'.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
