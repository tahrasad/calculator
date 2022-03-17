# exo1-1)
# x=3
# y=5
# x,y=y,x
# print (x,"c'est le valeur de x",y,"c'est le valeur de y")

# exo1-2)
# a=7
# b=1
# c=0

# exo1-3)
# n2=17
# while n2!=0:
#     if (n2 % 2 != 0):
#         print(n2)
#         n2-=1
#     else :
#         n2-=1  

# exo2-1)
# s1=0
# n=5
# # j=0
# for i in range(1,n+1,2):
#         j=i+1
#         s1=s1+i**j

# print(s1)

# -2)
# s2=0
# n=int(input("donnez n"))
# for i in (1,n):

#     print( ((i**9)+1)/(i+4)  )


# exo3

# l=[]
# j=0
# i=0
# n=0
# m=0
# while n>=0:
#     n=int(input("  "))
#     if n>=0:
#         l.append(n)
#         i+=1
#         print(f"note{i}:{n}")
#     else :
#         j=i+1
#         print(f"note {j}:{n}")
#         print("note negative")

#         m=sum(l)/len(l)
#         print(f"le moyenne est: {m}")
#         break

# exo4-1)
# u=2
# n=float(input(" n= "))
# while n>0:

#     if n>0:
#         u=u*3-1
#         n-=1
#         print(u)
#     else :
#         break    

# u=2
# n=int(input("n= ? "))    
# for i in range(1,n+1):
#     if n>0:
#      u=u*3-1
#      print (u)    

#     else:
#         exit()       


# exo5

# def illi(ch):
#     alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     cod=""
#     for e in ch:
#      i=alpha.find(e)
#      pos=i+1
#      if pos==26:
#       pos=0
#      cod+= alpha[pos]    
#     return cod 


# v="HRLLO"

# print(illi(v))

# exo1-cours

# ch=" "
# i=(input(" i =? "))


# for j in range(len(i)-1,0,-1):
#     print (i[j])

# les matrices
# creation des matrices vide
# additionner les matrices
# multuplication des matrices
# l'affichage

# A=[[3,1,5],[9,8,-1],[10,12,2]]
# m=len(A)
# n=len(A[0])
# T=[]
# for i in range (0,n):
#    u=0*i
#    T.append(u) 
# c=[]
# for i in range(0,m):
#     for e in T:
#         c.append(e)


# print(T)
# print(c)

# correction l'inverse d'une M
# A=[[3,1,5],[9,8,-1],[10,12,2]]
# m=len(A)
# n=len(A[0])
# c=[[0]*n for i in range (m)]
# for i in range(m):
#     for j in range(n):
#         c[j][i]=A[i][j]       
# print(c)        

# def no(l,e):
#     mode=0
#     for n in l:
#         if n==e:
#             mode+=1
#     print(mode)
#     return mode        
# no([1,2,3,4,4,4,4,4,9],4)





# def is_square(M):
#     l = len(M)
#     c = len(M[0])
#     d = False
#     if c == l:
#         d = True
#     print(d)
#     return d
# A = [[3, 1, 5], [9, 8, -1], [10, 12, 2]]
#
# print(is_square(A))




# def trace(M):
#     l = len(M)
#     c = len(M[0])
#     s = 0
#     if l == c:
#         for i in range(l):
#             s = s + M[i][i]
#
#     else:
#         print("trace of a non square matrix is not defined")
#     print(s)
#     return M
#
#
#A= [[3, 1, 5], [9, 8, -1], [10, 12, 2],[1,6,8]]
# trace(A)



# A = [[3, 0, 0], [0, 8, 0], [0, 0, 2]]
# def is_diagonal(m):
#     c = len(m[0])
#     l = len(m)
#     b=True
#     if l==c:
#        for i in range(l):
#            for j in range(c):
#                 if ((i != j)and(m[i][j] == 0)):
#                 # while (m[i][j] == 0):
#                      b=False
#        if b == True:
#            print("la matrice n'est pas diagonal")
#        else:
#            print("est diagonal")
#     else:
#         print("la matrice n'est pas carre")
#
# is_diagonal(A)


# def triangulaire(M):
#     l=len(M)
#     c=len(M[0])
#     b=True
#     for i in range(l):
#         for j in range(c) :
#             if j < i and M[i][j] != 0:
#                 b=False
#     if b==True:
#         print(f"la matrice {M} est triangulaire")
#     else:
#         print(f"{M} n'est pas une matrice triangulaire")
#
#
# A = [[3, 0, 0], [6, 8, 0], [0, 0, 2]]
# triangulaire(A)
for i in range(100):
    print(i)