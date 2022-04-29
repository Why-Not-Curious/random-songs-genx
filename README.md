## random-songs-generator

Random songs generator Flask based web app. Based on number stated by user app returns corresponding number of random songs including random word in the title. How it works?

* User requests number from 5 to 20 as part of URL e.g. *127.0.0.1:5000/random_songs/7*
* Random set of unique words is generated. Data is revreived from external API.
* Random sorted list of unique songs is generated. Every song includes subsequent random word from set in it's title. For every word -  song pair there's information about album title and artist name. Chosen songs are always best ranked songs from resource list. Data is revreived from external API.
* Result is returned through simple web app.

### How to start server?

Fork this repo and clone it to your choosen directory (alternatively you can just download a .zip file and unpack it).
```
git clone https://github.com/kajarosz/random-songs-generator.git
```

Install dependencies - required packages are listed in requirements.txt file. You may need to use pip3 instead of just pip.
```
pip install -r requirements.txt
```

Run run_app.py file in Python. You may need to use python3 instead of just python.
```
python run_app.py
```

### How to make requests?

Flask web server starts at port 127.0.0.1:5000 by default. In order to generate {number} of random songs enter following URL in your browser:

*127.0.0.1:5000/random_songs/{number}*

### How to run tests?

In project directory run:
```
pytest
```

### Possible improvements

In order to provide better UX, better solution for user requests could be developed. Typing chosen number as user input in URL is not optimal solution, as it's not user friendly and creates risk for wrong input (number out of range, nonintiger etc.). Great improvement would be creating view with numbered buttons -  after clicking button with chosen number, user would receive page response with random songs.

Another idea is adding links to presented songs e.g. Spotify deeplinks. This could be obtained through Spotify API.

### Public APIs used in the project

* *https://random-words-api.vercel.app/word*
* *https://musicbrainz.org/doc/MusicBrainz_API*
