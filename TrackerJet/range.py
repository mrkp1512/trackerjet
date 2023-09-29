# # i(1,n,1),j(1,i+1)  ~~Directly Proportional  and increasing
# # i(n,0,-1),j(n,i-1,-1) ~~Directly Proportional and decreasing
# for i in range(6,1,-1):
#     for j in range(1,i-1):
#         print(j,end="")
#     print(" ")
# print('output')
    
# for i in range(6,1,1):
#     for j in range(6,i+1):
#         print("*",end="")
#     print(" ")
# for i in range(1,6,1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print(" ")
    
    
# for i in range(1,6,1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(" ")
    
    
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print(" ")

# for i in range(0,6):
#     for j in range(0,i+1):
#         print(j,end="")
#     print(" ")
    
    
# for i in range(1,6):
#     for j in range(6,1,-1):
#         print(" ",end="")
#     print("*")
# Define the radius of the circle
# radius = 5

# import math

# radius = 5  # Set the radius of the circle

# for i in range(2 * radius + 1):
#     for j in range(2 * radius + 1):
#         distance = math.sqrt((i - radius) ** 2 + (j - radius) ** 2)
#         if distance > radius - 0.5 and distance < radius + 0.5:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

for i in range(1, 6):
    for j in range(1, 6):
        if j==3 or i==3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
