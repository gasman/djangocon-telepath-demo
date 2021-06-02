from django.db import models

from django import forms
from wagtail.core.telepath import Adapter, register

class FormAdapter(Adapter):
    def pack(self, obj, context):
        context.add_media(js='js/formdata.js')
        return ('wagtail.forms.Form', [obj.fields])


register(FormAdapter(), forms.Form)


class FieldAdapter(Adapter):
    def pack(self, obj, context):
        context.add_media(js='js/formdata.js')
        return ('wagtail.forms.Field', [obj.widget])


register(FieldAdapter(), forms.Field)
