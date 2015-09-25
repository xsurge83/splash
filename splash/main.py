import os
import random
import click

from . import desktop
from .unsplash_download import UnSplashImageDownloader


@click.command()
@click.option('--folder', default=os.getenv('HOME'), help='Download images path.')
def main(folder):
    if not os.path.exists(folder):
        click.echo('Creating image folder: %s.' % folder)
        os.makedirs(folder)

    click.echo('Downloading to folder %s.' % folder)
    un_splash_downloader = UnSplashImageDownloader(folder)
    downloaded_images = un_splash_downloader.start()
    for image_path in downloaded_images:
        click.echo(click.style('Saved image in path %s.' % image_path, fg='green'))

    # randomly select image
    random_image = downloaded_images[random.randrange(0, len(downloaded_images) - 1)]
    desktop.set_desktop_background(random_image)
    click.echo(click.style('Set background image to %s.' % random_image, fg='green'))

if __name__ == "__main__":
    main()
