$(() => {
    const stateContainer = $('.container-state');
    const countryField = $('#id_address-country');
    const updateStateVisibility = () => {
        const country = countryField.val();
        if (country == '' || country == 'US') {
            stateContainer.slideDown('fast');
        } else {
            stateContainer.slideUp('fast');
        }
    }
    countryField.on('change', updateStateVisibility);
    updateStateVisibility();

    const voucherCodeFormCount = $('#id_vouchers-TOTAL_FORMS');
    const voucherCodeList = $('#voucher-codes');
    const voucherCodeFormTemplate = $('#voucher-code-form-template').text();
    $('#add-voucher-code').on('click', () => {
        const newFormIndex = parseInt(voucherCodeFormCount.val());
        voucherCodeFormCount.val(newFormIndex + 1);
        const newFormHtml = voucherCodeFormTemplate.replaceAll('__prefix__', newFormIndex);
        const newFormLi = $('<li></li>').html(newFormHtml);
        voucherCodeList.append(newFormLi);
        newFormLi.hide().slideDown('fast');
    })
});
