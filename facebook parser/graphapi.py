import requests

# Замените access_token на ваш действительный токен доступа
access_token = '32d5ac6101169855e29ad33d45d09fa8'
group_id = '3253703491385664'  # Идентификатор группы

# Формирование заголовка авторизации
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Получение постов из группы с использованием Graph API
url = f'https://graph.facebook.com/v12.0/{group_id}/feed'
params = {
    'fields': 'attachments,message',
    'limit': 5  # Получение последних 5 постов
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

# Печать URL фотографий из постов
for post in data.get('data', []):
    message = post.get('message', '')
    print(f'Message: {message}')

    attachments = post.get('attachments', {}).get('data', [])
    
    for attachment in attachments:
        media_type = attachment.get('type', '')

        if media_type == 'photo':
            image_url = attachment.get('media', {}).get('image', {}).get('src', '')
            print(f'Image URL: {image_url}')
            print('---')
