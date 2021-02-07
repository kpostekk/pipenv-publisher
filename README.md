# Pipenv publisher
Pipenv integration for setuptools.

## Install

### From pypi
```shell
pip install pipenv-publisher
```

### From git
```shell
pip install https://github.com/kpostekk/pipenv-publisher.git
```

### Initialise in your project
```shell
pipenv-pub setup
```
After this, remember to update package meta in Pipfile!

## Usage

### Sync version
```shell
pipenv run stamp <package> # or pipenv-pub stamp 
```

Remember to add this into your `__init__.py`
```python
from mypkg._version import __version__, __author__
```

Tip: in PyCharm you can enable file watcher to automate this task.

### Lock before build
```shell
pipenv run slock # or pipenv-pub lock 
```

## FAQ

- Where I should define all setuptools's stuff?
    - In `setup` section of pipfile
- How about my `README.md` or `README.rst`, where I should declare it?
    - Nowhere! It's magiaclly detected and added to setuptools.
- What is `setup-lock.json`
    - This a file with, peresistent lock of section `setup` from Pipfile. It has all configuration for `setup.py`, including `install_requires`. It **shouldn't** be in `.gitignore`
- Can I still use `setup.cfg`
    - Yes.
- Why does it exist?
    - Because I can and there isn't any good tool for integrate `setuptools` and `Pipenv`.