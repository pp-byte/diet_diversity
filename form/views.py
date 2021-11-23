from django.shortcuts import render
# Create your views here.
from form.models import table


def index(request):
    if request.method=="POST":
        print("this is post")
        Recipe_List=request.POST['Recipe_List']
        Frequency_Days=request.POST['Frequency_Days']
        Frequency_Weeks=request.POST['Frequency_Weeks']
        Frequency_Months=request.POST['Frequency_Months']
        Amount=request.POST['Amount']
        Amount_Measure=request.POST['Amount_Measure']
        Consistency=request.POST['Consistency']
        Remark=request.POST['Remark']
        Tabular=table(Recipe_List=Recipe_List,Frequency_Days=Frequency_Days,Frequency_Weeks=Frequency_Weeks,Frequency_Months=Frequency_Months,Amount_Measure=Amount_Measure,Amount=Amount,Consistency=Consistency,Remark=Remark)
        Tabular.save()
    return render(request,'index.html')
