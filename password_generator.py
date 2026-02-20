import sys
import random
import string
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QFrame, 
                             QSpinBox, QCheckBox, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Window Configuration
        self.setWindowTitle("Secure Password Generator")
        self.setFixedSize(650, 450)
        
        # Main Widget and Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.init_ui()
        
    def init_ui(self):
        # ================= SIDEBAR (Left) =================
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet("background-color: #2c3e50; color: white;")
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(20, 30, 20, 30)
        self.sidebar_layout.setSpacing(20)
        
        # Sidebar Title
        app_title = QLabel("⚙️ OPTIONS")
        app_title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        app_title.setAlignment(Qt.AlignCenter)
        
        # Sidebar Description
        desc_label = QLabel("Customize your\npassword complexity\nusing the settings\non the right.")
        desc_label.setFont(QFont("Segoe UI", 10))
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setStyleSheet("color: #bdc3c7;")
        
        # Exit Button
        self.exit_btn = QPushButton("❌ Exit App")
        self.exit_btn.setCursor(Qt.PointingHandCursor)
        self.exit_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c; border-radius: 5px; padding: 10px; font-weight: bold; color: white;
            }
            QPushButton:hover { background-color: #c0392b; }
        """)
        self.exit_btn.clicked.connect(self.close)
        
        # Assemble Sidebar
        self.sidebar_layout.addWidget(app_title)
        self.sidebar_layout.addWidget(desc_label)
        self.sidebar_layout.addStretch()
        self.sidebar_layout.addWidget(self.exit_btn)
        
        # ================= MAIN AREA (Right) =================
        self.main_area = QFrame()
        self.main_area.setStyleSheet("background-color: #ecf0f1; color: #2c3e50;")
        self.main_area_layout = QVBoxLayout(self.main_area)
        self.main_area_layout.setContentsMargins(40, 30, 40, 30)
        self.main_area_layout.setSpacing(15)
        
        # Title
        self.header_label = QLabel("Generate a Secure Password")
        self.header_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        
        # Length Input
        length_layout = QHBoxLayout()
        length_label = QLabel("Password Length:")
        length_label.setFont(QFont("Segoe UI", 12))
        
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(4, 128) # Validation: Min 4, Max 128
        self.length_spinbox.setValue(12)     # Default value
        self.length_spinbox.setFont(QFont("Segoe UI", 12))
        self.length_spinbox.setStyleSheet("padding: 5px; border: 1px solid #bdc3c7; border-radius: 4px;")
        
        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_spinbox)
        length_layout.addStretch()
        
        # Complexity Checkboxes
        self.chk_upper = QCheckBox("Uppercase Letters (A-Z)")
        self.chk_upper.setChecked(True)
        self.chk_upper.setFont(QFont("Segoe UI", 11))
        
        self.chk_lower = QCheckBox("Lowercase Letters (a-z)")
        self.chk_lower.setChecked(True)
        self.chk_lower.setFont(QFont("Segoe UI", 11))
        
        self.chk_numbers = QCheckBox("Numbers (0-9)")
        self.chk_numbers.setChecked(True)
        self.chk_numbers.setFont(QFont("Segoe UI", 11))
        
        self.chk_symbols = QCheckBox("Symbols (!@#$...)")
        self.chk_symbols.setChecked(True)
        self.chk_symbols.setFont(QFont("Segoe UI", 11))
        
        # Generate Button
        self.generate_btn = QPushButton("🔑 Generate Password")
        self.generate_btn.setCursor(Qt.PointingHandCursor)
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60; color: white; border-radius: 8px; 
                padding: 12px; font-size: 14px; font-weight: bold; margin-top: 10px;
            }
            QPushButton:hover { background-color: #2ecc71; }
        """)
        self.generate_btn.clicked.connect(self.generate_password)
        
        # Output Area
        output_layout = QHBoxLayout()
        self.output_field = QLineEdit()
        self.output_field.setReadOnly(True)
        self.output_field.setPlaceholderText("Your password will appear here...")
        self.output_field.setFont(QFont("Courier New", 14))
        self.output_field.setStyleSheet("padding: 10px; border: 2px solid #bdc3c7; border-radius: 5px; background-color: white;")
        
        self.copy_btn = QPushButton("📋 Copy")
        self.copy_btn.setCursor(Qt.PointingHandCursor)
        self.copy_btn.setStyleSheet("""
            QPushButton {
                background-color: #2980b9; color: white; border-radius: 5px; 
                padding: 10px; font-weight: bold;
            }
            QPushButton:hover { background-color: #3498db; }
        """)
        self.copy_btn.clicked.connect(self.copy_to_clipboard)
        
        output_layout.addWidget(self.output_field)
        output_layout.addWidget(self.copy_btn)
        
        # Assemble Main Area
        self.main_area_layout.addWidget(self.header_label)
        self.main_area_layout.addLayout(length_layout)
        self.main_area_layout.addWidget(self.chk_upper)
        self.main_area_layout.addWidget(self.chk_lower)
        self.main_area_layout.addWidget(self.chk_numbers)
        self.main_area_layout.addWidget(self.chk_symbols)
        self.main_area_layout.addWidget(self.generate_btn)
        self.main_area_layout.addStretch()
        self.main_area_layout.addLayout(output_layout)
        
        # ================= ASSEMBLE WINDOW =================
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.main_area)

    def generate_password(self):
        """Logic to generate a random password based on user constraints."""
        length = self.length_spinbox.value()
        
        # Build the character pool based on selected checkboxes
        character_pool = ""
        if self.chk_upper.isChecked():
            character_pool += string.ascii_uppercase
        if self.chk_lower.isChecked():
            character_pool += string.ascii_lowercase
        if self.chk_numbers.isChecked():
            character_pool += string.digits
        if self.chk_symbols.isChecked():
            character_pool += string.punctuation
            
        # Validation: Ensure at least one complexity option is selected
        if not character_pool:
            QMessageBox.warning(self, "Validation Error", "Please select at least one character type (Uppercase, Lowercase, etc.).")
            return
            
        # Generate the password
        generated_password = "".join(random.choices(character_pool, k=length))
        
        # Display the result
        self.output_field.setText(generated_password)

    def copy_to_clipboard(self):
        """Copies the generated password to the system clipboard."""
        password = self.output_field.text()
        if password:
            QApplication.clipboard().setText(password)
            QMessageBox.information(self, "Success", "Password copied to clipboard!")
        else:
            QMessageBox.warning(self, "Empty", "No password to copy! Please generate one first.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())