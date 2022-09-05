from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker


class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('ScreenPicker.kv')

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.open()


Test().run()