import os

import signatures

class Maker:

    def __init__(self, sigtype, target, siglocation):
        '''
        Inputs:
          sigtype: Type of signature to make
          target: Target directory with libraries to make
          siglocation: Output location for signature file

        Purpose: Instantiate the class
        '''
        self.sigtype = None
        self.target = None
        self.siglocation = None

        s = signatures.Signature()

        if s.is_valid_sigtype(sigtype):
            self.sigtype = sigtype
        else:
            raise Exception('Not a valid sigtype')

        if os.path.exists(target):
            self.target = target
        else:
            raise Exception('Not a valid target location')


    def sigmake(self):
        '''
        Inputs: none

        Purpose: Uses the instance attributes to create signatures.

        Outputs: Signature file
        '''
        pass

def main():
    pass

if __name__ == '__main__':
    main()
