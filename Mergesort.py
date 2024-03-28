import time



def merge(data,left,mid,right,drawrectangle,delay):
    drawrectangle(data,getColorArray(len(data),left,mid,right))
    time.sleep(delay)

    leftpart=data[left:mid+1]
    rightpart=data[mid+1:right+1]
    leftidx=rightidx=0

    for dataIdx in range(left,right+1):
        if leftidx<len(leftpart) and rightidx<len(rightpart):
            if(leftpart[leftidx]<=rightpart[rightidx]):
                data[dataIdx]=leftpart[leftidx]
                leftidx+=1
            else:
                data[dataIdx] = rightpart[rightidx]
                rightidx += 1;
        elif leftidx < len(leftpart):
            data[dataIdx] = leftpart[leftidx]
            leftidx += 1
        else:
            data[dataIdx] = rightpart[rightidx]
            right += 1
    drawrectangle(data, ["blue" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(delay)

def getColorArray(length,left,middle,right):
    colorArray=[]
    for i in range(length):
        if i>=left and i<=right:
            if i>=left and i<=middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")
    return colorArray


def mergeSort(data,left,right,drawrectangle,delay):
    if left<right:
        mid=(left)+(right-left)//2
        mergeSort(data,left,mid,drawrectangle,delay)
        mergeSort(data,mid+1,right,drawrectangle,delay)
        merge(data,left,mid,right,drawrectangle,delay)


def merge_sort(data,drawrectangle,delay):
    mergeSort(data,0,len(data)-1,drawrectangle,delay)