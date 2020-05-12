# Import tkinter module and all classes from it to create perfect GUI
from tkinter import *
from tkinter import filedialog

# Class For Menubar :)
class Menubar:
	def __init__(self, master):
		text_font = ("Consolas", 10)

		menubar = Menu(master.root, font = text_font)
		master.root.config(menu = menubar)

		# Create file dropdown where will located commands - Save, Save as, New File, Open File, Exit
		file_dd = Menu(menubar, font = text_font, tearoff = 0)
		file_dd.add_command(label = "New File", accelerator = "Ctrl+N", command = master.new_file)
		file_dd.add_command(label = "Save", accelerator = "Ctrl+S", command = master.save)
		file_dd.add_command(label = "Save as", accelerator = "Ctrl+Shift+S", command = master.save_as)
		file_dd.add_command(label = "Open File", accelerator = "Ctrl+O", command = master.open_file)
		# Add separator, because it will be more beautiful(I think)
		file_dd.add_separator()
		file_dd.add_command(label = "Exit", command = master.root.destroy)

		# Now add our cascade to our menubar :)
		menubar.add_cascade(label = "File", menu = file_dd)

		# Create Font Drop Down
		file_fs = Menu(menubar, font = text_font, tearoff = 0)
		file_fs.add_command(label = "Consolas", command = master.set1)
		file_fs.add_command(label = "Ubuntu", command = master.set2)
		file_fs.add_command(label = "System", command = master.set3)
		file_fs.add_command(label = "Terminal", command = master.set4)
		file_fs.add_command(label = "Modern", command = master.set5)
		file_fs.add_command(label = "Roman", command = master.set6)
		file_fs.add_command(label = "Script", command = master.set7)
		file_fs.add_command(label = "Arial", command = master.set8)
		file_fs.add_command(label = "Tahoma", command = master.set9)
		file_fs.add_command(label = "Onyx", command = master.set10)

		menubar.add_cascade(label = "Font Style", menu = file_fs)

		# Create "UI Themes" cascade
		file_ui = Menu(menubar, font = text_font, tearoff = 0)
		file_ui.add_command(label = "Dark Theme", command = master.ui_dark)
		file_ui.add_command(label = "Ocean Theme", command = master.ui_ocean)
		file_ui.add_command(label = "White/Yellow Theme", command = master.ui_mocha)
		file_ui.add_command(label = "White Theme", command = master.ui_white)

		menubar.add_cascade(label = "UI Themes", menu = file_ui)

# Status Bar Class :)
class StatusBar:
	def __init__(self, master):
		# Class where we create status bar :)

		# Create string variable, and set equal for it
		self.status = StringVar()
		self.status.set("Bandera`s Writer - 1.0")

		# Also statusbar
		statustext = Label(master.text, textvariable = self.status, fg = "red", bg = "black", anchor = "sw", font = "Onyx 12")
		statustext.pack(side = BOTTOM, fill = BOTH)

# Main Class :)
class TextClass:
	def __init__(self, root):
		# Just set window title, standart width and height and icon :)
		root.title("Untitled - Bandera`s Writer")
		root.geometry("920x640")
		root.iconbitmap("icon.ico")

		self.root = root
		self.filename = None

		# Create our text area and scrollbar for it :)
		self.text = Text(root, wrap = WORD)
		self.scroll = Scrollbar(root, command = self.text.yview)
		self.text.configure(yscrollcommand = self.scroll.set)
		self.text.pack(side = LEFT, fill = BOTH, expand = True)
		self.scroll.pack(side = RIGHT, fill = Y)

		# Create our menubar :)
		self.menubar = Menubar(self)
		self.statusbar = StatusBar(self)

		# Bind shortcuts :)
		self.shortcuts()

	# This method help us to set window title, example: if we open file "main.py" then window title will changed for "{path for file main.py}\main.py"
	def set_window_title(self, name = None):
		if name:
			self.root.title(name + " - Bandera`s Writer")
		else:
			self.root.title("Untitled - Bandera`s Writer")

	# Method that help us clear textarea and create new file :)
	def new_file(self, *args):
		self.text.delete(1.0, END)
		self.filename = None
		self.set_window_title()

	# Save file method :)
	def save(self, *args):
		if self.filename:
			try:
				text_content = self.text.get(1.0, END)
				with open(self.filename, "w") as f:
					f.write(text_content)
			except Exception as e:
				pass
		else:
			self.save_as()

	# Save as file method :)
	def save_as(self, *args):
		try:
			new_file = filedialog.asksaveasfilename(initialfile = "LetterToBandera.txt", defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Files"), ("MarkDown Documents", "*.md"), ("RTF Files", "*.rtf"), ("Python Files", "*.py"), ("C# Files", "*.cs"), ("C++ Files", "*.cpp"), ("Header Files", "*.h"), ("C Files", "*.c"), ("Ruby Scripts", "*.rb"), ("JavaScript", "*.js"), ("Java Files", "*.java"), ("PHP Files", "*.php"), ("HTML Document", "*.html"), ("CSS Document", "*.css")])
			text_content = self.text.get(1.0, END)
			with open(new_file, "w") as f:
				f.write(text_content)
			self.filename = new_file
			self.set_window_title(self.filename)
		except Exception as e:
			pass

	# Method that help us open files :)
	def open_file(self, *args):
		self.filename = filedialog.askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Files"), ("MarkDown Documents", "*.md"), ("RTF Files", "*.rtf"), ("Python Files", "*.py"), ("C# Files", "*.cs"), ("C++ Files", "*.cpp"), ("Header Files", "*.h"), ("C Files", "*.c"), ("Ruby Scripts", "*.rb"), ("JavaScript", "*.js"), ("Java Files", "*.java"), ("PHP Files", "*.php"), ("HTML Document", "*.html"), ("CSS Document", "*.css")])
		if self.filename:
			self.text.delete(1.0, END)
			with open(self.filename, "r") as f:
				self.text.insert(1.0, f.read())
			self.set_window_title(self.filename)

	# From this place all methods "set{and some number}" is helping us to set font for textarea :)
	def set1(self):
		self.text.config(font = ("Consolas", 16))

	def set2(self):
		self.text.config(font = ("Ubuntu", 16))

	def set3(self):
		self.text.config(font = ("System", 16))

	def set4(self):
		self.text.config(font = ("Terminal", 16))

	def set5(self):
		self.text.config(font = ("Modern", 16))

	def set6(self):
		self.text.config(font = ("Roman", 16))

	def set7(self):
		self.text.config(font = ("Script", 16))

	def set8(self):
		self.text.config(font = ("Arial", 16))

	def set9(self):
		self.text.config(font = ("Tahoma", 16))

	def set10(self):
		self.text.config(font = ("Onyx", 16))

	# Methods to setup themes :)
	def ui_dark(self):
		self.text.config(bg = "black", fg = "white")

	def ui_ocean(self):
		self.text.config(bg = "cyan", fg = "darkgrey")

	def ui_mocha(self):
		self.text.config(bg = "white", fg = "yellow")

	def ui_white(self):
		self.text.config(bg = "white", fg = "black")

	# Bind shortcuts, commands with file that will execute if we press down some keys :)
	def shortcuts(self):
		self.text.bind("<Control-n>", self.new_file)
		self.text.bind("<Control-s>", self.save)
		self.text.bind("<Control-S>", self.save_as)
		self.text.bind("<Control-o>", self.open_file)

# Also Mainloop :)
if __name__ == "__main__":
	root = Tk()
	t = TextClass(root)
	root.mainloop()
