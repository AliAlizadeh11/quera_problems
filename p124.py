import requests
page = requests.get('https://varzesh3.com')
print(page)
print(page.text)