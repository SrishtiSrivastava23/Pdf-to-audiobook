# Pdf-to-audiobook📖
PDF to Audiobook is a program that converts the written text from PDF documents into audio.

# Project Objective
The main goal of this project is to make reading more accessible and engaging by converting text-based PDFs into audible content. This is especially useful for:

Visually impaired users

Multitaskers (listen while doing other tasks)

Students or professionals who prefer auditory learning

#Features
📄 PDF Text Extraction
The application uses PyPDF2 to open and read PDF files. It extracts text page by page, handling plain-text PDFs.

🔊 Text-to-Speech (TTS)
The pyttsx3 library is used for offline speech synthesis. It reads out the extracted text using the system's built-in voices.

🧵 Multithreading
Speech runs in a separate thread, preventing the GUI from freezing while reading is in progress.


# GUI
The Graphical User Interface (GUI) for the PDF to Audiobook project is built using Tkinter, Python’s standard GUI library. The GUI allows users to interact with the program easily through visual elements like buttons, entry fields, and file dialogs instead of typing commands.

Key GUI Features:
File Selection: A “Browse” button opens a file dialog to let users choose a PDF file from their computer.

Entry Field: Displays the selected file path for user confirmation.

Read Button: Starts reading the selected PDF aloud using a text-to-speech engine.

Stop Button: Stops the audio playback at any time.


# Technologies Used
Python 3

Tkinter (GUI)

PyPDF2 (PDF reading)

pyttsx3 (Text-to-Speech)

Pillow (Image handling)

threading (Concurrency)

How to Run

1. Clone or download the repo

2. Install required libraries:

```
pip install pyttsx3 PyPDF2 pillow
```
3. Place your background image in the same folder (e.g. background.png)

4. Run the script:

```
python main.py
```

# Screenshot
[Screenshot](SS.png)

# Note:
1. Only pdf can be used with proper text.
2. Images cannot be used.
