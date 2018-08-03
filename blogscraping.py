import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://finance.oxinion.com/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='post-outer-container')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find(
            class_='post-title-container').get_text().replace('\n', '')
        date = post.select('.post-header')[0].get_text()
        csv_writer.writerow([title, date])
