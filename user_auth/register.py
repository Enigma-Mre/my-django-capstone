from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    """
    A form for user registration.

    This form allows users to create a new account by providing a username, email,
    and password. It includes validation to ensure that the passwords match.

    Attributes:
        password (CharField): The password input field, rendered as a password input.
        password_confirm (CharField): A confirmation password input field, also rendered as a password input.
    """
    
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        """
        Validate the form data.

        This method checks if the two password fields match. If they do not match,
        a ValidationError is raised.

        Returns:
            dict: A dictionary of cleaned data.
        
        Raises:
            ValidationError: If the passwords do not match.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
