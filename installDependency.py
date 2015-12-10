__author__ = 'Zhiyu'

import pip

def install_dependency():
    install_single_package('jsonpickle')
    #install_single_package('wheel')
    #pip.main(['wheel','numpy'])
    #install_single_package('matplotlib')


def install_single_package(name):
    pip.main(['install', name])

if __name__ == '__main__':
    install_dependency()

