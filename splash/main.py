import os
import random
import click
import json

from . import desktop
from .unsplash_download import UnSplashImageDownloader

DATA_STORE_FILE = 'store.json'


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """ Menu."""
    state = STATES.MAIN
    while 1:
        if state == STATES.MAIN:
            click.echo('Main menu:')
            click.echo('  s: select image')
            click.echo('  v: preview image')
            click.echo('  q: quit')
            char = click.getchar()
            if char == 's':
                state = STATES.SELECT
            elif char == 'v':
                state = STATES.VIEW
            elif char == 'q':
                state = STATES.QUIT
            else:
                click.echo('Invalid input')
        elif state == STATES.SELECT:
            click.echo('Select menu:')
            selected_image = select_image_prompt('b')
            if selected_image:
                desktop.set_desktop_background(selected_image)
            state = STATES.MAIN
        elif state == STATES.VIEW:
            click.echo('View menu:')
            launch_selected_image()
            state = STATES.MAIN
        elif state == 'quit':
            return


@cli.command()
@click.option('--folder', default=os.getenv('HOME'), help='Download images path.')
def download(folder):
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



class STATES:
    MAIN = 'main'
    SELECT = 'select'
    VIEW = 'view'
    QUIT = 'quit'


def launch_selected_image():
    selected_image_path = select_image_prompt()
    if selected_image_path:
        path = 'file://%s' % selected_image_path
        click.echo(path)
        click.launch(path)


def select_image_prompt(abort_char='q'):
    result = False
    with open(DATA_STORE_FILE) as infile:
        json_data = json.load(infile)
        click.echo(click.style('Available selections:', fg='blue'))
        download_images = json_data['downloaded_images']
        for index, image_path in enumerate(download_images):
            click.echo(click.style('%s: Image path %s.' % (index, image_path), fg='green'))
        selection = click.prompt('Please select from above:', default='q', type=int, show_default=False)
        click.echo('You selection : ' + str(selection))

        if selection == abort_char:
            click.echo('Abort!')
        else:
            index = int(selection)
            if 0 <= index <= len(download_images) - 1:
                image_path = download_images[index]
                click.echo(click.style('Selected index %s: image %s.' % (index, image_path), fg='green'))
                result = image_path
            else:
                click.echo('Image selection out of range')
    return result
