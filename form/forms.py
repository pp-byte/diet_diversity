from django import forms
from .send_list import get_list
recipe=get_list()

list=list(range(1,30))
choice=[('','Select'),
("pieces","pieces"),
("vati/katori","vati/katori"),
("cup","cup"),
("tablespoon","tablespoon"),
("glass","glass"),
("teaspoon","teaspoon"),
]

cons=[
    ("thick","thick"),
    ("normal","normal"),
    ("thin","thin")

]
class chkform(forms.Form):
    # age_when_last_weighed = forms.FloatField(label='Previous Age (in weeks)', max_value=100)
    # previous_weight = forms.FloatField(label= 'Previous Weight (in kg) ', max_value=100)
    # weight_at_birth = forms.FloatField(label= 'Weight at Birth (in kg) ', max_value=100)
    recipe_name = forms.CharField(label='Select Dish', widget=forms.Select(choices=recipe))
    daily_freq = forms.IntegerField(label='Daily Frequency')
    weekly_freq = forms.IntegerField(label='Daily Frequency')
    monthly_freq = forms.IntegerField(label='Daily Frequency')
    quan=forms.IntegerField(label='Quantity')
    unit=forms.CharField(label='Measuring Unit',widget=forms.Select(choices=choice))
    remark=forms.CharField(label='Remarks')
    consistency=forms.CharField(label='Consistency',widget=forms.RadioSelect(choices=cons))
    op=forms.CharField(label='op')