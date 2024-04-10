from tkinter import *
from pygame import mixer
import speech_recognition
import math

#intialization of mixer and add in audio in function
mixer.init()
#function for calculation
def click(value):
    ex=entryfield.get()  #collect value (789)
    answer=""
    try:
        if value=='C':
            ex=ex[0:len(ex)-1]  #remove value 1 by 1 (78)
            entryfield.delete(0,END)  #delete every this
            entryfield.insert(0,ex)   #insert value after delete one value 9
            return
        elif value=='CE':
            entryfield.delete(0,END)
            
        elif value=='√':
            answer=math.sqrt((eval(ex)))   #why we not use int not convert float to int 4-0.2 but 0.2-error
                                        #eval convert it in int
        elif value=="π":
            answer=math.pi
        elif value=="cosθ":
            answer=math.cos(math.radians(eval(ex)))
        elif value=="tanθ":
            answer=math.tan(math.radians(eval(ex)))
        elif value=="sinθ":
            answer=math.sin(math.radians(eval(ex)))
        elif value=="2π":
            answer=2*math.pi
        elif value=="cosh":
            answer=math.cosh(eval(ex)) #cas-h where h hyperbolic
        elif value=="tanh":
            answer=math.tanh(eval(ex))
        elif value=="sinh":
            answer=math.sinh(eval(ex))
            
        elif value==chr(8731):  #for cube root
            answer=eval(ex)**(1/3)
            
        elif value=='x\u02b8' :   #for x to the power y 2**2=4 
            entryfield.insert(END,'**')  #it do 2**3 where 2 user input we calculate this using = later
            return
        elif value=='x\u00B3': # cube of x,2**3=8
            answer=eval(ex)**3
            
        elif value=="x\u00B2":  #square of x,2**2=4
            answer=eval(ex)**2
        elif value=="log2":   
            answer=math.log2(eval(ex))
        elif value=='deg':
            answer=math.degrees(eval(ex))
        elif value=='rad':
            answer=math.radians(eval(ex))
        elif value=='e':
            answer=math.e
        elif value=='log10':
            answer=math.log10(eval(ex))
        elif value=='x!':
            answer=math.factorial(eval(ex))
        elif value=='/':
            entryfield.insert(END,"/")
            return  #if we not write return and we add 7 and click / 7 is auto delete
        elif value=='=':
            answer=eval(ex)
        else:
            entryfield.insert(END,value)
            return #contro should not go last two line delete insert otherwise all input will be delete 
        entryfield.delete(0,END)  #delete every this
        entryfield.insert(0,answer)
    except (SyntaxError,ZeroDivisionError):
        entryfield.delete(0,END)
        entryfield.insert(0,"Error")
# define function to perform opertaion for voice input
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm(a,b):
    l=math.lcm(a,b)
    return l
def hcf(a,b):
    h=math.gcd(a,b)
    return h

#create a dictionary for call these function with different name as key

opertaions={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub,'DIFFERENCE':sub,'MINUS':sub,'SUBTRACT':sub,
            'PRODUCT':mul,'MULTIPLICATION':mul,'MULTIPLY':mul,
            'DIVISION':div,'DIV':div,'DIVIDE':div,
            'LCM':lcm,'HCF':hcf,
            'MOD':mod,'REMAINDER':mod,'MODULUS':mod,}

# function to find a number from the list
def findnumber(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l
#function for audio play and input,output
def audio():
    #for loading a file
    mixer.music.load('music1.mp3')
    
    #for play the audio
    mixer.music.play()
    
    # create object for recognizers class
    sr=speech_recognition.Recognizer()
    
    #create microphone class object with help of keyword (with)
    with speech_recognition.Microphone()as m:   #with keyword use to avoid inseption
        try:
            sr.adjust_for_ambient_noise(m,duration=0.5)          # use to set the gap between sentences
            voice=sr.listen(m)                                   #listen microphone voice using listen method
            text=sr.recognize_google(voice)                         #sr.recognize_google(voice) (user to convert voice into text)
            print(text)
            mixer.music.load('music2.mp3')                        
            mixer.music.play()
            text_list=text.split(" ")
            print(text_list)
            for word in text_list:
                if word.upper() in opertaions.keys():
                    l=findnumber(text_list)                 #create a function to find a number in list
                    result=opertaions[word.upper()](l[0],l[1])  #call the function using key [add](a,b)=> add(a,b)
                    entryfield.delete(0,END)
                    entryfield.insert(END,result)
                else:
                    pass  #its work when you not speak keys(mul,lcm,hec etc)
        except:  #when your voice is not clear the except block run
            pass
           
root=Tk()
root.title("Voice Calculater")
root.config(bg="blue")
root.geometry("680x486+100+100") #680x486 is widthxheight and distance from x-axis and y-axis

#add calculater image
logoImage=PhotoImage(file="logo.png")
logoLabel=Label(root,image=logoImage,bg='blue')
logoLabel.grid(row=0,column=0)
#add voice image and button
miceImage=PhotoImage(file='microphone.png')
miceLabel=Button(root,image=miceImage,bg='blue',bd=0,activebackground='blue',command=audio)
miceLabel.grid(row=0,column=7)

#add entry field
entryfield=Entry(root,font=('arial',20,'bold'),bg='blue',fg='white',bd=10,relief=SUNKEN,width=30)
entryfield.grid(row=0,column=0,columnspan=8)  #colspan give a space to 8 column

#list of buttons which we need to add
button_list=[
    "C","CE","√","+","π","cosθ","tanθ","sinθ",
    "1","2","3","-","2π","cosh","tanh","sinh",
    "4","5","6","*",chr(8731),"x\u02b8","x\u00B3","x\u00B2",
    "7","8","9",'/',"log2","deg","rad","e",
    "0",".","%","=","log10","(",")","x!" ]
rowvalue=1
columnvalue=0
for i in button_list:
    button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='blue',fg='white'
    ,font=('arial',18,'bold'),activebackground='blue',command=lambda button=i:click(button))
     #click function and we call it

    button.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue+=1
    if columnvalue>7:
        rowvalue+=1
        columnvalue=0

root.mainloop()
