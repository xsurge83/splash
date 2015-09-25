import subprocess

UPDATE_BACKGROUND_SCRIPT = "sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db " \
                           "\"update data set value = '%s'\";killall Dock;"


def set_desktop_background(filename):
    print filename
    output = UPDATE_BACKGROUND_SCRIPT % filename
    subprocess.Popen(output, shell=True)


__all__ = ['set_desktop_background']
