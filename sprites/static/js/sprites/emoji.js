EMOJI_BY_NAME = {
    'rocket': '🚀',
    'heart': '❤️',
    'smile': '🙂',
    'rainbow': '🌈',
}

class Emoji {
    constructor(name, size) {
        this.element = document.createElement('div');
        this.element.innerText = EMOJI_BY_NAME[name];
        this.element.style.fontSize = '' + size + 'px';
        this.element.style.position = 'absolute';
        document.body.appendChild(this.element);
    }
    animate() {
        let x = Math.random() * 800;
        let y = Math.random() * 400;
        let dx = Math.random() * 10; let dy = Math.random() * 10;
        const step = () => {
            x += dx; y += dy;
            if (x > 800) dx = -Math.abs(dx);
            if (x <= 0) dx = Math.abs(dx);
            if (y > 400) dy = -Math.abs(dy);
            if (y <= 0) dy = Math.abs(dy);
            this.element.style.left = '' + x + 'px';
            this.element.style.top = '' + y + 'px';
        }
        setInterval(step, 20);
    }
}
telepath.register('sprites.Emoji', Emoji)
