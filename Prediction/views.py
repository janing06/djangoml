from django.shortcuts import render
import joblib

def index(request):
    return render(request, "index.html")

def result(request):


    model = joblib.load('FinalModel2')

    lis = []

    lis.append(request.POST['n1'])
    lis.append(request.POST['n2'])
    lis.append(request.POST['n3'])
    lis.append(request.POST['n4'])
    lis.append(request.POST['n5'])
    lis.append(request.POST['n6'])
    lis.append(request.POST['n7'])
    lis.append(request.POST['n8'])
    lis.append(request.POST['n9'])


    
    result = model.predict([lis])
    print(result)
    if result ==[1]:
        result2 = "MALIGNANT"
        
    else:
        result2 = "BENIGN"

    return render(request,"result.html",{'result2':result2})




