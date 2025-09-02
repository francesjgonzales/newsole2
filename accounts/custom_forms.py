from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    phone_number = forms.CharField(max_length=15, required=False)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea, required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.phone_number = self.cleaned_data.get('phone_number')
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.address = self.cleaned_data.get('address')
        user.save()
        return user
