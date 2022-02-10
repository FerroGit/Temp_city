from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest


class TrovaTemperatura(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        Window.size = (360, 640)

        self.window.add_widget(Image(source = "logo.png"))

        self.input_text = TextInput(
            size_hint = (1, 0.2),
            font_size = "30sp",
            padding = "5sp",
            halign = "center"
        )
        self.window.add_widget(self.input_text)

        self.input_button = Button(
            text = "CERCA",
            size_hint = (1, 0.2),
            bold = True,
            background_color = "#01affe"
        )
        self.window.add_widget(self.input_button)
        self.input_button.bind(on_press = self.find_temp)


        self.input_label = Label(
            text = "SEARCH FOR A CITY",
            font_size="20sp",
            color = "#01affe"
        )
        self.window.add_widget(self.input_label)

        return self.window


    def find_temp(self, instance):
        def edit_label(request, result):
            temp = result['main']['temp']
            country = result['sys']['country']
            self.input_label.text = f"Oggi a {self.input_text.text}({country}) ci sono {temp} °C"

        link = f"https://api.openweathermap.org/data/2.5/weather?q={self.input_text.text}&appid=80caba22e6ecd64b8aead788f2a58c0c&units=metric"
        UrlRequest(link, edit_label)

TrovaTemperatura().run()