
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("my pyQt app")
		self.setLayout(qtw.QVBoxLayout())
		self.setUI()
		self.temps_nums = []
		self.fin_nums = []

		self.show()

	def setUI(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		# create the buttons
		self.input_result = qtw.QLineEdit()
		btn_result = qtw.QPushButton('Résultat', clicked = self.result)
		btn_clear = qtw.QPushButton('Effacer', clicked = self.clear)

		btn_1 = qtw.QPushButton('1', clicked = lambda: self.numbers('1'))
		btn_2 = qtw.QPushButton('2', clicked = lambda: self.numbers('2'))
		btn_3 = qtw.QPushButton('3', clicked = lambda: self.numbers('3'))
		btn_4 = qtw.QPushButton('4', clicked = lambda: self.numbers('4'))
		btn_5 = qtw.QPushButton('5', clicked = lambda: self.numbers('5'))
		btn_6 = qtw.QPushButton('6', clicked = lambda: self.numbers('6'))
		btn_7 = qtw.QPushButton('7', clicked = lambda: self.numbers('7'))
		btn_8 = qtw.QPushButton('8', clicked = lambda: self.numbers('8'))
		btn_9 = qtw.QPushButton('9', clicked = lambda: self.numbers('9'))
		btn_0 = qtw.QPushButton('0', clicked = lambda: self.numbers('0'))
		
		btn_plus = qtw.QPushButton('+', clicked = lambda: self.operators('+'))
		btn_min = qtw.QPushButton('-', clicked = lambda: self.operators('-'))
		btn_div = qtw.QPushButton('/', clicked = lambda: self.operators('/'))
		btn_mult = qtw.QPushButton('x', clicked = lambda: self.operators('*'))
		


		# add buttons to layout
		container.layout().addWidget(btn_7,0, 0 )
		container.layout().addWidget(btn_8,0, 1 )
		container.layout().addWidget(btn_9,0, 2 )
		container.layout().addWidget(btn_plus,0, 3 )

		container.layout().addWidget(btn_4,1, 0 )
		container.layout().addWidget(btn_5,1, 1 )
		container.layout().addWidget(btn_6,1, 2 )
		container.layout().addWidget(btn_min,1, 3 )

		container.layout().addWidget(btn_1,2, 0 )
		container.layout().addWidget(btn_2,2, 1 )
		container.layout().addWidget(btn_3,2, 2 )
		container.layout().addWidget(btn_div,2, 3 )

		container.layout().addWidget(btn_0,3,0 )
		container.layout().addWidget(btn_mult,3,3 )

		container.layout().addWidget(self.input_result,4,0, 1, 2 )
		container.layout().addWidget(btn_result,4, 2 )
		container.layout().addWidget(btn_clear,4, 3 )

		self.layout().addWidget(container)
	
	#def onClick(self):
	#	qtw.QMessageBox.about(self, "HELLO", "test")
	def numbers(self,key_number):
		self.temps_nums.append(key_number)
		temp_string = ''.join(self.temps_nums)
		if self.fin_nums:
			self.input_result.setText(''.join(self.fin_nums) + temp_string)
		else:
			self.input_result.setText(temp_string)

	def operators(self, operator):
		temp_string = ''.join(self.temps_nums)
		self.fin_nums.append(temp_string)
		self.fin_nums.append(operator)
		self.temps_nums = []
		self.input_result.setText(''.join(self.fin_nums))

	def result(self):
		fin_string = ''.join(self.fin_nums) + ''.join(self.temps_nums)
		result_string = eval(fin_string)
		fin_string += '='
		fin_string += str(result_string)
		self.input_result.setText(fin_string)
	
	def clear(self):
		self.input_result.clear()
		self.temps_nums = []
		self.fin_nums = []

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
