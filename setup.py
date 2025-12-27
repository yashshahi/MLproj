from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of requirements,
    excluding '-e .' if present.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newline characters and ignore empty lines
        requirements = [req.strip() for req in requirements if req.strip()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='MLproj',
    version='0.0.1',
    author='Yash',
    author_email='yashshahi51974@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
