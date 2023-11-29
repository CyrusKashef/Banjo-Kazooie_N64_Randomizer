'''
Purpose:
'''

###################
##### IMPORTS #####
###################

from setuptools import find_packages, setup

####################
##### WORKFLOW #####
####################

packages = find_packages(exclude=["BK_Rando.egg-info", "build", "dist", "do_not_commit", "docs", "tests"])

setup(
    name="BK_Rando",
    version="1.0.0",
    description='None',
    # url='None',
    author='BK_Rando_Dev_Team',
    # author_email='None',
    license='MIT',
    packages=packages,
    zip_safe=False,
)