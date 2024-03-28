import time

def partition(data, head, tail, drawrectangle, delay):
    border = head
    pivot = data[tail]

    drawrectangle(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(delay)

    for j in range(head, tail):
        if data[j] < pivot:
            drawrectangle(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(delay)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawrectangle(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(delay)


    #swap pivot with border value
    drawrectangle(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(delay)

    data[border], data[tail] = data[tail], data[border]

    return border

def quicksort(data, head, tail, drawrectangle, delay):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawrectangle,  delay)

        #LEFT PARTITION
        quicksort(data, head, partitionIdx-1, drawrectangle, delay)

        #RIGHT PARTITION
        quicksort(data, partitionIdx+1, tail, drawrectangle, delay)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray

def quick_sort(data,drawrectangle,delay):
    quicksort(data,0,len(data)-1,drawrectangle,delay)