import json
from django.shortcuts import render
from .forms import ImageForm
from wagtail.core.telepath import JSContext


def index(request):
    form = ImageForm()

    js_context = JSContext()
    packed_form = js_context.pack(form)

    return render(request, 'formdata/index.html', {
        'form': form,
        'form_json': json.dumps(packed_form, indent=4),
        'media': form.media + js_context.media,
    })
