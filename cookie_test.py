import requests

response = requests.get("https://www.csdn.com")

cookies = response.cookies

for cookie in cookies:
    print(f"Name:{cookie.name}, Value:{cookie.value}")