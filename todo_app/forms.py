from django import forms

class TodoForm(forms.Form):
	text = forms.CharField(max_length=90,
		widget=forms.TextInput(attrs={
			'class' : 'form-control',
			'placeholder':'Enter task',
			'aria-label':'Todo',
			'aria-describedby':'add-btn',
			}))	