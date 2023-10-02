from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    this function will returns the list of requirements
    '''

    requirements = []

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]#when done line by line read \n will generate so we are removing that by space

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
name ='mlproject',
version = '0.0.1',
author = 'ravimb962',
author_email = 'ravimb962@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')






)