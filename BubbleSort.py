import time

def bubbleSort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            drawrectangle(data, getColorArray(len(data), j, j+1))
            time.sleep(delay)

def getColorArray(length, index1, index2):
    colorArray = []
    for i in range(length):
        if i == index1 or i == index2:
            colorArray.append("red")
        else:
            colorArray.append("white")
    return colorArray

def bubble_sort(data, drawrectangle, delay):
    bubbleSort(data, drawrectangle, delay)