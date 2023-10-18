from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'kafka'
VERSION = '0.0.1'
AUTHOR = 'Rohit Kumar'
DESCRIPTION = 'Project to connect to Kafka and exchange messages'

REQUIREMENT_FILE_NAME = 'requirements.txt'

HYPHEN_E_DOT = '-e .'

def get_requirements_list() -> List[str]:
    """_summary_
    Description: This function returns a list of requirements mentioned in the requirements.txt file

    Returns:
        List[str]: _description_
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace('\n','') for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
    
setup(
    name = PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)