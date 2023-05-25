import numpy as np
import random
import math

my_data = np.genfromtxt("iris.csv", delimiter=",")
data = my_data.tolist()

random.shuffle(data)

# Dataset preparation (Randomly Split the dataset into Training (70%), Validation (15%) and Test (15%) set):
Train_set = []
Val_set = []
Test_set = []

for S in range(len(data)):
    R = random.uniform(0, 1)
    if 0 <= R <= 0.7:
        Train_set.append(data[S])
    elif 0.7 < R <= 0.85:
        Val_set.append(data[S])
    else:
        Test_set.append(data[S])

# KNN Classification (Use Iris data):
# determine Val_acc

k = 5
L = []
dis = []
Class_for_sample_v = []
accurate = 0

for V in range(len(Val_set)):
    for T in range(len(Train_set)):
        x1 = Val_set[V][0]
        x2 = Train_set[T][0]
        y1 = Val_set[V][1]
        y2 = Train_set[T][1]
        z1 = Val_set[V][2]
        z2 = Train_set[T][2]
        a1 = Val_set[V][3]
        a2 = Train_set[T][3]

        dis = (math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2) + math.pow(z1 - z2, 2) + math.pow(a1 - a2, 2)))

        A1 = Train_set[T][0]
        A2 = Train_set[T][1]
        A3 = Train_set[T][2]
        A4 = Train_set[T][3]
        A5 = Train_set[T][4]
        L.append([A1, A2, A3, A4, A5, dis])
    L.sort(key=lambda a: a[5])
    for x in range(k):
        Class_for_sample_v.append(L[x][4])

    zero = Class_for_sample_v.count(0)
    one = Class_for_sample_v.count(1)
    two = Class_for_sample_v.count(2)
    assumption = 0

    if one < zero > two:
        assumption = 0
    elif two < one > zero:
        assumption = 1
    else:
        assumption = 2

    if assumption == Val_set[V][4]:
        accurate = accurate + 1

    Class_for_sample_v.clear()
    L.clear()

accuracy = (accurate / len(Val_set)) * 100
print(f'Accurate Elements of Val_Set Where K is ({k}): {accurate}')
print(f'Total Elements of Val_Set Where K is ({k}): {len(Val_set)}')
print(f'Validation Accuracy Where K is ({k}): {accuracy} %')
print("\n")

# determine Test_acc
accurate_T = 0
k = 5

for Tst in range(len(Test_set)):
    for T in range(len(Train_set)):
        x1 = Test_set[Tst][0]
        x2 = Train_set[T][0]
        y1 = Test_set[Tst][1]
        y2 = Train_set[T][1]
        z1 = Test_set[Tst][2]
        z2 = Train_set[T][2]
        a1 = Test_set[Tst][3]
        a2 = Train_set[T][3]

        dis = (math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2) + math.pow(z1 - z2, 2) + math.pow(a1 - a2, 2)))

        A1 = Train_set[T][0]
        A2 = Train_set[T][1]
        A3 = Train_set[T][2]
        A4 = Train_set[T][3]
        A5 = Train_set[T][4]
        L.append([A1, A2, A3, A4, A5, dis])
    L.sort(key=lambda a: a[5])
    for x in range(k):
        Class_for_sample_v.append(L[x][4])

    zero = Class_for_sample_v.count(0)
    one = Class_for_sample_v.count(1)
    two = Class_for_sample_v.count(2)
    assumption = 0

    if one < zero > two:
        assumption = 0
    elif two < one > zero:
        assumption = 1
    else:
        assumption = 2

    if assumption == Test_set[Tst][4]:
        accurate_T = accurate_T + 1

    Class_for_sample_v.clear()
    L.clear()

accuracy_T = (accurate_T / len(Test_set)) * 100

print(f'Accurate Elements of Test_Set Where K is ({k}): {accurate_T}')
print(f'Total Elements of Test_Set Where K is ({k}): {len(Test_set)}')
print(f'Test Accuracy Where K is ({k}): {accuracy_T} %')