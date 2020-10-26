from django import forms
from django.core.exceptions import ValidationError

from app.models import Winner, PUser


class CheckForm(forms.Form):
    case_number = forms.CharField(required=True, error_messages={'required': 'The Case Number is required.'})
    # birth = forms.DateField(required=True, error_messages={'required': 'The Applicant\'s date of birth is invalid.'})
    confirm = forms.CharField(required=True, error_messages={
        'required': 'The Electronic Diversity Visa Confirmation Number is required.'})
    status = forms.CharField(required=True,
                             error_messages={
                                 'required': "Please indicate your role on the case by selecting an item from the 'I am the' dropdown list."})
    captcha = forms.CharField(widget=forms.Textarea(), required=True,
                              error_messages={
                                  'required': "The characters you entered did not match the characters displayed in the box. Please try again."})

    def clean_confirm(self):
        case_number = self.cleaned_data.get('case_number')
        data = Winner.objects.filter(case_number=case_number).exists()

        if not data:
            raise ValidationError('The Case Number is invalid.')
        return case_number
    #
    # def clean_birth(self):
    #     day = self.cleaned_data.get('day')
    #     month = self.cleaned_data.get('month')
    #     year = self.cleaned_data.get('year')

    # class Meta:
    #     model = PUser
    #     fields = ['confirm', 'name', 'birth', 'captcha']


class CheckLogin(forms.Form):
    case_number = forms.CharField(required=True, error_messages={'required': 'The Case Number is required.'})

    def clean_case_number(self):
        case_number = self.cleaned_data.get('case_number')
        data = Winner.objects.filter(case_number__exact=case_number).exists()

        if not data:
            raise ValidationError('The Case Number is invalid.')
        return case_number


class EnterInformationForm(forms.Form):
    confirm = forms.CharField(required=True, error_messages={'required': 'Confirmation Number is required.'})
    lastname = forms.CharField(required=True, error_messages={'required': 'You must provide a valid Last/Family Name'})
    birth = forms.IntegerField(required=True, error_messages={'required': 'Year of Birth is required'})
    captcha = forms.CharField(widget=forms.Textarea(), required=True,
                              error_messages={'required': 'Please enter the code as you see or hear it.'})
    org_captcha = forms.CharField(required=False, show_hidden_initial=True)

    def clean_confirm(self):
        confirm = self.cleaned_data.get('confirm')
        data = PUser.objects.filter(confirm_number__exact=confirm).exists()

        if not data:
            raise ValidationError('The information entered is not valid.')
        return confirm

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
