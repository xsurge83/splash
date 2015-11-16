import os
import json
import random
import click

from splash.unsplash_download import UnSplashImageDownloader
from splash import desktop
from splash.config import DATA_STORE_FILE


@click.command('download')
@click.option('--folder', default=os.getenv('HOME'), help='Download images path.')
def cli(folder):
    if not os.path.exists(folder):
        click.echo('Creating image folder: %s.' % folder)
        os.makedirs(folder)

    data = {
        'downloaded_images': []
    }

    click.echo('Downloading to folder %s.' % folder)
    un_splash_downloader = UnSplashImageDownloader(folder)
    downloaded_images = un_splash_downloader.start()
    for image_path in downloaded_images:
        click.echo(click.style('Saved image in path %s.' % image_path, fg='green'))
        data['downloaded_images'].append(image_path)

    # randomly select image
    random_image = downloaded_images[random.randrange(0, len(downloaded_images) - 1)]
    desktop.set_desktop_background(random_image)
    click.echo(click.style('Set background image to %s.' % random_image, fg='green'))

    with open(DATA_STORE_FILE, 'w') as outfile:
        json.dump(data, outfile)

