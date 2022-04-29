## random-songs-generator

Description

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

Improvements
