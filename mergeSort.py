def mergeSort(li):
    if len(li)<=1:
        return
    else:
        left=li[:int(len(li)/2)]
        right=li[int(len(li)/2):]
        mergeSort(left)
        mergeSort(right)
        i1=0
        i2=0
        for i in range(0,len(li)):
            if i2>=len(right) or (i1<len(left) and left[i1]<right[i2]):
                li[i]=left[i1]
                i1+=1
            else:
                li[i]=right[i2]
                i2+=1
