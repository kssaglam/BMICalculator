from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.config(padx=20, pady=20)
window.minsize(width=150, height=250)
char_list = ["0","1","2","3","4","5","6","7","8","9"]
def calculator():
    user_weight = weight_entry.get()
    user_height = height_entry.get()
    if user_weight and user_height:
        if user_weight.isdigit() and user_height.isdigit():
            calculated_BMI = int(user_weight)/ (int(user_height)/100)**2
            if calculated_BMI < 18.5:
                result_label.config(text=" BMI: {:.2f}\nZayıf".format(calculated_BMI))
            elif calculated_BMI>=18.5 and calculated_BMI <25:
                result_label.config(text="BMI: {:.2f}\nNormal".format(calculated_BMI))
            elif calculated_BMI >=25 and calculated_BMI<30:
                result_label.config(text="BMI: {:.2f}\nKilolu".format(calculated_BMI))
            elif calculated_BMI >=30 and calculated_BMI< 35:
                result_label.config(text="BMI: {:.2f}\nSeviye-I Obez".format(calculated_BMI))
            elif calculated_BMI >=35 and calculated_BMI<40:
                result_label.config(text="BMI: {:.2f}\nSeviye-II Obez".format(calculated_BMI))
            elif calculated_BMI >=40:
                result_label.config(text="BMI: {:.2f}\nSeviye-III Obez".format(calculated_BMI))
        else:
            result_label.config(text="Enter a valid number!")
    else:
        result_label.config(text="Enter both weight and height!")



weight_label = Label(text="Enter Your Weight (kg)")
weight_label.pack()

weight_entry = Entry()
weight_entry.pack()

height_label = Label(text="Enter Your Height (cm)")
height_label.pack()

height_entry = Entry()
height_entry.pack()

calc_button = Button(text="Calculate", command=calculator)
calc_button.pack()

result_label = Label()
result_label.config(pady=50)
result_label.pack()



window.mainloop()