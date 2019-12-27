# Automatically created by: gerapy
from setuptools import setup, find_packages
setup(
    name='weibo_temp',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy':['settings=weibo_temp.settings']},
)