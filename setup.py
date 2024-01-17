import setuptools
from typing import List

def get_reqs(file_path:str)->List[str]:
    req = []
    with open(file_path) as obj:
        req = obj.readlines()
        req = [x.replace("\n","") for x in req]
        
        if '-e .' in req:
            req.remove('-e .')
    return req

setuptools.setup(
    name='First project',
    author= 'Pranav Moses',
    packages=setuptools.find_packages(),
    install_requires= get_reqs('requirements.txt')
)