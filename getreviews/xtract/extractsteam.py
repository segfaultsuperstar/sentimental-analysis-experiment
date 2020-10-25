import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def extract_sims():
    print("Starting extraction of The Sims 3 Steam reviews")
    good = 0
    bad = 0
    driver = webdriver.Chrome("/home/amazingjames/PycharmProjects/getreviews/venv/chromedriver")
    driver.get('https://steamcommunity.com/app/47890/negativereviews/?p=1&browsefilter=toprated')
    for scroll in range(0, 500):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        scroll += 1
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    for reviews in soup.select('div.apphub_UserReviewCardContent'):
        if bad < 45:
            bad += 1
            file = open("~/researchproj/dataset/sims3/steam/no" + str(bad) + ".txt", "w")
        else:
            break
        feedback = reviews.find("div", {"class": "apphub_CardTextContent"}).text
        file.write(feedback)
        file.close()
    driver.get('https://steamcommunity.com/app/47890/positivereviews/?p=1&browsefilter=toprated')
    for scroll in range(0, 500):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        scroll += 1
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    for reviews in soup.select('div.apphub_UserReviewCardContent'):
        if good < 45:
            good += 1
            file = open("~/researchproj/dataset/sims3/steam/yes" + str(good) + ".txt", "w")
        else:
            break
        feedback = reviews.find("div", {"class": "apphub_CardTextContent"}).text
        file.write(feedback)
        file.close()
    driver.quit()


def extract_gtaiv():
    print("Starting extraction of GTA4 Steam reviews")
    good = 0
    bad = 0
    driver = webdriver.Chrome("/home/amazingjames/PycharmProjects/getreviews/venv/chromedriver")
    driver.get('https://steamcommunity.com/app/12210/negativereviews/?p=1&browsefilter=toprated')
    for scroll in range(0, 500):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        scroll += 1
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    for reviews in soup.select('div.apphub_UserReviewCardContent'):
        if bad < 45:
            bad += 1
            file = open("~/researchproj/dataset/gta4/steam/no" + str(bad) + ".txt", "w")
        else:
            break
        feedback = reviews.find("div", {"class": "apphub_CardTextContent"}).text
        file.write(feedback)
        file.close()
    driver.get('https://steamcommunity.com/app/12210/positivereviews/?p=1&browsefilter=toprated')
    for scroll in range(0, 500):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        scroll += 1
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    for reviews in soup.select('div.apphub_UserReviewCardContent'):
        if good < 45:
            good += 1
            file = open("~/researchproj/dataset/gta4/steam/yes" + str(good) + ".txt", "w")
        else:
            break
        feedback = reviews.find("div", {"class": "apphub_CardTextContent"}).text
        file.write(feedback)
        file.close()
    driver.quit()


def extract_masseffect():
    print("Starting extraction of Mass Effect 2 Steam reviews")
    good = 0
    bad = 0
    driver = webdriver.Chrome("/home/amazingjames/PycharmProjects/getreviews/venv/chromedriver")
    driver.get('https://steamcommunity.com/app/24980/negativereviews/?p=1&browsefilter=toprated')
    for scroll in range(0, 500):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        scroll += 1
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    for reviews in soup.select('div.apphub_UserReviewCardContent'):
        if bad < 45:
            bad += 1
            file = open("~/researchproj/dataset/me2/steam/no" + str(bad) + ".txt", "w")
        else:
            break
        feedback = reviews.find("div", {"class": "apphub_CardTextContent"}).text
        file.write(feedback)
        file.close()
    driver.get('https://steamcommunity.com/app/24980/positivereviews/?p=1&browsefilter=toprated')
    for scroll in range(0, 500):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        scroll += 1
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    for reviews in soup.select('div.apphub_UserReviewCardContent'):
        if good < 45:
            good += 1
            file = open("~/researchproj/dataset/me2/steam/yes" + str(good) + ".txt", "w")
        else:
            break
        feedback = reviews.find("div", {"class": "apphub_CardTextContent"}).text
        file.write(feedback)
        file.close()
    driver.quit()


extract_sims()
extract_gtaiv()
extract_masseffect()
