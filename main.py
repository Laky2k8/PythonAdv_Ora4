import random

print("TASK 1 \n \n")

def yieldEven(i):
    for j in i:
        if j % 2 == 0:
            yield j

test_list = []
while len(test_list)< 20:
    value = random.randint(1,100)
    if not test_list.__contains__(value):
        test_list.append(value)

print("Our original list is:", test_list)
print("The even numbers in out list are:",end=" ")

for j in yieldEven(test_list):
    print(j,end=" ")
print("\n \n")

print("TASK 2 \n \n")
buyStuffList = ["3D printer", "Gamebuino", "Oculus Quest 2", "eGPU", "NVIDIA GTX 1650 Ti", "hamburgir", "sussy energy balls", "wii phone", "xbox 720 lol", "clippy"]
buyStuffCost = [120,97,400,284,143,2,10,99,1000]