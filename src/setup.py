from setuptools import setup

setup(
    name = 'bangla',
    version = '1',
    description = 'This is a package consist of bengali words, stop words, stemmer module, etc.',
    packages = ['bangla'],
    package_data={'bangla': ['data/*.pkl', 'lib/*.py']},
    zip_safe = False,
    include_package_data = True
    )