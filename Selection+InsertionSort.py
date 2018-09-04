def swap(li,a,b):
    c=li[a]
    li[a]=li[b]
    li[b]=c
"""
Runtime BigO(N^2)
"""  
def selectSort(li):
    for i in range(0,len(li)):
        min=i
        for j in range(i+1,len(li)):
            if li[j]<li[min]:
                min=j
        swap(li,min,i)
def insertSort(li):
    for i in range(1,len(li)):
            temp=li[i]
            j=i
            while (li[j-1]>temp and j>=1):
                li[j]=li[j-1]
                j-=1
            li[j]=temp
