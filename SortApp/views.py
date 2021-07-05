from django.http import HttpResponse
from django.shortcuts import render
from .algorithms import linearSearch, binarySearch,\
    bubbleSort, mergeSort, insertionSort, selectionSort

# Create your views here.

def index(request):
    return render(request, 'SortApp/index.html')

def sort(request):
    return render(request, 'SortApp/sort.html')
    
def search(request):
    return render(request, 'SortApp/search.html')

def element_to_array(dic):
    print('Hiii')
    val = int(dic.get('sub'))
    print('Hello')
    arr = []
    for i in range(1, val + 1):
        arr.append(int(dic.get(str(i))))
    return arr


def linearview(request):
    if request.method == 'GET':
        context = {'req': request.GET.get('data')}
        return render(request, 'SortApp/linear/linear.html', context)
    if request.method == 'POST':
        arr = element_to_array(request.POST)
        array = arr
        key = int(request.POST.get('textfield'))
        value = linearSearch(arr,key)
        return render(request, 'SortApp/linear/linearsearch.html', {'req': value,'key':key,'array':array})
    else:
        return render(request, 'SortApp/linear/linear.html', {'req': 'linearview'})


def binaryview(request):
    if request.method == 'GET':
        context = {'req': request.GET.get('data')}
        return render(request, 'SortApp/binary/binaryview.html', context)
    if request.method == 'POST':
        arr = element_to_array(request.POST)
        array = arr
        key = int(request.POST.get('textfield'))
        value = binarySearch(arr,key)
        return render(request, 'SortApp/binary/binraysearch.html', {'req': value,'key':key,'array':array})
    else:
        return render(request, 'SortApp/binary/binaryview.html', {'req': 'binaryview'})


def bubblesortview(request):
    if request.method == 'GET':
        context = {'req': request.GET.get('data')}
        return render(request, 'SortApp/bubble/bubbleview.html', context)
    if request.method == 'POST':
        arr = element_to_array(request.POST)
        arr = bubbleSort(arr)
        return render(request, 'SortApp/bubble/bubblesort.html', {'req': arr})
    else:
        return render(request, 'SortApp/binary/binaryview.html', {'req': 'bubblesortview'})


def mergesortview(request):
    if request.method == 'GET':
        context = {'req': request.GET.get('data')}
        return render(request, 'SortApp/merge/mergeview.html', context)
    if request.method == 'POST':
        arr = element_to_array(request.POST)
        arr = mergeSort(arr)
        return render(request, 'SortApp/merge/mergesort.html', {'req': arr})
    else:
        return render(request, 'SortApp/merge/mergeview.html', {'req': 'mergesortview'})



def insertionsortview(request):
    if request.method == 'GET':
        context = {'req': request.GET.get('data')}
        return render(request, 'SortApp/insertion/insertionview.html', context)
    if request.method == 'POST':
        arr = element_to_array(request.POST)
        arr = insertionSort(arr)
        return render(request, 'SortApp/insertion/insertionsort.html', {'req': arr})
    else:
        return render(request, 'SortApp/insertion/insertionview.html', {'req': 'insertionsortview'})

def selectionsortview(request):
    if request.method == 'GET':
        context = {'req': request.GET.get('data')}
        return render(request, 'SortApp/selection/selectionview.html', context)
    if request.method == 'POST':
        arr = element_to_array(request.POST)
        arr = selectionSort(arr)
        return render(request, 'SortApp/selection/selectionsort.html', {'req': arr})
    else:
        return render(request, 'SortApp/selection/selectionview.html', {'req': 'selectionsortview'})

def stackview(request):
    if request.method == 'GET':    
        return render(request, 'SortApp/stack.html', {'req': 'stackview'})
    else:
        return render(request, 'SortApp/index.html')