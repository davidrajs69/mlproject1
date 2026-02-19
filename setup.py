from setuptools import setup, find_packages
from typing import List

HYPERN_E_DOT = '-e .'

def getRequirements(file_path:str) -> List[str]:
    with open(file_path) as f:
        requirements = f.read().splitlines()
    return [req for req in requirements if req != HYPERN_E_DOT]

setup(
    name='mlproject1',
    version='0.0.1',
    author="Devid Raj",
    author_email="david.raj@gmail.com",
    packages=find_packages(),
    install_requires=getRequirements('requirements.txt')
)