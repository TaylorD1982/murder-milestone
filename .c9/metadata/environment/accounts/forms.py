{"filter":false,"title":"forms.py","tooltip":"/accounts/forms.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":7,"column":58},"action":"insert","lines":["from django import forms","","","class UserLoginForm(forms.Form):","    \"\"\"Form to be used to log users in\"\"\"","","    username = forms.CharField()","    password = forms.CharField(widget=forms.PasswordInput)"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":7,"column":58},"action":"remove","lines":["from django import forms","","","class UserLoginForm(forms.Form):","    \"\"\"Form to be used to log users in\"\"\"","","    username = forms.CharField()","    password = forms.CharField(widget=forms.PasswordInput)"],"id":2},{"start":{"row":0,"column":0},"end":{"row":23,"column":64},"action":"insert","lines":["from django import forms","from django.contrib.auth.models import User","from django.contrib.auth.forms import UserCreationForm","from django.core.exceptions import ValidationError","","","class UserLoginForm(forms.Form):","    \"\"\"Form to be used to log users in\"\"\"","","    username = forms.CharField()","    password = forms.CharField(widget=forms.PasswordInput)","","","class UserRegistrationForm(UserCreationForm):","    \"\"\"Form used to register a new user\"\"\"","","    password = forms.CharField(widget=forms.PasswordInput)","    password2 = forms.CharField(","        label=\"Password Confirmation\",","        widget=forms.PasswordInput)","    ","    class Meta:","        model = User","        fields = ['email', 'username', 'password1', 'password2']"]}],[{"start":{"row":0,"column":0},"end":{"row":23,"column":64},"action":"remove","lines":["from django import forms","from django.contrib.auth.models import User","from django.contrib.auth.forms import UserCreationForm","from django.core.exceptions import ValidationError","","","class UserLoginForm(forms.Form):","    \"\"\"Form to be used to log users in\"\"\"","","    username = forms.CharField()","    password = forms.CharField(widget=forms.PasswordInput)","","","class UserRegistrationForm(UserCreationForm):","    \"\"\"Form used to register a new user\"\"\"","","    password = forms.CharField(widget=forms.PasswordInput)","    password2 = forms.CharField(","        label=\"Password Confirmation\",","        widget=forms.PasswordInput)","    ","    class Meta:","        model = User","        fields = ['email', 'username', 'password1', 'password2']"],"id":4},{"start":{"row":0,"column":0},"end":{"row":44,"column":24},"action":"insert","lines":["from django import forms","from django.contrib.auth.models import User","from django.contrib.auth.forms import UserCreationForm","from django.core.exceptions import ValidationError","","","class UserLoginForm(forms.Form):","    \"\"\"Form to be used to log users in\"\"\"","","    username = forms.CharField()","    password = forms.CharField(widget=forms.PasswordInput)","","","class UserRegistrationForm(UserCreationForm):","    \"\"\"Form used to register a new user\"\"\"","","    password1 = forms.CharField(","        label=\"Password\",","        widget=forms.PasswordInput)","    password2 = forms.CharField(","        label=\"Password Confirmation\",","        widget=forms.PasswordInput)","    ","    class Meta:","        model = User","        fields = ['email', 'username', 'password1', 'password2']","    ","    def clean_email(self):","        email = self.cleaned_data.get('email')","        username = self.cleaned_data.get('username')","        if User.objects.filter(email=email).exclude(username=username):","            raise forms.ValidationError(u'Email address must be unique')","        return email","","    def clean_password2(self):","        password1 = self.cleaned_data.get('password1')","        password2 = self.cleaned_data.get('password2')","","        if not password1 or not password2:","            raise ValidationError(\"Please confirm your password\")","        ","        if password1 != password2:","            raise ValidationError(\"Passwords must match\")","        ","        return password2"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":0},"end":{"row":5,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"start","mode":"ace/mode/python"}},"timestamp":1585916894093,"hash":"33192e9c2c672271a969f7afd93bb2e4bacd99db"}