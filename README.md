# RAX Python Class

## Tooling
### Getting your environment set up
``` wget https://glyph.im/pip/bootstrap.sh ```

``` cd ~/Downloads ```

``` . bootstrap.sh ```

### Projects
``` pip install --editable . # make all local packages available for dev ```

``` pip wheel . # packages wheel to ~/.wheelhouses/ ```

``` python setup.py bdist_wheel # for when you have all dependencies installed in your env ```


### Virtualenv stuff
``` mktmpenv # disposable virtualenv```

#### Versioning a Python virtualenv
``` mkvirtualenv 26RaxPython -p `which python2.6` ```

## Python 3.x
``` from __future__ import print_function # deprecates old style print```