import datetime
from urllib import request
from bs4 import BeautifulSoup


def scraping_contribution():
    username = "YuyaNakamura0139"
    today = datetime.date.today()

    url = "https://github.com/users/" + username + "/contributions"
    response = request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    response.close()
    contributions = soup.find_all("rect", class_="ContributionCalendar-day")

    for _, date in enumerate(contributions[::-1]):
        try:
            if date.get("data-date") == str(today):
                return int(date.get("data-count"))
        except Exception as err:
            print(err)
    return 0
