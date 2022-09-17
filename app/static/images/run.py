import requests

r = requests.get('https://media4.giphy.com/media/BQ1QyFrFEa7rmdSamD/giphy.gif')
with open('triangles.gif', 'wb') as f:
	f.write(r.content)