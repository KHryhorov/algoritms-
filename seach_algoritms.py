#linear search
array=[5,6,7,9,23,2,3,56,87,67]
key=int(input())
is_found=False
for item in array:
    if item == key:
        is_found=True
        break
if is_found:
    print("Found")
else:
    print("Not Found")
#complexity-O(n)
