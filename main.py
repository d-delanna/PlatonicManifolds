# Run the line below to install snappy on sage
# sage -pip install snappy

import snappy.database as db
from snappy.database import Manifold
from platonicCensus import *  # import large snappy database

if __name__ == '__main__':
    print(db.TetrahedralOrientableCuspedCensus['otet02_00001'])
    print(db.TetrahedralOrientableCuspedCensus.identify(Manifold("m004")))
    print(len(db.OctahedralNonorientableCuspedCensus(solids = 4)))
