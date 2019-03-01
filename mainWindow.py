from PySide2 import QtWidgets



class MainWindow( QtWidgets.QMainWindow ):
	def __init__( self ):
		super( MainWindow, self ).__init__()
		# create a central widget in main window
		self.centralWidget = QtWidgets.QWidget( self )
		self.setCentralWidget( self.centralWidget )
		# create a layout for central widget
		self.layout = QtWidgets.QGridLayout( self.centralWidget )

		self.historyBox = QtWidgets.QPlainTextEdit( self.centralWidget )
		self.layout.addWidget( self.historyBox, 0, 0, -1, 1)
		self.historyBox.setFixedSize( 150, 150 )

		self.textBox = QtWidgets.QLineEdit( self.centralWidget )
		self.layout.addWidget( self.textBox, 0, 1, 1, 1 )

		self.datatextBox = QtWidgets.QLabel( self.centralWidget )
		self.layout.addWidget( self.datatextBox, 1, 1, 1, 1 )

		# parent of closeButton should be centralWidget, since the button should be in
		self.closeButton = QtWidgets.QPushButton( self.centralWidget )
		self.layout.addWidget( self.closeButton, 2, 1, 1, 1 )


		self.initSignalsAndSlots()

		self._setName()


	def initSignalsAndSlots( self ):
		self.historyBox.setReadOnly(True)
		# self.showMessage implemented at below
		self.textBox.editingFinished.connect( self.showAnswer )
		# self.close is a built-in method that close the main window
		self.closeButton.clicked.connect( self.close )



	def _setName( self ):
		# this is for setText of the buttons
		self.textBox.setText( 'Enter a number' )
		self.closeButton.setText( 'Close' )



	def showAnswer( self ):
		def factorial(n):
			answer = 1
			while n>1:
				answer *= n
				n -= 1
			return answer
		try:
			number = self.textBox.text()
			answer = str(factorial(int(number)))
			self.datatextBox.setText( "Answer: \n"+number+"!="+answer )
			self.historyBox.appendPlainText( number+"!="+answer )
		except:
			self.datatextBox.setText( 'Please type in an integer!' )
