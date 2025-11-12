import os
import shutil

# Create destination directory if it doesn't exist
os.makedirs('./nodesc', exist_ok=True)
error_sub= "502 Bad Gateway"
no_info_sub ="This function has no description."

# Get all files in current directory
for filename in os.listdir('.'):
    filepath = os.path.join('.', filename)
    
    if os.path.isfile(filepath) and filename.endswith('.md'):
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if no_info_sub in line:
                    destination = os.path.join('./nodesc', filename)
                    shutil.move(filepath, destination)
                    print(f"Moved {filename}")
                    break
                if error_sub in line:
                    destination = os.path.join('./502', filename)
                    shutil.move(filepath, destination)
                    print(f"Moved {filename}")
   
