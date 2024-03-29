import json
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField


class programaIAR(MDApp):
	#Descomprime el archivo data.json y coloca la información dentro de la variable 'data'
	with open('data.json') as file:
		data = json.load(file)

	#Toma el valor, ya sea de 'x' o de 'y', que hay dentro de la variable de 'data' y lo coloca dentro de la variable 'direction'
	def open_direction (self, direction):
		direction = self.data[direction]
		return direction

	#Guarda los valores colocados por el usuario, los ingresa en la variable 'data' y lo comprime nuevamente como data.json
	def save(self):
		if (self.root.ids.cambio_x.text == "" and self.root.ids.cambio_y.text == ""):
			self.data["x"] = self.root.ids.pos_x.text
			self.data["y"] = self.root.ids.pos_y.text
			with open('data.json', 'w') as file:
				json.dump(self.data, file)
		else:
			self.data["x"] = self.root.ids.cambio_x.text
			self.data["y"] = self.root.ids.cambio_y.text
			with open('data.json', 'w') as file:
				json.dump(self.data, file)
	
	#Agrega a la Asención Recta el valor ingresados en la casilla de grados, limitándolo en los 180º
	def mod_x_add(self):
		calculo = str(int(self.root.ids.pos_x.text) + int(self.root.ids.grados.text))
		if (int(self.root.ids.pos_x.text) >= 0 and int(self.root.ids.pos_x.text) < 180):
			if (int(calculo) <= 180):
				self.root.ids.pos_x.text = calculo
			else:
				self.root.ids.pos_x.text = "180"
		
		elif (int(self.root.ids.pos_x.text) > 180):
			self.root.ids.pos_x.text = "180"
			
		elif (int(self.root.ids.pos_x.text) < 0):
			self.root.ids.pos_x.text = "0"

	#Resta a la Asención Recta el valor ingresados en la casilla de grados, limitándolo en los 0º
	def mod_x_remove(self):
		calculo = str(int(self.root.ids.pos_x.text) - int(self.root.ids.grados.text))
		if (int(self.root.ids.pos_x.text) > 0 and int(self.root.ids.pos_x.text) <= 180):
			if (int(calculo) >= 0):
				self.root.ids.pos_x.text = calculo
			else:
				self.root.ids.pos_x.text = "0"
		
		elif (int(self.root.ids.pos_x.text) > 180):
			self.root.ids.pos_x.text = "180"
			
		elif (int(self.root.ids.pos_x.text) < 0):
			self.root.ids.pos_x.text = "0"
			
	#Agrega a la Declinación el valor ingresados en la casilla de grados, limitándolo en los 90º
	def mod_y_add(self):
		calculo = str(int(self.root.ids.pos_y.text) + int(self.root.ids.grados.text))
		if (int(self.root.ids.pos_y.text) >= 0 and int(self.root.ids.pos_y.text) < 90):
			if (int(calculo) <= 90):
				self.root.ids.pos_y.text = calculo
			else:
				self.root.ids.pos_y.text = "90"
				
		elif (int(self.root.ids.pos_y.text) > 90):
			self.root.ids.pos_y.text = "90"
			
		elif (int(self.root.ids.pos_y.text) < 0):
			self.root.ids.pos_y.text = "0"		
	
	#Resta a la Declinación el valor ingresados en la casilla de grados, limitándolo en los 0º
	def mod_y_remove(self):
		calculo = str(int(self.root.ids.pos_y.text) - int(self.root.ids.grados.text))
		if (int(self.root.ids.pos_y.text) > 0 and int(self.root.ids.pos_y.text) <= 90):
			if (int(calculo) >= 0):
				self.root.ids.pos_y.text = calculo
			else:
				self.root.ids.pos_y.text = "0"

		elif (int(self.root.ids.pos_y.text) > 90):
			self.root.ids.pos_y.text = "90"
			
		elif (int(self.root.ids.pos_y.text) < 0):
			self.root.ids.pos_y.text = "0"
	
	#Realiza la conexión entre el archivo programaIAR.py y pantallaPrin.kv
	def build (self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "BlueGray"
		self.text_x = self.open_direction("x")
		self.text_y = self.open_direction("y")
		return Builder.load_file('pantalla.kv')

		


programaIAR().run()
