from ezcliy import Command, Positional, Flag

from .meta import create_meta_json
from .sample import copy_sample_setup, add_sctipts, copy_version
from .setup_json import generate_setup_json


class PipenvAmigo(Command):
    class Setup(Command):
        name = 'setup'
        description = 'Creates setup.py'
        allow_empty_calls = True

        def invoke(self):
            copy_sample_setup()
            generate_setup_json()
            add_sctipts()

    class VersionStamp(Command):
        name = 'stamp'
        description = 'Recreates meta.json and updates _version.py'
        pkg_name = Positional('package', ask_if_missing='name of package')
        pkg_name.description = 'Directory of package.'
        no_copy = Flag('--no-copy')
        no_copy.description = 'Passing this flag results in skipping copying of _version file.'

        def invoke(self):
            if not self.no_copy:
                copy_version(str(self.pkg_name))
                print('Remember to add import in __init__')
            create_meta_json(str(self.pkg_name))

    class Lock(Command):
        def invoke(self):
            generate_setup_json()
