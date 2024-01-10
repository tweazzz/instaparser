import warnings
from facebook_scraper import get_posts

group_id = '3253703491385664'  # Это числовой идентификатор группы

warnings.filterwarnings("ignore", category=UserWarning, module="facebook_scraper")

for post in get_posts(group_id, pages=5, options={'lang': 'en_US'}):
    print(post['text'])
    print('---')
