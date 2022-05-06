"""
Ce fichier permet de créer des exécutables pour tous les sytèmes.
Sont actuellement supportés :
- Windows (via un exécutable .exe)
- MacOSX (via un exécutable .app)
- Linux (via l'exécution simple d'un fichier python, avec la commande utilitaire "python"

"""


import sys
from setuptools import setup

mainscript = 'MyApplication.py'

if sys.platform == 'darwin':
    extra_options = dict(
        setup_requires=['py2app'],
        app=[mainscript],
        # Cross-platform applications generally expect sys.argv to
        # be used for opening files.
        # Don't use this with GUI toolkits, the argv
        # emulator causes problems and toolkits generally have
        # hooks for responding to file-open events.
        options=dict(py2app=dict(argv_emulation=True)),
     )
elif sys.platform == 'win32':
    extra_options = dict(
        setup_requires=['py2exe'],
        app=[mainscript],
    )
else:
    extra_options = dict(
        # Normally unix-like platforms will use "setup.py install"
        # and install the main script as such
        scripts=[mainscript],
    )

setup(
    name="MyApplication",
    **extra_options
)
