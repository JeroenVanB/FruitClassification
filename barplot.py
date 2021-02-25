import numpy as np
import matplotlib.pyplot as plt

train = "Apples: 6404, Bananas: 1430, Cherries: 3444, Grapes: 3419, Onions: 1333, Peaches: 1722, Pears: 5037, Peppers: 2478, Plums: 1767, Potatoes: 1803, Tomatoes: 5103"
test = "Apples: 2137, Bananas: 484, Cherries: 1148, Grapes: 1146, Onions: 451, Peaches: 574, Pears: 1689, Peppers: 826, Plums: 597, Potatoes: 601, Tomatoes: 1707"
train_array = train.split(", ")
test_array = test.split(", ")
print(train_array)
print(test_array)

classes = []
train_count = []
test_count = []

for idx, i in enumerate(train_array):
    a = i.split(": ")
    classes.append(a[0])
    train_count.append(int(a[1]))

for idx, i in enumerate(test_array):
    a = i.split(": ")
    # classes.append(a[0])
    test_count.append(int(a[1]))

print(classes)
print(train_count)
print(test_count)



# Make a fake dataset:
labels = classes

x = np.arange(len(labels))
width = 0.35  # the width of the bars


fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, train_count, width, label='Train')
rects2 = ax.bar(x + width/2, test_count, width, label='Test')

# Create names on the x-axis
plt.xticks(x, labels, rotation="vertical")

plt.xlabel("Classes")
plt.ylabel("Number of Images")
plt.legend(["Train data", "Test data"])
plt.title("Class distribution")
plt.tight_layout()

plt.savefig('barplot_data.png')
