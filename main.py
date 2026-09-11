import tkinter as tk

bg_color="#1a1424"
fg_color="#412c64"
button_bg_color="#0e9419"
button_fg_color="#ffffff"
a_button_bg_color="#034B09"
a_button_fg_color="#ffffff"

textFont="Montserrat"
textFont_type="bold"
click_qty=0
seconds=10
start_sec=3

cpsList=[]

root=tk.Tk()
root.title("CPS TEST")
root.geometry("250x220")
root.configure(bg=bg_color)

best_cps_label=tk.Label(root,
                    text="BEST CPS: ---",
                    font=(textFont,14,textFont_type),
                    bg=bg_color,
                    fg=fg_color,
                    )
best_cps_label.pack(padx=10, pady=10)

timer_label=tk.Label(root,
               text="10 SEGUNDOS",
               font=(textFont,14,textFont_type),
               bg=bg_color,
               fg=fg_color,
               )
timer_label.pack(pady=12)

def cont_click():
    
    global click_qty
    click_qty+=1
    botao.config(text=str(click_qty))
    if click_qty==1:
        calc_cps()

def calc_cps():

    global seconds
    timer_label.config(
        text=f"{seconds}"
    )
    
    if seconds>0:
        seconds -= 1
        root.after(1000, calc_cps)
    else:
        cps=click_qty/10
        cpsList.append(cps)

        timer_label.config(
                    text=f"CPS: {cps}")
        botao.config(text="INICIAR",
                    font=(textFont,10,textFont_type),
                    activebackground=button_bg_color,
                    bg=button_bg_color,
                    fg=button_fg_color,
                    command="",)
        
        best_cps=max(cpsList)
        best_cps_label.config(text=f"BEST CPS: {best_cps}")
        root.after(2000, reset_to_default)

def reset_to_default():

    global click_qty
    global seconds
    click_qty=0
    seconds=10
    botao.config(
                text=f"INICIAR",
                font=(textFont,10,textFont_type),
                command=cont_click,
                fg=button_fg_color,
                bg=button_bg_color,
                activebackground=a_button_bg_color,
                activeforeground=a_button_fg_color,)
    timer_label.config(text="10 SEGUNDOS")

botao=tk.Button(root, 
                text=f"INICIAR",
                font=(textFont,10,textFont_type),
                command=cont_click,
                fg=button_fg_color,
                bg=button_bg_color,
                activebackground=a_button_bg_color,
                activeforeground=a_button_fg_color,
                width=200,
                height=50,
                )
botao.pack()

root.mainloop()
