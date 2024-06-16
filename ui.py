import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
import speech_recognition as sr

class SpeechRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Speech Recognition Output")
        self.text_edit.setReadOnly(True)

        self.recognition_button = QPushButton("Start Speech Recognition")
        self.recognition_button.clicked.connect(self.recognize_speech)

        layout.addWidget(self.text_edit)
        layout.addWidget(self.recognition_button)

        self.setLayout(layout)

        self.setGeometry(0, 0, 2000, 1000)
        self.setWindowTitle("Speech Recognition App")

    def recognize_speech(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            self.text_edit.setPlainText(f"You said: {text}")
        except sr.UnknownValueError:
            self.text_edit.setPlainText("Could not understand audio.")
        except sr.RequestError as e:
            self.text_edit.setPlainText(f"Error connecting to Google API: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpeechRecognitionApp()
    window.show()
    sys.exit(app.exec_())
