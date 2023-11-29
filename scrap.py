import requests

def get_user_id(username, access_token):
    url = f'https://graph.instagram.com/v13.0/{username}?fields=id,username&access_token={access_token}'
    response = requests.get(url)
    user_data = response.json()
    user_id = user_data.get('id')
    return user_id

def get_user_posts(user_id, access_token, limit=2):
    url = f'https://graph.instagram.com/me?fields=id,username&access_token=IGQWRNaks4M2ZA3REwwRnRqQVo0VXhCWjNXeWZAHT3Q4Wl9UZAnpDaGhHeUZAHM2RjUkE0a1o1dkdmcVdPWGxsSEJmcElTbVBRMXlnQ0VxUlVJOGdMa283eXl6SFNweU5qY2VscnViZAjRRRHZApejBxX3NrNUUxTWZAmdkR2bm1VVDBkaTdxQQZDZD&limit={limit}'
    response = requests.get(url)
    posts_data = response.json().get('data', [])
    return posts_data

# Пример использования
username = 'tamiriszhangazinova'
access_token = 'IGQWRNaks4M2ZA3REwwRnRqQVo0VXhCWjNXeWZAHT3Q4Wl9UZAnpDaGhHeUZAHM2RjUkE0a1o1dkdmcVdPWGxsSEJmcElTbVBRMXlnQ0VxUlVJOGdMa283eXl6SFNweU5qY2VscnViZAjRRRHZApejBxX3NrNUUxTWZAmdkR2bm1VVDBkaTdxQQZDZD'

user_id = get_user_id(username, access_token)
if user_id:
    user_posts = get_user_posts(user_id, access_token, limit=2)
    for post in user_posts:
        print(f"Post ID: {post.get('id')}")
        print(f"Caption: {post.get('caption', '')}")
        print(f"Media Type: {post.get('media_type', '')}")
        print(f"Media URL: {post.get('media_url', '')}")
        print("\n")


https://graph.instagram.com/me?fields=id,username&access_token=IGQWRNaks4M2ZA3REwwRnRqQVo0VXhCWjNXeWZAHT3Q4Wl9UZAnpDaGhHeUZAHM2RjUkE0a1o1dkdmcVdPWGxsSEJmcElTbVBRMXlnQ0VxUlVJOGdMa283eXl6SFNweU5qY2VscnViZAjRRRHZApejBxX3NrNUUxTWZAmdkR2bm1VVDBkaTdxQQZDZD