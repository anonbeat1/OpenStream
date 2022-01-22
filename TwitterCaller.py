import requests

from utils import *

TWITTER_TOKEN = '<TWITTER_TOKEN>'

def create_url(username, user_fields ):

    url = "https://api.twitter.com/2/users/by?usernames={}&{}".format(username, user_fields)
    return url

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {TWITTER_TOKEN}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_user_info(profile_link):
    try:

        username = get_url_from_link(profile_link)
        user_info = dict()
        user_fields  = "user.fields=public_metrics"

        url = create_url(username,user_fields)
        json_response = connect_to_endpoint(url)

        user_info = {
            'follower':json_response['data'][0]['public_metrics']['followers_count'],
            'tweet':json_response['data'][0]['public_metrics']['tweet_count'],
            'profile_link':username
        }
        return user_info if user_info else {}
    except Exception as e:
        print("An error occurred while getting data ",e)
        return None
