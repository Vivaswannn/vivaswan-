import numpy as np
import math
print()
print("=====================================")
print("| Welcome to  |")
print("|      created by Vivaswan Singh    |")
print("| of Lovely Professional University |")
print("|          Section: K22FG           |")
print("|         Roll No: RK22FGA07        |")
print("=====================================")
print()
while True:
    n=int(input("Press 1 to generate story and 2 to exit: "))
    print()
    if n==1:
        m=int(input("enter dimensions: "))
        n=int(input())
        table=np.zeros((m,n))
        k=m*n
        mi=math.floor(float(m)/(2));
        middle=int(mi)
        n=n-1;
        table[middle][n]=1;
        for i in range(2,k+1):
            try:
                middle=middle+1
                n=n+1;
                if(table[middle][n]==0):
                    table[middle][n]=i
                else:
                    middle=middle-1
                    n=n-2
                    table[middle][n]=i;
            except:
                try:
                    if(table[middle][0]==0):
                        n=0;
                        table[middle][n]=i
                    else:
                        table[middle][n-1]=i
                except:
                    try:
                        middle=0;
                        table[middle][n]=i;
                    except:
                        middle=middle-1
                        n=n-1;
                        table[middle][n-1]=i
        print(table)
    else:
        print("Thank you for using ")
        break
                                    
	
