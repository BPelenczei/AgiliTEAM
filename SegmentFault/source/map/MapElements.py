"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : MapElements.py
/ AUTHOR       : 
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ 

/*********************************************************************
/*********************************************************************
"""
from enum import Enum
class ExtendedEnum(str, Enum):

    @classmethod
    def list_value(cls):
        return list(map(lambda c: c.value, cls))

class MapElements(str, Enum):
    Wall = '#'
    Place = '_'
    Door = '-'
    Point = ' '
    Coin = 'o'
    PacMan = 'O'
    Blinky = 'B' # red ghost
    Pinky = 'P'  # pink ghost
    Inky = 'I'   # cyan ghost
    Clyde = 'C'  # orange ghost