import requests

class JokeGenerator:
    def __init__(self):
        self.api_url = 'https://api.jokes.one/jod'

    def fetch_joke(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            joke = response.json()['contents']['jokes'][0]['joke']['text']
            return joke
        except requests.exceptions.HTTPError as http_err:
            return f'HTTP error occurred: {http_err}'
        except Exception as e:
            return f'An error occurred: {e}'

    def display_joke(self):
        print('Fetching a random joke...')
        joke = self.fetch_joke()
        print('Here is your joke:')
        print(joke)

if __name__ == '__main__':
    joke_generator = JokeGenerator()
    joke_generator.display_joke()