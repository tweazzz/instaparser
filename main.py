import instaloader
import os
import pickle
import time

def download_posts_data(account_list, posts_per_account, pickle_directory):
    try:
        # Создаем экземпляр Instaloader
        loader = instaloader.Instaloader()

        # Проходимся по каждому аккаунту в списке
        for account in account_list:
            # Устанавливаем контекст Instaloader на текущий аккаунт
            loader.context.username = 'gggg_gkkkkllll'

            # Получаем профиль Instagram для текущего аккаунта
            profile = instaloader.Profile.from_username(loader.context, account)
            count = 0

            # Загружаем информацию о ранее скачанных данных постов (если она есть)
            existing_posts_data_file_path = os.path.join(pickle_directory, f'{account}_posts_data.pickle')
            if os.path.exists(existing_posts_data_file_path):
                with open(existing_posts_data_file_path, 'rb') as existing_posts_data_file:
                    existing_posts_data = pickle.load(existing_posts_data_file)
            else:
                existing_posts_data = []

            # Создаем список для хранения данных постов для каждого аккаунта
            account_data = []

            # Проходимся по каждому посту профиля
            for post in profile.get_posts():
                # Если достигнуто указанное количество постов для аккаунта, выходим из цикла
                if count >= posts_per_account:
                    break

                # Проверяем, есть ли пост с таким айди в ранее скачанных данных
                if any(existing_post['id'] == str(post.mediaid) for existing_post in existing_posts_data):
                    print(f"Post {post.mediaid} already exists in the previous data. Skipping...")
                    continue

                # Создаем словарь для хранения данных о текущем посте
                post_data = {
                    'id': str(post.mediaid),
                    'text': post.caption,
                    'timestamp': post.date_utc.timestamp(),
                    'media': []  # Создаем список для хранения данных о медиафайлах (изображениях и видео)
                }

                # Обработка изображений
                for image in post.get_sidecar_nodes():
                    media_data = {
                        'url': image.display_url,
                        'is_video': image.is_video
                    }
                    post_data['media'].append(media_data)

                # Обработка видео (если есть)
                if post.is_video:
                    video_url = post.video_url
                    video_data = {
                        'url': video_url,
                        'is_video': True
                    }
                    post_data['media'].append(video_data)

                # Добавляем данные поста в список для текущего аккаунта
                account_data.append(post_data)

                print(f"Downloaded data for post {count + 1} from {account}")
                print("-" * 30)

                count += 1

                # Добавляем задержку перед следующим запросом
                time.sleep(2)

            # Сохраняем данные в файл pickle после успешного скачивания для текущего аккаунта
            pickle_file_path = os.path.join(pickle_directory, f'{account}_posts_data.pickle')
            with open(pickle_file_path, 'wb') as pickle_out:
                pickle.dump(account_data + existing_posts_data, pickle_out)

    except instaloader.exceptions.InstaloaderException as e:
        print("Ошибка:", e)

# Остальной код без изменений

# Список аккаунтов для парсинга
account_list = ['aya_shalkar']  # Замените на реальные имена аккаунтов
# Количество постов для каждого аккаунта
posts_per_account = 3  # Замените на нужное количество постов для каждого аккаунта
# Директория для сохранения файлов pickle
pickle_directory = 'C:/Users/Professional/Desktop/instapars'  # Замените на путь к директории, где вы хотите сохранить файлы pickle

# Вызываем функцию для скачивания данных и сохранения их в файлы pickle
download_posts_data(account_list, posts_per_account, pickle_directory)
