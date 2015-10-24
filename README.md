
# splash 
* cli from downloading image from unsplash and set them to background 
 desktop.
  
### Supports 
  - OSX

### Installation

Splash may be installed directly from the GitHub repository via:
```
pip install git+git://github.com/xsurge83/splash.git
```

When developing splash, ``pip`` can be used to create a "development" install
which uses symlink magic to allow changes in files to be reflected without
re-installing:

```
git clone git://github.com/xsurge83/splash.git
cd splash
pip install -e .
```

### Example usage

These examples assume that splash has been installed as per the instructions
below. Before installation, invoke via `python -m splash`.

```
splash download  --folder  # Download images from splash to specified folder 
splash menu                # View and execute menu 
```
