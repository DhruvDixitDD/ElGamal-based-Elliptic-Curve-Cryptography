print("ElGamal based Elliptic Curve Cryptography\nby Dhruv Dixit:\t 15BCE1324\nVIT University, Chennai\n\nElliptic Curve General Form:\t y^2 mod n=(x^3  + a*x + b)mod n\nEnter 'n':")

def polynomial(LHS,RHS,n):
    for i in range(0,n):
        LHS[0].append(i)
        RHS[0].append(i)
        LHS[1].append((i*i*i + a*i + b)%n)
        RHS[1].append((i*i)%n)


def points_generate(arr_x,arr_y,n):
    count=0
    for i in range(0,n):
        for j in range(0,n):
            if(LHS[1][i]==RHS[1][j]):
                count+=1
                arr_x.append(LHS[0][i])
                arr_y.append(RHS[0][j])
    return count

#main
n=int(input())
LHS=[[]]
RHS=[[]]
LHS.append([])
RHS.append([])
print("Enter value of 'a':")
a=int(input())
print("Enter value of 'b':")
b=int(input())

#Polynomial
polynomial(LHS,RHS,n)

arr_x=[]
arr_y=[]
#Generating base points
count=points_generate(arr_x,arr_y,n)
    
#Print Generated Points
print("Generated points are:")
for i in range(0,count):
    print(i+1," (",arr_x[i],",",arr_y[i],")\n")



#Calculation of Base Point
bx=arr_x[0]
by=arr_y[0]
print("Base Point taken is:\t(",bx,",",by,")\n")


print("Enter the random number 'd' i.e. Private key of Sender (d<n):")
d=int(input())
if(d>=n):
    print("'d' should be less than 'n'.")
else:
    #Q i.e. sender's public key generation
    Qx=d*bx
    Qy=d*by
    print("Public key of sender is:\t(",Qx,",",Qy,")\n")

    #Encrytion
    print("Enter the random number 'k' (k<n):\n")
    k=int(input())
    if(k>=n):
        print("'k' should be less than 'n'")
    else:
        print("Enter the message to be sent:\n")
        M=int(input())

        #Cipher text 1 generation
        C1x=k*bx
        C1y=k*by
        print("Value of Cipher text 1 i.e. C1:\t(",C1x,",",C1y,")\n")

        #Cipher text 2 generation
        C2x=k*Qx+M
        C2y=k*Qy+M
        print("Value of Cipher text 2 i.e. C2:\t(",C2x,",",C2y,")\n")

    #Decryption
        Mx=C2x-d*C1x
        My=C2y-d*C1y
        print("The message recieved by reciever is:\t",Mx)            
