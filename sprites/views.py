import json
from django.shortcuts import render

import telepath


@telepath.register
class Emoji:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def telepath_pack(self, context):
        context.add_media(js='js/sprites/emoji.js')
        return ('sprites.Emoji', [self.name, self.size])


@telepath.register
class Banner:
    def __init__(self, text, color):
        self.text = text
        self.color = color

    def telepath_pack(self, context):
        context.add_media(js='js/sprites/banner.js')
        return ('sprites.Banner', [self.text, self.color])


def index(request):
    sprites = [
        Emoji('rocket', 200),
        Emoji('heart', 100),
        Emoji('heart', 100),
        Emoji('heart', 100),
        Banner("Hello DjangoCon!", "purple"),
    ]
    js_context = telepath.JSContext()
    sprites_json = json.dumps(js_context.pack(sprites))
    return render(request, 'sprites.html', {
        'sprites_json': sprites_json,
        'media': js_context.media,
    })
