import requests

# Замените YOUR_APP_ID, YOUR_APP_SECRET и YOUR_TEMPORARY_CODE на соответствующие значения
app_id = 'YOUR_APP_ID'
app_secret = 'YOUR_APP_SECRET'
temp_code = 'YOUR_TEMPORARY_CODE'
redirect_uri = 'https://google.com/'  # Замените на свой redirect_uri

url = f'https://graph.facebook.com/v18.0/oauth/access_token'
params = {
    'client_id': app_id,
    'client_secret': app_secret,
    'code': temp_code,
    'redirect_uri': redirect_uri,
}

response = requests.get(url, params=params)
data = response.json()

access_token = data.get('access_token')
print(f'Access Token: {access_token}')
