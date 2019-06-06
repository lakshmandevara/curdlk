from django import forms
class InsertingDataForm(forms.Form):
    Product_Id=forms.IntegerField(
        label='Enter Your Product Id',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Productid'
            }

        )

    )
    Product_Name=forms.CharField(
        label='Enter Your Product Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Product Name'
            }
        )
    )
    Product_Cost=forms.IntegerField(
        label='Enter Your Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Product Cost'
            }

        )
    )
    Product_Color=forms.CharField(
        label='Enter Your Product Color',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    Product_Class=forms.CharField(
        label='Enter Your Product Class',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    Customer_Name=forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Name'
            }
        )
    )
    Customer_Mobile=forms.IntegerField(
        label='Enter Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    Customer_Email=forms.EmailField(
        label='Enter Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )

    )
class UpdatingDataForm(forms.Form):
    Product_Id = forms.IntegerField(
        label='Enter Your Product Id',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Productid'
            }

        )

    )
    Product_Cost = forms.IntegerField(
        label='Enter Your Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Product Cost'
            }

        )
    )
class DeletingDataForm(forms.Form):
    Product_Id = forms.IntegerField(
        label='Enter Your Product Id',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Productid'
            }

        )

    )

