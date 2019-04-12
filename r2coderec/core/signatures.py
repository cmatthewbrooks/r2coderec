import os

SIGTYPE_DIRECTORY_NAME = 'sigtypes'
SIGS_DIRECTORY_NAME = 'sigs'

SIGTYPE_DIRECTORY = os.path.join(
    os.path.abspath(
        os.path.dirname(__file__)
    ), SIGTYPE_DIRECTORY_NAME
)

SIGTYPE_FILE_LIST = []
SIGTYPE_IGNORE_LIST = ['__init__.py']

VALID_SIGTYPE_LIST  = []

DEFAULT_SIGS_DIRECTORY = os.path.join(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__),'..')
    ), SIGS_DIRECTORY_NAME
)

class Signature:

    def __init__(self):

        self.initialize_sigtype_file_list()
        self.initialize_valid_sigtype_list()

    def initialize_sigtype_file_list(self):

        for f in os.listdir(SIGTYPE_DIRECTORY):
            
            if f not in SIGTYPE_IGNORE_LIST: 
            
                SIGTYPE_FILE_LIST.append(
                    os.path.join(SIGTYPE_DIRECTORY, f)
                )

    def initialize_valid_sigtype_list(self):

        for f in os.listdir(SIGTYPE_DIRECTORY):

            if f not in SIGTYPE_IGNORE_LIST:

                VALID_SIGTYPE_LIST.append(
                    f[:(len(f)-len('.py'))]
                )

    def is_valid_sigtype(self, sigtype):

        if sigtype in VALID_SIGTYPE_LIST:
            return True
        else:
            return False

def main():
    pass


if __name__ == '__main__':
    main()
