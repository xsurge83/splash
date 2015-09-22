__author__ = 'sergeyshteyn'

from os.path import join, abspath, dirname

here = lambda *dirs: join(abspath((dirname(__file__))), *dirs)
BASE_DIR  = here("..", "..")
print BASE_DIR