#!/usr/bin/env python
import sys
import re
import os
import subprocess
import requests
import random
from bs4 import BeautifulSoup

## TODO setup cron job or http://alvinalexander.com/mac-os-x/mac-osx-startup-crontab-launchd-jobs

PHOTO_REG_EXPR = re.compile(r".*/(.*)\?.*fm=(.{3})&.*")


def get_image_links(url):
    rv = requests.get(url)
    content = rv.text

    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find_all('div', class_='photo')

    urls = []
    for link in result:
        urls.append(link.find('img').get('src'))
    return urls


def download_images(image_urls, picture_folder):
    downloaded_paths =[]
    for url in image_urls:
        matches = PHOTO_REG_EXPR.match(url)
        print 'downloading image {url}...'.format(url=url)
        if matches:
            full_path = '{picture_folder}/{file_name}.{ext}'\
                .format(picture_folder=picture_folder, file_name=matches.group(1), ext=matches.group(2))
            downloaded_paths.append(full_path)
            with open(full_path, 'wb') as handle:
                response = requests.get(url, stream=True)
                for block in response.iter_content(1024):
                    handle.write(block)
    return downloaded_paths

UPDATE_BACKGROUND_SCRIPT = "sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db \"update data set value = '%s'\";killall Dock;"


def set_desktop_background(filename):
    print filename
    output = UPDATE_BACKGROUND_SCRIPT % filename
    subprocess.Popen(output, shell=True)


def main():
    image_links = get_image_links('https://unsplash.com/')
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    picture_folder = sys.argv[1] if len(sys.argv) > 1 else os.getenv('HOME')
    if not os.path.exists(picture_folder):
        os.makedirs(picture_folder)
    print picture_folder
    downloaded_paths = download_images(image_links, picture_folder)

    set_desktop_background(downloaded_paths[random.randrange(0, len(downloaded_paths)-1)])

if __name__ == "__main__":
    main()
