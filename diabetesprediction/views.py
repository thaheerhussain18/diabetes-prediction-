from django.shortcuts import render
from joblib import load
model = load('./savedModels/Di_model.joblib')

def predictor(request):
    return render(request,"main.html")

def formInfo(request):
    Pregnancies=int(request.GET.get("Pregnancies"))
    Glucose=int(request.GET.get("Glucose"))
    BloodPressure=int(request.GET.get("BloodPressure"))
    SkinThickness=int(request.GET.get("SkinThickness"))
    Insulin=float(request.GET.get("Insulin"))
    BMI=float(request.GET.get("BMI"))
    DiabetesPedigreeFunction=float(request.GET.get("DiabetesPedigreeFunction"))
    
    Age=int(request.GET.get("Age"))
    y_pred=model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    z=''
    if y_pred[0]==1:
        z+="diabetic"
    else:
        z+="non-diabetic"
    
    return render(request,"result.html",{'result':z})



 