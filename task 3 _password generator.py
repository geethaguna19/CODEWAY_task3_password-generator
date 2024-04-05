from tkinter import*
from random import randint

root=Tk()
root.title(' password generator')
root.geometry("500x300")
root.config(bg="#68F1E2")

my_password=chr(randint(33,126))
def new_rand():
    # Clear Our Entry Box
    pw_entry.delete(0, END)

    # Get password Length And Convert To Integer

    pw_length= int(my_entry.get())

    # Create A Variable To Hold Our Password

    my_password=''

    # Loop Through The Pasword
    for x in range(pw_length):
          my_password += chr(randint(33, 126))

    # Output For The Screen
    pw_entry.insert(0,my_password)




    pass
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    pass

# Label Frame
lf=LabelFrame(root,text=('How many characters?'))
lf.pack(pady=20)

# Create Entry Box To Designate Number Of  Characters
my_entry = Entry(lf, font=("Helvetica",24))
my_entry.pack(pady=20,padx=20)

#Create Entry Box For Our Returned Passwords
pw_entry= Entry(root, text = '' , font=("Helvetica", 24 ),bd=0,bg="systembuttonface")
pw_entry.pack(pady=20)

# Create A frame for our buttons
my_frame=Frame(root)
my_frame.pack(pady=20)

# Create our buttons

my_button=Button(my_frame,text='generate a strong password',command=new_rand,bg="#F8FAA6")
my_button.grid(row=0,column=0,padx=10)

clip_button=Button(my_frame,text="copy to clip board",command=clipper)
clip_button.grid(row=0,column=1, padx=10)

root.mainloop()

