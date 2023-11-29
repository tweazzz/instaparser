import instaloader
import os
import re
import requests

def clean_username(username):
    return re.sub(r'[^\w]', '', username)

def download_user_posts(target_username, max_posts=5):
    L = instaloader.Instaloader()

    # Подставьте сюда свои учетные данные
    your_username = 'gggg_gkkkkllll'
    your_password = '777kaz777'

    L.context.login(your_username, your_password)

    profile = instaloader.Profile.from_username(L.context, target_username)

    clean_username_str = clean_username(target_username)

    user_directory = f'{clean_username_str}_posts'
    os.makedirs(user_directory, exist_ok=True)

    posts = profile.get_posts()
    posts_downloaded = 0

    for post in posts:
        if posts_downloaded >= max_posts:
            break

        if not hasattr(post, 'location') or post.location is not None:
            continue

        post_directory = os.path.join(user_directory, f'post_{post.date_utc.strftime("%Y%m%d_%H%M%S")}')
        os.makedirs(post_directory, exist_ok=True)

        try:
            download_post(post, post_directory)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к Instagram API: {e}")
            continue
        except Exception as e:
            print(f"Ошибка при скачивании поста: {e}")
            continue

        posts_downloaded += 1

    print(f"Загружено {posts_downloaded} постов.")

def download_post(post, post_directory):
    if post.is_video:
        video_url = post.url
        video_filename = os.path.join(post_directory, 'video.mp4')
        try:
            response = requests.get(video_url)
            response.raise_for_status()
            with open(video_filename, 'wb') as video_file:
                video_file.write(response.content)
        except Exception as e:
            print(f"Ошибка при скачивании видео: {e}")
    else:
        try:
            image_url = post.url
            image_filename = os.path.join(post_directory, f'image_1.jpg')
            response = requests.get(image_url)
            response.raise_for_status()
            with open(image_filename, 'wb') as img_file:
                img_file.write(response.content)
        except Exception as e:
            print(f"Ошибка при скачивании изображения: {e}")

    caption_text = post.caption if post.caption is not None else ''
    caption_filename = os.path.join(post_directory, 'caption.txt')
    with open(caption_filename, 'w', encoding='utf-8') as caption_file:
        caption_file.write(caption_text)

    print(f"Пост успешно скачан.")

download_user_posts('ksm_malika', max_posts=5)