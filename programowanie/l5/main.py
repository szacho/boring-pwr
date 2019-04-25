import kivy, requests, json
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.core.window import Window
Window.size = (310, 500)

class ChooseCurrency(Button):
    types = ListProperty()
    selected = StringProperty(None)
    def __init__(self, **kwargs):
        super(ChooseCurrency, self).__init__(**kwargs)
        self.drop_list = DropDown()

        self.bind(on_release=self.drop_list.open)
        self.drop_list.bind(on_select=self.handleSelect)

    def handleSelect(self, instance, value):
        setattr(self, 'text', value)
        self.selected = value

    def renderList(self):
        for i in self.types:
            btn = Button(text=i, size_hint_y=None, height=45)
            btn.bind(on_release=lambda btn: self.drop_list.select(btn.text))
            self.drop_list.add_widget(btn)

    def on_types(self, instance, value):
        self.renderList()

class Converter(BoxLayout):
    convert_value_input = ObjectProperty()
    from_currency_dropdown = ObjectProperty()
    to_currency_dropdown = ObjectProperty()
    values = ObjectProperty()
    converted_label = ObjectProperty()

    def show_message(self, msg):
        self.converted_label.text = str(msg)

    def validate(self, value):
        try:
            return True, float(value)
        except:
            return False, "Provide a number."

    def convert(self, value):
        val = self.validate(value)
        if val[0]:
            from_ = self.from_currency_dropdown.selected
            to_ = self.to_currency_dropdown.selected
            if not all([from_, to_]):
                self.show_message("Choose currencies.")
            else:
                v = self.values[from_]/self.values[to_]*val[1]
                self.show_message(f'{val[1]} {from_} = {round(v, 2)} {to_}')
        else:
            self.show_message(val[1])

    def set_data(self, data):
        self.values = { rate['code']:rate['mid'] for rate in data[0]['rates'] }
        self.values['PLN'] = 1.0
        listOfTypes = list(self.values.keys())
        self.from_currency_dropdown.types = listOfTypes
        self.to_currency_dropdown.types = listOfTypes

    def save_data(self, data):
        with open('nbprates.json', 'w') as json_file:
            json.dump(data, json_file)

    def load_from_file(self):
        try:
            with open('nbprates.json', 'r') as json_file:
                data = json.loads(json_file.read())
                self.set_data(data)
        except:
            self.show_message("No data, sorry.")

    def fetch_data(self):
        try:
            data = requests.get('http://api.nbp.pl/api/exchangerates/tables/A?format=json').json()
            self.save_data(data)
            self.set_data(data)
        except:
            self.load_from_file()

class ConverterApp(App):
    def build(self):
        conv = Converter()
        conv.fetch_data()
        return conv



if __name__ == '__main__': ConverterApp().run()
