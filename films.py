import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui
from PyQt5.QtNetwork import QNetworkCookieJar, QNetworkCookie
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor


class CustomCookieJar(QNetworkCookieJar):
    def __init__(self, parent=None):
        super(CustomCookieJar, self).__init__(parent)
        self.cookies = []

    def setCookiesFromUrl(self, cookieList, url):
        self.cookies = cookieList

    def cookiesForUrl(self, url):
        return self.cookies


class RequestInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, cookie_jar):
        super(RequestInterceptor, self).__init__()
        self.cookie_jar = cookie_jar

    def interceptRequest(self, info):
        info.setHttpHeader(b"Cookie", b"")


class FenPrincipale(QMainWindow):
    def __init__(self):
        super(FenPrincipale, self).__init__()
        self.setWindowIcon(QtGui.QIcon("logo.ico"))
        self.navigateur = QWebEngineView()
        self.navigateur.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.navigateur)
        self.showMaximized()

        # Supprimer les cookies sur chaque page web
        cookie_jar = CustomCookieJar()
        interceptor = RequestInterceptor(cookie_jar)
        profile = QWebEngineProfile.defaultProfile()
        profile.setRequestInterceptor(interceptor)


app = QApplication(sys.argv)
QApplication.setApplicationName("navigateur")
fenetre = FenPrincipale()
app.exec()