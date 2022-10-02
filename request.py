import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Price per week':15, 'Population of city':1800000, 'Monthly income of riders':5800, 'Average parking rates per month':50})

print(r.json())



