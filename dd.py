import instaloader
import os
import pickle
import time

def download_posts_data(instagram_data_path, posts_per_account, pickle_directory):
    try:
        loader = instaloader.Instaloader()

        with open(instagram_data_path, 'rb') as instagram_data_file:
            instagram_data = pickle.load(instagram_data_file)

        accounts_data = []

        for data in instagram_data:
            account_name = data.get('account_name')
            school_id = data.get('school')

            print(f"Processing account {account_name} from school {school_id}")

            profile = instaloader.Profile.from_username(loader.context, account_name)
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

                for image in post.get_sidecar_nodes():
                    media_data = {
                        'url': image.display_url,
                        'is_video': image.is_video
                    }
                    post_data['media'].append(media_data)

                if post.is_video:
                    video_url = post.video_url
                    video_thumbnail_url = f"{post.url.rstrip('/')}/photo"
                    video_data = {
                        'url': video_url,
                        'is_video': True,
                        'thumbnail_url': video_thumbnail_url
                    }
                    post_data['media'].append(video_data)

                account_data.append(post_data)

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
    posts_per_account = 3
    pickle_directory = 'C:/Users/dg078/Desktop/instaloader'

    download_posts_data(instagram_data_path, posts_per_account, pickle_directory)
