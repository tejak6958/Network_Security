from setuptools import setup,find_packages
from typing import List

def get_requirements():
    """
    This function returns a list of requirements for the project.
    """
    requirements_lst = []
    try:
        with open('requirements.txt') as f:
          lines = f.reaadline()
          for line in lines:
             requirement = line.strip()
             if requirement and not requirement.startswith('#'):
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please create it with the required packages.")
        
    return requirements_lst

    setup(
    name='mlproject',
    version='0.0.1',
    author='teja', 
    author_email = 'tejak6958@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
    )