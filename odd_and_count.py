start_range=int(input("enter the start range:"))
end_range=int(input("enter the end range:"))
odd_count=0
for num in range(start_range,end_range + 1):
    if num % 2 !=0:
        print(num)
        odd_count+=1
print("The Number of odd no in given range:", odd_count)
