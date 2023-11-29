import requests

url = "https://api.instagram.com/oauth/access_token"

# Замените placeholder'ы вашими реальными значениями
data = {
    'client_id': '696056549163724',
    'client_secret': 'f6728e4731248741b643ad72f7d53838',
    'grant_type': 'authorization_code',
    'redirect_uri': 'https://www.google.com/',
    'code': 'AQDxZUiuvC9l18-1Fh01QmBGkGu4Xohh4Oo1qBMXG6ppT95WuauOeQ4HDhvOngPLtYYxRPhBp1R0Y0eqdj4J-bYl3Nfem6pxrp-I1DiDZsK-1gACr-jwRMct1lnilyRA7x93PKj8to1qRMFbomcYH9b-gr0BPz4pIAOTkGmQWV4-9Q2jBprE3pzpSpxHaYXuHkiQfUEzKk741nH3TuFa8yTaNFkmoZEBb2mqBYLkhcSIgw'
}

response = requests.post(url, data=data)

# Печать ответа сервера
print(response.json())


f6728e4731248741b643ad72f7d53838

AQDxZUiuvC9l18-1Fh01QmBGkGu4Xohh4Oo1qBMXG6ppT95WuauOeQ4HDhvOngPLtYYxRPhBp1R0Y0eqdj4J-bYl3Nfem6pxrp-I1DiDZsK-1gACr-jwRMct1lnilyRA7x93PKj8to1qRMFbomcYH9b-gr0BPz4pIAOTkGmQWV4-9Q2jBprE3pzpSpxHaYXuHkiQfUEzKk741nH3TuFa8yTaNFkmoZEBb2mqBYLkhcSIgw


curl -X POST \
    https://api.instagram.com/oauth/access_token \
    -r client_id=696056549163724 \
    -r client_secret=f6728e4731248741b643ad72f7d53838 \
    -r grant_type=authorization_code \
    -r redirect_uri=https://www.google.com \
    -r code=AQAobO2njftc1Hj5d57c5RjvKyQEvD-rLuDP723j9KDD84kLyhxuPOCu8TecsBXpuN_nImmaofdCBbDfItVqVgEHGsk6UpGZTGDWs5OpPtjAnQmWtONRpWW-6pVERauCsgm0QzQI3Cn7jTq9KogOGxetSfWB4Af8swbw0-eNKoOfqKwjp1AnG6H-J3IPhzNmxKtdFhumyDk6l4_lRXoc8YclCr7spCCK0kr1j_lB-yhjwA



{'access_token': 'IGQWRNaks4M2ZA3REwwRnRqQVo0VXhCWjNXeWZAHT3Q4Wl9UZAnpDaGhHeUZAHM2RjUkE0a1o1dkdmcVdPWGxsSEJmcElTbVBRMXlnQ0VxUlVJOGdMa283eXl6SFNweU5qY2VscnViZAjRRRHZApejBxX3NrNUUxTWZAmdkR2bm1VVDBkaTdxQQZDZD', 'user_id': 6502394376532729}

