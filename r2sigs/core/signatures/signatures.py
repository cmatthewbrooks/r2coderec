import os
import sys

SIGNATURE_GEN_DIRECTORY = os.path.abspath(
    os.path.dirname(__file__)
)

SIGNATURE_GEN_FILE_LIST = []

def initialize_signature_gen_file_list():

    ignore = ['__init__.py','signatures.py']

    for f in SIGNATURE_GEN_DIRECTORY:
        
        SIGNATURE_GEN_FILE_LIST.append(
            os.path.join(SIGNATURE_GEN_DIRECTORY, f)
        )



class Signatures:

    def __init__(self):

        pass


def main():
    pass

if __name__ == '__main__':
    main()
