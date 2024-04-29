def quick_Sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        Pivot = arr[0]
        less_Then_Pivot = [x for x in arr[1:]if x<= Pivot]
        greater_Then_Pivot = [x for x in arr[1:]if x > Pivot]
        return quick_Sort(less_Then_Pivot) + [Pivot] + quick_Sort(greater_Then_Pivot)

n = int(input())
arr = list(map(int , input().split()))

Sorted_arr = quick_Sort(arr)

print(*Sorted_arr)
