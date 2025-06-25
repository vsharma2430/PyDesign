from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QGroupBox, QTableWidget, QTableWidgetItem, QCheckBox
from ui.pr_config.models import FlareConfig, WalkwayConfig, DuctConfig, ElectricTreeConfig

class ComponentsTab(QScrollArea):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        content = QWidget()
        layout = QVBoxLayout()
        
        # Flares Group
        flares_group = QGroupBox("Flares")
        flares_layout = QVBoxLayout()
        
        self.flares_table = QTableWidget(3, 3)
        self.flares_table.setHorizontalHeaderLabels(["Position", "Design Load", "Support Member"])
        
        default_flares = [
            FlareConfig(2.5, 3, True),
            FlareConfig(5, 0.35, False),
            FlareConfig(6, 0.3, False)
        ]
        self.populate_flares_table(default_flares)
        
        flares_layout.addWidget(self.flares_table)
        flares_group.setLayout(flares_layout)
        
        # Walkways Group
        walkways_group = QGroupBox("Walkways")
        walkways_layout = QVBoxLayout()
        
        self.walkways_table = QTableWidget(2, 1)
        self.walkways_table.setHorizontalHeaderLabels(["Position"])
        
        default_walkways = [WalkwayConfig(1), WalkwayConfig(4.5)]
        self.populate_walkways_table(default_walkways)
        
        walkways_layout.addWidget(self.walkways_table)
        walkways_group.setLayout(walkways_layout)
        
        # Ducts Group
        ducts_group = QGroupBox("Instrumentation Ducts")
        ducts_layout = QVBoxLayout()
        
        self.ducts_table = QTableWidget(1, 3)
        self.ducts_table.setHorizontalHeaderLabels(["Width", "Height", "Position"])
        
        default_ducts = [DuctConfig(1.2, 0.4, 6)]
        self.populate_ducts_table(default_ducts)
        
        ducts_layout.addWidget(self.ducts_table)
        ducts_group.setLayout(ducts_layout)
        
        # Electric Trees Group
        trees_group = QGroupBox("Electric Tree Supports")
        trees_layout = QVBoxLayout()
        
        self.trees_table = QTableWidget(1, 1)
        self.trees_table.setHorizontalHeaderLabels(["Position"])
        
        default_trees = [ElectricTreeConfig(3)]
        self.populate_trees_table(default_trees)
        
        trees_layout.addWidget(self.trees_table)
        trees_group.setLayout(trees_layout)
        
        layout.addWidget(flares_group)
        layout.addWidget(walkways_group)
        layout.addWidget(ducts_group)
        layout.addWidget(trees_group)
        
        content.setLayout(layout)
        self.setWidget(content)
        self.setWidgetResizable(True)
    
    def populate_flares_table(self, flares_data):
        self.flares_table.setRowCount(len(flares_data))
        for i, flare in enumerate(flares_data):
            self.flares_table.setItem(i, 0, QTableWidgetItem(str(flare.position)))
            self.flares_table.setItem(i, 1, QTableWidgetItem(str(flare.design_load)))
            
            checkbox = QCheckBox()
            checkbox.setChecked(flare.support_member)
            self.flares_table.setCellWidget(i, 2, checkbox)
    
    def populate_walkways_table(self, walkways_data):
        self.walkways_table.setRowCount(len(walkways_data))
        for i, walkway in enumerate(walkways_data):
            self.walkways_table.setItem(i, 0, QTableWidgetItem(str(walkway.position)))
    
    def populate_ducts_table(self, ducts_data):
        self.ducts_table.setRowCount(len(ducts_data))
        for i, duct in enumerate(ducts_data):
            self.ducts_table.setItem(i, 0, QTableWidgetItem(str(duct.width)))
            self.ducts_table.setItem(i, 1, QTableWidgetItem(str(duct.height)))
            self.ducts_table.setItem(i, 2, QTableWidgetItem(str(duct.position)))
    
    def populate_trees_table(self, trees_data):
        self.trees_table.setRowCount(len(trees_data))
        for i, tree in enumerate(trees_data):
            self.trees_table.setItem(i, 0, QTableWidgetItem(str(tree.position)))
    
    def get_flares_data(self):
        flares = []
        for i in range(self.flares_table.rowCount()):
            if self.flares_table.item(i, 0):
                flare = {
                    'position': float(self.flares_table.item(i, 0).text()),
                    'design_load': float(self.flares_table.item(i, 1).text()),
                    'support_member': self.flares_table.cellWidget(i, 2).isChecked()
                }
                flares.append(flare)
        return flares
    
    def get_walkways_data(self):
        walkways = []
        for i in range(self.walkways_table.rowCount()):
            if self.walkways_table.item(i, 0):
                walkway = {'position': float(self.walkways_table.item(i, 0).text())}
                walkways.append(walkway)
        return walkways
    
    def get_ducts_data(self):
        ducts = []
        for i in range(self.ducts_table.rowCount()):
            if self.ducts_table.item(i, 0):
                duct = {
                    'width': float(self.ducts_table.item(i, 0).text()),
                    'height': float(self.ducts_table.item(i, 1).text()),
                    'position': float(self.ducts_table.item(i, 2).text())
                }
                ducts.append(duct)
        return ducts
    
    def get_trees_data(self):
        trees = []
        for i in range(self.trees_table.rowCount()):
            if self.trees_table.item(i, 0):
                tree = {'position': float(self.trees_table.item(i, 0).text())}
                trees.append(tree)
        return trees
    
    def load_components(self, flares_data, walkways_data, ducts_data, trees_data):
        self.populate_flares_table(flares_data)
        self.populate_walkways_table(walkways_data)
        self.populate_ducts_table(ducts_data)
        self.populate_trees_table(trees_data)