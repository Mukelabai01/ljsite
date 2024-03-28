from django import forms

class ProductForm(forms.Form):
    size_choices = [
        ('A5', 'A5'),
        ('A4', 'A4'),
        ('A3', 'A3'),
        ('A2', 'A2'),
    ]
    size = forms.ChoiceField(choices=size_choices)
    shipping_address = forms.CharField(max_length=100)