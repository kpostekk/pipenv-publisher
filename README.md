# <img alt="Pipenv publisher" src="https://raw.githubusercontent.com/kpostekk/pipenv-publisher/main/.github/untitled.png">
Pipenv integration for setuptools.

## Install

### From pypi
```shell
pipenv install pipenv-publisher
```

### From git
```shell
pipenv install https://github.com/kpostekk/pipenv-publisher.git#egg=publisher
```

### Initialise in your project
```shell
pipenv-pub setup
```
After this, remember to update package meta in Pipfile!

## Usage

### Sync version
```shell
pipenv-pub stamp . # or pipenv run stamp 
```

> You can replace dot with package name

Remember to add this into your `__init__.py`
```python
from mypkg._version import __version__, __author__
```

Tip: in PyCharm you can enable file watcher to automate this task.

<img src="https://raw.githubusercontent.com/kpostekk/pipenv-publisher/main/.github/pycharm64_20210207_193318.png" height="320px">
<img src="https://raw.githubusercontent.com/kpostekk/pipenv-publisher/main/.github/pycharm64_20210207_193323.png" height="320px">

### Lock before build
```shell
pipenv-pub lock # or pipenv run slock 
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
    - Because I can and there isn't any good tool to integrate `setuptools` and `Pipenv`.
- Examples?
    - This repo is an example lmao.
