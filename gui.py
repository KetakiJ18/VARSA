import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QTextEdit, QLabel, QListWidget, QListWidgetItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from core.speech import speak, listen  
from main import handle_command    


class VarsaGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VARSA")
        self.resize(600, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.status_label = QLabel("Press the mic button and speak...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.status_label)

        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setFont(QFont("Consolas", 12))
        self.layout.addWidget(self.output_area)

        self.file_list_widget = QListWidget()
        self.file_list_widget.hide()
        self.file_list_widget.itemClicked.connect(self.open_selected_file)
        self.layout.addWidget(self.file_list_widget)

        self.mic_button = QPushButton("🎙️")
        self.mic_button.setFont(QFont("Arial", 40))
        self.mic_button.setFixedSize(120, 120)
        self.mic_button.setStyleSheet("""
            QPushButton {
                border-radius: 60px;
                background-color: #0078d7;
                color: white;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)
        self.mic_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.mic_button.clicked.connect(self.listen_and_respond)

        self.layout.addWidget(self.mic_button, alignment=Qt.AlignHCenter)

    def listen_and_respond(self):
        self.status_label.setText("Listening...")
        QApplication.processEvents()  

        command = listen()
        if not command:
            self.status_label.setText("Didn't catch that. Try again. Say \"exit\" to quit")
            return

        self.status_label.setText(f"You said: {command}")

        result = handle_command(command)
        if not isinstance(result, dict):
            self.output_area.append("Command processed.")
            return

        self.output_area.clear()
        self.file_list_widget.clear()
        self.file_list_widget.hide()

        if result.get("status") == "file_list":
            files = result.get("files", [])
            message = result.get("message", f"Found {len(files)} files. Select one to open.")
            self.output_area.append(message)
            for file_path in files:
                item = QListWidgetItem(os.path.basename(file_path))
                item.setData(Qt.UserRole, file_path)
                self.file_list_widget.addItem(item)
            self.file_list_widget.show()

        else:
            if "message" in result:
                self.output_area.append(result["message"])

        if result.get("status") == "exit":
            self.status_label.setText("VARSA says goodbye!")
            QApplication.quit()

    def open_selected_file(self, item):
        file_path = item.data(Qt.UserRole)
        if file_path and os.path.exists(file_path):
            speak(f"Opening {os.path.basename(file_path)}")
            os.startfile(file_path)

            self.output_area.append(f"Opened: {os.path.basename(file_path)}")
            self.file_list_widget.clear()
            self.file_list_widget.hide()
        else:
            self.output_area.append("File does not exist or cannot be opened.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = VarsaGUI()
    gui.show()
    speak("Good Day! I'm VARSA! Ready to serve")
    sys.exit(app.exec_())
