from setuptools import setup

setup(name='LostInTranslation',
    version='0.1',
    description='Translate text through a chain of languages and back to the original. Because why not?',
    url='http://github.com/iscrow/LostInTranslation',
    author='Ivan Ivanov',
    author_email='iscrow@gmail.com',
    license='The Unlicense',
    install_requires=[
    	'googletrans',
    ],
    zip_safe=False,
    scripts=['LostInTranslation'])
