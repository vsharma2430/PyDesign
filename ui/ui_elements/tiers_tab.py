from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QComboBox, QCheckBox, QHBoxLayout, QPushButton
from PyQt6.QtGui import QFont
from ui.pr_config.models import TierConfig

class TiersTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Tiers configuration
        tiers_label = QLabel("Tiers Configuration")
        tiers_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(tiers_label)
        
        # Table for tiers
        self.tiers_table = QTableWidget(6, 7)
        self.tiers_table.setHorizontalHeaderLabels([
            "Elevation (m)", "Type", "Operating Load", 
            "Wind Load (+)", "Wind Load (-)", 
            "Transverse Beam", "Bracket Provision"
        ])
        
        # Default tier data
        default_tiers = [
            TierConfig(3, "Standard", -0.4, 1.42, -1.42, False, False),
            TierConfig(6, "Standard", -0.4, 1.316, -1.316, False, False),
            TierConfig(9.5, "Standard", -0.35, 1.014, -1.014, True, True),
            TierConfig(12, "Standard", -0.3, 1.118, -1.118, True, True),
            TierConfig(14.5, "ElectricalIntrumentation", 0, 1.635, -1.635, False, False),
            TierConfig(17.5, "Flare", 0, 2.549, -2.549, False, False)
        ]
        
        self.populate_tiers_table(default_tiers)
        layout.addWidget(self.tiers_table)
        
        # Buttons for tiers
        tier_buttons = QHBoxLayout()
        add_tier_btn = QPushButton("Add Tier")
        remove_tier_btn = QPushButton("Remove Tier")
        reset_tiers_btn = QPushButton("Reset to Default")
        
        add_tier_btn.clicked.connect(self.add_tier_row)
        remove_tier_btn.clicked.connect(self.remove_tier_row)
        reset_tiers_btn.clicked.connect(lambda: self.populate_tiers_table(default_tiers))
        
        tier_buttons.addWidget(add_tier_btn)
        tier_buttons.addWidget(remove_tier_btn)
        tier_buttons.addWidget(reset_tiers_btn)
        tier_buttons.addStretch()
        
        layout.addLayout(tier_buttons)
        self.setLayout(layout)
    
    def populate_tiers_table(self, tiers_data):
        self.tiers_table.setRowCount(len(tiers_data))
        for i, tier in enumerate(tiers_data):
            self.tiers_table.setItem(i, 0, QTableWidgetItem(str(tier.elevation)))
            
            combo = QComboBox()
            combo.addItems(["Standard", "ElectricalIntrumentation", "Flare"])
            combo.setCurrentText(tier.tier_type)
            self.tiers_table.setCellWidget(i, 1, combo)
            
            self.tiers_table.setItem(i, 2, QTableWidgetItem(str(tier.operating_load)))
            self.tiers_table.setItem(i, 3, QTableWidgetItem(str(tier.wind_load_pos)))
            self.tiers_table.setItem(i, 4, QTableWidgetItem(str(tier.wind_load_neg)))
            
            trans_checkbox = QCheckBox()
            trans_checkbox.setChecked(tier.intermediate_transverse_beam)
            self.tiers_table.setCellWidget(i, 5, trans_checkbox)
            
            bracket_checkbox = QCheckBox()
            bracket_checkbox.setChecked(tier.bracket_provision)
            self.tiers_table.setCellWidget(i, 6, bracket_checkbox)
    
    def add_tier_row(self):
        current_rows = self.tiers_table.rowCount()
        self.tiers_table.insertRow(current_rows)
        
        # Add default values
        self.tiers_table.setItem(current_rows, 0, QTableWidgetItem("0.0"))
        combo = QComboBox()
        combo.addItems(["Standard", "ElectricalIntrumentation", "Flare"])
        self.tiers_table.setCellWidget(current_rows, 1, combo)
        
        self.tiers_table.setItem(current_rows, 2, QTableWidgetItem("0.0"))
        self.tiers_table.setItem(current_rows, 3, QTableWidgetItem("0.0"))
        self.tiers_table.setItem(current_rows, 4, QTableWidgetItem("0.0"))
        
        trans_checkbox = QCheckBox()
        self.tiers_table.setCellWidget(current_rows, 5, trans_checkbox)
        
        bracket_checkbox = QCheckBox()
        self.tiers_table.setCellWidget(current_rows, 6, bracket_checkbox)
    
    def remove_tier_row(self):
        current_row = self.tiers_table.currentRow()
        if current_row >= 0:
            self.tiers_table.removeRow(current_row)
    
    def get_tiers_data(self):
        tiers = []
        for i in range(self.tiers_table.rowCount()):
            if self.tiers_table.item(i, 0):
                tier = {
                    'elevation': float(self.tiers_table.item(i, 0).text()),
                    'tier_type': self.tiers_table.cellWidget(i, 1).currentText(),
                    'operating_load': float(self.tiers_table.item(i, 2).text()),
                    'wind_load_pos': float(self.tiers_table.item(i, 3).text()),
                    'wind_load_neg': float(self.tiers_table.item(i, 4).text()),
                    'intermediate_transverse_beam': self.tiers_table.cellWidget(i, 5).isChecked(),
                    'bracket_provision': self.tiers_table.cellWidget(i, 6).isChecked()
                }
                tiers.append(tier)
        return tiers
    
    def load_tiers(self, tiers_data):
        self.tiers_table.setRowCount(0)
        self.populate_tiers_table(tiers_data)