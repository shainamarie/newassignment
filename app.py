import requests, json
from flask import Flask, render_template, jsonify
import textwrap



app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = 'gwapakooo'


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/artists', methods=['GET'])
def artists():
	url = 'https://musicdemons.com/api/v1/artist'
	headers = {}
	response = requests.request('GET', url, headers = headers, allow_redirects=False)
	artist_dict = json.loads(response.text)


	return render_template('artists.html', artists=artist_dict)



@app.route('/songs', methods=['GET'])
def songs():
	url = 'https://musicdemons.com/api/v1/song'
	headers = {}
	response = requests.request('GET', url, headers = headers, allow_redirects=False)
	song_dict = json.loads(response.text)
	print(song_dict)

	return render_template('songs.html', songs=song_dict)


@app.route('/artist_songs/<artist_id>/<artist_name>', methods=['GET'])
def artist_songs(artist_id, artist_name):
	artist = artist_name
	print(artist)
	url = 'https://musicdemons.com/api/v1/artist/{}/songs'.format(artist_id)
	headers = {}
	response = requests.request('GET', url, headers = headers, allow_redirects=False)
	print(url)
	song_dict = json.loads(response.text)

	return render_template('artist_songs.html', songs=song_dict, artist=artist)


@app.route('/lyrics/<song_title>/<song_id>', methods=['GET'])
def lyrics(song_title, song_id):
	song_title=song_title
	url = 'https://musicdemons.com/api/v1/song/{}/lyrics'.format(song_id)
	url2 = 'https://musicdemons.com/api/v1/song/{}/artists'.format(song_id)
	headers = {}
	headers2 = {}
	response = requests.request('GET', url, headers = headers, allow_redirects=False)
	response2 = requests.request('GET', url2, headers = headers2, allow_redirects=False)
	print(url)
	print(url2)
	# print(response.text)
	song_dict = json.loads(response2.text)
	print(song_dict)

	lyric_dict = response.text
	value = """{}""".format(lyric_dict)


	final = textwrap.TextWrapper(width=30)

	word_list = final.wrap(text=value)


	

	for element in word_list:

		print(element)

	return render_template('lyrics.html', lyrics=word_list, title=song_title, songs=song_dict )



if __name__ == '__main__':
	app.run(debug=True)