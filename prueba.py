import json
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField

class prueba(MDApp):
	def mod(self):
		if (self.root.ids.text3.text > "0"):
			self.root.ids.text3.text = str(int(self.root.ids.text1.text) + 1)

	def build (self):
		return Builder.load_file('prueba.kv')	
		
prueba().run()



