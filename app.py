import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import pyttsx3
import threading
from PIL import Image, ImageTk  # Pillow for images

# Initialize TTS engine globally so we can control it
engine = pyttsx3.init()
speech_thread = None
stop_flag = False

def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )
    if file_path:
        entry_var.set(file_path)

def speak_pdf(pdf_path):
    global stop_flag
    try:
        pdf_file = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page in pdf_reader.pages:
            if stop_flag:
                break
            text = page.extract_text()
            if text:
                engine.say(text)
        engine.runAndWait()
        pdf_file.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read PDF:\n{e}")

def read_pdf():
    global speech_thread, stop_flag
    pdf_path = entry_var.get()
    stop_flag = False

    if not pdf_path:
        messagebox.showerror("Error", "Please select a PDF file.")
        return

    speech_thread = threading.Thread(target=speak_pdf, args=(pdf_path,))
    speech_thread.start()

def stop_speaking():
    global stop_flag
    stop_flag = True
    engine.stop()

# Create the GUI window
window = tk.Tk()
window.title("📖 PDF to Audiobook")
window.geometry("449x256")

# Load the background image
# Make sure your image file name and extension is correct!
bg_image = Image.open("background.png")  # change extension if needed
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label with the image and place it
background_label = tk.Label(window, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Entry and file selection
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, width=50)
entry.pack(pady=10)

browse_button = tk.Button(window, text="Browse PDF", command=browse_file)
browse_button.pack(pady=5)

# Read and Stop buttons
read_button = tk.Button(window, text="▶️ Read Aloud", command=read_pdf)
read_button.pack(pady=10)

stop_button = tk.Button(window, text="⏹️ Stop", command=stop_speaking)
stop_button.pack(pady=5)

# Start GUI event loop
window.mainloop()
