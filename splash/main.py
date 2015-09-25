import os
import sys
import random
from . import desktop
from .unsplash_download import UnSplashImageDownloader


def main():
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)

    picture_folder = sys.argv[1] if len(sys.argv) > 1 else os.getenv('HOME')
    if not os.path.exists(picture_folder):
        os.makedirs(picture_folder)
    print picture_folder

    un_splash_downloader = UnSplashImageDownloader(picture_folder)
    downloaded_paths = un_splash_downloader.start()

    # randomly select image
    desktop.set_desktop_background(downloaded_paths[random.randrange(0, len(downloaded_paths) - 1)])


if __name__ == "__main__":
    main()
