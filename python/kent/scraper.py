from bs4 import BeautifulSoup
import requests
import re
from PIL import Image, ImageTk
from io import BytesIO
from tqdm import tqdm
import pickle

# Read HTML content from a file
with open('/Users/philipphaus/Documents/coding/python/kent/students.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
print('red file')

# Initialize BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
print('soup started')
# Initialize an empty dictionary to store the student data
student_data = {}

# Loop through each student entry in the HTML
student_entries = soup.find_all('div', {'class': 'directory-Entry_Header'})
print('all entries found')
for student_entry in tqdm(student_entries):
    # Extract the image URL
    image_div = student_entry.find('div', {'class': 'directory-Entry_PersonPhoto--square'})
    image_url = re.search(r'url\((.*?)\)', image_div['style']).group(1)
    
    # Download the image
    try:
        image_response = requests.get(image_url)
        image_bytes = image_response.content
        image = Image.open(BytesIO(image_bytes))
        #image = image.resize((100, 100), Image.LANCZOS)
        #tk_image = ImageTk.PhotoImage(image)
    except:
        pass
    
    # Extract the student name
    name_div = student_entry.find('div', {'class': 'directory-Entry_Title'})
    name = name_div.text.strip()
    name = name.split()[0]
    
    # Extract the student form
    form_div = student_entry.find('div', {'class': 'directory-Entry_Tag'})
    form_name = form_div.text.strip()
    
    # Save the data into the dictionary
    student_data[name] = {
        'image': image,
        'form': form_name
    }
with open("student_data.pkl", "wb") as f:
    pickle.dump(student_data, f)
print(student_data)

'''
# Print the student data (for demonstration purposes)
for name, data in student_data.items():
    print(f"Name: {name}, Form: {data['form']}")
    # Uncomment the line below to save the image to a file
    # with open(f"{name}.jpg", "wb") as f:
    #     f.write(data['image'])
'''
'''
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

# Initialize Tkinter window
root = tk.Tk()
root.title("Student Directory")

# Loop through the student_data dictionary to display images and information
row = 0
for name, data in student_data.items():
    try:
        # Convert image bytes to a PIL Image object
        image = Image.open(BytesIO(data['image']))
        
        # Resize the image
        image = image.resize((100, 100), Image.LANCZOS)
        
        # Convert PIL Image object to Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(image)
        
        # Create and place the image label
        img_label = tk.Label(root, image=tk_image)
        img_label.image = tk_image  # Keep a reference to prevent garbage collection
        img_label.grid(row=row, column=0)
        
    except Exception as e:
        print(f"Error displaying image for {name}: {e}")
    
    # Create and place the name label
    name_label = tk.Label(root, text=f"Name: {name}")
    name_label.grid(row=row, column=1)
    
    # Create and place the form label
    form_label = tk.Label(root, text=f"Form: {data['form']}")
    form_label.grid(row=row, column=2)
    
    row += 1

# Run the Tkinter event loop
root.mainloop()
'''