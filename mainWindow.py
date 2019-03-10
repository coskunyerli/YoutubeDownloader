from PySide2 import QtWidgets



class MainWindow( QtWidgets.QMainWindow ):
	def __init__( self ):
		super( MainWindow, self ).__init__()
		# create a central widget in main window
		self.centralWidget = QtWidgets.QWidget( self )
		self.setCentralWidget( self.centralWidget )
		# create a layout for central widget
		self.layout = QtWidgets.QGridLayout( self.centralWidget )

		self.historyBox = QtWidgets.QListWidget( self.centralWidget )
		self.layout.addWidget( self.historyBox, 0, 0, -1, 1)
		self.historyBox.setFixedSize( 150, 150 )

		self.textBox = QtWidgets.QLineEdit( self.centralWidget )
		self.layout.addWidget( self.textBox, 0, 1, 1, 1 )

		self.datatextBox = QtWidgets.QLineEdit( self.centralWidget )
		self.layout.addWidget( self.datatextBox, 1, 1, 1, 1 )
		self.datatextBox.setFixedSize( 150, 89 )

		# parent of closeButton should be centralWidget, since the button should be in
		self.closeButton = QtWidgets.QPushButton( self.centralWidget )
		self.layout.addWidget( self.closeButton, 2, 1, 1, 1 )

		self.historyBox.itemClicked.connect( self.msgBox )

		self.initSignalsAndSlots()

		self._setName()


	def initSignalsAndSlots( self ):
		# self.showMessage implemented at below
		self.textBox.returnPressed.connect( self.showAnswer )
		# self.close is a built-in method that close the main window
		self.closeButton.clicked.connect( self.close )
		self.datatextBox.setReadOnly( True )

	def _setName( self ):
		# this is for setText of the buttons
		self.textBox.setPlaceholderText( 'Enter a number' )
		self.closeButton.setText( 'Close' )

	def msgBox( self ):
		item = self.historyBox.currentItem()
		num = item.text()
		separate = num.find("!")
		ans = int( num[:separate] )
		recal = self.factorial( ans )
		QtWidgets.QMessageBox.about( self, "Full Answer", num[:separate]+"!=" + str( recal ) )

	def factorial( self, n ):
		fac = 1
		while n > 1:
			fac *= n
			n -= 1
		return fac

	def showAnswer( self ):
		number = int( self.textBox.text() )
		answer = str( self.factorial( number ) )
		fullitem = str( number ) + "!=" + answer
		try:
			if len( answer ) <= 11:
				self.datatextBox.setText( fullitem )
				self.historyBox.addItem( fullitem )
			else:
				item = str( number ) + "!=" + answer[:12] + "..."
				self.datatextBox.setText( item )
				self.historyBox.addItem( item )
		except:
			self.datatextBox.setText( 'Please type in an integer!' )
