import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/2")
print(response.status_code)  # HTTP status code
print(response.text)         # Response body as a string
print(response.json())       # Response body as a Python dictionary

# data = {"title": "New Post", "body": "Hello, world!", "userId": 1}
# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
# print(response.status_code)  # 201 Created
# print(response.json())
