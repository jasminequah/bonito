import os
import re
from subprocess import check_call
from setuptools import setup, find_packages
from setuptools.command.install import install


__pkg_name__ = 'bonito'

verstrline = open(os.path.join(__pkg_name__, '__init__.py'), 'r').read()
vsre = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(vsre, verstrline, re.M)
if mo:
    __version__ = mo.group(1)
else:
    raise RuntimeError('Unable to find version string in "{}/__init__.py".'.format(__pkg_name__))

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

# class download_latest_model(install):
#    def run(self):
#        install.run(self)
#        check_call("bonito download --models --latest -f".split())

setup(
    name="ont-%s" % __pkg_name__,
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Oxford Nanopore Technologies, Ltd',
    author_email='support@nanoporetech.com',
    url='https://github.com/nanoporetech/bonito',
#    cmdclass={
#        'install': download_latest_model,
#    },
    entry_points = {
        'console_scripts': [
            '{0} = {0}:main'.format(__pkg_name__)
        ]
    },
)
