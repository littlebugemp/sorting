#implementing bubble sort
#best case O(n^2)
#worst case O(n^2)

def bubble_sort(li):
    i,j=0,0
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                temp = li[j]
                li[j]= li[j+1]
                li[j+1]=temp
    return li

# print(bubble_sort([0,1,2,2,0,0,1,0,1,2]))

def improved_bubble_sort(li):
    has_swapped=True
    while(has_swapped):
        has_swapped=False
        for i in range(0,len(li)-1):
            for j in range(0,len(li)-1):
                if li[j] > li[j+1]:
                    li[j],li[j+1]=li[j+1],li[j]
                    has_swapped=True
                
    return li

print(improved_bubble_sort([0,1,2,2,0,0,1,0,1,2]))
print(improved_bubble_sort([1,2,3]))