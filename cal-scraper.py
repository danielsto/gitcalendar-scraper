import bs4
import requests
import json
import sys


def calendar_to_json(git_calendar):
    with open('contributions.json', 'w') as outfile:
        json.dump(git_calendar, outfile)


def retrieve_data(user_name):
    url = 'https://github.com/' + user_name
    req = requests.get(url)
    status_code = req.status_code
    parsed_calendar = {}

    if status_code == 200:
        html = bs4.BeautifulSoup(req.text, "html.parser")
        calendar = html.find_all('rect', {'class': 'day'})

        for day in calendar:
            date = day.attrs['data-date']
            contributions = day.attrs['data-count']
            parsed_calendar[date] = contributions
    else:
        print('\033[31m' + 'ERROR: user does not exist')
        exit()
    return parsed_calendar


if __name__ == "__main__":
    user_name = sys.argv[1]
    print('..... Retrieving data from user named: ' + user_name)
    calendar = retrieve_data(user_name)
    print('..... Dumping data into JSON format in the file: contributions.json')
    calendar_to_json(calendar)
