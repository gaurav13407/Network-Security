'''
The setup.py file is an essential part of packaging and distributing Python projects .It is used by setuptools 
(or distyutils in older Python version)to define the configuration of your project,such as its
metadata,dependencies and more
'''


from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return list of requirement
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ## REad line from the file
            lines=file.readlines()
            ## Procees each file
            for line in lines:
                requirement=line.strip()
                ##ignore empty line and -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_list

setup(
    name="NetworkSecurity",
    version='0.0.1',
    author="Gaurav Joshi",
    author_email="gaurav9997961651jjk277584@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements()
)