class Form {
    constructor(fields) {
        this.fields = fields;
        this.widgets = {};
        for (let fieldName in this.fields) {
            this.widgets[fieldName] = this.fields[fieldName].widget.bind(
                document.body, fieldName, 'id_' + fieldName
            )
        }
    }

    getState() {
        const result = {};
        for (let name in this.widgets) {
            result[name] = this.widgets[name].getState()
        }
        return result;
    }

    setState(newState) {
        for (let name in this.widgets) {
            this.widgets[name].setState(newState[name])
        }
    }
}
telepath.register('wagtail.forms.Form', Form)

class Field {
    constructor(widget) {
        this.widget = widget
    }
}
telepath.register('wagtail.forms.Field', Field)
