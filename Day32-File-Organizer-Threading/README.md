# 🗂️ File Organizer with Threading (Day 32 - 100 Days of Python)

This project is part of my **100 Days of Python** challenge — specifically, **Day 32**, where I practiced and understood how to use **threads in Python** to simulate concurrent file processing.

The program simulates a file organizer that moves files into appropriate folders based on their file extension. Each file is processed in a separate thread using the `threading` module, and a `time.sleep(1)` delay simulates real file movement time.

---

## 🚀 Features

- Accepts a list of file names (e.g., `book.pdf, image.jpg, movie.mp4`)
- Detects file types by extension
- "Moves" files to the following folders:
  - 📷 **Images** (`.jpg`, `.png`)
  - 📄 **Documents** (`.pdf`, `.docx`)
  - 🎞️ **Videos** (`.mp4`, `.mov`)
  - 📁 **Others** for unsupported or unknown extensions
- Each file is processed in its own thread
- Prints the final folder contents

---

## 🧵 Concepts Practiced

- Python **`threading.Thread`**
- Function modularity and separation of concerns
- String parsing and validation
- Dictionary-based categorization
- Simulating real-time behavior with `time.sleep()`
- Safe handling of invalid input

---



