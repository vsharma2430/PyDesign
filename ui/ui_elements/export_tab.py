from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit, QFileDialog, QMessageBox
from PyQt6.QtCore import QDateTime
import json
import pickle
import os

class ExportTab(QWidget):
    def __init__(self, get_configuration):
        super().__init__()
        self.get_configuration = get_configuration  # Store the get_configuration method
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Export options
        export_group = QGroupBox("Export Options")
        export_layout = QVBoxLayout()
        
        # File path selection
        path_layout = QHBoxLayout()
        self.export_path_edit = QLineEdit("piperack_objects/")
        browse_btn = QPushButton("Browse...")
        browse_btn.clicked.connect(self.browse_export_path)
        
        path_layout.addWidget(QLabel("Export Directory:"))
        path_layout.addWidget(self.export_path_edit)
        path_layout.addWidget(browse_btn)
        
        export_layout.addLayout(path_layout)
        
        # Preview area
        preview_label = QLabel("Configuration Preview:")
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        self.preview_text.setMaximumHeight(200)
        
        export_layout.addWidget(preview_label)
        export_layout.addWidget(self.preview_text)
        
        export_group.setLayout(export_layout)
        
        # Action buttons
        button_layout = QHBoxLayout()
        
        preview_btn = QPushButton("Preview Configuration")
        preview_btn.clicked.connect(self.preview_configuration)  # Connect directly
        
        export_btn = QPushButton("Export Pickle File")
        export_btn.clicked.connect(self.export_pickle)
        export_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }")
        
        save_json_btn = QPushButton("Save as JSON")
        save_json_btn.clicked.connect(self.save_as_json)
        
        load_json_btn = QPushButton("Load from JSON")
        load_json_btn.clicked.connect(self.load_from_json)
        
        button_layout.addWidget(preview_btn)
        button_layout.addWidget(save_json_btn)
        button_layout.addWidget(load_json_btn)
        button_layout.addStretch()
        button_layout.addWidget(export_btn)
        
        layout.addWidget(export_group)
        layout.addLayout(button_layout)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def browse_export_path(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Export Directory")
        if directory:
            self.export_path_edit.setText(directory)
    
    def save_as_json(self):
        config = self.get_configuration()
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Configuration", f"{config['name']}.json", "JSON Files (*.json)"
        )
        if filename:
            try:
                with open(filename, 'w') as f:
                    json.dump(config, f, indent=2)
                QMessageBox.information(self, "Success", f"Configuration saved to {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save configuration: {str(e)}")
    
    def load_from_json(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Load Configuration", "", "JSON Files (*.json)"
        )
        if filename:
            try:
                with open(filename, 'r') as f:
                    config = json.load(f)
                QMessageBox.information(self, "Success", f"Configuration loaded from {filename}")
                return config
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load configuration: {str(e)}")
                return None
    
    def preview_configuration(self):
        config = self.get_configuration()
        preview_text = json.dumps(config, indent=2)
        self.preview_text.setPlainText(preview_text)
    
    def export_pickle(self):
        try:
            config = self.get_configuration()
            
            # Create export directory if it doesn't exist
            export_dir = self.export_path_edit.text()
            os.makedirs(export_dir, exist_ok=True)
            
            # Generate filename
            filename = os.path.join(export_dir, f"{config['name']}.pkl")
            
            # Mock piperack object creation
            piperack_data = {
                'config': config,
                'generated_at': str(QDateTime.currentDateTime().toString()),
                'version': '1.0'
            }
            
            # Save pickle file
            with open(filename, 'wb') as f:
                pickle.dump(piperack_data, f)
            
            QMessageBox.information(
                self, "Export Successful", 
                f"Piperack configuration exported to:\n{filename}"
            )
            
        except Exception as e:
            QMessageBox.critical(self, "Export Failed", f"Failed to export pickle file:\n{str(e)}")