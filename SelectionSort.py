import time

def selectionsort(data,drawrectangle,delay):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            drawrectangle(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
            time.sleep(delay)
        data[j + 1] = key
    drawrectangle(data, ['green' for x in range(len(data))])