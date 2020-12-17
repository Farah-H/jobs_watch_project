# the purpose of this is to define directory locations in a more dynamic way, which works regardless of os 

import os

SEPERATOR = os.path.sep
ROOT_DIR = f'{os.path.abspath(os.getcwd())}{SEPERATOR}'
TEST_RESOURCES_FOLDER = f'{ROOT_DIR}tests{SEPERATOR}test_resources{SEPERATOR}'
OUTPUT_LOC = f'{ROOT_DIR}outputs{SEPERATOR}'  

if __name__ == '__main__':
    print(ROOT_DIR)
