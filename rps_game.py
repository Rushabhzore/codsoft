import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class RPSGame(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Game State
        self.user_score = 0
        self.computer_score = 0
        self.choices = ['Rock', 'Paper', 'Scissors']
        
        # Window Configuration
        self.setWindowTitle("Rock Paper Scissors - Demo")
        self.setFixedSize(700, 450)
        
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
        score_title = QLabel("SCOREBOARD")
        score_title.setFont(QFont("Arial", 14, QFont.Bold))
        score_title.setAlignment(Qt.AlignCenter)
        
        # Score Trackers
        self.user_score_label = QLabel(f"You: {self.user_score}")
        self.user_score_label.setFont(QFont("Arial", 12))
        
        self.comp_score_label = QLabel(f"Computer: {self.computer_score}")
        self.comp_score_label.setFont(QFont("Arial", 12))
        
        # Reset / Play Again Button
        self.reset_btn = QPushButton("🔄 Reset Game")
        self.reset_btn.setCursor(Qt.PointingHandCursor)
        self.reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c; border-radius: 5px; padding: 10px; font-weight: bold;
            }
            QPushButton:hover { background-color: #c0392b; }
        """)
        self.reset_btn.clicked.connect(self.reset_game)
        
        # Add to Sidebar Layout
        self.sidebar_layout.addWidget(score_title)
        self.sidebar_layout.addWidget(self.user_score_label)
        self.sidebar_layout.addWidget(self.comp_score_label)
        self.sidebar_layout.addStretch()
        self.sidebar_layout.addWidget(self.reset_btn)
        
        # ================= MAIN AREA (Right) =================
        self.main_area = QFrame()
        self.main_area.setStyleSheet("background-color: #ecf0f1; color: #34495e;")
        self.main_area_layout = QVBoxLayout(self.main_area)
        self.main_area_layout.setContentsMargins(40, 40, 40, 40)
        self.main_area_layout.setSpacing(20)
        
        # Instructions
        self.instruction_label = QLabel("Make your choice to play!")
        self.instruction_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.instruction_label.setAlignment(Qt.AlignCenter)
        
        # Result Display Area
        self.result_label = QLabel("Waiting for your move...")
        self.result_label.setFont(QFont("Arial", 14))
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True)
        self.result_label.setStyleSheet("color: #7f8c8d; margin: 20px 0;")
        
        # Action Buttons Layout
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(20)
        
        # Styling for play buttons
        btn_style = """
            QPushButton {
                background-color: #3498db; color: white; border-radius: 10px; 
                padding: 15px; font-size: 16px; font-weight: bold;
            }
            QPushButton:hover { background-color: #2980b9; }
        """
        
        # Rock Button
        self.rock_btn = QPushButton("🪨 Rock")
        self.rock_btn.setStyleSheet(btn_style)
        self.rock_btn.setCursor(Qt.PointingHandCursor)
        self.rock_btn.clicked.connect(lambda: self.play_round('Rock'))
        
        # Paper Button
        self.paper_btn = QPushButton("📄 Paper")
        self.paper_btn.setStyleSheet(btn_style)
        self.paper_btn.setCursor(Qt.PointingHandCursor)
        self.paper_btn.clicked.connect(lambda: self.play_round('Paper'))
        
        # Scissors Button
        self.scissors_btn = QPushButton("✂️ Scissors")
        self.scissors_btn.setStyleSheet(btn_style)
        self.scissors_btn.setCursor(Qt.PointingHandCursor)
        self.scissors_btn.clicked.connect(lambda: self.play_round('Scissors'))
        
        # Add buttons to horizontal layout
        self.buttons_layout.addWidget(self.rock_btn)
        self.buttons_layout.addWidget(self.paper_btn)
        self.buttons_layout.addWidget(self.scissors_btn)
        
        # Add to Main Area Layout
        self.main_area_layout.addWidget(self.instruction_label)
        self.main_area_layout.addWidget(self.result_label)
        self.main_area_layout.addStretch()
        self.main_area_layout.addLayout(self.buttons_layout)
        
        # ================= ASSEMBLE WINDOW =================
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.main_area)

    def play_round(self, user_choice):
        """Game logic and validation happens here."""
        # Computer randomly selects
        comp_choice = random.choice(self.choices)
        
        # Determine Winner
        if user_choice == comp_choice:
            result = "It's a Tie! 🤝"
            color = "#f39c12" # Orange
        elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
             (user_choice == 'Paper' and comp_choice == 'Rock') or \
             (user_choice == 'Scissors' and comp_choice == 'Paper'):
            result = "You Win! 🎉"
            color = "#27ae60" # Green
            self.user_score += 1
        else:
            result = "Computer Wins! 😢"
            color = "#c0392b" # Red
            self.computer_score += 1
            
        # Update UI Feedback
        feedback_text = f"You chose <b>{user_choice}</b>.<br>Computer chose <b>{comp_choice}</b>.<br><br><span style='font-size:18px; color:{color};'>{result}</span>"
        self.result_label.setText(feedback_text)
        
        # Update Scoreboard
        self.user_score_label.setText(f"You: {self.user_score}")
        self.comp_score_label.setText(f"Computer: {self.computer_score}")
        self.instruction_label.setText("Play Again?")

    def reset_game(self):
        """Resets scores and UI back to default."""
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.setText(f"You: {self.user_score}")
        self.comp_score_label.setText(f"Computer: {self.computer_score}")
        self.instruction_label.setText("Make your choice to play!")
        self.result_label.setText("Waiting for your move...")
        self.result_label.setStyleSheet("color: #7f8c8d; margin: 20px 0;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Optional: Set a global font
    font = QFont("Arial", 10)
    app.setFont(font)
    
    window = RPSGame()
    window.show()
    
    sys.exit(app.exec_())