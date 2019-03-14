import os
import argparse

from core.maker import Maker as Maker
from core.matcher import Matcher as Matcher

def main():
    
    parser = argparse.ArgumentParser()



    subparsers = parser.add_subparsers(help='Commands')

    make_parser = subparsers.add_parser('make',help='Make signatures')
    make_parser.set_defaults(mode='make')

    make_parser.add_argument('--sigtype',
        help='The type of sigfile being created')
    make_parser.add_argument('--target',
        help='The target directory with libraries for sig making')

    match_parser = subparsers.add_parser('match',help='Match signatures')
    match_parser.set_defaults(mode='match')

    match_parser.add_argument('--siglocation',
        help='Specific file or directory instead of default')
    match_parser.add_argument('--target',
        help='A target binary if not inside an r2 session')



    args = parser.parse_args()
    


    if args.mode == 'make':
        m = Maker()
    elif args.mode == 'match':
        m = Matcher()



if __name__ == '__main__':
    main()
