from dotenv import load_dotenv
import os
import requests
import pandas as pd
# import webbrowser


# Load environment variables
load_dotenv('.env')
# print(os.getenv('NEWS_API_KEY'))

# Get news from newsapi.org


def get_news(*args):
    # create empty list to store news data
    news_data = []
    # iterate through the country codes passed as arguments
    for country_code in args:
        # build the URL for the API request using the country code,category and the API key
        URL = f'https://newsapi.org/v2/top-headlines?country={country_code}&category=general&technology&apiKey=' + os.getenv(
            'NEWS_API_KEY')
        # send the request and store the response in a variable
        response = requests.get(URL)
        # check if the request was successful
        if response.status_code == 200:
            # parse the JSON response and store it in a variable(data)
            data = response.json()
            news_data.append(data)
        else:
            # print the error message if the request was not successful
            print(
                f"Request for {country_code} failed with status code: {response.status_code}")
    # return the list of news data
    return news_data


# Pass multiple country codes as arguments to the function
news = get_news('us', 'ro', 'mx')

# iterate through the list of news data
for country_news in news:
    # store the news articles in a variable
    articles = country_news['articles']
    # iterate through the list of articles
    for article in articles:
        # store the article details in variables
        title = article['title']
        description = article['description']
        url = article['url']

        # Color codes for formatting the output
        RESET = "\033[0m"      # Reset all formatting
        RED = "\033[91m"       # Red text
        GREEN = "\033[92m"     # Green text
        YELLOW = "\033[93m"    # Yellow text
        BLUE = "\033[94m"      # Blue text
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        RESET = "\033[0m"

        # print the title, description, and URL for each article
        print(RED, BOLD + "Title:" + RESET, BOLD + title + RESET)
        print(GREEN, BOLD + "Description:" + RESET, description)
        print(YELLOW + "URL:" + RESET, UNDERLINE, BLUE + url + RESET)
        print()  # Add an empty line between articles
