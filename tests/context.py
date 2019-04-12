# This idea was taken from:
# https://docs.python-guide.org/writing/structure/ 

import os,sys

sys.path.append( 
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

import r2coderec.core.utils as utils
from r2coderec.core import signatures as signatures
from r2coderec.core import maker as maker
