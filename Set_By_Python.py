class Set:
    def __init__(self):
        self.items=[]
    def Size(self):
        return len(self.items)

    def Contains(self, e):
        return e in self.items

    def Insert(self, e):
        if e not in self.items:
            self.items.append(e)

    def Delete(self, e):
        if e in self.items:
            self.items.remove(e)

    # def Equals(self, setb):

    def Union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for i in setB.items:
            if i not in setC.items:
                setC.items.append(i)
        return setC

    def Intersect(self,setB):
        setC = Set()
        for i in self.items:
            if i in setB.items:
                setC.items.append(i)
        return setC

    def Difference(self,setB):
        setC = Set()
        setC.items = list(self.items)
        for i in setB.items:
            if i in setC.items:
                setC.items.remove(i)
        return setC

    def Display(self, msg):
        print(msg,self.items)

