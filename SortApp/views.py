from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'SortApp/index.html')

def sort(request):
    return render(request, 'SortApp/sort.html')

def search(request):
    return render(request, 'SortApp/sort.html')

def getelement(request):
    context = {'req' : request.GET.get('data')}
    return render(request, 'SortApp/getele.html',context)


def linearview(request):
    if request.method == 'POST':
        print('\n\nsdfsd\n')
        val = int(request.POST.get('sub'))
        arr = []
        for i in range(1,val+1):
            arr.append(int(request.POST.get(str(i))))
            print(arr)
        key = int(request.POST.get('textfield', None))
        
        # return HttpResponse(arr)
        # arr = [10, 20, 30, 40, 50, 60, 70, 80]
        # key = int(input("Enter Element you want to find:"))

        return LinearSearch(arr, key)
    else:
        return render(request, 'SortApp/getele.html', {'req' : 'linearview'})

def binaryview(request):
    if request.method == 'POST':
        # noinspection DuplicatedCode
        arr = [int(request.POST.get('textfield1', None)), int(request.POST.get('textfield2', None)),
               int(request.POST.get('textfield3', None)), int(request.POST.get('textfield4', None)),
               int(request.POST.get('textfield5', None))]

        key = int(request.POST.get('textfield', None))

        return BinarySearch(arr, key)

    else:
        return render(request, 'SortApp/getele.html', {'req' : 'binaryview'})


########### ALGOS ############
def LinearSearch(arr, key):
    flag = 0
    for i in range(len(arr)):
        if key == arr[i]:
            flag = 1
            return HttpResponse("Element found at position {}".format(i + 1))
    if flag == 0:
        return HttpResponse("Element Not Found")


def BinarySearch(arr, key):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if key == arr[mid]:
            return HttpResponse("Element found at position {}".format(mid + 1))
        elif key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1

    return HttpResponse("Element Not Found")
########### ALGOS END ############
