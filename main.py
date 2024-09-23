from tkinter import *
import requests as rq

def get_quote():
    
    response = rq.get(url= "https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()["quote"]
    print(data)

    canvas.itemconfig(quote_text, text=data,font=("Arial", 20, "italic"), fill="black")
    #Write your code here.


#Window setup
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

#Canvas
canvas = Canvas(width=300, height=414)
#bg image
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
#Text Quote
quote_text = canvas.create_text(150, 210, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")

#Button
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)


#UI layout
canvas.grid(row=0, column=0)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()