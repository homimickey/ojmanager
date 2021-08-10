import requests
from bs4 import BeautifulSoup


def get_codechef_score(handle):

    URL = f"https://www.codechef.com/users/{handle}"
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, 'html.parser')
    tag = soup.find_all('div', 'rating-number')
    return int(tag[0].get_text())



def get_code_forces_score(handle):

    URL = f"https://codeforces.com/profile/{handle}"
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, 'html.parser')
    tag = soup.find('div', '_UserActivityFrame_counterValue')
    return int(tag.get_text().split(" ")[0])



def get_hacker_earth_score(handle):

    pass