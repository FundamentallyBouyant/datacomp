from django import forms
from mainapp.models import Profile

class UserProfileForm(forms.ModelForm):
	first_name = forms.CharField(label='First name', max_length=30)
	last_name = forms.CharField(label = 'Last name', max_length=30)
	college = forms.CharField(max_length=100,required=True)

	batch = forms.CharField(max_length=20,required=True)
	def __init__(self, *args, **kw):
		super(UserProfileForm, self).__init__(*args, **kw)
		self.fields['first_name'].initial = self.instance.user.first_name
		self.fields['last_name'].initial = self.instance.user.last_name
		self.fields['college'].initial = self.instance.user.college
		self.fields['batch'].initial = self.instance.user.batch
		self.fields.keyOrder = [
			'first_name',
			'last_name',
			'college'
			'batch'
			]

	def save(self, *args, **kw):
		super(UserProfileForm, self).save(*args, **kw)
		self.instance.user.first_name = self.cleaned_data.get('first_name')
		self.instance.user.last_name = self.cleaned_data.get('last_name')
		self.instance.user.college = self.cleaned_data.get('college')
		self.instance.user.batch = self.cleaned_data.get('batch')
		self.instance.user.save()

	class Meta:
		model = Profile
		fields = "__all__" 