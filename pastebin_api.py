import requests
key = "f20307e4cf5989e2b96c6295edd029d3"
url = "https://pastebin.com/api/api_post.php"

with open("test.py", "r") as file:
    print('hi')
    data = {
        "api_dev_key": key,
        "api_option": "paste",
        "api_paste_code": file.read(),
        "api_paste_format": "python"
    }
    r = requests.post(url, data = data)
    print(r.content)