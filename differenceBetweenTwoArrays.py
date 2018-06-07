A = [1, 2, 100, 200, 4, 5]
B = [1, 100, 900,9,2000]
print("Elements that are available in A but not in B.")
for i in A:
    if i not in B:
        print(i)
