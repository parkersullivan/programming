from matplotlib import pyplot
from numpy import arange
import bisect


def scatterplot(x, y):
    pyplot.plot(x, y, 'b.')
    pyplot.xlim(min(x)-1, max(x)+1)
    pyplot.ylim(min(y)-1, max(y)+1)
    pyplot.show()

scatterplot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])


def barplot(labels, data):
    pos = arange(len(data))
    pyplot.xticks(pos+0.4, labels)
    pyplot.bar(pos, data)
    pyplot.show()

barplot(['blue', 'green ', 'orange', 'red', 'purple'], [40, 32, 37, 12, 22])


print("hello parker/world!")
print(2+2)
# if expression:
#    statement(s)
# else:
#    statement(s)

if (1 == 1):
    print("yes, 1=1")
else:
    print("i dont think this will print")


    
