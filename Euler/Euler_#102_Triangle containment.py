import math
numtri = int(input("Number of triangles: "))
def areaoftri(x1, y1, x2, y2, x3, y3): #find the area of triangle
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0) 


x = 0
y = 0
triangleorigin = []
for a in range(0,numtri):
    x1,y1,x2,y2,x3,y3= (input("entercoordinates: ").split(" "))
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    x3 = int(x3)
    y3 = int(y3)
    def isInside(x1, y1, x2, y2, x3, y3, x, y): 
      
        # Calculate area of triangle XYZ 
        maintri = areaoftri(x1, y1, x2, y2, x3, y3) 
  
        # Calculate area of triangle 0BC  
        tri1 = areaoftri(x, y, x2, y2, x3, y3) 
          
        # Calculate area of triangle 0AC  
        tri2 = areaoftri(x1, y1, x, y, x3, y3) 
          
        # Calculate area of triangle 0AB  
        tri3 = areaoftri(x1, y1, x2, y2, x, y) 

        print("total of 3 triangle",(tri1 + tri2 + tri3))
        print("area of tri1: ",tri1,"area of tri 2: ", tri2,"area of tri 3: ",tri3)
        print("area of main triangle: ",maintri)
        print(x1,y1,x2,y2,x3,y3,x,y)
 
        # Check if sum of A1, A2 and A3  
        # is same as A 
        if(maintri == tri1 + tri2 + tri3): 
            triangleorigin.append("1")
            print("heres the vaLUE OF TRIANGLEORIGIN: ",triangleorigin)

    isInside(x1,y1,x2,y2,x3,y3,x,y)

             
print(len(triangleorigin))
	  
