from django import forms


class PasswordGenForm(forms.Form):
    password_length = forms.ChoiceField(
        choices=((str(x), x) for x in range(4,101))
    )
    has_lower = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'checked':True}
        )
    )
    has_upper = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'checked':True}
        )
    )
    has_digit = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'checked':True}
        )
    )
    has_punctuation = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'checked':True}
        )
    )