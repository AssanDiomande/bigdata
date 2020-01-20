class Point :
    
    def __init__(self,x=0,y=0,z=None) :
        self.x = x
        self.y = y
        self.z = z
    
    def toString(self) :
        if self.z is not None :
            print("X : %.2f , Y : %.2f, Z : %.2f" %(self.x,self.y,self.z))
        else :
            print("X : %.2f , Y : %.2f" %(self.x,self.y))
        
        

pt1 = Point(0,1)
pt1.toString()
pt2 = Point(1,2,3)
pt2.toString()