import json
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField


class programaIAR(MDApp):
	with open('data.json') as file:
		data = json.load(file)

	def open_x (self):
		x = self.data["x"]
		return x	

	def open_y (self):
		y = self.data["y"]
		return y

	def save(self):
		with open('data.json', 'w') as file:
	 		json.dump(self.data, file)

	def build (self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Blue"
		self.text_x = self.open_x()
		self.text_y = self.open_y()
		return Builder.load_file('pantallaPrin.kv')

		


programaIAR().run()
