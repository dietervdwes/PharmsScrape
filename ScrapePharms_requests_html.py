#Good news: there is now a requests module that supports javascript: https://pypi.org/project/requests-html/

from requests_html import HTMLSession
from bs4 import BeautifulSoup
from lxml import html

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'Origin': 'http://10.184.55.233:8080',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://10.184.55.233:8080',
    'Accept': 'text/html, */*; q=0.01',
}

payload = {
  'IWEDITUSERNAME': 'WARD^',
  'IWEDITPASSWORD': 'WARD^',
  }



session = HTMLSession()

r = session.get('http://10.184.55.233:8080')

r.html.render()  # this call executes the js in the page
#As a bonus this wraps BeautifulSoup, I think, so you can do things like

r.find('#myElementID').text
#which returns the content of the HTML element as you'd expect.