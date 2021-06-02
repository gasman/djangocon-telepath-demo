from django.shortcuts import render

from .forms import AddressForm, VoucherCodeFormSet


def order_form(request):
    address_form = AddressForm(prefix='address')
    voucher_code_formset = VoucherCodeFormSet(prefix='vouchers')
    return render(request, 'order_form.html', {
        'address_form': address_form,
        'voucher_code_formset': voucher_code_formset,
    })
