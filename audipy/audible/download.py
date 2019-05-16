import re
import requests
import browser_cookie3
from bs4 import BeautifulSoup


class Downloader:

    def __init__(self, browser: str = "all"):
        self.headers = self.set_headers()
        self.browser = browser
        self.available_browsers = dict(firefox=browser_cookie3.Firefox,
                                       chrome=browser_cookie3.Chrome,
                                       all=browser_cookie3)
        self.cookies = self.available_browsers[self.browser].load("audible.com")
        self.session = self.construct_session()
        self.lib_url = 'https://www.audible.com/lib?&pageSize=50'
        self.library = self.get_library_page()

    def construct_session(self):
        sess = requests.Session()
        sess.cookies = self.cookies
        return sess

    def get_library_page(self) -> bytes:
        r = self.session.get(self.lib_url, headers=self.headers)
        return r.content if r.status_code == 200 else b""

    @staticmethod
    def is_download_link(href):
        return href and re.compile("https://cds.audible.com/download").search(href)

    @staticmethod
    def set_headers():
        headers = dict()
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0'
        headers['Referer'] = 'https://www.audible.com/?serial='
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        headers['Accept-Language'] = 'en-US,en;q=0.5'
        headers['Accept-Encoding'] = 'gzip, deflate, br'
        return headers

    def get_download_links(self, library_html) -> list:
        soup = BeautifulSoup(library_html, 'html.parser')
        if soup.title.text == 'Download Audiobooks with Audible.com':
            return [link.get('href') for link in soup.find_all(href=self.is_download_link)]
        else:
            return []
