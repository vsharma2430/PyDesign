from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QGroupBox, QFormLayout, QLineEdit, QDoubleSpinBox, QComboBox, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtGui import QFont

class BasicTab(QScrollArea):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        content = QWidget()
        layout = QVBoxLayout()
        
        # Basic Structure Group
        basic_group = QGroupBox("Basic Structure")
        basic_layout = QFormLayout()
        
        self.name_edit = QLineEdit("MPR_C-C")
        self.width_spin = QDoubleSpinBox()
        self.width_spin.setRange(1, 50)
        self.width_spin.setValue(8)
        self.width_spin.setSuffix(" m")
        
        self.pedestal_height_spin = QDoubleSpinBox()
        self.pedestal_height_spin.setRange(0, 10)
        self.pedestal_height_spin.setSingleStep(0.25)
        self.pedestal_height_spin.setValue(2)
        self.pedestal_height_spin.setSuffix(" m")
        
        self.foundation_depth_spin = QDoubleSpinBox()
        self.foundation_depth_spin.setRange(0, 5)
        self.foundation_depth_spin.setValue(1)
        self.foundation_depth_spin.setSingleStep(0.25)
        self.foundation_depth_spin.setSuffix(" m")
        
        basic_layout.addRow("Name:", self.name_edit)
        basic_layout.addRow("Width:", self.width_spin)
        basic_layout.addRow("Pedestal Height:", self.pedestal_height_spin)
        basic_layout.addRow("Foundation Depth:", self.foundation_depth_spin)
        basic_group.setLayout(basic_layout)
        
        # Portal Distances Group
        portal_group = QGroupBox("Portal Configuration")
        portal_layout = QVBoxLayout()
        
        portal_label = QLabel("Portal Distances:")
        self.portal_distances_layout = QVBoxLayout()
        self.portal_distances = []
        
        # Initialize with default distances
        default_distances = [0, 8, 16, 24, 32, 40, 48]
        for distance in default_distances:
            self.add_portal_distance(distance)
        
        # Add/Remove buttons
        buttons_layout = QHBoxLayout()
        add_button = QPushButton("Add Distance")
        remove_button = QPushButton("Remove Last Distance")
        add_button.clicked.connect(self.add_portal_distance)
        remove_button.clicked.connect(self.remove_portal_distance)
        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(remove_button)
        
        portal_layout.addWidget(portal_label)
        portal_layout.addLayout(self.portal_distances_layout)
        portal_layout.addLayout(buttons_layout)
        portal_group.setLayout(portal_layout)
        
        # Bracing Group
        bracing_group = QGroupBox("Bracing Configuration")
        bracing_layout = QFormLayout()
        
        self.brace_pattern_combo = QComboBox()
        self.brace_pattern_combo.addItems(["X_Pattern", "V_Pattern"])
        
        self.bracket_size_spin = QDoubleSpinBox()
        self.bracket_size_spin.setRange(0, 10)
        self.bracket_size_spin.setValue(2)
        self.bracket_size_spin.setSingleStep(0.25)
        self.bracket_size_spin.setSuffix(" m")
        
        self.max_expansion_spin = QDoubleSpinBox()
        self.max_expansion_spin.setRange(0, 20)
        self.max_expansion_spin.setValue(8)
        self.max_expansion_spin.setSingleStep(0.25)
        self.max_expansion_spin.setSuffix(" m")
        
        braces_label = QLabel("Braces Placement (comma-separated True/False):")
        self.braces_edit = QLineEdit("False, True, False, False, True, False")
        
        bracing_layout.addRow("Brace Pattern:", self.brace_pattern_combo)
        bracing_layout.addRow("Bracket Size:", self.bracket_size_spin)
        bracing_layout.addRow("Max Expansion Bay:", self.max_expansion_spin)
        bracing_layout.addRow(braces_label, self.braces_edit)
        bracing_group.setLayout(bracing_layout)
        
        layout.addWidget(basic_group)
        layout.addWidget(portal_group)
        layout.addWidget(bracing_group)
        layout.addStretch()
        
        content.setLayout(layout)
        self.setWidget(content)
        self.setWidgetResizable(True)
    
    def add_portal_distance(self, value=None):
        # If no value is provided, use last distance + 8 or 0 if no distances exist
        if value is None:
            value = self.portal_distances[-1][0].value() + 8 if self.portal_distances else 0.0
            
        distance_layout = QHBoxLayout()
        distance_spin = QDoubleSpinBox()
        distance_spin.setRange(0, 100)
        distance_spin.setSingleStep(0.25)
        distance_spin.setValue(value)
        distance_spin.setSuffix(" m")
        
        distance_label = QLabel(f"Distance {len(self.portal_distances) + 1}:")
        distance_layout.addWidget(distance_label)
        distance_layout.addWidget(distance_spin)
        
        self.portal_distances.append((distance_spin, distance_layout))
        self.portal_distances_layout.addLayout(distance_layout)
    
    def remove_portal_distance(self):
        if self.portal_distances:
            distance_spin, distance_layout = self.portal_distances.pop()
            # Remove widgets from layout
            while distance_layout.count():
                item = distance_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            self.portal_distances_layout.removeItem(distance_layout)
            distance_layout.deleteLater()
    
    def get_portal_distances(self):
        return [spin.value() for spin, _ in self.portal_distances]