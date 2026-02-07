a=int(input("Enter a num:"))
#TO PRINT STARS
"""
for i in range(1,a+1):
   print()#Row to print the next value 
   for j in range(1,i+1):# staring at one star and increase the star count ,j is the no.of coloumn
      print("*",end="")#end will use for gap between the elements
 """
"""
TO PRINT ROW VALUES
for i in range(1,a+1):
   print()#Row to print the next value 
   for j in range(1,i+1):# staring at one star and increase the star count ,j is the no.of coloumn
      print(i,end="")#end will use for gap between the elements and i print no.of rows value
"""
"""
TO PRINT COLOUMN VALUES
for i in range(1,a+1):
   print()#Row to print the next value 
   for j in range(1,i+1):# staring at one star and increase the star count ,j is the no.of coloumn
      print(j,end="")#end will use for gap between the elements
   """  
"""
TO PRINT THE ORDER VALUE ONE TWO THREE ETC..
for i in range(1,a+1):
   print()#Row to print the next value 
   for j in range(1,i+1):# staring at one star and increase the star count ,j is the no.of coloumn
      print(j+i,end="")#end will use for gap between the elements
      """

for i in range(1,a+1):
    val=i%2#Start with 1 for odd value and even rows for 0
    print()
    for j in  range(i):
        print(val,end="")#print val(0or1),end keep output on the same line in a space
        val=1-val#flip the value for coloumn 0 to 1 and 1to0
  
     