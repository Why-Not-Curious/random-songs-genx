import requests

word_gen_api = 'https://random-words-api.vercel.app/word'
song_gen_api = 'https://musicbrainz.org/ws/2/recording?fmt=json&limit=1&query=recording:'

# Create exceptions
class GeneralException(Exception):
    pass

class InvalidInputException(GeneralException):
    pass

class ExternalRequestException(GeneralException):
    pass


# Check if requestis  number between 5 and 20
def is_number_valid(user_input):
    try:
        number = int(user_input)
    except: 
        raise InvalidInputException
    if 5 <= number <= 20:
        return number
    else:
        raise InvalidInputException

# Single request from external API
def API_request(url):
    try:
        response = requests.get(url)
        response_json = response.json()
    except:
        raise ExternalRequestException
    return response_json

# Generate words list from random words API
def random_words(number):
    result = set()
    for i in range(1, number+1):
        response_json = API_request(word_gen_api)
        word = response_json[0].get('word')
        result.add(word)
    return result

# Generate songs list from Music Brainz API
def random_songs(words):
    result = []
    titles = []
    for word in words:
        url = song_gen_api + word
        response_json = API_request(url)
        try:
            recordings = response_json.get('recordings')[0]
            title = recordings.get('title')
            if title in titles:
                continue
            else:
                titles.append(title)
                artist_credit = recordings.get('artist-credit')[0]
                artist_name = artist_credit.get('name')
                releases = recordings.get('releases')[0]
                release_title = releases.get('title')
                song = {'word': word,
                            'title': title, 
                            'artist': artist_name,
                            'album': release_title}
        except:
            song = {'word': word,
                    'title': 'No recording found!', 
                    'artist': '-',
                    'album': '-'}
        result.append(song)
        result.sort(key=lambda k: (k.get('word')))
    return result

# Return songs list for given number
def songs_list(user_input):
    number = is_number_valid(user_input)
    words = random_words(number)
    result = random_songs(words)
    return result

        