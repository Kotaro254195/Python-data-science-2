import matplotlib.pyplot as plt

number1=[1,2,3,4,5,6]
number2=[7,4,3,5,6,7]
number3=[6,8,3,7,2,8]
number4=[3,5,7,9,2,4]
number5=[5,3,2,6,9,10]

# stackplot don't allow u to create label in the background

plt.stackplot(number1,number2,number3,number4,number5)

# plt.legend()
plt.show()