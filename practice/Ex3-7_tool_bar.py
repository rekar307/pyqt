## Ex 3-7 Create Tool bar

import sys
from  PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from  PyQt5.QtGui import QIcon


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        # Tool bar
        saveAction = QAction(QIcon('images/save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save application')
        saveAction.triggered.connect(qApp.quit)

        editAction = QAction(QIcon('images/edit.png'), 'Edit', self)
        editAction.setShortcut('Ctrl+E')
        editAction.setStatusTip('Exit application')
        editAction.triggered.connect(qApp.quit)

        printAction = QAction(QIcon('images/print.png'), 'Print', self)
        printAction.setShortcut('Ctrl+P')
        printAction.setStatusTip('Exit application')
        printAction.triggered.connect(qApp.quit)

        exitAction = QAction(QIcon('images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('save')
        self.toolbar.addAction(saveAction)
        self.toolbar = self.addToolBar('Edit')
        self.toolbar.addAction(editAction)
        self.toolbar = self.addToolBar('Print')
        self.toolbar.addAction(printAction)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # Menu bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(True)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu = menubar.addMenu('&Edit')
        filemenu.addAction(exitAction)
        filemenu = menubar.addMenu('&View')
        filemenu.addAction(exitAction)
        filemenu = menubar.addMenu('&Tools')
        filemenu.addAction(exitAction)
        filemenu = menubar.addMenu('&Help')
        filemenu.addAction(exitAction)

        # Common
        self.statusBar()
        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())