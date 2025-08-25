my_list =[]
for i in range(11):
        my_list.append(i)
print("Original list is:" , my_list)

slice = (my_list[1:6])
print("Extracted first five elems:" , slice)

rev = sorted(slice , reverse=True)
print("Reversed list is:" , rev)

