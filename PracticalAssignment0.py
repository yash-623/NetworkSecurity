# Firstly import the modules necessary to design the GUI
import tkinter as tk
from tkinter import ttk

#PART A : Contains the encryption and decryption function of the algorithm

def encryption(inputString):	    
	outputString =""
	for i in range(len(inputString)):
		letter = inputString[i]
		if letter.islower():
			letter = ord(letter)
			letter -=97
			etter = letter %26
			letter = 122 - letter
			outputString += chr(letter)
		elif letter.isupper():
			letter = ord(letter)
			letter -=65
			letter = letter %26
			letter = 90 - letter
			outputString += chr(letter)
		elif letter == " " :
			outputString += " "
		else:
			outputString += letter
	return outputString
	
def decryption(inputString):
	outputString =""
	for i in range(len(inputString)):
		letter = inputString[i]
		if letter.islower():
			letter = ord(letter)
			letter -=97
			etter = letter %26
			letter = 122 - letter
			outputString += chr(letter)
		elif letter.isupper():
			letter = ord(letter)
			letter -=65
			letter = letter %26
			letter = 90 - letter
			outputString += chr(letter)
		elif letter == " " :
			outputString += " "
		else:
			outputString += letter
	return outputString
	

# PART B : This contains the code for the GUI made using Tkinter package
class GUI:
	
	    def __init__(self, root):
	
	        self.inputString = tk.StringVar(root, value="")
	        self.encryptedString = tk.StringVar(root, value="")
	        self.key = tk.IntVar(root)

	        # Setting Window Title to GUI
	        root.title("Practical Assignment 0")
	        # Making window resizable
	        root.resizable(True,True)
	       
	       # LABEL TO DENOTE THE INPUT STRING
	        self.labelInput = tk.Label(root, text="INPUT STRING ",font = ('Arial' , 20), anchor = "w")
	        self.labelInput.grid(row=1, column=1)

	        # TEXTBOX TO TAKE INPUT STRING FROM USER 
	        self.textboxInput= tk.Entry(root, textvariable = self.inputString, font = ('Arial' , 20), bd = 8, bg = "yellow", insertwidth = 4, width=32)
	        self.textboxInput.grid(row=2, column=0, rowspan=2 , columnspan=2)
	        
	        # BUTTON TO CLEAR THE ABOVE TEXTBOX
	        self.buttonInput = tk.Button(root, text="CLEAR", fg="red", command=lambda: self.clear('input'))
	        self.buttonInput.grid(row=4, column=1)
	
	        # BUTTON TO PERFORM ENCRYPTION
	        self.buttonEncrypt = tk.Button(root, text="Encrypt", command=lambda: self.performEncryption())
	        self.buttonEncrypt.grid(row=2, column=3)

        	# BUTTON TO PERFORM DECRYPTION
	        self.buttonDecrypt = tk.Button(root, text="Decrypt", command=lambda: self.performDecryption())
	        self.buttonDecrypt.grid(row=3, column=3)
			
			# LABEL TO DENOTE THE ENCRYPTED STRING
	        self.labelEncrypt = tk.Label(root, text="ENCRYPTED STRING",font = ('Arial' , 20), anchor = "w" )
	        self.labelEncrypt.grid(row=1, column=4)

	        # TEXTBOX TO DISPLAY THE ENCRYPTED STRING
	        self.textboxEncrypt = tk.Entry(root, textvariable = self.encryptedString , font = ('Arial' , 20), bd = 8, bg = "yellow", insertwidth = 4, width=32)
	        self.textboxEncrypt.grid(row=2, column=4, rowspan=2 , columnspan=2)
		
			# BUTTON TO CLEAR THE ABOVE TEXTBOX
	        self.buttonEncrypt = tk.Button(root, text="CLEAR", fg="red", command=lambda: self.clear('encrypted'))
	        self.buttonEncrypt.grid(row=4, column=4)

	    #FUNCTION TO ENCRYPT THE USER INPUT STRING
	    def performEncryption(self):
	        encryptedString = encryption(self.textboxInput.get())
	        self.textboxEncrypt.delete(0, "end")
	        self.textboxEncrypt.insert(0, encryptedString)

		#FUNCTION TO DECRYPT THE USER INPUT STRING
	    def performDecryption(self):
	        inputString = decryption(self.textboxEncrypt.get())
	        self.textboxInput.delete(0, "end")
	        self.textboxInput.insert(0, inputString)
	
		#FUNCTION TO CLEAR THE TEXTBOXS
	    def clear(self, str_val):
	        if str_val == 'input':
	            self.textboxInput.delete(0, 'end')
	        else:
	            self.textboxEncrypt.delete(0, 'end')


# Start the GUI window
root = tk.Tk()
test = GUI(root)
root.mainloop()