# 1.Output[1]
# list1=[1, 1, 1]
# i=0
# a=[]
# while i<len(list1):
#     if list1[i] not in a:
#         a.append(list1[i])
#     i+=1
# print(a)

# 2.Output[ ]
# list1=[ ]
# i=0
# while i<len(list1):
#     i+=1
# print(list1)

# 3.Output=[20, 17]
a= [15, 20, 20, 17]
c=[]
i=0
while i<len(a):
    if a[i] not in c:
        c.append(a[i])
    i+=1
print(c)
j=0
max=0
sec=0
while j<len(c):
    if c[j]>max:
        max=c[j]
    elif c[j]<max and c[j]>sec:
        sec=c[j]
    j+=1
print(max)
print(sec)
        









# i=0
# first=0
# sec=0
# a=[]
# while i<len(list1):
#     if list1[i]>first:
#         first=list1[i]
#     i+=1
#     j=0
#     b=[]
#     while j<len(list1):
#         if first>list1[j] and list1[j]>sec:
#             sec=list1[j]
#             b.append(i)
#             b.append(j)
#             a.append(b)
#         j+=1
# print(a)




