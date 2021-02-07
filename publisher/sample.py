from pathlib import Path
import shutil

from pipenv.project import Project


def copy_sample_setup():
    print('Copy setup.py')
    shutil.copyfile(Path(__file__).parent.joinpath('_sample/_sample_setup.py'), Path.cwd().joinpath('setup.py'))


def copy_version(package_name: str):
    print('Copy _version.py')
    shutil.copyfile(Path(__file__).parent.joinpath('_sample/_sample_version.py'), Path.cwd().joinpath(package_name, '_version.py'))


def add_sctipts():
    project = Project(which='Pipfile')
    print('Adding wheel package to dev packages...')
    project.add_package_to_pipfile('wheel', dev=True)
    print('Adding scripts to Pipfile...')
    p = project.parsed_pipfile
    # noinspection PyTypeChecker
    p['scripts'] = p.get('scripts', {}) | {
        'build': 'python setup.py bdsit_wheel sdist',
        'slock': 'pipenv-pub lock',
        'stamp': 'pipenv-pub stamp'
    }
    project.write_toml(p)
    print('Remember to lock Pipfile!')
