from django import forms


class AddressForm(forms.Form):
    name = forms.CharField()
    street = forms.CharField()
    city = forms.CharField()
    state = forms.ChoiceField(required=False, choices=[
        ('', '---'),
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
    ])
    country = forms.ChoiceField(choices=[
        ('', '---'),
        ('FR', 'France'),
        ('DE', 'Germany'),
        ('UK', 'United Kingdom'),
        ('US', 'United States'),
    ])


class VoucherCodeForm(forms.Form):
    voucher_code = forms.CharField()


VoucherCodeFormSet = forms.formset_factory(VoucherCodeForm)
