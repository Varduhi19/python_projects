class simpleArrayList:
    def __init__ (self,name):
        self.name = name
        self.array = []

    def add(self,object):
        self.array.append(object)
        print(self.array)

    def size(self):
        count = 0
        for i in self.array:
            count += 1
        return count

    def putEnd(self,OIL): #object in list
        for i in range(0,len(self.array)):
            if OIL == self.array[i]:
                ETI = self.array[i] #in the end throw info
                for j in range(i,len(self.array)-1):
                    self.array[j] = self.array[j+1]
                self.array[len(self.array)-1] = ETI

    def show(self):
        for i in range(len(self.array)-1):
            print(self.array[i], end = " ")
        print(self.array[len(self.array) - 1])


    def giveIndx(self,object):
        count = 0
        for i in range(0,len(self.array)-1):
            if self.array[i] == object:
                break
            else:
                count += 1
        return count

    def delElement(self,object):
        self.array.remove(object)

    def STS(self):#string to string
        newList = []
        for i in self.array:
            newList.append(str(i))
        print(newList)


            


c1 = simpleArrayList("classA")
c1.add("Ara")
c1.add(1)
c1.add("Felo")
c1.add("Hakob")
c1.add(None)
c1.show()
print(c1.size())
c1.putEnd("Ara")
c1.show()
print(c1.giveIndx("Ara"))
c1.delElement("Hakob")
c1.show()
c1.STS()