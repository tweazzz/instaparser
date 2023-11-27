
import instaloader
import os
import re

def clean_username(username):
    return re.sub(r'[^\w]', '', username)

def download_user_posts(target_username, max_posts=5):
    L = instaloader.Instaloader()

    your_username = 'gggg_gkkkkllll'
    your_password = 'gambitcsgo777'


    L.context.login(your_username, your_password)

    profile = instaloader.Profile.from_username(L.context, target_username)

    clean_username_str = clean_username(target_username)

    user_directory = f'{clean_username_str}_posts'


    for index, post in zip(range(max_posts), profile.get_posts()):
        L.download_post(post, target=user_directory)

download_user_posts('cristiano', max_posts=2)