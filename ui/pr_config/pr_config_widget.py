import json
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from ui.ui_elements.basic_tab import BasicTab
from ui.ui_elements.tiers_tab import TiersTab
from ui.ui_elements.components_tab import ComponentsTab
from ui.ui_elements.export_tab import ExportTab

class PipeRackConfigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_default_values()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Create tab widget
        self.tabs = QTabWidget()
        
        # Initialize tabs
        self.basic_tab = BasicTab()
        self.tiers_tab = TiersTab()
        self.components_tab = ComponentsTab()
        self.export_tab = ExportTab(self.get_configuration)  # Pass get_configuration method
        
        # Add tabs to widget
        self.tabs.addTab(self.basic_tab, "Basic Configuration")
        self.tabs.addTab(self.tiers_tab, "Tiers")
        self.tabs.addTab(self.components_tab, "Components")
        self.tabs.addTab(self.export_tab, "Export")
        
        layout.addWidget(self.tabs)
        self.setLayout(layout)
    
    def get_configuration(self):
        """Extract all configuration data from the UI"""
        config = {
            'name': self.basic_tab.name_edit.text(),
            'width': self.basic_tab.width_spin.value(),
            'pedestal_height': self.basic_tab.pedestal_height_spin.value(),
            'foundation_depth': self.basic_tab.foundation_depth_spin.value(),
            'portal_distances': self.basic_tab.get_portal_distances(),
            'brace_pattern': self.basic_tab.brace_pattern_combo.currentText(),
            'bracket_size': self.basic_tab.bracket_size_spin.value(),
            'max_expansion': self.basic_tab.max_expansion_spin.value(),
            'braces_placement': [x.strip().lower() == 'true' for x in self.basic_tab.braces_edit.text().split(',')],
            'tiers': self.tiers_tab.get_tiers_data(),
            'flares': self.components_tab.get_flares_data(),
            'walkways': self.components_tab.get_walkways_data(),
            'ducts': self.components_tab.get_ducts_data(),
            'electric_trees': self.components_tab.get_trees_data()
        }
        return config
    
    def load_configuration(self, config):
        """Load configuration data into the UI"""
        self.basic_tab.name_edit.setText(config.get('name', ''))
        self.basic_tab.width_spin.setValue(config.get('width', 8))
        self.basic_tab.pedestal_height_spin.setValue(config.get('pedestal_height', 2))
        self.basic_tab.foundation_depth_spin.setValue(config.get('foundation_depth', 1))
        
        portal_distances = config.get('portal_distances', [])
        self.basic_tab.portal_distances_edit.setText(', '.join(map(str, portal_distances)))
        
        self.basic_tab.brace_pattern_combo.setCurrentText(config.get('brace_pattern', 'X_Pattern'))
        self.basic_tab.bracket_size_spin.setValue(config.get('bracket_size', 2))
        self.basic_tab.max_expansion_spin.setValue(config.get('max_expansion', 8))
        
        braces_placement = config.get('braces_placement', [])
        self.basic_tab.braces_edit.setText(', '.join(map(str, braces_placement)))
        
        self.tiers_tab.load_tiers(config.get('tiers', []))
        self.components_tab.load_components(
            config.get('flares', []),
            config.get('walkways', []),
            config.get('ducts', []),
            config.get('electric_trees', [])
        )
    
    def load_default_values(self):
        """Load default values into the UI"""
        pass
    
    def preview_configuration(self):
        self.export_tab.preview_configuration()
    
    def save_as_json(self):
        self.export_tab.save_as_json()
    
    def load_from_json(self):
        config = self.export_tab.load_from_json()
        if config:
            self.load_configuration(config)
    
    def export_pickle(self):
        self.export_tab.export_pickle()