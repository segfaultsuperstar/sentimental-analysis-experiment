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
        pagenum += 1
        url = 'https://www.gamespot.com/the-sims-3/reviews/?sortBy=lowestScore&page='+str(pagenum)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        for comments in soup.select("li.media.media-game.userReview-list__item"):
            score = comments.find('strong').text
            if total_extracted == 90:
                break
            if float(score) < 5.5 and bad < 45:
                bad += 1
                file = open("~/researchproj/dataset/sims3/gamespot/no"+str(bad)+".txt", "w")
            elif float(score) >= 5.5 and total_extracted < 90:
                good += 1
                file = open("~/researchproj/dataset/sims3/gamespot/yes"+str(good)+".txt", "w")
            else:
                continue
            rev_part = comments.select('p')
            for moreof in rev_part:
                extended = moreof.select('a')
                for full in extended:
                    lnk = full.get('href')
                    if lnk:
                        full_version = urljoin(url, lnk)
                        more_soup = BeautifulSoup(requests.get(full_version).text, "html.parser")
                        for contents in more_soup.select("section.userReview-body.typography-format"):
                            review = contents.text
                            total_extracted += 1
                            file.write(review)
                            file.close()
                            print(total_extracted)


def extract_masseffect():
    good = 0
    bad = 0
    total_extracted = 0
    pagenum = 0
    print("Starting extraction of mass effect 2... ")
    while True:
        pagenum += 1
        if total_extracted == 90:
            break
        url = "https://www.gamespot.com/mass-effect-2/reviews/?sortBy=lowestScore&page="+str(pagenum)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        for comments in soup.select("li.media.media-game.userReview-list__item"):
            score = comments.find('strong').text
            if total_extracted == 90:
                break
            if float(score) < 5.5 and bad < 45:
                bad += 1
                file = open("~/researchproj/dataset/me2/gamespot/no"+str(bad)+".txt", "w")
            elif float(score) >= 5.5 and total_extracted < 90:
                good += 1
                file = open("~/researchproj/dataset/me2/gamespot/yes"+str(good)+".txt", "w")
            else:
                continue
            rev_part = comments.select('p')
            for moreof in rev_part:
                extended = moreof.select('a')
                for full in extended:
                    lnk = full.get('href')
                    if lnk:
                        full_version = urljoin(url, lnk)
                        more_soup = BeautifulSoup(requests.get(full_version).text, "html.parser")
                        for contents in more_soup.select("section.userReview-body.typography-format"):
                            review = contents.text
                            total_extracted += 1
                            file.write(review)
                            file.close()
                            print(total_extracted)


def extract_gtaiv():
    good = 0
    bad = 0
    total_extracted = 0
    pagenum = 0
    print("Starting extraction of gta 4...")
    while True:
        pagenum += 1
        if total_extracted == 90:
            break
        url = "https://www.gamespot.com/grand-theft-auto-iv/reviews/?sortBy=lowestScore&page="+str(pagenum)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        for comments in soup.select("li.media.media-game.userReview-list__item"):
            score = comments.find('strong').text
            if total_extracted == 90:
                break
            if float(score) < 5.5 and bad < 45:
                bad += 1
                file = open("~/researchproj/dataset/gta4/gamespot/no"+str(bad)+".txt", "w")
            elif float(score) >= 5.5 and total_extracted < 90:
                good += 1
                file = open("~/researchproj/dataset/gta4/gamespot/yes"+str(good)+".txt", "w")
            else:
                continue
            rev_part = comments.select('p')
            for moreof in rev_part:
                extended = moreof.select('a')
                for full in extended:
                    lnk = full.get('href')
                    if lnk:
                        full_version = urljoin(url, lnk)
                        more_soup = BeautifulSoup(requests.get(full_version).text, "html.parser")
                        for contents in more_soup.select("section.userReview-body.typography-format"):
                            review = contents.text
                            total_extracted += 1
                            file.write(review)
                            file.close()
                            print(total_extracted)


extract_sims()
extract_masseffect()
extract_gtaiv()
