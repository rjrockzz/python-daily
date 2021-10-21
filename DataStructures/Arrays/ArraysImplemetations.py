class Array(object):
    def __init__(self,sizeArray,arrayType = int):
        self.sizeArray = len(list(map(arrayType, range(sizeArray))))
        self.arrayItems = [arrayType(0)]* sizeArray
        