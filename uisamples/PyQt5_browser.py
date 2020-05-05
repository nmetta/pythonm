#!/usr/bin/env python

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.QtWebKit import *
#from PyQt5.QtWebKitWidgets import *
import PyQt5.QtWebEngineWidgets

from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
from PyQt5.QtWebEngineWidgets import QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("https://pythonspot.com"))
web.show()

sys.exit(app.exec_())
