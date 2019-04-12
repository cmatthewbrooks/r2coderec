import os
import argparse

from core.maker import Maker as Maker
from core.matcher import Matcher as Matcher

def main():

    about = ('r2sigs: Make and match function '
             'signatures in disassembly')
    
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description = about,
        epilog = '''

Examples:

    - Make zighash signatures from a target directory:

        $ %(prog)s make --sigtype zighash --target /path/to/dir

        '''
    
    )



    subparsers = parser.add_subparsers(title='commands', dest='command')

    make = subparsers.add_parser(
        'make',
        help = 'Make signatures from location'
    )

    make.add_argument(
        '--sigtype',
        help = 'The type of function signatures being created'
    )
    
    make.add_argument(
        '--target',
        help = 'The target directory with libraries for signature generation'
    )

    make.add_argument(
        '--siglocation',
        help = 'A location for the signatures file (if default not desired)' 
    )


    match = subparsers.add_parser(
        'match',
        help = 'Match signatures inside r2 session'
    )

    match.add_argument(
        '--siglocation',
        help = 'Specific file or directory (if not using default)'
    )
     
    match.add_argument(
        '--rename',
        action = 'store_true',
        help = ('Rename the functions inside an r2 session with matching '
               'signature names')
    )



    args = parser.parse_args()
    
    print args

    if args.command == 'make':
       
        m = Maker(args.sigtype, args.target, args.siglocation)
        m.sigmake()

    elif args.command == 'match':
       
        m = Matcher(args.siglocation)
        m.sigmatch(args.rename)


if __name__ == '__main__':
    main()
