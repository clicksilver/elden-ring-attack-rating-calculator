"""
Class container for stats array
"""

STR='stre'
DEX='dext'
INT='inte'
FAI='fait'
ARC='arca'

class Stats(object):
    def __init__(self, stre, dext=None, inte=None, fait=None, arca=None):
        if isinstance(stre, list):
            self.stre = stre[0]
            self.dext = stre[1]
            self.inte = stre[2] 
            self.fait = stre[3] 
            self.arca = stre[4] 
        else:
            self.stre = stre
            self.dext = dext
            self.inte = inte
            self.fait = fait
            self.arca = arca

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)
