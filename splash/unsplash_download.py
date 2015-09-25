#!/usr/bin/env python
import re
import requests
from bs4 import BeautifulSoup


## TODO setup cron job or http://alvinalexander.com/mac-os-x/mac-osx-startup-crontab-launchd-jobs
class UnSplashImageDownloader:
    PHOTO_REG_EXPR = re.compile(r".*/(.*)\?.*fm=(.{3})&.*")
    UN_SPLASH_URL = 'https://unsplash.com/'

    def __init__(self, download_to):
        self.download_to = download_to
        self.downloaded_images = []

    def start(self):
        url_links = self._get_image_links(self.UN_SPLASH_URL)
        return self.download_images(url_links)

    @staticmethod
    def _get_image_links(url):
        rv = requests.get(url)
        content = rv.text

        soup = BeautifulSoup(content, 'html.parser')
        result = soup.find_all('div', class_='photo')

        urls = []
        for link in result:
            urls.append(link.find('img').get('src'))
        return urls

    def download_images(self, image_urls):
        downloaded_paths = []
        for url in image_urls:
            matches = UnSplashImageDownloader.PHOTO_REG_EXPR.match(url)
            print 'downloading image {url}...'.format(url=url)
            if matches:
                full_path = '{picture_folder}/{file_name}.{ext}' \
                    .format(picture_folder=self.download_to, file_name=matches.group(1), ext=matches.group(2))
                downloaded_paths.append(full_path)
                with open(full_path, 'wb') as handle:
                    response = requests.get(url, stream=True)
                    for block in response.iter_content(1024):
                        handle.write(block)
        return downloaded_paths


