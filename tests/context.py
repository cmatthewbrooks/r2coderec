# This idea was taken from:
# https://docs.python-guide.org/writing/structure/ 

import os,sys

sys.path.append( 
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from r2sigs.core.signatures import signatures
