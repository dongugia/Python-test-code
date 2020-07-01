'''
li = [1,2,3,4,5,6,7,8,9,10]
evenNumber = list(map(lambda x: x**2, filter(lambda i: i%2==0,li)))
print(evenNumber)'''


evenNumber = list(filter(lambda x: x%2==0,range(1,21)))
print(evenNumber)
