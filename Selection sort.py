def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_indx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_indx]:
                min_indx=j
        arr[i],arr[min_indx] = arr[min_indx],arr[i]

#test array
arr=[34,56,75,32,53]
selection_sort(arr)
print("Sorted array: ",arr)

#input from user
nums=input("Enter list of number, separted by space: ").split() 
#split() is used to split the input string into individual numbers based on spaces, creating a list of strings.
nums = [int(num) for num in nums] #converts the string into integer


selection_sort(nums)
print("Sorted list: ",nums)
