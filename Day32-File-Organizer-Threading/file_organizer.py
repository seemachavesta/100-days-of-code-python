import threading
import time

file_organizer = {
    "Images": [],
    "Documents": [],
    "Videos": [],
    "Others": []
}


# Checks the file type (extension)
def check_type(user_input):
    if '.' not in user_input:
        print('Invalid input type.')
        return
    name, ext = user_input.rsplit('.', 1)
    return name, ext.lower()
    
    
def find_matching_folder(ext: str):
    
    if ext == "jpg" or ext == "png":
        return 'Images'
    if ext == "pdf" or ext == "docx":
        return 'Documents'
    if ext == "mp4" or ext == "mov":
        return "Videos"
        
    return "Others"
    
    
def process_file(file_name):
    result = check_type(file_name)
    if result is None or result[1] is None:
        print(f"⚠️ Skipping invalid file: '{file_name}'")
        return
    
    name, ext = result
    if ext is None:
        return 
   
    folder = find_matching_folder(ext)
    time.sleep(1)
    file_organizer[folder].append(file_name)
    print(f"✅ Moved '{file_name}' to '{folder}' folder.")
    
    
def process_input(user_input):
    files = user_input.split(',')
    threads = []
    for file in files:
        cleaned_file = file.strip()
        
        thread = threading.Thread(target=process_file, args=(cleaned_file,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

        
def main():
    user_input = input("Enter file names separated by commas (e.g. book.pdf, image.jpg): ")

    process_input(user_input)

    print("\n🗂 Final Folder Contents:")
    for folder, files in file_organizer.items():
        print(f"{folder}: {files}")