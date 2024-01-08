import instaloader
import os
import pickle

def download_posts_data(usernames, n, pickle_file):
    try:
        loader = instaloader.Instaloader()

        posts_data = {}  # Создаем словарь для хранения данных постов

        for username in usernames:
            loader.context.username = 'gggg_gkkkkllll'

            profile = instaloader.Profile.from_username(loader.context, username)
            count = 0

            posts_data[username] = []  # Создаем подсловарь для каждого пользователя

            for post in profile.get_posts():
                if count >= n:
                    break

                post_data = {
                    'id': post.mediaid,
                    'text': post.caption,
                    'timestamp': post.date_utc.timestamp(),
                    'images': []  # Создаем список для хранения данных о каждой фотографии
                }

                # Добавляем данные для каждой фотографии в карусели
                for index, image in enumerate(post.get_sidecar_nodes()):
                    image_data = {
                        'url': image.display_url,
                        'is_video': image.is_video
                    }
                    post_data['images'].append(image_data)

                posts_data[username].append(post_data)  # Добавляем данные поста в подсловарь

                print(f"Downloaded data for post {count + 1} from {username}")
                print("-" * 30)

                count += 1

        # Save data to pickle file after successful download
        with open(pickle_file, 'wb') as pickle_out:
            pickle.dump(posts_data, pickle_out)

    except instaloader.exceptions.InstaloaderException as e:
        print("Ошибка:", e)

# Скачиваем данные и сохраняем в pickle файл
download_posts_data(['lalalalisa_m'], n=2, pickle_file='posts_data.pickle')
