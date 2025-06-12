from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class BybitBot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="Bybit Trading Bot"))

        self.symbol_input = TextInput(hint_text="Symbol (e.g. ADAUSDT)", multiline=False)
        self.add_widget(self.symbol_input)

        self.status = Label(text="Status: Idle")
        self.add_widget(self.status)

        self.trade_btn = Button(text="Start Trading")
        self.trade_btn.bind(on_press=self.start_trading)
        self.add_widget(self.trade_btn)

    def start_trading(self, instance):
        symbol = self.symbol_input.text.upper()
        if symbol:
            self.status.text = f"Trading started for {symbol}"
        else:
            self.status.text = "Please enter a symbol"

class BybitApp(App):
    def build(self):
        return BybitBot()

if __name__ == '__main__':
    BybitApp().run()
