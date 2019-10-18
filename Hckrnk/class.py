'''Input Format

You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in  lines of input; the first line contains , and the second line describes the  array.

Sample Input

3
1 2 5
Sample Output

4
Explanation

The scope of the  array and  integer is the entire class instance. The class constructor saves the argument passed to the constructor as the  instance variable (where the computeDifference method can access it).

To find the maximum difference, computeDifference checks each element in the array and finds the maximum difference between any  elements: 

'''


class Difference:
    def __init__(self, a):
        self.__elements = a
    def __init__(self,elements):
        #entered as a list
        self.elements = elements
        self.maximumDifference = 0
    def computeDifference(self):
        lenelements = len(self.elements)
       
        for cases in range(0,lenelements-1):
            for k in range(cases,lenelements):
                difference = abs(self.elements[cases]-self.elements[k])
                self.maximumDifference = max(difference,self.maximumDifference)
            
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
