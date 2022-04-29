from typing import Counter
from flask_app.main.api_requests import API_request, is_number_valid, InvalidInputException, ExternalRequestException, API_request, random_words, random_songs, songs_list
import pytest, collections

# FUNCTION: is_number_valid(user_input)
# test if function returns intiger for valid user input (intiger between 5 and 20)
def test_is_number_valid_passed():
    result = is_number_valid(5)
    assert isinstance(result, int)

# test if function returns exception for valid user ininput (non intiger)
def test_is_number_valid_nonintiger():
    with pytest.raises(InvalidInputException):
        is_number_valid('a')

# test if function returns exception for invalid user input (number out of 5 - 20 range)
def test_is_number_valid_outofrange():
    with pytest.raises(InvalidInputException):
        is_number_valid(1)

# FUNCTION: API_request(url)
# test if function returns json if random words API request is valid
def test_API_request_words_passed():
    response = API_request('https://random-words-api.vercel.app/word')
    assert isinstance(response, list)

# test if function returns json if random songs API request is valid
def test_API_request_songs_passed():
    response = API_request('https://musicbrainz.org/ws/2/recording?fmt=json&limit=1&query=recording:snake')
    assert isinstance(response, dict)

# test if function returns exception if API request is invalid
def test_API_request_APIerror():
    with pytest.raises(ExternalRequestException):
        response = API_request('https://random-words-api.vercel.app/worddddd')

# FUNCTION: random_words(number)
# test if function returns intiger for valid user input (intiger between 5 and 20)
def test_random_words_passed():
    result = random_words(5)
    assert isinstance(result, set)
    assert 0 < len(result) < 6

# FUNCTION: random_songs(words)
# test if function returns list of dictionaries with correct content for valid set of random words
def test_random_songs_passed():
    result = random_songs({'Lion'})
    assert isinstance(result, list)
    assert result[0].get('word') == 'Lion'
    assert 'Lion' in result[0].get('title')
    assert isinstance(result[0].get('artist'), str)
    assert isinstance(result[0].get('album'), str)

# test if function removes duplicate songs
def test_random_songs_duplicates():
    result =  random_songs({'Lion', 'Lion'})
    titles_list = []
    for song in result:
        titles_list.append(song.get('title'))
    titles_set = set(titles_list)
    assert len(titles_list) == len(titles_set)

# test if function returns list of dictionaries with correct content for set of unexisting words
def test_random_songs_doesntexist():
    result = random_songs({'jkhdjgewdhwehdwejhdkjewdkhdjhgfj'})
    assert isinstance(result, list)
    assert result[0].get('word') == 'jkhdjgewdhwehdwejhdkjewdkhdjhgfj'
    assert result[0].get('title') == 'No recording found!'
    assert result[0].get('artist') == '-'
    assert result[0].get('album') == '-'

# FUNCTION: random_words(user_input)
# test if function returns intiger for valid user input (intiger between 5 and 20)
def test_songs_list_passed():
    result = songs_list(5)
    assert isinstance(result, list)




