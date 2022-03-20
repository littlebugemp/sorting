def selection_sort(li):
    k=0
    for i in range(0,len(li)):
        # print(f"i->{i}")
        min=i
        for j in range(i+1,len(li)):
            k=k+1
            # print(f"\tj->{j}")
            if li[j] < li[min]:
                min = j
        li[i],li[min]=li[min],li[i]
    # print(k)
    return li

# print(selection_sort([3,2,1,4,22,31,2,1,0]))