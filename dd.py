import instaloader
import os
import pickle
import time
import requests
import qrcode

def download_posts_data(instagram_data_path, posts_per_account, pickle_directory, media_directory):
    try:
        loader = instaloader.Instaloader()
        loader.context.username = 'gggg_gkkkkllll'
        profile = instaloader.Profile.from_username(loader.context, 'gggg_gkkkkllll')

        with open(instagram_data_path, 'rb') as instagram_data_file:
            instagram_data = pickle.load(instagram_data_file)

        accounts_data = []

        for data in instagram_data:
            account_name = data.get('account_name')
            school_id = data.get('school')

            print(f"Processing account {account_name} from school {school_id}")

            try:
                profile = instaloader.Profile.from_username(loader.context, account_name)
            except instaloader.exceptions.ProfileNotExistsException:
                print(f"Profile {account_name} does not exist.")
                continue

            account_data = []

            count = 0
            for post in profile.get_posts():
                if count >= posts_per_account:
                    break

                post_data = {
                    'id': str(post.mediaid),
                    'text': post.caption,
                    'timestamp': post.date_utc.timestamp(),
                    'media': [],
                    'login': account_name,
                    'school': school_id
                }

                video_index = 0
                try:
                    for index, node in enumerate(post.get_sidecar_nodes()):
                        media_data = {'is_video': False}

                        if node.is_video:
                            # Обработка видео
                            video_url = f"https://www.instagram.com/p/{post.shortcode}/?img_index={video_index + 1}"
                            post_data['video_url'] = video_url

                            # Генерация QR-кода для видео
                            qr = qrcode.QRCode(
                                version=1,
                                error_correction=qrcode.constants.ERROR_CORRECT_L,
                                box_size=10,
                                border=4,
                            )
                            qr.add_data(video_url)
                            qr.make(fit=True)

                            qr_code_path = os.path.join(media_directory, f"{post.mediaid}_video_qr.png")
                            img = qr.make_image(fill_color="black", back_color="white")
                            img.save(qr_code_path)

                            video_thumb_path = os.path.join(media_directory, f"{post.mediaid}_{video_index}.jpg")
                            with open(video_thumb_path, 'wb') as thumb_file:
                                thumb_file.write(requests.get(node.display_url).content)

                            media_data.update({
                                'video_thumble': video_thumb_path,
                                'local_url': qr_code_path,
                                'is_video': True
                            })

                            video_index += 1

                        else:
                            # Обработка изображений
                            media_data['local_url'] = os.path.join(media_directory, f"{post.mediaid}_{index}.jpg")
                            with open(media_data['local_url'], 'wb') as image_file:
                                image_url = node.url if node.url else node.display_url
                                image_file.write(requests.get(image_url).content)

                        post_data['media'].append(media_data)

                    account_data.append(post_data)
                except Exception as e:
                    print(f"Failed to fetch metadata for post {post.mediaid}. Error: {e}")

                print(f"Downloaded data for post {count + 1} from {account_name} (school {school_id})")
                print(f"Post text: {post_data['text']}")
                print("-" * 30)

                count += 1

                time.sleep(2)

            if account_data:
                first_post = account_data[0]
                print(f"First post in {account_name} (school {school_id}): {first_post['text']}")
                print("-" * 30)

            accounts_data.extend(account_data)

        instagram_pickle_path = os.path.join(pickle_directory, 'instagram_data.pickle')
        with open(instagram_pickle_path, 'wb') as instagram_pickle_file:
            pickle.dump(accounts_data, instagram_pickle_file)

        print(f"Данные Instagram успешно сохранены в pickle файл: {instagram_pickle_path}")

    except instaloader.exceptions.InstaloaderException as e:
        print("Ошибка при загрузке данных:", e)

if __name__ == "__main__":
    instagram_data_path = 'C:/Users/dg078/Desktop/instaloader/school_socialmedia_data.pickle'
    posts_per_account = 1
    pickle_directory = 'C:/Users/dg078/Desktop/instaloader'
    media_directory = 'C:/Users/dg078/Desktop/instaloader/media'

    download_posts_data(instagram_data_path, posts_per_account, pickle_directory, media_directory)
