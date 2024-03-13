#!/usr/bin/env python3
import requests
import sys


def get_instagram_info(access_token):
    """
    I want to display my instagram account info
    """
    urls = f"https://graph.instagram.com/me?fields=id,username&access_token={access_token}"
    response = requests.get(urls)
    print(response.status_code)

    if response.status_code == 200:
        prof_data = response.json()
        user_id = prof_data.get('id')
        username = prof_data.get('username')

        print('Your Instagram User id is:', user_id)
        print('Your username is:', username)
        print()
    else:
        print("Failed to fetch your profile information")
    
    media_url = f"https://graph.instagram.com/me/media?fields=id,username&access_token={access_token}"
    media_r = requests.get(media_url)
    print(media_r.status_code)
    
    if media_r.status_code == 200:
        media_data = media_r.json()
        print(media_data)
        print()
    
    else:
        print("Failed to fetch media posts")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: <./executable.py> <access_token>")
        exit(1)
    access_token = sys.argv[1]
    get_instagram_info(access_token)


#https://api.instagram.com/oauth/authorize?client_id=1045952816468252&redirect_uri=https://www.delez.tech/auth/&scope=user_profile,user_media