"""
Class container for stats array
"""

class Stats:
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
