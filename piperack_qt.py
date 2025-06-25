import sys
from PyQt6.QtWidgets import QApplication
from ui.ui_elements.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Piperack Creator")
    app.setStyle('Fusion')
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()