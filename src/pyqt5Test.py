import sys
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle("Guru99")
    w.show()
    sys.exit(app.exec_())
    