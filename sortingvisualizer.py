from tkinter import *
from tkinter import ttk
import random
from BubbleSort import  bubbleSort
from SelectionSort import selectionsort
from insertionsort import insertionsort
from Mergesort import merge_sort
from QuickSort import quick_sort
# from BubbleSort import bubble_sort

root=Tk()
root.title('Sorting algorithm visualizer')
root.geometry("750x600")
root.config(bg="#000fff000")

select_algorithm=StringVar()
arr=[]

#Generate the array



def Generate_array():
    global arr
    lowest =int(lowest_Entry.get())
    highest =int(highest_Entry.get())
    size=int(arrsize_Entry.get())
    arr=[]
    for i in range(size):
        arr.append(random.randrange(lowest,highest+1))
    drawrectangle(arr,['red' for x in range(len(arr))])

#Drawing array elements as rectangles
def drawrectangle(arr,colorArray):
    canvas.delete("all")
    canvas_height=380
    canvas_width=600
    bar_width=canvas_width/(len(arr)+1)
    border_offset =30
    spacing=10
    normalized_array =[i /max(arr) for i in arr]
    for i,height in enumerate(normalized_array):
        x0=i*bar_width +border_offset+spacing
        y0=canvas_height-height*340
        x1=(i+1)*bar_width+border_offset
        y1=canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(arr[i]))
    root.update_idletasks()
    root.update()

def sorting():
    global arr
    if not arr: return

    if algomenu.get() == 'Bubble sort':
        bubbleSort(arr, drawrectangle,sortingspeed.get())

    elif algomenu.get() == 'Selection sort':
        selectionsort(arr, drawrectangle, sortingspeed.get())

    elif algomenu.get() == 'Insertion sort':
        insertionsort(arr, drawrectangle, sortingspeed.get())

    elif algomenu.get() == 'Quick sort':
        quick_sort(arr,drawrectangle, sortingspeed.get())

    elif algomenu.get() == 'Merge sort':
        merge_sort(arr, drawrectangle, sortingspeed.get())


    drawrectangle(arr, ['blue' for x in range(len(arr))])


#GUI coding part

opt_frame = Frame(root, width= 700, height=300, bg='pink')
opt_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=700, height=350, bg='White')
canvas.grid(row=1, column=0, padx=10, pady=5)


Label(opt_frame, text="Algorithm Choice: ",).grid(row=0, column=0, padx=10, pady=10)

algomenu = ttk.Combobox(opt_frame, textvariable=select_algorithm, values=['Bubble sort','Selection sort','Insertion sort','Quick sort','Merge sort'],width=10)
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

sortingspeed = Scale(opt_frame, from_=0.01,to=4.0,length=100,digits=2, resolution=0.2, orient=HORIZONTAL, label="Sorting Speed " )
sortingspeed.grid(row=0,column=2,padx=10,pady=10)

Button(opt_frame,text="Start sorting",command=sorting,bg='red',height=5).grid(row=0,column=3,padx=5,pady=5)
lowest_Entry=Scale(opt_frame,from_=5,to=20,resolution=1,orient=HORIZONTAL,label="Lower Limit")
lowest_Entry.grid(row=1,column=0,padx=5,pady=5)

highest_Entry=Scale(opt_frame,from_=20,to=100,resolution=1,orient=HORIZONTAL,label="Upper Limit")
highest_Entry.grid(row=1,column=1,padx=5,pady=5)

arrsize_Entry =Scale(opt_frame,from_=3,to=25,resolution=1,orient=HORIZONTAL,label="Arraysize")
arrsize_Entry.grid(row=1,column=2,padx=5,pady=5)

Button(opt_frame,text="Current Array",command=Generate_array,bg='blue',height=5).grid(row=1,column=3,padx=10,pady=10)
root.mainloop()
