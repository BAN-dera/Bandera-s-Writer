# Import tkinter to create GUI
from tkinter import *
from tkinter import filedialog

# Create some functions :)
def set_window_title(name = None):
	if name:
		root.title(name + " - Bandera`s Writer")
	else:
		root.title("Untitled - Bandera`s Writer")

def new_file():
	textarea.delete(1.0, END)
	filename = None
	set_window_title()

def open_file():
	filename = filedialog.askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Files"), ("MarkDown Documents", "*.md"), ("RTF Files", "*.rtf"), ("Python Files", "*.py"), ("C# Files", "*.cs"), ("C++ Files", "*.cpp"), ("Header Files", "*.h"), ("C Files", "*.c"), ("Ruby Scripts", "*.rb"), ("JavaScript", "*.js"), ("Java Files", "*.java"), ("PHP Files", "*.php"), ("HTML Document", "*.html"), ("CSS Document", "*.css")])
	if filename:
		textarea.delete(1.0, END)
		with open(filename, "r") as f:
			textarea.insert(1.0, f.read())
		set_window_title(filename)

def save():
	if filename:
		try:
			textarea_content = text.get(1.0, END)
			with open(filename, "w") as f:
				f.write(textarea_content)
		except Exception:
			pass
	else:
		save_as()

def save_as():
	try:
		new_file = filedialog.asksaveasfilename(initialfile = "LetterToBandera.txt", defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Files"), ("MarkDown Documents", "*.md"), ("RTF Files", "*.rtf"), ("Python Files", "*.py"), ("C# Files", "*.cs"), ("C++ Files", "*.cpp"), ("Header Files", "*.h"), ("C Files", "*.c"), ("Ruby Scripts", "*.rb"), ("JavaScript", "*.js"), ("Java Files", "*.java"), ("PHP Files", "*.php"), ("HTML Document", "*.html"), ("CSS Document", "*.css")])
		textarea_content = textarea.get(1.0, END)
		with open(new_file, "w") as f:
			f.write(textarea_content)
		filename = new_file
		set_window_title(filename)
	except Exception:
		pass

def set1():
	text_style = "Consolas"
	textarea.config(font = "Consolas 16")

def set2():
	text_style = "Ubuntu"
	textarea.config(font = "Ubuntu 16")

def set3():
	text_style = "System"
	textarea.config(font = "System 16")

def set4():
	text_style = "Terminal"
	textarea.config(font = "Terminal 16")

def set5():
	text_style = "Modern"
	textarea.config(font = "Modern 16")

def set6():
	text_style = "Roman"
	textarea.config(font = "Roman 16")

def set7():
	text_style = "Script"
	textarea.config(font = "Script 16")

def set8():
	text_style = "Arial"
	textarea.config(font = "Arial 16")

def set9():
	text_style = "Tahoma"
	textarea.config(font = "Tahoma 16")

def set10():
	text_style = "Onyx"
	textarea.config(font = "Onyx 16")

# Create window and set window title, icon, standart width and height
root = Tk()
root.geometry("720x560")
root.title("Untitled - Bandera`s Writer")
root.iconbitmap("icon.ico")

# Create graphic objects :)


# Textarea and scrollbar!
textarea = Text(root, fg = "white", bg = "grey", wrap = WORD)
scroll = Scrollbar(root, command = textarea.yview)
textarea.configure(yscrollcommand = scroll.set)
textarea.pack(side = LEFT, fill = BOTH, expand = True)
scroll.pack(side = RIGHT, fill = Y)

# Create our menubar :)
menu_font = ("Consolas", 10)

menubar = Menu(root, font = menu_font)
root.config(menu = menubar)

# Create "File" cascade
file_dd = Menu(menubar, font = menu_font, tearoff = 0)
file_dd.add_command(label = "New File", command = new_file)
file_dd.add_command(label = "Open File", command = open_file)
file_dd.add_command(label = "Save", command = save)
file_dd.add_command(label = "Save as", command = save_as)
file_dd.add_separator()
file_dd.add_command(label = "Exit", command = root.destroy)

# Add our "File" cascade to menubar
menubar.add_cascade(label = "File", menu = file_dd)

# Create "Font Style" cascade
file_fs = Menu(menubar, font = menu_font, tearoff = 0)
file_fs.add_command(label = "Consolas", command = set1)
file_fs.add_command(label = "Ubuntu", command = set2)
file_fs.add_command(label = "System", command = set3)
file_fs.add_command(label = "Terminal", command = set4)
file_fs.add_command(label = "Modern", command = set5)
file_fs.add_command(label = "Roman", command = set6)
file_fs.add_command(label = "Script", command = set7)
file_fs.add_command(label = "Arial", command = set8)
file_fs.add_command(label = "Tahoma", command = set9)
file_fs.add_command(label = "Onyx", command = set10)

# Add our "Font Style" cascade
menubar.add_cascade(label = "Font Style", menu = file_fs)

# Create statusbar
status = StringVar()
status.set("Bandera`s Writer - 1.0")

statuslabel = Label(textarea, textvariable = status, fg = "red", bg = "black", anchor = "sw", font = "Onyx 12")
statuslabel.pack(side = BOTTOM, fill = BOTH)

# Mainloop
root.mainloop()
