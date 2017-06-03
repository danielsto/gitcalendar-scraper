import bs4
import requests
import time
import datetime
import json


def calendar_to_json(git_calendar):
    with open('contributions.json', 'w') as outfile:
        json.dump(git_calendar, outfile)


def retrieve_data(user_name):
    url = 'https://github.com/' + user_name
    req = requests.get(url)
    status_code = req.status_code
    git_calendar = {}

    if status_code == 200:
        html = bs4.BeautifulSoup(req.text, "html.parser")
        calendar = html.find_all('rect', {'class': 'day'})

        for i, day in enumerate(calendar):
            date = day.attrs['data-date']
            timestamp = time.mktime(
                datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())
            contributions = day.attrs['data-count']
            git_calendar[timestamp] = contributions

    return git_calendar


def main():
    if __name__ == "__main__":
        calendar = retrieve_data('danielsto')
        calendar_to_json(calendar)


main()
