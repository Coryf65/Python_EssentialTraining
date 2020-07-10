#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys, os

def main():
    v = sys.version_info
    platform = sys.platform
    system = os.name
    current_directory = os.getcwd()


    print('Python version {}.{}.{}'.format(*v))
    print(f'Your PC is a: {platform} {system}')
    print(f'Current Working Directory: {current_directory}')

if __name__ == '__main__': main()
