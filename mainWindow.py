from PySide2 import QtWidgets



class MainWindow( QtWidgets.QMainWindow ):
	def __init__( self ):
		super( MainWindow, self ).__init__()
		# create a central widget in main window
		self.centralWidget = QtWidgets.QWidget( self )
		self.setCentralWidget( self.centralWidget )
		# create a layout for central widget
		self.layout = QtWidgets.QVBoxLayout( self.centralWidget )

		# parent of closeButton should be centralWidget, since the button should be in
		self.closeButton = QtWidgets.QPushButton( self.centralWidget )
		self.layout.addWidget( self.closeButton )

		# parent of printButton should be centralWidget, since the button should be in
		self.printButton = QtWidgets.QPushButton( self.centralWidget )
		self.layout.addWidget( self.printButton )

		self.initSignalsAndSlots()

		self._setName()


	def initSignalsAndSlots( self ):
		# self.close is a built-in method that close the main window
		self.closeButton.clicked.connect( self.close )
		# self.showMessage implemented at below
		self.printButton.clicked.connect( self.showMessage )


	def _setName( self ):
		# this is for setText of the buttons
		self.closeButton.setText( 'Close' )
		self.printButton.setText( 'Show' )


	def showMessage( self ):
		QtWidgets.QMessageBox.warning(self,'Info Message',"Keep calm and keep calm")