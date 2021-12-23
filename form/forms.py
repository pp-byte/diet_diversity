import io
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# from form.views import new_recipe
from .models import  UploadWellPictureModel, new_item,table
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from csv import writer
from django import forms
import pandas as pd
from .send_list import get_list
recipe=get_list()
lists=list(range(1,30))
choice=[('','Select'),
("pieces","pieces"),
("vati/katori","vati/katori"),
("cup","cup"),
("tablespoon","tablespoon"),
("glass","glass"),
("teaspoon","teaspoon"),
]

cons=[('','Select'),
    ("thick","thick"),
    ("normal","normal"),
    ("thin","thin")

]

# dish_name=['Grenn gram curry','Paneer masala','Jowar soya dosa with sesame seed powder']
# recipe={
#     'ground nut':1,

# }


class chkform(forms.ModelForm):
    # age_when_last_weighed = forms.FloatField(label='Previous Age (in weeks)', max_value=100)
    # previous_weight = forms.FloatField(label= 'Previous Weight (in kg) ', max_value=100)
    # weight_at_birth = forms.FloatField(label= 'Weight at Birth (in kg) ', max_value=100)
    recipe_name = forms.CharField(label='Select Item', widget=forms.Select(choices=recipe))
    daily_freq = forms.IntegerField(label='Daily Frequency')
    weekly_freq = forms.IntegerField(label='Weekly Frequency')
    monthly_freq = forms.IntegerField(label='Monthly Frequency')
    quan=forms.IntegerField(label='Quantity')
    unit=forms.CharField(label='Measuring Unit',widget=forms.Select(choices=choice))
    remark=forms.CharField(label='Remarks')
    # consistency=forms.CharField(label='Consistency',widget=forms.RadioSelect('cons'))
    consistency=forms.CharField(label='Consistency',widget=forms.Select(choices=cons))
    
    
    # dish_name=['Grenn gram curry','Paneer masala','Jowar soya dosa with sesame seed powder']
    
    # dish_name='Green gram curry'
    # def get_recipe(dish_name):
    #     for i in range(len(dish_name)):
    #         dish_name = dish_name.lower()
    #     recipe={}
    #     dfr=pd.read_csv('recipe.csv')
    #     df=dfr.copy()
    #     df['ingredient'] = df['ingredient'].str.strip()
    #     df['recipe'] = df['recipe'].str.strip()
    #     df['ingredient'] = df['ingredient'].str.lower()
    #     df['recipe'] = df['recipe'].str.lower()
    #     if dish_name in df['recipe'].values:
    #        for ind in df.index:
    #           if df['recipe'][ind]==dish_name:
    #             if df['measurement'][ind]=='g':
    #                 recipe[df['ingredient'][ind]]=df['quantity'][ind]/100
    #             elif df['measurement'][ind]=='tsp':
    #                 recipe[df['ingredient'][ind]]=df['quantity'][ind]*4.5/100
    #             elif df['measurement'][ind] == 'tbsp':
    #                 recipe[df['ingredient'][ind]] = df['quantity'][ind] * 13.5 / 100
    #             elif df['measurement'][ind] == 'cup':
    #                 recipe[df['ingredient'][ind]] = df['quantity'][ind] * 120 / 100
    #             elif df['measurement'][ind] == 'no':
    #                 recipe[df['ingredient'][ind]] = df['quantity'][ind]
    #     else:
    #        print('dish_name'+ ' not in recipe list')
    #        data=[[dish_name]]
    #        dataframe = pd.DataFrame(data)
    #        dataframe.to_csv("recipe_missing.csv", index=False, mode='a', header=False)
    #     return recipe
    # print(get_recipe(dish_name))

    # def cal(recipe):
    #   dfd = pd.read_csv('IYCF.csv')
    #   df=dfd.copy()
    #   cols = list(df.columns) # list of all columns in csv
    #   micro_list = []  # list of micro nutrients in csv
    #   for i in range(2, len(cols), 3):  
    #       micro_list.append(cols[i])
    #       df[cols[i-1]]=df[cols[i-1]].str.strip()
    #       df[cols[i - 1]] = df[cols[i - 1]].str.lower()
    #   print(len(micro_list))
    #   fin_val = {}  # dictionary to be returned
    #   for i in micro_list:
    #       fin_val[i] = 0
    #       # print(fin_val)
    #   food_name = recipe.keys()
    #   print(food_name)
    #   for i in range(1, len(cols), 3):
    #       for j in food_name:
    #           if j in df[cols[i]].values:
    #             # print('yes')
    #             val = int(df[df[cols[i]] == j][cols[i + 1]])
    #             val = val * recipe[j]
    #             fin_val[cols[i + 1]] += val
    #             # print(val)
    #           else:
    #             # print('no')
    #             data = [ [j,cols[i+1]],]
    #             dataframe = pd.DataFrame(data)
    #             dataframe.to_csv("ingredient_missing.csv", index=False, mode='a', header=False)
    #   return fin_val
    # print(cal(get_recipe(dish_name)))


    class Meta:
        model = table
        fields=('recipe_name','daily_freq','weekly_freq','monthly_freq','quan','unit','remark','consistency')
    


    # op=forms.CharField(label='op')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    check_me_out = forms.BooleanField(required=False)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('email', css_class='form-group col-md-6 mb-0'),
    #             Column('password', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #          'check_me_out',
    #         Submit('submit', 'Sign in')
    #     )
class chk(forms.Form):
    recipe_name = forms.CharField(label='New Item' ,widget=forms.TextInput(attrs={'placeholder': 'Add New Item'}))
    # data=[[new_recipe_name]]
    # dataframe = pd.DataFrame(data)
    # print(dataframe)
    # dataframe.to_csv("new_recipe.csv", index=False, mode='a', header=False)
    daily_freq = forms.IntegerField(label='Daily Frequency')
    weekly_freq = forms.IntegerField(label='Weekly Frequency')
    monthly_freq = forms.IntegerField(label='Monthly Frequency')
    quan=forms.IntegerField(label='Quantity')
    unit=forms.CharField(label='Measuring Unit',widget=forms.Select(choices=choice))
    remark=forms.CharField(label='Remarks')
    # consistency=forms.CharField(label='Consistency',widget=forms.RadioSelect('cons'))
    consistency=forms.CharField(widget=forms.Select(choices=cons))
    class Meta:
        model = new_item
        fields=('recipe_name','daily_freq','weekly_freq','monthly_freq','quan','unit','remark','consistency')
    # like_website = forms.TypedChoiceField(
    #     label = "Do you like this website?",
    #     choices = ((1, "Yes"), (0, "No") ,(2,"Other")),
    #     # coerce = lambda x: bool(int(x)),
    #     widget = forms.RadioSelect,
    #     initial = '1',
    #     required = True,
    # )

class UploadWellPictureForm(forms.ModelForm):
    class Meta:
        model = UploadWellPictureModel
        fields = ('picture','name','well_nm')

