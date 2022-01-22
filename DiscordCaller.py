import requests
import json
from utils import *

DISCORD_API_URL = 'https://discord.com/api/v9/invites/{}?with_counts=true&with_expiration=true'

def keys(d, c = []):
      return [i for a, b in d.items() for i in ([c+[a]] if not isinstance(b, dict) else keys(b, c+[a]))]

def get_discord_info(discord_profile):
    try:
        discord_user_info = dict()
        discord_id = get_url_from_link(discord_profile)
        url = DISCORD_API_URL.format(discord_id)
        response = requests.request("GET", url)
        if response.text:
            response_body = json.loads(response.text)
            objectKeys = list(map('.'.join, keys(response_body)))
            if 'approximate_member_count' in objectKeys:
                discord_user_info.update({'MemberCount':response_body['approximate_member_count'] })
            if 'approximate_presence_count' in objectKeys:
                discord_user_info.update({'OnlineCount':response_body['approximate_presence_count'] })
        return discord_user_info
    except Exception as e:
        print("An error occurred while getting user info",e)
