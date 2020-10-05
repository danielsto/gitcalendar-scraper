# gitcalendar-scraper

Retrieve your GitHub contributions in a usable format such as JSON or Python lists and dictionaries. A great way to format your contributions for data visualizations libraries such as [Chartjs](http://www.chartjs.org).

## Getting Started
If you have all of the prerequisites installed you can simply use this script as:
```bash
python3 gitcalendar-scraper.py <username>
```
And it will retrieve and store them in a file called `contributions.json`

### Prerequisites
- A GitHub valid username
- Python 3+
- BeautifulSoup4 and requests module 

### Installing packages
Prerequisites can be installed using the PIP:
```bash
$ pip3 install -r requirements.txt
```
It will install all of the requirements contained in `requirements.txt`.

## License
This project is licensed under the GNU GPL 3.0 License - see the [LICENSE](https://github.com/danielsto/gitcalendar-scraper/blob/master/LICENSE) for details
