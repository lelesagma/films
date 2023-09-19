import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWebView, QVBoxLayout, QWidget

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Web Browser')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.browser = QWebView()
        layout.addWidget(self.browser)

        # Charger une page web (par exemple, google.com)
        self.browser.setUrl('https://www.google.com')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())
