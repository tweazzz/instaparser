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
    os.makedirs(user_directory, exist_ok=True)

    for index, post in zip(range(max_posts), profile.get_posts()):
        post_directory = os.path.join(user_directory, f'post_{index + 1}')
        os.makedirs(post_directory, exist_ok=True)

        # Скачиваем изображения
        for i, image in enumerate(post.get_sidecar_nodes()):
            image_filename = os.path.join(post_directory, f'image_{i + 1}.jpg')
            with open(image_filename, 'wb') as img_file:
                img_file.write(image.get_resources()[0].content)

        if post.is_video:
            video_url = post.video_url
            video_filename = os.path.join(post_directory, 'video.mp4')
            L.download_videos(video_url, target=video_filename)

download_user_posts('cristiano', max_posts=2)