from django.shortcuts import render
from .forms import chkform
# Create your views here.
from .models import table


def index(request):
    data=request
    print(data.GET.keys())
    print(data.POST.keys())
    if request.method=="POST":
        print("this is post")
        print(data.POST['op'])
       # print(request.POST['tab'])

        # if request.POST.get('submit'):
        #     print(request.POST.get('table'))
        # Recipe_List=request.POST['Recipe_List']
        # Frequency_Days=request.POST['Frequency_Days']
        # Frequency_Weeks=request.POST['Frequency_Weeks']
        # Frequency_Months=request.POST['Frequency_Months']
        # Amount=request.POST['Amount']
        # Amount_Measure=request.POST['Amount_Measure']
        # Consistency=request.POST['Consistency']
        # Remark=request.POST['Remark']
        # Tabular=table(Recipe_List=Recipe_List,Frequency_Days=Frequency_Days,Frequency_Weeks=Frequency_Weeks,Frequency_Months=Frequency_Months,Amount_Measure=Amount_Measure,Amount=Amount,Consistency=Consistency,Remark=Remark)
        #
        #     print(Recipe_List)
        #     print(Tabular)
        #
        # Tabular.save()
    form=chkform()
    return render(request,'index.html',{'form':form})
