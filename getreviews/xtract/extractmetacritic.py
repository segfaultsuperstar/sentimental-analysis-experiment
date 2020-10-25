from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def extract_sims():
    good = 0
    bad = 0
    total_extracted = 0
    pagenum = 0
    print("Starting extraction of the sims 3...")
    while True:
        if total_extracted == 90:
            break
        url = "https://www.metacritic.com/game/pc/the-sims-3/user-reviews?sort-by=score&num_items=100&page="+str(pagenum)
        pagenum += 1
        head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        page = requests.get(url, headers=head)
        soup = BeautifulSoup(page.text, 'html.parser')
        for comments in soup.select('li.review.user_review'):
            score = comments.find('div', {'class': 'review_grade'})
            score = str(score.div.string)
            if int(score) > 5 and good < 45:
                good += 1
                file = open("~/researchproj/dataset/sims3/metacritic/yes"+str(good)+".txt", "w")
            elif int(score) <= 5 and total_extracted < 90:
                bad += 1
                file = open("~/researchproj/dataset/sims3/metacritic/no"+str(bad)+".txt", "w")
            elif total_extracted < 90:
                continue
            else:
                break
            review = comments.find('span', {'class': 'blurb blurb_expanded'})
            if review:
                review = str(review.text)
                file.write(review)
                file.close()
                total_extracted += 1
                print(total_extracted)
                continue
            review = comments.find('div', {'class': 'review_body'})
            review = str(review.text)
            file.write(review)
            file.close()
            total_extracted += 1
            print(total_extracted)


def extract_masseffect():
    good = 0
    bad = 0
    total_extracted = 0
    pagenum = 0
    print("Starting extraction of mass effect 2...")
    while True:
        if total_extracted == 90:
            break
        url = "https://www.metacritic.com/game/pc/mass-effect-2/user-reviews?sort-by=score&num_items=100&page="+str(pagenum)
        pagenum += 1
        head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        page = requests.get(url, headers=head)
        soup = BeautifulSoup(page.text, 'html.parser')
        for comments in soup.select('li.review.user_review'):
            score = comments.find('div', {'class': 'review_grade'})
            score = str(score.div.string)
            if int(score) > 5 and good < 45:
                good += 1
                file = open("~/researchproj/dataset/me2/metacritic/yes"+str(good)+".txt", "w")
            elif int(score) <= 5 and total_extracted < 90:
                bad += 1
                file = open("~/researchproj/dataset/me2/metacritic/no"+str(bad)+".txt", "w")
            elif total_extracted < 90:
                continue
            else:
                break
            review = comments.find('span', {'class': 'blurb blurb_expanded'})
            if review:
                review = str(review.text)
                file.write(review)
                file.close()
                total_extracted += 1
                print(total_extracted)
                continue
            review = comments.find('div', {'class': 'review_body'})
            review = str(review.text)
            file.write(review)
            file.close()
            total_extracted += 1
            print(total_extracted)


def extract_gtaiv():
    good = 0
    bad = 0
    total_extracted = 0
    pagenum = 0
    print("Starting extraction of gta 4...")
    while True:
        if total_extracted == 90:
            break
        url = "https://www.metacritic.com/game/pc/grand-theft-auto-iv/user-reviews?sort-by=score&num_items=100&page="+str(pagenum)
        pagenum += 1
        head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        page = requests.get(url, headers=head)
        soup = BeautifulSoup(page.text, 'html.parser')
        for comments in soup.select('li.review.user_review'):
            score = comments.find('div', {'class': 'review_grade'})
            score = str(score.div.string)
            if int(score) > 5 and good < 45:
                good += 1
                file = open("~/researchproj/dataset/gta4/metacritic/yes"+str(good)+".txt", "w")
            elif int(score) <= 5 and total_extracted < 90:
                bad += 1
                file = open("~/researchproj/dataset/gta4/metacritic/no"+str(bad)+".txt", "w")
            elif total_extracted < 90:
                continue
            else:
                break
            review = comments.find('span', {'class': 'blurb blurb_expanded'})
            if review:
                review = str(review.text)
                file.write(review)
                file.close()
                total_extracted += 1
                print(total_extracted)
                continue
            review = comments.find('div', {'class': 'review_body'})
            review = str(review.text)
            file.write(review)
            file.close()
            total_extracted += 1
            print(total_extracted)

extract_sims()
extract_gtaiv()
extract_masseffect()