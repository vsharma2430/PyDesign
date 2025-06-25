from PyQt6.QtWidgets import QMainWindow, QMessageBox
from ui.pr_config.pr_config_widget import PipeRackConfigWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Piperack Creator")
        self.setGeometry(100, 100, 1200, 800)
        
        # Set central widget
        self.piperack_widget = PipeRackConfigWidget()
        self.setCentralWidget(self.piperack_widget)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create status bar
        self.statusBar().showMessage("Ready")
    
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('File')
        
        new_action = file_menu.addAction('New Configuration')
        new_action.triggered.connect(self.new_configuration)
        
        open_action = file_menu.addAction('Open Configuration')
        open_action.triggered.connect(self.piperack_widget.load_from_json)
        
        save_action = file_menu.addAction('Save Configuration')
        save_action.triggered.connect(self.piperack_widget.save_as_json)
        
        file_menu.addSeparator()
        
        export_action = file_menu.addAction('Export Pickle')
        export_action.triggered.connect(self.piperack_widget.export_pickle)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction('Exit')
        exit_action.triggered.connect(self.close)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        about_action = help_menu.addAction('About')
        about_action.triggered.connect(self.show_about)
    
    def new_configuration(self):
        reply = QMessageBox.question(
            self, 'New Configuration', 
            'Are you sure you want to create a new configuration? Unsaved changes will be lost.',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            # Reset to default values
            self.piperack_widget = PipeRackConfigWidget()
            self.setCentralWidget(self.piperack_widget)
    
    def show_about(self):
        QMessageBox.about(
            self, "About Piperack Creator",
            "Piperack Creator v1.0\n\n"
            "A PyQt6 application for configuring and exporting\n"
            "piperack parameters as pickle files.\n\n"
            "Built with PyQt6 and Python."
        )