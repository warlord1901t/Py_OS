#Changes to be made in line numbers: 26 , 2952 , 3313

#importing Modules
from tkinter import *
import time
import subprocess

#installing shutil and distutil
#uncomment if distutil and shutil are not installed
'''try:
    try:
        subprocess.run(["pip", "install", "shutil"])
        print("shutil installed successfully.")
    except:
        print("shutil not installed.")
    finally:
        subprocess.run(["pip", "install", "distutil"])
        print("distutil installed successfully.")
except Exception as e:
    print(f"Error: {e}")'''

#creating main window    
win = Tk()
win.title("Py_Os")
win.config(bg="black") 
win.geometry("400x600")
win.resizable(False,False)
favicon_path = "path_to_favicon.ico"          #Replace the path 
win.iconbitmap(favicon_path)

#setting none values initially to global variables
BMI_Frame=None
BMR_Frame=None
TDEE_Frame=None
MHR_Frame=None
BMI_title_Label=None
BMR_title_Label=None
TDEE_Title_Label=None
MHR_Title_Label=None
BMI_Frame=None
BMR_Frame=None
TDEE_Frame=None
MHR_Frame=None
BMI_title_Label=None
BMR_title_Label=None
TDEE_Title_Label=None
MHR_Title_Label=None


#creating data collection structures
my_dict={}
s1_history=[]
s2_history=[]
i=0
j=0
sent_photos1=[]
recieved_photos1=[]
sent_photos2=[]
recieved_photos2=[]
sent_videos1=[]
recieved_videos1=[]
sent_videos2=[]
recieved_videos2=[]
s1_transact_history=[]
s2_transact_history=[]
media_storage_1=[]
media_storage_2=[]


#creating 2nd window for chat app
global win2
win2 = Tk()
win2.geometry("400x600")
win2.title("Chat win2dow")
win2.config(bg="black")



'''Apps'''
# fitness app
def fitness_app():
    def fitness_interface():
        global MHR_val,TDEE_val,BMR_val,BMI_val
        MHR_val=None
        TDEE_val=None
        BMR_val=None
        BMI_val=None
        tdee=None
        
        Interface=Frame(win,width=400,height=600)
        Interface.place(x=0,y=0)

        MainOptions=Frame(Interface,bg="Red",width=400,height=600)

        

        def Fitness_Calculator_Interface():
            Fitness_Calculator_Frame=Frame(Interface,width=400,height=600,bg="black")
            Fitness_Calculator_Frame.place(x=0,y=0)
                
                
                
            def BMI_Interface():
                global BMI_title_Label,BMI_Frame
                try:
                    del_BMI()
                except:
                    print("error")
                finally:
                    BMI_title_Label = Label(Interface, text="BMI Calculator", font="Purisa 20 bold", bg="red", fg="yellow")
                    BMI_title_Label.pack(side="top", fill=X)

                    BMI_Frame = Frame(Interface, bg="Black", height=600, width=400)

                    def del_BMI():
                        BMI_title_Label.destroy()
                        BMI_Frame.destroy()

                    Exit_Interface=Button(BMI_title_Label,text="Back",relief="solid",bg="red",fg="White",bd=1,command=del_BMI)
                    Exit_Interface.pack(side="right",padx=10)

                    BMI_Weight_Frame = Frame(BMI_Frame, bg="Yellow", height=105, width=150)
                    BMI_Weight_Frame.place(x=30, y=100)

                    BMI_Weight_Label = Label(BMI_Frame, bg="black", fg="White", text="Weight in kg", font=("Purisa 15 bold"), width=11)
                    BMI_Weight_Label.place(x=35, y=105)

                    BMI_Weight_Entry = Entry(BMI_Frame, font=("Purisa 15 bold"), width=11, bd=2, cursor="xterm", justify='center')
                    BMI_Weight_Entry.place(x=40, y=155)

                    BMI_Height_Frame = Frame(BMI_Frame, bg="yellow", height=105, width=150)
                    BMI_Height_Frame.place(x=220, y=100)

                    BMI_Height_Label = Label(BMI_Frame, bg="black", fg="White", text="Height in cm", font=("Purisa 15 bold"), width=11)
                    BMI_Height_Label.place(x=225, y=105)

                    BMI_Height_Entry = Entry(BMI_Frame, font=("Purisa 15 bold"), width=11, bd=2, cursor="xterm", justify='center')
                    BMI_Height_Entry.place(x=230, y=155)

                    def calculate_bmi():
                        try:
                            weight_val = float(BMI_Weight_Entry.get())
                            height_val = float(BMI_Height_Entry.get()) / 100

                            BMI_Warning = Label(BMI_Frame, text="", font=("Purisa 15 bold"), bg="black", fg="red")  
                            BMI_Warning.place_forget()

                            global BMI_val

                            BMI_val = weight_val / (height_val ** 2)
                            BMI_Result = Label(BMI_Frame, text=f"BMI: {BMI_val:.2f}", font=("Purisa 15 bold"), bg="black", fg="green")
                            BMI_Result.place(x=150, y=300)

                        except ValueError:
                            BMI_Warning = Label(BMI_Frame, text="Please enter NUMERIC VALUES only", font=("Purisa 10 bold"), bg="black", fg="red")
                            BMI_Warning.place(x=90, y=300)
                            win.after(2000,lambda:BMI_Warning.destroy())


                    BMI_Calculate_Button = Button(BMI_Frame, font=("Purisa 15 bold"), text="Calculate", bd=2, cursor="hand2", bg="blue", fg="white", command=calculate_bmi)
                    BMI_Calculate_Button.place(x=150, y=230)

                    BMI_Frame.pack(fill=Y)

            def BMR_interface():
                global BMR_title_Label,BMR_Frame
                try:
                    del_BMR()
                except:
                    print("error")
                finally:
                    global Gender_male, Gender_female, BMR_title_Label, BMR_Frame, BMR_Weight_Entry, BMR_Height_Entry, BMR_Age_Entry, value1, value2, value3, value4, BMR_Warning,BMR_val
                    value1 = 0
                    value2 = 0
                    value3 = 0
                    value4 = 0

                    
                    def male_Button_pressed():
                        global value1, value2, value3, value4
                        Gender_female.config(bg="gray", fg="black")
                        Gender_male.config(bg="Blue", fg="White")
                        value1 = 88.362
                        value2 = 13.397
                        value3 = 4.799
                        value4 = 5.677

                    def female_Button_pressed():
                        global value1, value2, value3, value4
                        Gender_male.config(bg="gray", fg="black")
                        Gender_female.config(bg="Light Pink", fg="White")
                        value1 = 447.593
                        value2 = 9.247
                        value3 = 3.098
                        value4 = 4.330

                    BMR_title_Label = Label(Interface, text="BMR Calculator", font="Purisa 20 bold", bg="red", fg="yellow")
                    BMR_title_Label.pack(side="top", fill=X)

                    BMR_Frame = Frame(Interface, bg="Black", height=600, width=400)

                    def del_BMR():
                        BMR_title_Label.destroy()
                        BMR_Frame.destroy()

                    Exit_Interface=Button(BMR_title_Label,text="Back",relief="solid",bg="red",fg="White",bd=1,command=del_BMR)
                    Exit_Interface.pack(side="right",padx=10)

                    Gender_male = Button(BMR_Frame, bg="gray", fg="black", text="♂ Male", font=("Purisa 15 bold"), width=10,command=male_Button_pressed)
                    Gender_male.place(x=50, y=50)
                    Gender_female = Button(BMR_Frame, bg="gray", fg="black", text="♀ Female", font=("Purisa 15 bold"), width=10, command=female_Button_pressed)
                    Gender_female.place(x=200, y=50)

                    BMR_Weight_Label = Label(BMR_Frame, text="Weight in kg:", font=("Purisa 15 bold"), fg="white", bg="black")
                    BMR_Weight_Label.place(x=60, y=120)
                    BMR_Weight_Entry = Entry(BMR_Frame, font=("Purisa 15 bold"), width=11, justify="center")
                    BMR_Weight_Entry.place(x=200, y=120)

                    BMR_Height_Label = Label(BMR_Frame, text="Height in cm:", font=("Purisa 15 bold"), fg="white", bg="black")
                    BMR_Height_Label.place(x=60, y=160)
                    BMR_Height_Entry = Entry(BMR_Frame, font=("Purisa 15 bold"), width=11, justify="center")
                    BMR_Height_Entry.place(x=200, y=160)

                    BMR_Age_Label = Label(BMR_Frame, text="Age:", font=("Purisa 15 bold"), fg="white", bg="black")
                    BMR_Age_Label.place(x=100, y=200)
                    BMR_Age_Entry = Entry(BMR_Frame, font=("Purisa 15 bold"), width=11, justify="center")
                    BMR_Age_Entry.place(x=200, y=200)

                    def calculate_bmr():
                        global BMR_Weight_Entry, BMR_Height_Entry, BMR_Age_Entry, BMR_Frame, value1, value2, value3, value4,BMR_Warning,BMR_val
                        
                        weight_val =(BMR_Weight_Entry.get())
                        height_val =(BMR_Height_Entry.get())
                        age_val =(BMR_Age_Entry.get())
                        if weight_val.isnumeric()==False or height_val.isnumeric()==False or age_val.isnumeric()==False:
                            BMR_Warning = Label(BMR_Frame, text="Please enter NUMERIC VALUES only", font=("Purisa 10 bold"), bg="black", fg="red")
                            BMR_Warning.place(x=90, y=300)
                            win.after(2000,lambda:BMR_Warning.destroy())
                        else:
                            weight_val=float(weight_val)
                            height_val=float(height_val)
                            age_val=float(age_val)
                            if value1 == 0 or value2 == 0 or value3 == 0 or value4==0:
                                BMR_Warning = Label(BMR_Frame, text="Please Select Any One Gender", font=("Purisa 10 bold"), bg="black", fg="red")
                                BMR_Warning.place(x=100, y=300)
                                win.after(2000,lambda:BMR_Warning.destroy())
                            else:
                                try:
                                    print(f"Weight: {weight_val}, Height: {height_val}, Age: {age_val}")
                                    print(f"Constants: {value1}, {value2}, {value3}, {value4}")

                                    BMR_val = value1 + (value2 * weight_val) + (value3 * height_val) - (value4 * age_val)

                                    if BMR_val <= 1500:
                                        BMR_Result = Label(BMR_Frame, text=f"BMR: {BMR_val:.2f}", font=("Purisa 15 bold"), bg="light goldenrod", fg="black")
                                        BMR_Result.place(x=135, y=320)
                                    elif 1500 < BMR_val < 1800:
                                        BMR_Result = Label(BMR_Frame, text=f"BMR: {BMR_val:.2f}", font=("Purisa 15 bold"), bg="light green", fg="Black")
                                        BMR_Result.place(x=135, y=320)
                                    else:
                                        BMR_Result = Label(BMR_Frame, text=f"BMR: {BMR_val:.2f}", font=("Purisa 15 bold"), bg="red", fg="white")
                                        BMR_Result.place(x=135, y=320)

                                    def TDEE_interface():
                                        from tkinter import ttk
                                        try:
                                            del_TDEE()
                                        except:
                                            print(f"Error")
                                        finally:
                                            try:
                                                del_BMR()
                                            except:
                                                print("None")

                                        global TDEE_Frame, TDEE_Title_Label, TDEE_slider, activity_label,BMR_val

                                        TDEE_Title_Label = Label(Interface, text=" Total Daily Energy Expenditure", font="Purisa 15 bold", bg="Black", fg="White",anchor="w")
                                        TDEE_Title_Label.pack(side="top", fill=X)

                                        TDEE_Frame = Frame(Interface, bg="white", height=600, width=400)
                                        TDEE_Frame.pack(fill=Y)

                                        def del_TDEE():
                                            TDEE_Title_Label.destroy()
                                            TDEE_Frame.destroy()

                                        Exit_Interface_TDEE=Button(TDEE_Title_Label,text="Back",relief="solid",bg="red",fg="White",bd=1,command=del_TDEE)
                                        Exit_Interface_TDEE.pack(side="right",padx=10)

                                        activity_label = Label(TDEE_Frame, text="", font=("Arial", 12))
                                        activity_label.place(x=50, y=170)

                                        activity_levels = {
                                            1: " Sedentary \n (Little to no exercise)",
                                            2: " Lightly active \n (Exercise/sports 1-3 days/week)",
                                            3: " Moderately active  \n (Exercise/sports 3-5 days/week)",
                                            4: " Very active  \n (Exercise/sports 6-7 days a week)",
                                            5: " Extremely active  \n (Exercise/sports & physical job or training)"
                                        }

                                        def get_value(value):
                                            print(value)

                                        TDEE_slider = Scale(TDEE_Frame, from_=1, to=5, orient=VERTICAL, length=300, bg="black", fg="white", command=lambda v: get_value(v))
                                        TDEE_slider.set(1)
                                        TDEE_slider.place(x=50, y=50)


                                        TDEE_slider_Activity_Label_1=Label(TDEE_Frame,text=activity_levels[1],bg="White",fg="Black",font=("Purisa 10 bold"), anchor="center")
                                        TDEE_slider_Activity_Label_1.place(x=150,y=55)

                                        TDEE_slider_Activity_Label_2=Label(TDEE_Frame,text=activity_levels[2],bg="White",fg="Black",font=("Purisa 10 bold"), anchor="center")
                                        TDEE_slider_Activity_Label_2.place(x=125,y=120)

                                        TDEE_slider_Activity_Label_3=Label(TDEE_Frame,text=activity_levels[3],bg="White",fg="Black",font=("Purisa 10 bold"), anchor="center")
                                        TDEE_slider_Activity_Label_3.place(x=125,y=185)

                                        TDEE_slider_Activity_Label_4=Label(TDEE_Frame,text=activity_levels[4],bg="White",fg="Black",font=("Purisa 10 bold"), anchor="center")
                                        TDEE_slider_Activity_Label_4.place(x=120,y=250)

                                        TDEE_slider_Activity_Label_5=Label(TDEE_Frame,text=activity_levels[5],bg="White",fg="Black",font=("Purisa 10 bold"), anchor="center")
                                        TDEE_slider_Activity_Label_5.place(x=90,y=316)
                                        
                                        ttk.Separator(TDEE_Frame, orient='horizontal').place(x=0, y=370, relwidth=1)
                                        
                                        BMR_Indicator=Label(TDEE_Frame,text=f"BMR: {BMR_val}",font=("Purisa 12 bold"),anchor="center",bg="White",fg="Green")
                                        BMR_Indicator.place(x=120,y=380)

                                        def cal_TDEE():
                                            global TDEE_slider, BMR_val, activity_label

                                            try:
                                                global tdee
                                                tdee=TDEE_slider.get()
                                                activity_level = int(TDEE_slider.get())
                                                activity_multiplier = {
                                                    1: 1.2,  # Sedentary (Little to no exercise)
                                                    2: 1.375,  # Lightly active (Exercise/sports 1-3 days/week)
                                                    3: 1.55,  # Moderately active (Exercise/sports 3-5 days/week)
                                                    4: 1.725,  # Very active (Exercise/sports 6-7 days a week)
                                                    5: 1.9  # Extremely active (Exercise/sports & physical job or training)
                                                }

                                                if not BMR_val:
                                                    try:
                                                        TDEE_Result_Label.destroy()
                                                    except:
                                                        print("No TDEE Result")
                                                    finally:
                                                        TDEE_Result=Label(TDEE_Frame,fg="red",bg="White",font=("Purisa 10 bold"),text=("BMR value is not calculated."))
                                                        TDEE_Result.place(x=65,y=480)

                                                global TDEE_val
                                                TDEE_val = BMR_val * activity_multiplier[activity_level]

                                                TDEE_Result = Label(TDEE_Frame, text=f"TDEE: {TDEE_val:.2f} calories/day", font=("Purisa 15 bold"), bg="white", fg="black")
                                                TDEE_Result.place(x=70, y=480)

                                            except ValueError as e:
                                                try:
                                                    TDEE_Warning.destroy()
                                                except:
                                                    print("No Warning")
                                                finally:
                                                    TDEE_Warning = Label(TDEE_Frame, text=f"Error: {e}", font=("Purisa 10 bold"), bg="black", fg="red")
                                                    TDEE_Warning.place(x=50, y=490)
                                                    win.after(2000, lambda: TDEE_Warning.destroy())

                                        Cal_TDEE_Button=Button(TDEE_Frame,text="Calculate",font=("Purisa 15 bold"),justify="center",bg="Blue",fg="white",command=cal_TDEE)
                                        Cal_TDEE_Button.place(x=160,y=425)
                                        

                    

                                    BMI_Reset_Button = Button(BMR_Frame, text="Reset", font=("Purisa 15 bold"), bg="red", fg="white", command=lambda:({del_BMR(),BMR_interface()}), relief=FLAT)
                                    BMI_Reset_Button.place(x=165, y=370)
                                    TDEE_button_direct=Button(BMR_Frame,text="Check Your Total Daily Energy Expenditure (TDEE)",font=("Purisa 10 bold"),bg="black",fg="red",relief=FLAT,command=TDEE_interface)
                                    TDEE_button_direct.place(x=35,y=430)                    
                                 
                            
                                except ValueError:
                                    BMR_Warning = Label(BMR_Frame, text="Please enter NUMERIC VALUES only", font=("Purisa 10 bold"), bg="black", fg="red")
                                    BMR_Warning.place(x=90, y=300)
                                    win.after(2000,lambda:BMR_Warning.destroy())

                    BMR_Calculate_button = Button(BMR_Frame, text="Calculate", font=("Purisa 15 bold"), bd=2, cursor="hand2", bg="blue",fg="white", command=calculate_bmr)
                    BMR_Calculate_button.place(x=150, y=250)
                    
                    BMR_Frame.pack(fill=Y)


            def cal_MHR():
                try:
                    del_MHR()
                except:
                    print("Error")
                finally:
                    global MHR_title_Label, MHR_Frame, MHR_Age_Entry, MHR_Result_Label, MHR_Warning

                    MHR_title_Label = Label(Interface, text="Maximum Heart Rate Calculator", font="Purisa 15 bold", bg="red", fg="yellow")
                    MHR_title_Label.pack(side="top", fill=X)

                    MHR_Frame = Frame(Interface, bg="Black", height=600, width=400)

                    def del_MHR():
                        MHR_title_Label.destroy()
                        MHR_Frame.destroy()

                    Exit_Interface_MHR=Button(MHR_title_Label,text="Back",relief="solid",bg="red",fg="White",bd=1,command=del_MHR)
                    Exit_Interface_MHR.pack(side="right",padx=10)

                    MHR_Age_Label = Label(MHR_Frame, text="Age:", font=("Purisa 15 bold"), fg="white", bg="black")
                    MHR_Age_Label.place(x=100, y=200)
                    MHR_Age_Entry = Entry(MHR_Frame, font=("Purisa 15 bold"), width=11, justify="center")
                    MHR_Age_Entry.place(x=150, y=200)

                    def calculate_mhr():
                        global MHR_Age_Entry, MHR_Frame, MHR_Warning

                        age_val = MHR_Age_Entry.get()

                        if age_val.isnumeric() == False:
                            MHR_Warning = Label(MHR_Frame, text="Please enter a valid age", font=("Purisa 10 bold"), bg="black", fg="red")
                            MHR_Warning.place(x=90, y=300)
                            win.after(2000, lambda: MHR_Warning.destroy())
                        else:
                            global MHR_val
                            age_val = float(age_val)
                            MHR_val = 220 - age_val

                            MHR_Result_Label = Label(MHR_Frame, text=f"Maximum Heart Rate: {MHR_val} bpm", font=("Purisa 15 bold"), bg="white", fg="black")
                            MHR_Result_Label.place(x=50, y=340)

                    MHR_Calculate_Button = Button(MHR_Frame, text="Calculate", font=("Purisa 12 bold"),width=15, bd=2, cursor="hand2", bg="blue", fg="white", command=calculate_mhr)
                    MHR_Calculate_Button.place(x=125, y=250)

                    MHR_Frame.pack(fill=Y)
                
            BMI_Enter=Button(Fitness_Calculator_Frame,font=("Purisa 21 bold"),relief="solid",bd=2,text="BMI",bg="Yellow",fg="Black",command=BMI_Interface)
            BMI_Enter.place(x=167,y=100)

            BMR_Enter=Button(Fitness_Calculator_Frame,font=("Purisa 20 bold"),relief="solid",bd=2,text="BMR",bg="Blue",fg="White",command=BMR_interface)
            BMR_Enter.place(x=162,y=200)

            MHR_Enter=Button(Fitness_Calculator_Frame,font=("Purisa 20 bold"),relief="solid",bd=2,text="MHR",bg="Green",fg="White",command=cal_MHR)
            MHR_Enter.place(x=162,y=300)

            Back_Fitness_Cal=Button(Fitness_Calculator_Frame,font=("Purisa 20 bold"),relief="solid",bd=2,text="Back",bg="Red",fg="White",command=Fitness_Calculator_Frame.destroy)
            Back_Fitness_Cal.place(x=162,y=400)


        def Check_Record():
            global MHR_val,TDEE_val,BMR_val,BMI_val

            Check_Record_Label = Label(Interface, text="Test Your Fitness", font="Purisa 16 bold",width=40,anchor="w", bg="Light Pink", fg="Black")
            Check_Record_Label.place(x=0, y=0)

            Check_Record_Frame = Frame(Interface, bg="Black", height=600, width=400)
            
            def del_Check_Record():
                Check_Record_Label.destroy()
                Check_Record_Frame.destroy()

            Bmi_text=None
            Bmr_text=None
            Tdee_text=None
            Mhr_text=None

            if BMI_val!=None: 
                Bmi_text=f"{BMI_val:.2f}"
            if BMR_val!=None:
                Bmr_text=f"{BMR_val:.2f}"
            if TDEE_val!=None:
                Tdee_text=f"{TDEE_val:.2f}"
            if MHR_val!=None:
                Mhr_text=f"{MHR_val:.2f}"
                
                

            Exit_Interface_Check_Record=Button(Check_Record_Label,text="Back",relief="solid",bg="red",fg="White",bd=1,command=del_Check_Record)
            Exit_Interface_Check_Record.place(x=350,y=2)

            Table_Cal_Name= Label(Check_Record_Frame, text="Calculator", font="Purisa 12 bold", bg="Black", fg="Light Pink")
            Table_Cal_Name.place(x=75,y=50)

            Table_Cal_Result= Label(Check_Record_Frame, text="Result", font="Purisa 12 bold", bg="Black", fg="Light Pink")
            Table_Cal_Result.place(x=250,y=50)

            BMI_label=Label(Check_Record_Frame, text="BMI", font="Purisa 10 bold", bg="Black", fg="white")
            BMI_label.place(x=100,y=100)

            Bmi_Label=Label(Check_Record_Frame,text=f"{Bmi_text}", font="Purisa 10 bold", bg="Black", fg="white")
            Bmi_Label.place(x=260,y=100)

            BMR_label=Label(Check_Record_Frame, text="BMR", font="Purisa 10 bold", bg="Black", fg="white")
            BMR_label.place(x=100,y=150)

            Bmr_Label=Label(Check_Record_Frame,text=f"{Bmr_text}", font="Purisa 10 bold", bg="Black", fg="white")
            Bmr_Label.place(x=260,y=150)

            TDEE_label=Label(Check_Record_Frame, text="TDEE", font="Purisa 10 bold", bg="Black", fg="white")
            TDEE_label.place(x=98,y=200)

            TDEE_Label=Label(Check_Record_Frame,text=f"{Tdee_text}", font="Purisa 10 bold", bg="Black", fg="white")
            TDEE_Label.place(x=260,y=200)

            MHR_label=Label(Check_Record_Frame, text="MHR", font="Purisa 10 bold", bg="Black", fg="white")
            MHR_label.place(x=100,y=250)

            MHR_Label=Label(Check_Record_Frame,text=f"{Mhr_text}", font="Purisa 10 bold", bg="Black", fg="white")
            MHR_Label.place(x=260,y=250)
            
            def cal_score():
                def check_all_vals():
                    global MHR_val,TDEE_val,BMR_val,BMI_val
                    if BMI_val==0 or BMI_val==None:
                        try:
                            check_BMI.destroy()
                        except:
                            print(" ")
                        finally:
                            check_BMI=Label(Check_Record_Frame,text="X",fg="red",bg="Black",font=("Purisa 12 bold"))
                            check_BMI.place(x=325,y=100)
                    else:
                        try:
                            check_BMI.destroy()
                        except:
                            print(" ")
                        finally:
                            check_BMI=Label(Check_Record_Frame,text="✓",fg="green",bg="Black",font=("Purisa 12 bold"))
                            check_BMI.place(x=325,y=100)

                            
                    if BMR_val==0 or BMR_val==None:
                        try:
                            check_BMR.destroy()
                        except:
                            print(" ")
                        finally:
                            check_BMR=Label(Check_Record_Frame,text="X",fg="red",bg="Black",font=("Purisa 12 bold"))
                            check_BMR.place(x=325,y=150)
                    else:
                        try:
                            check_BMR.destroy()
                        except:
                            print(" ")
                        finally:
                            check_BMR=Label(Check_Record_Frame,text="✓",fg="green",bg="Black",font=("Purisa 12 bold"))
                            check_BMR.place(x=325,y=150)

                    
                    if TDEE_val==0 or TDEE_val==None:
                        try:
                            check_TDEE.destroy()
                        except:
                            print(" ")
                        finally:
                            check_TDEE=Label(Check_Record_Frame,text="X",fg="red",bg="Black",font=("Purisa 12 bold"))
                            check_TDEE.place(x=325,y=200)
                    else:
                        try:
                            check_TDEE.destroy()
                        except:
                            print(" ")
                        finally:
                            check_TDEE=Label(Check_Record_Frame,text="✓",fg="green",bg="Black",font=("Purisa 12 bold"))
                            check_TDEE.place(x=325,y=200)

                            
                    if MHR_val==0 or MHR_val==None:
                        try:
                            check_MHR.destroy()
                        except:
                            print(" ")
                        finally:
                            check_MHR=Label(Check_Record_Frame,text="X",fg="red",bg="Black",font=("Purisa 12 bold"))
                            check_MHR.place(x=325,y=250)
                    else:
                        try:
                            check_MHR.destroy()
                        except:
                            print(" ")
                        finally:
                            check_MHR=Label(Check_Record_Frame,text="✓",fg="green",bg="Black",font=("Purisa 12 bold"))
                            check_MHR.place(x=325,y=250)

                def scoring():
                    global MHR_val,TDEE_val,BMR_val,BMI_val,TDEE_slider
                    try:
                        Fitness_Score_Label.destroy()
                        Comment_Label.destroy()
                    except:
                        print("Nothing")
                    finally:
                        if BMI_val!=None and BMR_val!=None and TDEE_val!=None and MHR_val!=None:
                            pass
                        else:
                            def Redirect():
                                try:
                                    Check_Record_Frame.destroy()
                                except:
                                    print("No Check_Record_Frame")
                                finally:
                                    Fitness_Calculator_Interface()
                            warning_cal=Button(Check_Record_Frame,font=("Purisa 10 bold"),text="Error: Some fitness values (MHR, TDEE, BMR, BMI) \n are missing or not calculated properly. \n Click Here and Calculate them",command=lambda: (del_Check_Record(), Redirect()),fg="Red",bg="White")
                            warning_cal.place(x=37, y=390)
                check_all_vals()
                win.after(1000,scoring)

            check_record_button=Button(Check_Record_Frame,text="Check",font=("Purisa 12 bold"),command=cal_score)
            check_record_button.place(x=150,y=325)

            Check_Record_Frame.place(x=0,y=30)

            

            


            
        
        def mainoptions_screen():
            MainOptions.place(x=0,y=0)

            Fitness_Calculators=Button(MainOptions,font=("Purisa 20 bold"),relief="solid",bd=0,text="Calculate Fitness",bg="gold",fg="White",command=Fitness_Calculator_Interface)
            Fitness_Calculators.place(x=75,y=600)

            Fitness_Test=Button(MainOptions,font=("Purisa 20 bold"),relief="solid",bd=0,text="Check Record",bg="Blue",fg="White",command=Check_Record)
            Fitness_Test.place(x=95,y=800)

            Fitness_Interface_Exit=Button(MainOptions,font=("Purisa 20 bold"),relief="solid",bd=0,text="Exit",bg="Red",fg="White")
            Fitness_Interface_Exit.place(x=162,y=900)

            for y in range(300):
                Fitness_Interface_Exit.place(x=162, y=y)
                Fitness_Interface_Exit.config(command=Interface.destroy)
                MainOptions.config(bg="Red")
                MainOptions.update()

            for y in range(200):
                Fitness_Interface_Exit.config(bd=2)
                Fitness_Test.place(x=95, y=y)
                MainOptions.config(bg="Blue")
                MainOptions.update()
                
            for y in range(100):
                Fitness_Test.config(bd=2)
                Fitness_Calculators.place(x=75, y=y)
                Fitness_Calculators.config(command=Fitness_Calculator_Interface)
                MainOptions.config(bg="Gold")
                MainOptions.update()
                win.after(1000,lambda:{MainOptions.config(bg="Orange"),Fitness_Calculators.config(bd=2)})

            
        

            

        mainoptions_screen()

            
    fitness_interface()

#Bank APP
global Balance
Balance = 10000
def Bank_APPS():
    win.after(1000,del_apps)
    win.after(1000, lambda: Bank_Ap())
   
 
def Bank_Ap():
    del_nav()
    win.config(bg="orange")
    win.after(2500, bank_start())

global bank_Logo
def bank_start():
    global bank_Logo
    bank_Logo = Label(win,bg="orange", text="Bank  \n A Safe & Best Banking Experience",font=("Bold", 15))
    bank_Logo.pack(pady=200)
    win.after(6000, lock)

def lock():
    bank_Logo.destroy()  
    win.config(bg="Black")

    global Password, Username_Label, Login, Bank_Exit, Show_Pass

    Username_Label = Label(win, bg="Black", fg="Gray", text="\n Bank_User@02215", font=("Bold", 15))
    Username_Label.place(x=105, y=150)

    Password = Entry(win, bd=5, font=('Georgia 15'), show="*")

    def Show_pass():
        if Password.cget("show") == "*":
            Password.config(show="")
            Show_Pass.config(text="Hide")
        else:
            Password.config(show="*")
            Show_Pass.config(text="Show")

            
    Show_Pass = Button(Password, font=("Bold", 10), text="Show", command=Show_pass)
    Show_Pass.place(x=200, y=0)  
    Password.place(x=80, y=220)

    Login = Button(win, bg="Blue", fg="white", font=("Bold", 15), text="Login", command=Check_Pass)
    Login.place(x=210, y=270)

    Bank_Exit = Button(win, bg="Black", fg="red", font=("Bold", 15), text="Exit", relief=FLAT, command=bank_exit_login)
    Bank_Exit.place(x=140, y=270)

global Pass
Pass="User@Royal_College"

def Check_Pass():
    entered_password = Password.get()
    global result_label
    if entered_password == Pass:
        result_label = Label(win, bg="Black", text="Logging You In...", fg="green")
        result_label.place(x=150, y=350)
        win.after(2000, Del_Login)
        win.after(2000, lambda: bank_interface())
    else:
        result_label = Label(win, bg="Black", text="Incorrect Password. Try again.", fg="red")
        result_label.place(x=125, y=350)
        win.after(2000,lambda: result_label.destroy())
        
def Del_Login():
    Login.destroy()
    Password.destroy()
    Username_Label.destroy()
    Bank_Exit.destroy()
    try:
        result_label.destroy()
    except:
        pass

def bank_exit_login():
    win.after(1000, Del_Login())
    win.after(1000, main_win())
    
def bank_interface():
    global bal_button, Loan_Button, Settings, Exit_B
    Loan_Button = Button(win, bg="Blue", fg="white", font=("Bold", 15),  text="Loan", width=15, height=5,command= Loan_Page)
    Loan_Button.place(x=40, y=160)
    
    bal_button = Button(win, bg="Red", fg="white", font=("Bold", 15),  text="Balance", width=10, height=10, command=Bal_Page)
    bal_button.place(x=235, y=160)

    Settings = Button(win, bg="Gray", fg="Yellow", font=("Bold", 15),  text="Change Password", width=15, command=Settings_Page)
    Settings.place(x=40, y=310)

    Exit_B = Button(win, bg="Yellow", fg="Black", font=("Bold", 15),  text="Exit", width=15,command=Exit_Bank_APP)
    Exit_B.place(x=40, y=368)

def Del_Interface():
    global bal_button, Loan_Button, Settings, Exit_B
    bal_button.destroy()
    Loan_Button.destroy()
    Settings.destroy()
    Exit_B.destroy()

def Exit_Bank_APP():
    Del_Interface()
    show_nav()

    

def Bal_Page():
    win.after(1000, Del_Interface())
    global Bal_Label, Exit_Bal
    win.config(bg="Black")
    Bal_Label = Label(win, bg="Blue", fg="white", font=("Bold", 15), text=("Balance:",Balance), width=25, height=5)
    Bal_Label.place(x=60, y=170)
    Exit_Bal=Button(win, text="Exit",font=("Bold", 15),command=Exit_Bal_Page)
    Exit_Bal.place(x=180, y=320)
    

def Exit_Bal_Page():
    global Bal_Label, Exit_Bal
    Bal_Label.destroy()
    Exit_Bal.destroy()
    win.after(1000, lambda: bank_interface())


global loan_count
loan_count = 0


def show_warning(loan_frame, loan_label, loan_button):
    loan_frame.destroy()
    loan_label.destroy()

    warning_frame = Frame(win, bg="gray")
    warning_label = Label(warning_frame, bg="gray", fg="white", font=("Bold", 15),
                          text="You have reached the loan limit of \n Rs 100,000")
    warning_label.pack(pady=40)
    warning_accept=Button(warning_frame, bg="black", fg="white", font=("Bold", 15),
                          text="OK", command=lambda: cleanup_warning(warning_frame, warning_label, loan_button))
    warning_accept.pack(pady=10)
    warning_frame.pack(pady=70)

    


def cleanup_warning(warning_frame, warning_label, loan_button):
    warning_frame.destroy()
    warning_label.destroy()
    win.after(1000, bank_interface())

def loan_grant(loan_ammt):
    global Balance, Loan_Button

    if Balance >= 100000:
        win.after(1000, lambda: show_warning(Loan_Frame, Loan_Label, Loan_Button))
    else:
        if loan_ammt == Loan_10K:
            Balance += 10000
        elif loan_ammt == Loan_50K:
            Balance += 50000
        else:
            Balance += 90000


def Loan_Page():
    win.after(1000, Del_Interface())
        
    global Loan_Frame,Loan_10K,Loan_50K,Loan_100K,Loan_Label
    Loan_Label = Label(win, bg="Black", fg="white", font=("Bold", 20), text=("LOAN"), width=25, height=5)
    Loan_Label.pack(pady=40)
    
    Loan_Frame = Frame(win, bg="gray")
    
    Loan_10K = Button(Loan_Frame, bg="Black", fg="White", text="Rs.10,000", font=("Bold", 15), relief=FLAT,command= lambda: loan_grant(Loan_10K))
    Loan_10K.pack(padx=20, pady=15)
    
    Loan_50K = Button(Loan_Frame, bg="Black", fg="White", text="Rs.50,000", font=("Bold", 15), relief=FLAT, command= lambda: loan_grant(Loan_50K))
    Loan_50K.pack(padx=20, pady=15)
    
    Loan_90K = Button(Loan_Frame,bg="Black", fg="White",  text="Rs.90,000", font=("Bold", 15), relief=FLAT, command= lambda: loan_grant(Loan_90K))
    Loan_90K.pack(padx=20, pady=15)

    Exit_Loan = Button(Loan_Frame,bg="Red", fg="Black",  text="Back", font=("Bold", 15), relief=FLAT, command= lambda: Exit_Loan_Page())
    Exit_Loan.pack(padx=20, pady=15)

    Loan_Frame.place(x=125, y=150)

def Exit_Loan_Page():
    global Loan_Frame, Loan_Label, Loan_Button
    Loan_Frame.destroy()
    Loan_Label.destroy()
    win.after(1000, bank_interface)
    


def Settings_Page():
    global Setting_Frame,Current_Password,New_Password
    Setting_Frame=Frame(win,bg="Gray", height=600, width=400)
    
    Settings_Label=Label(Setting_Frame, bg="Gray",fg="Black",text="Settings", font=("Arial 20 bold"))
    Settings_Label.place(x=42, y=33)
    
    Back_Settings=Button(Setting_Frame, bg="Gray",fg="Black",text="<", font=("Arial 15 bold"),relief=FLAT,cursor="sb_left_arrow",command= del_Settings_Page)
    Back_Settings.place(x=10, y=30)

    text_current=StringVar()
    text_new=StringVar()
     
    Current_Password= Entry(Setting_Frame, textvariable=text_current, font=("Arial 14"), width=25)
    Current_Password.place(x=50, y=200)
    Current_Password.focus()

    Current_Password.insert(0, "Enter Current Password")

    
    New_Password= Entry(Setting_Frame, textvariable=text_new, font=("Arial 14 "), width=25)
    New_Password.place(x=50, y=250)
    New_Password.focus()

    New_Password.insert(0, "Enter New Password")

    CP_Button=Button(Setting_Frame, bg="white", fg="Black",text="Change Password",font=("Arial  15 bold"),command=change_Password)
    CP_Button.place(x=100,y=300)
    
    Setting_Frame.pack(fill="both", expand="yes")

def del_Settings_Page():
    global Setting_Frame
    Setting_Frame.destroy()

def change_Password():
    global Current_Pass,New_Password,Pass,Setting_Frame
    c_p=Current_Password.get()
    n_p=New_Password.get()
     
    if (c_p==Pass):
         Pass=n_p
         Change=Label(Setting_Frame, bg="Gray",fg="Green",text="Password Updated", font=("Arial 15 bold"))
         Change.place(x=90, y=350)
         win.after(2000,lambda:Change.destroy())
         win.after(1000,del_Settings_Page)
    else:
        Change=Label(Setting_Frame, bg="Gray",fg="Red",text="Incorrect Current Password", font=("Arial 15 bold"))
        Change.place(x=70, y=350)
        win.after(2000,lambda:Change.destroy())




#shop app
log = 0  
log_gui = 0

def Exit_Shopping_App():
    global menubar,LogIn,log_gui
    try:
        menubar.destroy()
        LogIn.destroy()
        log_gui=0
    except Exception as e:
        print(f"An error occurred during menubar destruction: {e}")
    
    
    show_nav()


def Shopping_Interface():
    global menubar,log,Ad_Frame_1,log,log_gui
    menubar = Menu(win)

    options = Menu(menubar, tearoff=0)
    options.add_command(label="Shop", command=shop_Check_log)
    options.add_command(label="My Orders", command=orders_Check_log)

    theme_submenu = Menu(options, tearoff=0)
    theme_submenu.add_command(label="Dark", command=lambda: Change_Theme("#1e1e1e"))
    theme_submenu.add_command(label="Light", command=lambda: Change_Theme("white"))
    theme_submenu.add_command(label="Gray", command=lambda: Change_Theme("#808080"))

    options.add_cascade(label="Theme Change", menu=theme_submenu)
    options.add_separator()
    options.add_command(label="Back", command=win.quit)

    menubar.add_cascade(label=" ≡ ", font=("arial 15 bold"), menu=options)

    Account = Menu(menubar, tearoff=0)
    Account.add_command(label="Log Out", command=Log_Out)
    Account.add_separator()

    menubar.add_cascade(label="Account", font=("arial 15 bold"), menu=Account)
    Exit = Menu(menubar, tearoff=0)
    Exit.add_command(label="Are You Sure: Yes", command=Exit_Shopping_App)
    Exit.add_command(label="Are You Sure: No", command=win.quit)
    menubar.add_cascade(label="Exit", menu=Exit)
    win.config(menu=menubar)

    if log == 0:
        if log_gui==0:
            log_gui = 1
            Ad_Frame_1 = Frame(win, bg="Red")
            Ad_1 = Label(Ad_Frame_1, bg="Red", fg="white",
                     text="You Need To Login Everytime You Open This App!! \n To Log In press button", font=("Arial 10 bold"))
            Ad_1.pack(pady=10)
            Ad_1_button = Button(Ad_Frame_1, bg="Green", fg="white", text=" Log In", font=("Arial 13 bold"),
                             command=lambda: more_ads())
            Ad_1_button.pack(pady=5)
            Ad_Frame_1.pack(pady=20)
        else:
            pass
    elif log == 1:
        more_ads()  

def more_ads():
    global log, Ad_Frame_1, log_gui
    log = 1
    log_gui = 0
    Ad_Frame_1.destroy()

def Log_Out():
    global LogIn, log, log_gui, Ad_Frame_1
    log = 0
    if log_gui == 0:
        log_gui = 1
        if 'Ad_Frame_1' in locals():
            Ad_Frame_1.destroy()
        LogIn = Frame(win, bg="Red")
        LogIn_Message = Label(LogIn, bg="Red", fg="White", font=("arial 10 bold"),
                              text="In Order To Continue Shopping You Need To LOG IN \n Log Into User@02215 (Passwordless)")
        LogIn_Message.pack(pady=30)

        def log_in_action():
            LogIn.destroy()
            global log, log_gui
            log = 1
            log_gui = 1

        LogIn_Button = Button(LogIn, bg="yellow", text="LOG IN", command=log_in_action)
        LogIn_Button.pack(pady=20)

        LogIn.pack(pady=50)
        LogIn.lift()
    else:
        pass

def Change_Theme(theme):
    win.config(bg=theme)


orders = []


def shop_Check_log():
    global log, LogIn, log_gui, Ad_Frame_1
    try:
        LogIn.destroy()
        log_gui = 0
        Ad_Frame_1.destroy()
    except:
        print("Exception")
    finally:
        if log == 1:
            Shopping()
        else:
            Log_Out()
            warning_Label = Label(win, bg=win.cget("bg"), fg="Red", text="Please Log In First To Access This Service")
            

def orders_Check_log():
    global log_gui, Ad_Frame_1
    try:
        LogIn.destroy()
        log_gui = 0
        Ad_Frame_1.destroy()
    except:
        print("Exception")
    finally:
        if log == 1:
            Your_Orders()
        else:
            Log_Out()
            warning_Label = Label(win, bg=win.cget("bg"), fg="Red", text="Please Log In First To Access This Service")

        
def Shopping():
    global shop_frame, buy_button, Exit_Shopping_Button, menubar,Balance
    win.after(1000, lambda: menubar.destroy())

    def buy_item(item):
        print(f"Item bought: {item}")

    shop_frame = Frame(win, bg=win.cget("bg"))
    scrollbar = Scrollbar(shop_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    shop_list = Listbox(shop_frame, yscrollcommand=scrollbar.set, bg="Light Blue",fg="black", selectbackground="blue",
                        selectmode=SINGLE)
    shop_list.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=shop_list.yview)

    shopping_items = [
        "3d Pen           5000/-",
        "Monitor          30000/-",
        "CPU              25000/-",
        "Pen              5/-",
        "Notebook         10/-",
        "Pencil Set       15/-",
        "Coffee Mug       20/-",
        "Keychain         25/-",
        "Mouse Pad        30/-",
        "Earphones        35/-",
        "Wall Clock       40/-",
        "Mobile Stand     45/-",
        "Sunglasses       50/-",
        "USB Flash Drive  55/-",
        "Desk Organizer   60/-",
        "Water Bottle     65/-",
        "Headphones       70/-",
        "Power Bank       75/-",
        "Playing Cards    80/-",
        "Hand Sanitizer   85/-",
        "Umbrella         90/-",
        "Notepad          95/-",
        "Plant Pot        100/-",
    ]

    for item in shopping_items:
        shop_list.insert(END, item)

    def on_buy_button_click():
        global Balance,less
        selected_item_indices = shop_list.curselection()

        if not selected_item_indices:
            print("Please select an item.")
            return

        selected_item_index = selected_item_indices[0]
        selected_item = shopping_items[selected_item_index]

        
        cost_str = selected_item.split()[-1]
        cost_str = cost_str.replace("/-", "").replace(",", "")  
        try:
            cost = int(cost_str)
            if Balance < cost:
                less=Label(shop_frame,fg="red",text="Insufficient Balance",font=("Purisa 10 bold"))
                less.pack()
                win.after(1000,lambda: less.destroy())
            else:
                Balance -= cost
                buy_item(selected_item)
                print(f"Remaining balance: {Balance}")
                print(f"Item bought: {selected_item}")
                orders.append(selected_item)
                print(orders)
        except ValueError:
            print(f"Invalid cost value: {cost_str}")
            try:
                win.after(1000,lambda: less.destroy())
            except:
                print("None")

            
    buy_button = Button(win, bg="Blue", fg="White", text="Buy Item", command=on_buy_button_click)
    buy_button.pack()

    Exit_Shopping_Button = Button(win, bg="red", fg="White", text="Back", command=Exit_Shopping)
    Exit_Shopping_Button.pack()

    shop_frame.pack()

def Exit_Shopping():
    global less
    shop_frame.destroy()
    buy_button.destroy()
    Exit_Shopping_Button.destroy()
    Shopping_Interface()
    try:
        less.destroy()
    except:
        print("error")

print("Background color:", win.cget("bg"))


def Your_Orders():
    global orders, orders_frame, Exit_Orders_Button, Balance,cancel_button
    win.after(1000, lambda: menubar.destroy())

    
    if 'orders_frame' in locals():
        orders_frame.destroy()

    
    orders_frame = Frame(win, bg=win.cget("bg"))
    scrollbar_2 = Scrollbar(orders_frame)
    scrollbar_2.pack(side=RIGHT, fill=Y)

    orders_list = Listbox(orders_frame, yscrollcommand=scrollbar_2.set, bg="Light Blue", fg="black")
    orders_list.pack(side=LEFT, fill=BOTH)
    scrollbar_2.config(command=orders_list.yview)

    for item in orders:
        orders_list.insert(END, item)
        
    def cancel_order():
        global Balance
        selected_order_indices = orders_list.curselection()

        if not selected_order_indices:
            print("Please select an order to cancel.")
            return

        selected_order_index = selected_order_indices[0]
        cancelled_item = orders[selected_order_index]

        refund_amount = get_refund_amount(cancelled_item)
        Balance += refund_amount

        print(f"Order cancelled: {cancelled_item}")
        print(f"Refund amount: {refund_amount}")
        print(f"Remaining balance: {Balance}")

        
        orders.pop(selected_order_index)
        orders_list.delete(selected_order_index)

    cancel_button = Button(win, bg="red", fg="white", text="Cancel Order", command=cancel_order)
    cancel_button.pack()

    Exit_Orders_Button = Button(win, bg="red", fg="white", text="Back", command=Exit_Orders)
    Exit_Orders_Button.pack()

    orders_frame.pack()


def get_refund_amount(cancelled_item):
    refund_amounts = {
        "3d Pen           5000/-": 5000,
        "Monitor          30000/-": 30000,
        "CPU              25000/-": 25000,
        "Pen              5/-": 5,
        "Notebook         10/-": 10,
        "Pencil Set       15/-": 15,
        "Coffee Mug       20/-": 20,
        "Keychain         25/-": 25,
        "Mouse Pad        30/-": 30,
        "Earphones        35/-": 35,
        "Wall Clock       40/-": 40,
        "Mobile Stand     45/-": 45,
        "Sunglasses       50/-": 50,
        "USB Flash Drive  55/-": 55,
        "Desk Organizer   60/-": 60,
        "Water Bottle     65/-": 65,
        "Headphones       70/-": 70,
        "Power Bank       75/-": 75,
        "Playing Cards    80/-": 80,
        "Hand Sanitizer   85/-": 85,
        "Umbrella         90/-": 90,
        "Notepad          95/-": 95,
        "Plant Pot        100/-": 100,
    }

    return refund_amounts.get(cancelled_item, 0)  

def Exit_Orders():
    global cancel_button 

    orders_frame.destroy()
    Exit_Orders_Button.destroy()
    cancel_button.destroy()

    Shopping_Interface()

def Shopping_App_start():
    del_apps()
    del_nav()
    win.config(bg="white")
    Logo_1 = Label(win, bg="white", fg="Red", text="FLIPTRA", font=("Purisa 20 bold"))
    Logo_1.pack(pady=250)
    win.after(2000, lambda: Logo_1.destroy())

    win.after(2000, lambda: win.config(bg="Red"))
    Logo_2 = Label(win, bg="Red", fg="white", text="FLIPTRA", font=("Purisa 20 bold"))
    Logo_2.pack(pady=250)
    win.after(4000, lambda: Logo_2.destroy())
    win.after(4000, lambda: win.config(bg="white"))
    win.after(4000, Shopping_Interface)



#chat app    
def chat_app():
    global win2
    scrollbar1 = Scrollbar(win, orient=VERTICAL)
    scrollbar1.pack(side=RIGHT,pady=30, fill=Y)

    if win2 and win2.winfo_exists():
        pass
    else:
        win2 = Tk()
        win2.geometry("400x600")
        win2.title("Chat window")
        win2.config(bg="black")
        
    global rmedia_click1
    rmedia_click1=False
    def media_popUp_1_start(): 
        global rmedia_click1,media_start_pop_up_1
        def media_start_pop_up_1():

            def exit_media_pop_up1():
                global media_select_pop_up1
                media_select_pop_up1.destroy()
            
            global media_select_pop_up1
            button_colors = {
                "Photo": {"bg": "slateblue3", "fg": "white"},
                "Video": {"bg": "orange", "fg": "white"},
                "File": {"bg": "hot pink", "fg": "white"},
                "Pay": {"bg": "Deepskyblue1", "fg": "white"},
                "Custom": {"bg": "dark green", "fg": "white"}
            }

            def on_enter(event):
                #reffered
                button_name = event.widget.cget("text")
                event.widget.config(bg=button_colors[button_name]["bg"], fg=button_colors[button_name]["fg"])

            def on_leave(event):
                #reffered
                event.widget.config(bg="white", fg="black")

            def select_photo():
                file_paths = filedialog.askopenfilenames(title="Select Images",filetypes=[("Image Files", "*.png;*.jpg;*.gif")])
                if file_paths:
                    for path in file_paths:
                        print("Selected File:", path)
                        sent_photos1.append(path)
                        recieved_photos2.append(path)
                        print(f"{recieved_photos2} \n {sent_photos1}")
                check_toggle()

            def select_video():
                file_paths = filedialog.askopenfilenames(title="Select Videos",filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
                if file_paths:
                    for path in file_paths:
                        print("Selected File:", path)
                        sent_videos1.append(path)
                        recieved_videos2.append(path)
                        print(f"{recieved_videos2} \n {sent_videos1}")
                check_toggle()

            def select_Files():
                file_paths = filedialog.askopenfilenames(title="Select Files",filetypes=[("PDF Files", "*.pdf"),("PowerPoint Files", "*.ppt;*.pptx"),("Audio Files", "*.mp3;*.wav"),("Text Files", "*.txt")])
                if file_paths:
                    for path in file_paths:
                        print("Selected File:", path)
                        media_storage_1.append(path)
                        print(media_storage_1)
                check_toggle()


            def select_Pay():
                from tkinter import ttk
                Pay_Frame1=Frame(media_select_pop_up1,width=393,height=144,bg="black",relief="solid",bd=1)
                Pay_Frame1.place(x=1,y=1)
                Pay_Title1=Label(Pay_Frame1,text="Pay",font="Purisa 20 bold",bg="black",fg="white")
                Pay_Title1.place(x=75,y=20)
                Pay_Label1=Label(Pay_Frame1,text="₹",font="Purisa 20 bold",bg="black",fg="white")
                Pay_Label1.place(x=75,y=60)
                Pay_Entry1 = Entry(Pay_Frame1,font="Purisa 12", relief="solid",width=25, bd=1,justify="center")
                Pay_Entry1.place(x=100, y=67)

                def del_Pay_FRAme():
                    Pay_Frame1.destroy()

                def payment():
                    from tkinter import ttk
                    import time
                    global abort
                    abort = False
                    

                    def abort_pb():
                        global abort
                        abort = True
                        Payment_Frame1.destroy()

                    if Pay_Entry1.get().isdigit()==True:
                        def update_progress():
                            global media_select_pop_up,Balance
                            pb_progress_label1=Label(Payment_Frame1,text="Payment in progress...",bg="black",fg="white",font=("purisa 8 bold"))
                            pb_progress_label1.place(x=225,y=90)
                            for i in range(86):  
                                pb1['value'] = i
                                media_select_pop_up1.update_idletasks()
                                time.sleep(0.01)
                                
                            pb_progress_label1.config(text="Almost there...",width=30,font=("purisa 8 bold"))
                            pb_progress_label1.place(x=205,y=90)
                            media_select_pop_up1.after(2000)
                            
                            for i in range(86, 101):
                                pb1['value'] = i
                                media_select_pop_up1.update_idletasks()
                                time.sleep(0.01)

                            media_select_pop_up1.after(2000)
                            pb1.destroy()
                            Payment_Title1.config(text="Paid")
                            Payment_Title1.place(x=165,y=20)
                            pb_progress_label1.destroy()
                            pb_Label1 = Label(Payment_Frame1, text="Payment Successful", font=("Arial 15 bold"), fg="green", bg="black")
                            pb_Label1.place(x=110, y=55)
                            s1_transact_history.append(f"You Sent ₹{Pay_Entry1.get()}")
                            s2_transact_history.append(f"You Recieved ₹{Pay_Entry1.get()}")
                            print(s1_transact_history)
                            print(s2_transact_history)
                            Balance-=int(Pay_Entry1.get())
                            print(Balance)
  
                        Payment_Frame1 = Frame(media_select_pop_up1, width=393, height=144, bg="black", relief="solid", bd=1)
                        Payment_Frame1.place(x=1, y=1)
                        Payment_Title1=Label(Payment_Frame1,text="Pay",font="Purisa 20 bold",bg="black",fg="white")
                        Payment_Title1.place(x=75,y=20)
                        pb1 = ttk.Progressbar(Payment_Frame1, orient='horizontal', mode='determinate', length=280)
                        pb1.place(x=75, y=65)
                        
                        
                        update_progress()

                        def exit_pb():
                            check_toggle()

                        pb_cancel_button1= Button(Payment_Frame1, text="OK", font="Purisa 10 bold", command=exit_pb)
                        pb_cancel_button1.place(x=185, y=100)

                    else:
                        Payment_Frame1 = Frame(media_select_pop_up1, width=393, height=144, bg="black", relief="solid", bd=1)
                        Payment_Frame1.place(x=1, y=1)
                        pb_Label1 = Label(Payment_Frame1, text="Invalid Values Entered", font=("Arial 15 bold"), fg="red", bg="black")
                        pb_Label1.place(x=90, y=50)
                        pb_cancel1_button = Button(Payment_Frame1, text="Cancel", font="Purisa 10 bold", command=abort_pb)
                        pb_cancel1_button.place(x=150, y=100)
                            
                    
                    
                    

                button_colors = {
                "Pay": {"bg": "Green", "fg": "white"},
                "Cancel": {"bg": "red", "fg": "white"},
                }

                def on_enter(event):
                #reffered
                    button_name = event.widget.cget("text")
                    event.widget.config(bg=button_colors[button_name]["bg"], fg=button_colors[button_name]["fg"])

                def on_leave(event):
                    #reffered
                    event.widget.config(bg="white", fg="black")

                Pay_Button1=Button(Pay_Frame1,text="Pay",font=("Purisa 9 bold"),command=payment,width=10,relief="solid",bd=1)
                Pay_Button1.place(x=250, y=100)
                Pay_Button1.bind("<Enter>", on_enter)
                Pay_Button1.bind("<Leave>", on_leave)

                Pay_Cancel1=Button(Pay_Frame1,text="Cancel",font=("Purisa 9 bold"),command=del_Pay_FRAme,width=10,relief="solid",bd=1)
                Pay_Cancel1.place(x=75, y=100)
                Pay_Cancel1.bind("<Enter>", on_enter)
                Pay_Cancel1.bind("<Leave>", on_leave)
                
                
                
                        
                
            from tkinter import filedialog, Tk
            media_select_pop_up1=Frame(chat_frame1,width=400,height=150,bg="bisque",relief="solid",bd=2)
            media_select_pop_up1.place(x=0,y=365)

            button_photo1 = Button(media_select_pop_up1, text="Photo",width=5,font=("bold"),relief="solid",bd=1,command=select_photo)
            button_photo1.place(x=60,y=50)
            button_photo1.bind("<Enter>", on_enter)
            button_photo1.bind("<Leave>", on_leave)

            button_video1 = Button(media_select_pop_up1, text="Video",width=5,font=("bold"),relief="solid",bd=1,command=select_video)
            button_video1.place(x=135,y=50)
            button_video1.bind("<Enter>", on_enter)
            button_video1.bind("<Leave>", on_leave)

            button_file1 = Button(media_select_pop_up1, text="File",width=5,font=("bold"),relief="solid",bd=1,command=select_Files)
            button_file1.place(x=210,y=50)
            button_file1.bind("<Enter>", on_enter)
            button_file1.bind("<Leave>", on_leave)

            button_pay1 = Button(media_select_pop_up1, text="Pay",width=5,font=("bold"),relief="solid",bd=1,command=select_Pay)
            button_pay1.place(x=285,y=50)
            button_pay1.bind("<Enter>", on_enter)
            button_pay1.bind("<Leave>", on_leave)

            button_custom1 = Button(media_select_pop_up1, text="Custom",width=10,font=("bold"),relief="solid",bd=1)
            button_custom1.place(x=150,y=100)
            button_custom1.bind("<Enter>", on_enter)
            button_custom1.bind("<Leave>", on_leave)



        def check_toggle():
            global rmedia_click1
            if rmedia_click1==False:
                media_start_pop_up_1()
                rmedia_click1=True
            else:
                media_select_pop_up1.destroy()
                rmedia_click1=False

        check_toggle()
        
        
    
    def check_message():
        chat_text1.config(state=NORMAL)
        chat_text1.delete("1.0", END)
        chat_text1.config(state=DISABLED)

        
        for key in my_dict.keys():
            if key.startswith("s1"):
                sender = "You"
            elif key.startswith("s2"):
                sender = "Sender"
            else:
                sender = "Unknown"

            message = my_dict[key]
            if message:
                display_message(chat_text1, f"{sender}: {message}")
        print("reset")
        line_number1 = 1
        for line in chat_text1.get("1.0", END).splitlines():
            if "You:" in line:
                start_index = f"{line_number1}.0"
                end_index = f"{line_number1}.{len(line)}"
                chat_text1.tag_add("highlight", start_index, end_index)

            line_number1 += 1

        chat_text1.tag_config("highlight", background="blue", foreground="white",font=("Arial 10 bold"))

        line_number = 1
        for line in chat_text2.get("1.0", END).splitlines():
            if "You:" in line:
                start_index = f"{line_number}.0"
                end_index = f"{line_number}.{len(line)}"
                chat_text2.tag_add("highlight", start_index, end_index)

            line_number += 1

    
        chat_text2.tag_config("highlight", background="red", foreground="white",font=("Arial 10 bold"))

        
        chat_text2.config(state=NORMAL)
        chat_text2.delete("1.0", END)
        chat_text2.config(state=DISABLED)

        
        for key in my_dict.keys():
            if key.startswith("s1"):
                sender = "You"
            elif key.startswith("s2"):
                sender = "Sender"
            else:
                sender = "Unknown"

            message = my_dict[key]
            if message:
                display_message(chat_text1, f"{sender}: {message}")
        print("reset")
        line_number1 = 1
        for line in chat_text1.get("1.0", END).splitlines():
            if "You:" in line:
                start_index = f"{line_number1}.0"
                end_index = f"{line_number1}.{len(line)}"
                chat_text1.tag_add("highlight", start_index, end_index)

            line_number1 += 1

        chat_text1.tag_config("highlight", background="blue", foreground="white",font=("Arial 10 bold"))

        line_number = 1
        for line in chat_text2.get("1.0", END).splitlines():
            if "You:" in line:
                start_index = f"{line_number}.0"
                end_index = f"{line_number}.{len(line)}"
                chat_text2.tag_add("highlight", start_index, end_index)

            line_number += 1

    
        chat_text2.tag_config("highlight", background="red", foreground="white",font=("Arial 10 bold"))


    
        text_entry1.delete(0, END)

    def display_message(widget, message):
        widget.config(state=NORMAL)
        widget.insert(END, f"{message}\n")
        widget.config(state=DISABLED)
                
    def send_entry_s1():
        variable_name = f"s1_{len(my_dict) + 1}"
        variable_value=text_entry1.get()
        my_dict[variable_name] = variable_value
        s1_history.append(variable_name)
        print(my_dict)
        print(s1_history)
        message = text_entry1.get()
        if message:
            chat_text1.config(state=NORMAL)
            chat_text1.insert(END, f"You: {message} \n")
            chat_text1.config(state=DISABLED)
            text_entry1.delete(0, END)
            chat_text2.config(state=NORMAL)
            chat_text2.insert(END, f"Sender: {message} \n")
            chat_text2.config(state=DISABLED)
            

            line_number1 = 1
            for line in chat_text1.get("1.0", END).splitlines():
                if "You:" in line:
                    start_index = f"{line_number1}.0"
                    end_index = f"{line_number1}.{len(line)}"
                    chat_text1.tag_add("highlight", start_index, end_index)

                line_number1 += 1

    
            chat_text1.tag_config("highlight", background="blue", foreground="white",font=("Arial 10 bold"))

            line_number = 1
            for line in chat_text2.get("1.0", END).splitlines():
                if "You:" in line:
                    start_index = f"{line_number}.0"
                    end_index = f"{line_number}.{len(line)}"
                    chat_text2.tag_add("highlight", start_index, end_index)

                line_number += 1

    
            chat_text2.tag_config("highlight", background="red", foreground="white",font=("Arial 10 bold"))

    
    
 
    chat_app_frame1=Frame(win,width=400,height=600)
    chat_app_frame1.place(x=0,y=0)

    def show_media_1():
        media_frame=Frame(chat_app_frame1,width=250,height=300,relief="solid",bd=1)
        media_frame.place(x=100,y=39)

        def del_media_frame():
            media_frame.destroy()
            
        def show_media_sent():
            def del_media_sent():
                media_exit_button1.config(command=media_frame.destroy)
                media_title_label1.config(text="Media")
                media_container_sent_frame1.destroy()

            def sent_photos_mod():
                def show_photos_sent():
                    def del_photos_sent():
                        media_title_label1.config(text="Sent Media")
                        media_container_photos_frame1.destroy()
                        media_frame.config(width=250, height=300)
                        media_frame.place(x=100, y=39)
                        media_exit_button1.config(command=del_media_sent)
                        

                    media_exit_button1.config(command=del_photos_sent)
                    media_title_label1.config(text="Sent Photos")

                    
                    media_frame.config(height=600, width=400)
                    media_frame.place(x=0, y=0)

                    media_container_photos_frame1 = Frame(media_container_frame1, width=400, height=550, bg="light cyan")
                    media_container_photos_frame1.place(x=0, y=0, relwidth=1, relheight=1)

                    import os
                    from tkinter import PhotoImage
                    from tkinter import messagebox

                    def open_photo(event):
                        selected_index = media_listbox.curselection()
                        if selected_index:
                            selected_image_path = sent_photos1[selected_index[0]]
                            try:
                                os.startfile(selected_image_path)
                            except Exception as e:
                                messagebox.showerror("Error", f"Unable to open photo: {e}")

                    def extract_image_name(path):
                        return os.path.basename(path)

                    media_listbox = Listbox(media_container_photos_frame1, selectmode="single", bg="white", fg="black", selectbackground="black",selectforeground="light green")
                    media_listbox.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

                    scrollbar = Scrollbar(media_container_photos_frame1, command=media_listbox.yview)
                    scrollbar.place(relx=0.9, rely=0.1, relheight=0.7)
                    media_listbox.config(yscrollcommand=scrollbar.set)

                    media_listbox.bind("<Double-Button-1>", open_photo)

                    for path in sent_photos1:
                        image_name = extract_image_name(path)
                        media_listbox.insert("end", image_name)

                show_photos_sent()

            def sent_videos_mod():
                def show_videos_sent():
                    def del_videos_sent():
                        media_title_label1.config(text="Sent Media")
                        media_container_videos_frame1.destroy()
                        media_frame.config(width=250, height=300)
                        media_frame.place(x=100, y=39)
                        media_exit_button1.config(command=del_media_sent)

                    media_exit_button1.config(command=del_videos_sent)
                    media_title_label1.config(text="Sent Videos")

                    
                    media_frame.config(height=600, width=400)
                    media_frame.place(x=0, y=0)

                    media_container_videos_frame1 = Frame(media_container_frame1, width=400, height=550, bg="light cyan")
                    media_container_videos_frame1.place(x=0, y=0, relwidth=1, relheight=1)

                    import os
                    from tkinter import messagebox

                    def open_video(event):
                        selected_index = media_listbox.curselection()
                        if selected_index:
                            selected_video_path = sent_videos1[selected_index[0]]
                            try:
                                os.startfile(selected_video_path)
                            except Exception as e:
                                messagebox.showerror("Error", f"Unable to open video: {e}")

                    def extract_video_name(path):
                        return os.path.basename(path)

                    media_listbox = Listbox(media_container_videos_frame1, selectmode="single", bg="white", fg="black", selectbackground="black", selectforeground="light green")
                    media_listbox.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

                    scrollbar = Scrollbar(media_container_videos_frame1, command=media_listbox.yview)
                    scrollbar.place(relx=0.9, rely=0.1, relheight=0.7)
                    media_listbox.config(yscrollcommand=scrollbar.set)

                    media_listbox.bind("<Double-Button-1>", open_video)

                    for path in sent_videos1:
                        video_name = extract_video_name(path)
                        media_listbox.insert("end", video_name)

                show_videos_sent()
                
            
            media_title_label1.config(text="Sent Media")
            media_container_sent_frame1 = Frame(media_container_frame1, width=400, height=550, bg="light cyan")
            media_container_sent_frame1.place(x=0, y=0,relwidth=1, relheight=1)

            media_option_photo_Button=Button(media_container_sent_frame1,text="Photos \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=sent_photos_mod)
            media_option_photo_Button.place(x=30,y=50)

            media_option_video_Button=Button(media_container_sent_frame1,text="Videos \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=sent_videos_mod)
            media_option_video_Button.place(x=30,y=100)

            media_option_file_Button=Button(media_container_sent_frame1,text="Files \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=show_transactions)
            media_option_file_Button.place(x=30,y=150)

            media_exit_button1.config(command=del_media_sent)
            
        def show_media_recieved():
            import os
            def del_media_received():
                media_exit_button1.config(command=media_frame.destroy)
                media_title_label1.config(text="Media")
                media_container_recieved_frame1.destroy()

            def received_photos_mod():
                def show_photos_received():
                    def del_photos_received():
                        media_title_label1.config(text="Received Media")
                        media_container_photos_frame1.destroy()
                        media_frame.config(width=250, height=300)
                        media_frame.place(x=100, y=39)
                        media_exit_button1.config(command=del_media_received)

                    media_exit_button1.config(command=del_photos_received)
                    media_title_label1.config(text="Received Photos")

                    
                    media_frame.config(height=600, width=400)
                    media_frame.place(x=0, y=0)

                    media_container_photos_frame1 = Frame(media_container_frame1, width=400, height=550, bg="light cyan")
                    media_container_photos_frame1.place(x=0, y=0, relwidth=1, relheight=1)

                    def open_photo(event):
                        selected_index = media_listbox.curselection()
                        if selected_index:
                            selected_image_path = recieved_photos1[selected_index[0]]
                            try:
                                os.startfile(selected_image_path)
                            except Exception as e:
                                messagebox.showerror("Error", f"Unable to open photo: {e}")

                    def extract_image_name(path):
                        return os.path.basename(path)

                    media_listbox = Listbox(media_container_photos_frame1, selectmode="single", bg="white", fg="black", selectbackground="black", selectforeground="light green")
                    media_listbox.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

                    scrollbar = Scrollbar(media_container_photos_frame1, command=media_listbox.yview)
                    scrollbar.place(relx=0.9, rely=0.1, relheight=0.7)
                    media_listbox.config(yscrollcommand=scrollbar.set)

                    media_listbox.bind("<Double-Button-1>", open_photo)

                    for path in recieved_photos1:
                        image_name = extract_image_name(path)
                        media_listbox.insert("end", image_name)

                show_photos_received()

            def received_videos_mod():
                def show_videos_received():
                    def del_videos_received():
                        media_title_label1.config(text="Received Media")
                        media_container_videos_frame1.destroy()
                        media_frame.config(width=250, height=300)
                        media_frame.place(x=100, y=39)
                        media_exit_button1.config(command=del_media_received)

                    media_exit_button1.config(command=del_videos_received)
                    media_title_label1.config(text="Received Videos")

                    
                    media_frame.config(height=600, width=400)
                    media_frame.place(x=0, y=0)

                    media_container_videos_frame1 = Frame(media_container_frame1, width=400, height=550, bg="light cyan")
                    media_container_videos_frame1.place(x=0, y=0, relwidth=1, relheight=1)

                    def open_video(event):
                        selected_index = media_listbox1.curselection()
                        if selected_index:
                            selected_video_path = recieved_videos1[selected_index[0]]
                            try:
                                os.startfile(selected_video_path)
                            except Exception as e:
                                messagebox.showerror("Error", f"Unable to open video: {e}")

                    def extract_video_name(path):
                        return os.path.basename(path)

                    media_listbox1 = Listbox(media_container_videos_frame1, selectmode="single", bg="white", fg="black", selectbackground="black", selectforeground="light green")
                    media_listbox1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

                    scrollbar1 = Scrollbar(media_container_videos_frame1, command=media_listbox1.yview)
                    scrollbar1.place(relx=0.9, rely=0.1, relheight=0.7)
                    media_listbox1.config(yscrollcommand=scrollbar1.set)

                    media_listbox1.bind("<Double-Button-1>", open_video)

                    for path in recieved_videos1:
                        vid_name = extract_video_name(path)
                        media_listbox1.insert("end", vid_name)


                show_videos_received()

            media_exit_button1.config(command=del_media_received)
            media_title_label1.config(text="Recieved Media")
            
            media_container_recieved_frame1 = Frame(media_container_frame1, width=400, height=550, bg="light cyan")
            media_container_recieved_frame1.place(x=0, y=0,relwidth=1, relheight=1)

            media_option_photo_Button=Button(media_container_recieved_frame1,text="Photos \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=received_photos_mod)
            media_option_photo_Button.place(x=30,y=50)

            media_option_video_Button=Button(media_container_recieved_frame1,text="Videos \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=received_videos_mod)
            media_option_video_Button.place(x=30,y=100)

            media_option_file_Button=Button(media_container_recieved_frame1,text="Files \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=show_transactions)
            media_option_file_Button.place(x=30,y=150)

        def show_transactions():
            def del_show_transactions():
                media_title_label1.config(text="Media")
                media_exit_button1.config(command=del_media_frame)
                media_container_recieved_frame1.destroy()

            media_exit_button1.config(command=del_show_transactions)
            media_title_label1.config(text="Received Media")
            
            
            media_container_recieved_frame1 = Frame(media_container_frame1, width=400, height=550, bg="light cyan")
            media_container_recieved_frame1.place(x=0, y=35, relwidth=1, relheight=1)

            tranact_text_widget = Text(media_container_recieved_frame1, wrap="word", font=("Arial", 12),state=DISABLED)
            tranact_text_widget.pack(side="left", fill="both", expand=True)

            for i in s1_transact_history:
                tranact_text_widget.config(state=NORMAL)
                tranact_text_widget.insert(END, f" {i}\n")
                tranact_text_widget.config(state=DISABLED)
            
            scrollbar_transact = Scrollbar(media_container_recieved_frame1, command=tranact_text_widget.yview)
            scrollbar_transact.pack(side="right", fill="y")
            
            tranact_text_widget.config(yscrollcommand=scrollbar_transact.set)
            



            
        media_title_frame1 = Frame(media_frame,width=200,height=100,bg="Green")
        media_title_frame1.place(x=0, y=0)
        
        media_exit_button1 = Button(media_title_frame1, text="<",font="Purisa 12 bold",command=del_media_frame,relief="flat",fg="White",bg="green")
        media_exit_button1.grid(row=0, column=0, padx=10, pady=0)

        media_title_label1 = Label(media_title_frame1, text="Media",fg="White",bg="green",width=35,anchor='w',font="Purisa 12 bold")
        media_title_label1.grid(row=0, column=1, padx=5, pady=5)
        

        media_container_frame1 = Frame(media_frame, width=200, height=200, bg="light cyan")
        media_container_frame1.place(x=0, y=35,relwidth=1, relheight=0.88)

        media_option_sent_Button=Button(media_container_frame1,text="Sent \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=show_media_sent)
        media_option_sent_Button.place(x=30,y=50)

        media_option_recieved_Button=Button(media_container_frame1,text="Recieved \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=show_media_recieved)
        media_option_recieved_Button.place(x=30,y=100)

        media_option_thistory_Button=Button(media_container_frame1,text="Transactions \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=show_transactions)
        media_option_thistory_Button.place(x=30,y=150)
        
    
    title_frame1 = Frame(chat_app_frame1,width=400,height=100,bg="Green")
    title_frame1.place(x=0, y=0)
    
    Exit_Click = False

    def exit_clicked():
        global Exit_Click
        Exit_Click = True
        if Exit_Click:
            chat_app_frame1.destroy()
            scrollbar1.destroy()
            Exit_Click = False

            
    exit_button1 = Button(title_frame1, text="<",font="Purisa 12 bold",command=exit_clicked,relief="flat",fg="White",bg="green")
    exit_button1.grid(row=0, column=0, padx=10, pady=0)

    title_label1 = Label(title_frame1, text="Chat",fg="White",bg="green",width=10,anchor='w',font="Purisa 12 bold")
    title_label1.grid(row=0, column=1, padx=5, pady=5)

    More_button1 = Button(title_frame1, text=",",font="Purisa 12 bold",command=show_media_1,relief="flat",fg="White",bg="green")
    More_button1.grid(row=0, column=2, padx=210, pady=0)

    
    chat_frame1 = Frame(chat_app_frame1, width=400, height=550, bg="red")
    chat_frame1.place(x=0, y=35,relwidth=1, relheight=0.86)

    chat_frame_main1 = Frame(chat_frame1, width=10, height=550)
    chat_frame_main1.pack(side="left",fill=Y)

    
    

    chat_text1 = Text(chat_frame_main1, wrap=WORD, yscrollcommand=scrollbar1.set, state=DISABLED)
    chat_text1.pack(expand=True, fill=BOTH)

    scrollbar1.config(command=chat_text1.yview)

    
    text_frame1 = Frame(chat_app_frame1,width=400,height=10,bd=2,relief="solid")
    text_frame1.place(x=0, y=553)

    Media_Button1=Button(text_frame1,text="+",font=("Purisa 12 bold"),relief="flat",command=media_popUp_1_start)
    Media_Button1.grid(row=0, column=1, padx=10, pady=5)
    text_entry1 = Entry(text_frame1, width=50,bd=1,relief="solid")
    text_entry1.grid(row=0, column=2, padx=5, pady=5)

    send_button1 = Button(text_frame1, text=">",relief="flat",font=("Purisa 12 bold"), command=send_entry_s1)
    send_button1.grid(row=0, column=3, padx=7, pady=5)

    

    def send_entry_s2():
        variable_name = f"s2_{len(my_dict) + 2}"
        variable_value=text_entry2.get()
        my_dict[variable_name] = variable_value
        s2_history.append(variable_name)
        print(my_dict)
        print(s2_history)
        message = text_entry2.get()
        if message:
            chat_text2.config(state=NORMAL)
            chat_text2.insert(END, f"You: {message}\n")
            chat_text2.config(state=DISABLED)
            text_entry2.delete(0, END)
            chat_text1.config(state=NORMAL)
            chat_text1.insert(END, f"Sender: {message}\n")
            chat_text1.config(state=DISABLED)
            
            
    global media_click
    media_click=False
    def media_popUp_2_start():
        global media_click,media_select_pop_up
        def media_start_pop_up_2():
            
            
            global media_select_pop_up
            button_colors = {
                "Photo": {"bg": "slateblue3", "fg": "white"},
                "Video": {"bg": "orange", "fg": "white"},
                "File": {"bg": "hot pink", "fg": "white"},
                "Pay": {"bg": "Deepskyblue1", "fg": "white"},
                "Custom": {"bg": "dark green", "fg": "white"}
            }

            def on_enter(event):
                #reffered
                button_name = event.widget.cget("text")
                event.widget.config(bg=button_colors[button_name]["bg"], fg=button_colors[button_name]["fg"])

            def on_leave(event):
                #reffered
                event.widget.config(bg="white", fg="black")

            def select_photo():
                file_paths = filedialog.askopenfilenames(title="Select Images",filetypes=[("Image Files", "*.png;*.jpg;*.gif")])
                if file_paths:
                    for path in file_paths:
                        print("Selected File:", path)
                        sent_photos2.append(path)
                        recieved_photos1.append(path)
                        print(f"{recieved_photos1} \n {sent_photos2}")
                check_toggle()

            def select_video():
                file_paths = filedialog.askopenfilenames(title="Select Videos",filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
                if file_paths:
                    for path in file_paths:
                        print("Selected File:", path)
                        sent_videos2.append(path)
                        recieved_videos1.append(path)
                        print(f"{recieved_videos2} \n {sent_videos1}")
                check_toggle()

            def select_Files():
                file_paths = filedialog.askopenfilenames(title="Select Files",filetypes=[("PDF Files", "*.pdf"),("PowerPoint Files", "*.ppt;*.pptx"),("Audio Files", "*.mp3;*.wav"),("Text Files", "*.txt")])
                if file_paths:
                    for path in file_paths:
                        print("Selected File:", path)
                        media_storage_1.append(path)
                        print(media_storage_1)
                check_toggle()


            def select_Pay():
                from tkinter import ttk
                Pay_Frame=Frame(media_select_pop_up,width=393,height=144,bg="black",relief="solid",bd=1)
                Pay_Frame.place(x=1,y=1)
                Pay_Title=Label(Pay_Frame,text="Pay",font="Purisa 20 bold",bg="black",fg="white")
                Pay_Title.place(x=75,y=20)
                Pay_Label=Label(Pay_Frame,text="₹",font="Purisa 20 bold",bg="black",fg="white")
                Pay_Label.place(x=75,y=60)
                Pay_Entry = Entry(Pay_Frame,font="Purisa 12", relief="solid",width=25, bd=1,justify="center")
                Pay_Entry.place(x=100, y=67)

                def del_Pay_FRAme():
                    Pay_Frame.destroy()

                def payment():
                    from tkinter import ttk
                    import time
                    global abort
                    abort = False
                    

                    def abort_pb():
                        global abort
                        abort = True
                        Payment_Frame.destroy()

                    if Pay_Entry.get().isdigit()==True:
                        def update_progress():
                            global media_select_pop_up,Balance
                            pb_progress_label=Label(Payment_Frame,text="Payment in progress...",bg="black",fg="white",font=("purisa 8 bold"))
                            pb_progress_label.place(x=225,y=90)
                            for i in range(86):  
                                pb['value'] = i
                                media_select_pop_up.update_idletasks()
                                time.sleep(0.01)
                                
                            pb_progress_label.config(text="Almost there...",width=30,font=("purisa 8 bold"))
                            pb_progress_label.place(x=205,y=90)
                            media_select_pop_up.after(2000)
                            
                            for i in range(86, 101):
                                pb['value'] = i
                                media_select_pop_up.update_idletasks()
                                time.sleep(0.01)

                            media_select_pop_up.after(2000)
                            pb.destroy()
                            Payment_Title.config(text="Paid")
                            Payment_Title.place(x=165,y=20)
                            pb_progress_label.destroy()
                            pb_Label = Label(Payment_Frame, text="Payment Successful", font=("Arial 15 bold"), fg="green", bg="black")
                            pb_Label.place(x=110, y=55)
                            s2_transact_history.append(f"You Sent ₹{Pay_Entry.get()}")
                            s1_transact_history.append(f"You Recieved ₹{Pay_Entry.get()}")
                            print(s1_transact_history)
                            print(s2_transact_history)
                            Balance+=int(Pay_Entry.get())
                            print(Balance)
  
                        Payment_Frame = Frame(media_select_pop_up, width=393, height=144, bg="black", relief="solid", bd=1)
                        Payment_Frame.place(x=1, y=1)
                        Payment_Title=Label(Payment_Frame,text="Pay",font="Purisa 20 bold",bg="black",fg="white")
                        Payment_Title.place(x=75,y=20)
                        pb = ttk.Progressbar(Payment_Frame, orient='horizontal', mode='determinate', length=280)
                        pb.place(x=75, y=65)
                        
                        
                        update_progress()

                        def exit_pb():
                            check_toggle()

                        pb_cancel_button = Button(Payment_Frame, text="OK", font="Purisa 10 bold", command=exit_pb)
                        pb_cancel_button.place(x=185, y=100)

                    else:
                        Payment_Frame = Frame(media_select_pop_up, width=393, height=144, bg="black", relief="solid", bd=1)
                        Payment_Frame.place(x=1, y=1)
                        pb_Label = Label(Payment_Frame, text="Invalid Values Entered", font=("Arial 15 bold"), fg="red", bg="black")
                        pb_Label.place(x=90, y=50)
                        pb_cancel_button = Button(Payment_Frame, text="Cancel", font="Purisa 10 bold", command=abort_pb)
                        pb_cancel_button.place(x=150, y=100)
                            
                    
                    
                    

                button_colors = {
                "Pay": {"bg": "Green", "fg": "white"},
                "Cancel": {"bg": "red", "fg": "white"},
                }

                def on_enter(event):
                #reffered
                    button_name = event.widget.cget("text")
                    event.widget.config(bg=button_colors[button_name]["bg"], fg=button_colors[button_name]["fg"])

                def on_leave(event):
                    #reffered
                    event.widget.config(bg="white", fg="black")

                Pay_Button=Button(Pay_Frame,text="Pay",font=("Purisa 9 bold"),command=payment,width=10,relief="solid",bd=1)
                Pay_Button.place(x=250, y=100)
                Pay_Button.bind("<Enter>", on_enter)
                Pay_Button.bind("<Leave>", on_leave)

                Pay_Cancel=Button(Pay_Frame,text="Cancel",font=("Purisa 9 bold"),command=del_Pay_FRAme,width=10,relief="solid",bd=1)
                Pay_Cancel.place(x=75, y=100)
                Pay_Cancel.bind("<Enter>", on_enter)
                Pay_Cancel.bind("<Leave>", on_leave)
                
                
                
                        
                
            from tkinter import filedialog, Tk
            media_select_pop_up=Frame(chat_frame2,width=400,height=150,bg="bisque",relief="solid",bd=2)
            media_select_pop_up.place(x=0,y=365)

            button_photo = Button(media_select_pop_up, text="Photo",width=5,font=("bold"),relief="solid",bd=1,command=select_photo)
            button_photo.place(x=60,y=50)
            button_photo.bind("<Enter>", on_enter)
            button_photo.bind("<Leave>", on_leave)

            button_video = Button(media_select_pop_up, text="Video",width=5,font=("bold"),relief="solid",bd=1,command=select_video)
            button_video.place(x=135,y=50)
            button_video.bind("<Enter>", on_enter)
            button_video.bind("<Leave>", on_leave)

            button_file = Button(media_select_pop_up, text="File",width=5,font=("bold"),relief="solid",bd=1,command=select_Files)
            button_file.place(x=210,y=50)
            button_file.bind("<Enter>", on_enter)
            button_file.bind("<Leave>", on_leave)

            button_pay = Button(media_select_pop_up, text="Pay",width=5,font=("bold"),relief="solid",bd=1,command=select_Pay)
            button_pay.place(x=285,y=50)
            button_pay.bind("<Enter>", on_enter)
            button_pay.bind("<Leave>", on_leave)

            button_custom = Button(media_select_pop_up, text="Custom",width=10,font=("bold"),relief="solid",bd=1)
            button_custom.place(x=150,y=100)
            button_custom.bind("<Enter>", on_enter)
            button_custom.bind("<Leave>", on_leave)

        def exit_media_pop_up():
            global media_select_pop_up
            media_select_pop_up.destroy()

        def check_toggle():
            global media_click
            if media_click==False:
                media_start_pop_up_2()
                media_click=True
            else:
                exit_media_pop_up()
                media_click=False

        check_toggle()

    def show_media_2():
        media_frame2=Frame(chat_frame2,width=250,height=300,relief="solid",bd=1)
        media_frame2.place(x=100,y=39)

        def del_media_frame():
            media_frame2.destroy()
            
        def show_media_sent():
            def del_media_sent():
                media_exit_button2.config(command=media_frame2.destroy)
                media_title_label2.config(text="Media")
                media_container_sent_frame2.destroy()

            def sent_photos_mod():
                def show_photos_sent():
                    def del_photos_sent():
                        media_title_label2.config(text="Sent Media")
                        media_container_photos_frame2.destroy()
                        media_frame2.config(width=250, height=300)
                        media_frame2.place(x=100, y=39)
                        media_exit_button2.config(command=del_media_sent)
                        

                    media_exit_button2.config(command=del_photos_sent)
                    media_title_label2.config(text="Sent Photos")

                    
                    media_frame2.config(height=600, width=400)
                    media_frame2.place(x=0, y=0)

                    media_container_photos_frame2 = Frame(media_container_frame2, width=400, height=550, bg="light cyan")
                    media_container_photos_frame2.place(x=0, y=0, relwidth=1, relheight=1)

                    import os
                    from tkinter import PhotoImage
                    from tkinter import messagebox

                    def open_photo(event):
                        selected_index = media_listbox2.curselection()
                        if selected_index:
                            selected_image_path = sent_photos2[selected_index[0]]
                            try:
                                os.startfile(selected_image_path)
                            except Exception as e:
                                messagebox.showerror("Error", f"Unable to open photo: {e}")

                    def extract_image_name(path):
                        return os.path.basename(path)

                    media_listbox2 = Listbox(media_container_photos_frame2, selectmode="single", bg="white", fg="black", selectbackground="black",selectforeground="light green")
                    media_listbox2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

                    scrollbar2 = Scrollbar(media_container_photos_frame2, command=media_listbox2.yview)
                    scrollbar2.place(relx=0.9, rely=0.1, relheight=0.7)
                    media_listbox2.config(yscrollcommand=scrollbar2.set)

                    media_listbox2.bind("<Double-Button-1>", open_photo)

                    for path in sent_photos2:
                        image_name = extract_image_name(path)
                        media_listbox2.insert("end", image_name)

                show_photos_sent()

            def sent_videos_mod():
                def show_videos_sent():
                    def del_videos_sent():
                        media_title_label2.config(text="Sent Media")
                        media_container_videos_frame2.destroy()
                        media_frame2.config(width=250, height=300)
                        media_frame2.place(x=100, y=39)
                        media_exit_button2.config(command=del_media_sent)

                    media_exit_button2.config(command=del_videos_sent)
                    media_title_label2.config(text="Sent Videos")

                    
                    media_frame2.config(height=600, width=400)
                    media_frame2.place(x=0, y=0)

                    media_container_videos_frame2 = Frame(media_container_frame2, width=400, height=550, bg="light cyan")
                    media_container_videos_frame2.place(x=0, y=0, relwidth=1, relheight=1)

                    import os
                    from tkinter import messagebox

                    def open_video(event):
                        selected_index = media_listbox2.curselection()
                        if selected_index:
                            selected_video_path = sent_videos2[selected_index[0]]
                            try:
                                os.startfile(selected_video_path)
                            except Exception as e:
                                messagebox.showerror("Error", f"Unable to open video: {e}")

                    def extract_video_name(path):
                        return os.path.basename(path)

                    media_listbox2 = Listbox(media_container_videos_frame2, selectmode="single", bg="white", fg="black", selectbackground="black", selectforeground="light green")
                    media_listbox2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

                    scrollbar2 = Scrollbar(media_container_videos_frame2, command=media_listbox2.yview)
                    scrollbar2.place(relx=0.9, rely=0.1, relheight=0.7)
                    media_listbox2.config(yscrollcommand=scrollbar2.set)

                    media_listbox2.bind("<Double-Button-1>", open_video)

                    for path in sent_videos2:
                        video_name = extract_video_name(path)
                        media_listbox2.insert("end", video_name)

                show_videos_sent()
                
            
            media_title_label2.config(text="Sent Media")
            media_container_sent_frame2 = Frame(media_container_frame2, width=400, height=550, bg="light cyan")
            media_container_sent_frame2.place(x=0, y=0,relwidth=1, relheight=1)

            media_option_photo_Button2=Button(media_container_sent_frame2,text="Photos \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=sent_photos_mod)
            media_option_photo_Button2.place(x=30,y=50)

            media_option_video_Button2=Button(media_container_sent_frame2,text="Videos \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=sent_videos_mod)
            media_option_video_Button2.place(x=30,y=100)

            media_option_file_Button2=Button(media_container_sent_frame2,text="Files \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=show_transactions)
            media_option_file_Button2.place(x=30,y=150)

            media_exit_button2.config(command=del_media_sent)
            
        def show_media_recieved():
            import os
            def del_media_received2():
                media_exit_button2.config(command=media_frame2.destroy)
                media_title_label2.config(text="Media")
                media_container_recieved_frame2.destroy()

            def received_photos_mod():
                def show_photos_received():
                    def del_photos_received():
                        media_title_label2.config(text="Received Media")
                        media_container_photos_frame2.destroy()
                        media_frame2.config(width=250, height=300)
                        media_frame2.place(x=100, y=39)
                        media_exit_button2.config(command=del_media_received2)

                    media_exit_button2.config(command=del_photos_received)
                    media_title_label2.config(text="Received Photos")

                    
                    media_frame2.config(height=600, width=400)
                    media_frame2.place(x=0, y=0)

                    media_container_photos_frame2 = Frame(media_container_frame2, width=400, height=550, bg="light cyan")
                    media_container_photos_frame2.place(x=0, y=0, relwidth=1, relheight=1)

                    def open_photo(event):
                        selected_index = media_listbox2.curselection()
                        if selected_index:
                            selected_image_path = recieved_photos2[selected_index[0]]
                            try:
                                os.startfile(selected_image_path)
                            except Exception as e:
                                messagebox.showerror("Error", f"Unable to open photo: {e}")

                    def extract_image_name(path):
                        return os.path.basename(path)

                    media_listbox2 = Listbox(media_container_photos_frame2, selectmode="single", bg="white", fg="black", selectbackground="black", selectforeground="light green")
                    media_listbox2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

                    scrollbar2 = Scrollbar(media_container_photos_frame2, command=media_listbox2.yview)
                    scrollbar2.place(relx=0.9, rely=0.1, relheight=0.7)
                    media_listbox2.config(yscrollcommand=scrollbar2.set)

                    media_listbox2.bind("<Double-Button-1>", open_photo)

                    for path in recieved_photos2:
                        image_name = extract_image_name(path)
                        media_listbox2.insert("end", image_name)

                show_photos_received()

            def received_videos_mod():
                def show_videos_received():
                    def del_videos_received():
                        media_title_label2.config(text="Received Media")
                        media_container_videos_frame2.destroy()
                        media_frame2.config(width=250, height=300)
                        media_frame2.place(x=100, y=39)
                        media_exit_button2.config(command=del_media_received2)

                    media_exit_button2.config(command=del_videos_received)
                    media_title_label2.config(text="Received Videos")

                    
                    media_frame2.config(height=600, width=400)
                    media_frame2.place(x=0, y=0)

                    media_container_videos_frame2 = Frame(media_container_frame2, width=400, height=550, bg="light cyan")
                    media_container_videos_frame2.place(x=0, y=0, relwidth=1, relheight=1)

                    def open_video(event):
                        selected_index = media_listbox2.curselection()
                        if selected_index:
                            selected_video_path = recieved_videos2[selected_index[0]]
                            try:
                                os.startfile(selected_video_path)
                            except Exception as e:
                                messagebox2.showerror("Error", f"Unable to open video: {e}")

                    def extract_video_name(path):
                        return os.path.basename(path)

                    media_listbox2 = Listbox(media_container_videos_frame2, selectmode="single", bg="white", fg="black", selectbackground="black", selectforeground="light green")
                    media_listbox2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

                    scrollbar2 = Scrollbar(media_container_videos_frame2, command=media_listbox2.yview)
                    scrollbar2.place(relx=0.9, rely=0.1, relheight=0.7)
                    media_listbox2.config(yscrollcommand=scrollbar2.set)

                    media_listbox2.bind("<Double-Button-1>", open_video)

                    for path in recieved_videos2:
                        vid_name = extract_video_name(path)
                        media_listbox2.insert("end", vid_name)

                show_videos_received()

            media_exit_button2.config(command=del_media_received2)
            media_title_label2.config(text="Recieved Media")
            
            media_container_recieved_frame2 = Frame(media_container_frame2, width=400, height=550, bg="light cyan")
            media_container_recieved_frame2.place(x=0, y=0,relwidth=1, relheight=1)

            media_option_photo_Button2=Button(media_container_recieved_frame2,text="Photos \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=received_photos_mod)
            media_option_photo_Button2.place(x=30,y=50)

            media_option_video_Button2=Button(media_container_recieved_frame2,text="Videos \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=received_videos_mod)
            media_option_video_Button2.place(x=30,y=100)

            media_option_file_Button2=Button(media_container_recieved_frame2,text="Files \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=show_transactions)
            media_option_file_Button2.place(x=30,y=150)

        def show_transactions():
            def del_show_transactions():
                media_title_label2.config(text="Media")
                media_exit_button2.config(command=del_media_frame)
                media_container_recieved_frame2.destroy()

            media_exit_button2.config(command=del_show_transactions)
            media_title_label2.config(text="Received Media")
            
            
            media_container_recieved_frame2 = Frame(media_container_frame2, width=400, height=550, bg="light cyan")
            media_container_recieved_frame2.place(x=0, y=35, relwidth=1, relheight=1)

            tranact_text_widget2 = Text(media_container_recieved_frame2, wrap="word", font=("Arial", 12),state=DISABLED)
            tranact_text_widget2.pack(side="left", fill="both", expand=True)

            for i in s2_transact_history:
                tranact_text_widget2.config(state=NORMAL)
                tranact_text_widget2.insert(END, f" {i}\n")
                tranact_text_widget2.config(state=DISABLED)
            
            scrollbar_transact2 = Scrollbar(media_container_recieved_frame2, command=tranact_text_widget2.yview)
            scrollbar_transact2.pack(side="right", fill="y")
            
            tranact_text_widget2.config(yscrollcommand=scrollbar_transact2.set)
            




            
        media_title_frame2 = Frame(media_frame2,width=200,height=100,bg="Green")
        media_title_frame2.place(x=0, y=0)
        
        media_exit_button2 = Button(media_title_frame2, text="<",font="Purisa 12 bold",command=del_media_frame,relief="flat",fg="White",bg="green")
        media_exit_button2.grid(row=0, column=0, padx=10, pady=0)

        media_title_label2 = Label(media_title_frame2, text="Media",fg="White",bg="green",width=35,anchor='w',font="Purisa 12 bold")
        media_title_label2.grid(row=0, column=1, padx=5, pady=5)
        

        media_container_frame2 = Frame(media_frame2, width=200, height=200, bg="light cyan")
        media_container_frame2.place(x=0, y=35,relwidth=1, relheight=0.88)

        media_option_sent_Button2=Button(media_container_frame2,text="Sent \t \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=show_media_sent)
        media_option_sent_Button2.place(x=30,y=50)

        media_option_recieved_Button2=Button(media_container_frame2,text="Recieved \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=show_media_recieved)
        media_option_recieved_Button2.place(x=30,y=100)

        media_option_thistory_Button2=Button(media_container_frame2,text="Transactions \t >",bg="aquamarine",relief="solid",bd=1,fg="dark blue",justify="left",width=20,font=("Ariel 11 bold"),command=show_transactions)
        media_option_thistory_Button2.place(x=30,y=150)

    
    
    title_frame2 = Frame(win2,width=400,height=200,bg="Green")
    title_frame2.place(x=0, y=0)

    exit_button2 = Button(title_frame2, text="<",font="Purisa 12 bold",relief="flat",fg="White",bg="green")
    exit_button2.grid(row=0, column=0, padx=10, pady=0)

    title_label2 = Label(title_frame2, text="Chat",fg="White",bg="green",anchor='w',font="Purisa 12 bold")
    title_label2.grid(row=0, column=1, padx=5, pady=5)

    More_button2 = Button(title_frame2, text=",",font="Purisa 12 bold",command=show_media_2,relief="flat",fg="White",bg="green")
    More_button2.grid(row=0, column=2, padx=270, pady=0)

    
    chat_frame2 = Frame(win2, width=400, height=550, bg="red")
    chat_frame2.place(x=0, y=35,relwidth=2, relheight=0.86)

    chat_frame_main2 = Frame(chat_frame2, width=20, height=550)
    chat_frame_main2.pack(side="left",fill=Y)


    scrollbar2 = Scrollbar(chat_frame_main2, orient=VERTICAL)
    scrollbar2.pack(side=RIGHT, fill=Y)

    chat_text2 = Text(chat_frame_main2, wrap=WORD, yscrollcommand=scrollbar2.set, state=DISABLED)
    chat_text2.pack(expand=True, fill=BOTH)

    scrollbar2.config(command=chat_text2.yview)

    
    text_frame2 = Frame(win2,width=400,height=20,bd=2,relief="solid")
    text_frame2.place(x=0, y=553)

    Media_Button2=Button(text_frame2,text="+",font=("Purisa 12 bold"),relief="flat",command=media_popUp_2_start)
    Media_Button2.grid(row=0, column=1, padx=10, pady=5)
    text_entry2 = Entry(text_frame2, width=50,bd=1,relief="solid")
    text_entry2.grid(row=0, column=2, padx=5, pady=5)

    send_button2 = Button(text_frame2, text=">",relief="flat",font=("Purisa 12 bold"), command=send_entry_s2)
    send_button2.grid(row=0, column=3, padx=6, pady=5)

    check_message()

    win2.mainloop()


#class to make frames/ any elememts dragable -refered
class DragManager():
    def add_dragable_widget(self,widget):
        self.widget=widget
        self.win=widget.winfo_toplevel()
        self.widget.bind("<B1-Motion>",self.on_drag)
        self.widget.bind("<ButtonRelease>",self.on_drop)

    def on_drag(self, event):
        #x,y=pyautogui.position()
        self.widget.place(x=self.win.winfo_pointerx()-self.win.winfo_rootx(),y=self.win.winfo_pointery()-self.win.winfo_rooty())

    def on_drop(self, event):
        #x,y=pyautogui.position()
        self.widget.place(x=self.win.winfo_pointerx()-self.win.winfo_rootx(),y=self.win.winfo_pointery()-self.win.winfo_rooty())


#calculator app        
def Calculator_app():
    class Calc:
        def __init__(self, master):
            self.MathVariable = 0
            self.Value = 0
            self.master = master

            
            self.Calc_Frame = Frame(master, width=272, height=155,bg="black")
            self.Calc_Frame.place(x=0, y=0)
            drag = DragManager()
            drag.add_dragable_widget(self.Calc_Frame)
            
            def del_cal():
                self.Calc_Frame.destroy()
                
            self.NumberEntry = Entry(self.Calc_Frame, width=25, relief="solid", justify="center")
            self.NumberEntry.grid(row=0, column=0, padx=30, pady=10, columnspan=5)

            self.NumberEntry.insert(0, "Cntrl+T to Exit")
            win.after(2000,lambda: self.NumberEntry.delete(0, END))

            i, j = 1, 0
            for btn in ['7', '4', '1', '8', '5', '2', '9', '6', '3', '+', '-', '0', '*', '/','=']:
                if i % 4 == 0:
                    i = 1
                    j += 1
                Button(self.Calc_Frame, text=btn,relief="flat",bd=1, bg="black",fg="red",font="Ariel 10 bold",width=5, command=lambda btn=btn: self.BtnClick(btn)).grid(row=i, column=j, ipadx=i)
                i += 1

            self.clear = Button(self.Calc_Frame, text="Clear",relief="flat", bg="black",fg="red",width=15, command=self.Clear).grid(row=5, columnspan=6, ipadx=70)

        def BtnClick(self, number):
            if number == '=':
                self.Equal()
            else:
                self.NumberEntry.insert(len(self.NumberEntry.get()) + 1, str(number))

        def Equal(self):
            value1 = self.NumberEntry.get()
            try:
                value1 = eval(value1)
                self.NumberEntry.delete(0, END)
                self.NumberEntry.insert(0, value1)
            except Exception as e:
                self.NumberEntry.delete(0, END)
                self.NumberEntry.insert(0, e)

        def Clear(self):
            self.NumberEntry.delete(0, END)
            self.Value = 0

    if __name__ == "__main__":
        inst=Calc(win)
        win.after(2000,lambda:win.bind("<Control-t>", lambda event: inst.Calc_Frame.destroy()))

def open_bmi():
    print("opening bmi")


#file manager app
def file_manager():
    import shutil
    import os
    import time
    from distutils.dir_util import copy_tree
    from send2trash import send2trash

    def update_cwd_label():
        current_path = os.getcwd()
        cwd_Label.delete(0, "end")
        cwd_Label.insert(0, os.getcwd())

    def list_folders_and_files():
        contents = os.listdir(os.getcwd())
        File_List.delete(0, END)  

        for item in contents:
            File_List.insert(END, item)

    def open_selected_folder(event):
        selected_item_index = File_List.curselection()

        if selected_item_index:
            selected_item = File_List.get(selected_item_index)
            selected_path = os.path.join(os.getcwd(), selected_item)
            Back_button.config(bg="Blue",fg="White")

            if os.path.isdir(selected_path):
                os.chdir(selected_path)
                update_cwd_label()
                list_folders_and_files()
                
        if os.getcwd() ==perma_path:
            Back_button.config(bg="White",fg="Gray")
                
    def go_back():
        global path
        if os.getcwd() != perma_path:
            os.chdir("..")
            Back_button.config(bg="Blue",fg="White")
            path = os.path.relpath(os.getcwd(), perma_path)
            update_cwd_label()
            list_folders_and_files()
        else:
            Back_button.config(bg="White",fg="Gray")
            print("Warning", "Already at the root directory.")
        if os.getcwd() ==perma_path:
            Back_button.config(bg="White",fg="Gray")
        
    def show_popup(event):
        def destroy_popup(event):
            PopUp_Frame.destroy()
            
        try:
            destroy_popup()
        except:
            print("no pop up")
        finally:
            # Get the current cursor position
            
            x, y = event.x, event.y
            
            PopUp_Frame=Frame(File_Frame,width=122,height=150,bg="white",bd=1, relief="solid")
            PopUp_Frame.place(x=x, y=y)
     
            New_popup_button=Button(PopUp_Frame,text=" New        (Ctrl+N)",width=16,relief=SOLID,bd=1,anchor="w",command=lambda event=None:{show_new_folder_frame(),destroy_popup(event)})
            New_popup_button.place(x=0,y=0)
            Cut_popup_button=Button(PopUp_Frame,text=" Cut          (Ctrl+X)",width=16,relief=SOLID,bd=1,anchor="w",command=lambda event=None:{cut_action(),destroy_popup(event)})
            Cut_popup_button.place(x=0,y=23)
            Copy_popup_button=Button(PopUp_Frame,text=" Copy       (Ctrl+C)",width=16,relief=SOLID,bd=1,anchor="w",command=lambda event=None:{copy_action(),destroy_popup(event)})
            Copy_popup_button.place(x=0,y=46)
            Paste_popup_button=Button(PopUp_Frame,text=" Paste       (Ctrl+V)",width=16,relief=SOLID,bd=1,anchor="w",command=lambda event=None:{paste_action(),destroy_popup(event)})
            Paste_popup_button.place(x=0,y=69)
            Rename_popup_button=Button(PopUp_Frame,text=" Rename  (Ctrl+R)",width=16,relief=SOLID,bd=1,anchor="w",command=lambda event=None:{rename_action(),destroy_popup(event)})
            Rename_popup_button.place(x=0,y=92)
            Delete_popup_button=Button(PopUp_Frame,text=" Delete  (Ctrl+D)",width=16,relief=SOLID,bd=1,anchor="w",command=lambda event=None:{delete_confirmation(event),destroy_popup(event)})
            Delete_popup_button.place(x=0,y=92)

            PopUp_Frame.bind('<FocusOut>', destroy_popup)
            PopUp_Frame.focus_set()

    def go_to_home():
        os.chdir(perma_path)
        update_cwd_label()
        list_folders_and_files()

    def create_new_folder():
        global folder_name_entry, New_Folder_Frame
        folder_name = folder_name_entry.get()
        if folder_name:
            folder_path = os.path.join(os.getcwd(), folder_name)

            try:
                os.makedirs(folder_path)
                print(f"New folder created: {folder_path}")
                list_folders_and_files()
                New_Folder_Frame.destroy()
            except FileExistsError:
                folder_name_warning = Label(New_Folder_Frame, text=f"Folder '{folder_name}' already exists.",
                                           font=("Purisa 10 bold"), bg="Light Gray", fg="red")
                folder_name_warning.place(x=50, y=37)
                print(f"Folder '{folder_name}' already exists.")
            except Exception as e:
                print(f"Error creating folder: {e}")
                folder_name_warning = Label(New_Folder_Frame, text=f"Error creating folder: {e}",
                                           font=("Purisa 10 bold"), bg="Light Gray", fg="red")
                folder_name_warning.place(x=10, y=37)

    cut_item = None  
    copied_item = None

    def cut_action():
        selected_item_index = File_List.curselection()

        if selected_item_index:
            selected_item = File_List.get(selected_item_index)
            selected_path = os.path.join(os.getcwd(), selected_item)

           
            print(f"Cut action for: {selected_path}")
            global cut_item
            cut_item = (selected_item, selected_path)  # Set cut_item to the selected item and its path


    def copy_action():
        selected_item_index = File_List.curselection()

        if selected_item_index:
            selected_item = File_List.get(selected_item_index)
            selected_path = os.path.join(os.getcwd(), selected_item)

            try:
                global copied_item  # Declare copied_item as a global variable
                copied_item = (selected_item, selected_path)
                print(f"Copy action for: {selected_path}")

            except Exception as e:
                print(f"Error during copy action: {e}")

    def paste_action():
        global cut_item, copied_item
        if cut_item:
            item_name, item_path = cut_item
            destination_path = os.path.join(os.getcwd(), item_name)

            try:
                if os.path.exists(destination_path):
                    raise FileExistsError(f"Destination path already exists: {destination_path}")

                # Using shutil.move for moving files or directories
                shutil.move(item_path, destination_path)

                list_folders_and_files()
                cut_item = copied_item = None  # Reset cut_item and copied_item after pasting
                print(f"Cut action successful: {item_path} to {destination_path}")
            except Exception as e:
                print(f"Error during cut action: {e}")

        elif copied_item:
            item_name, item_path = copied_item
            destination_path = os.path.join(os.getcwd(), f"Copy_of_{item_name}")

            try:
                if os.path.exists(destination_path):
                    raise FileExistsError(f"Destination path already exists: {destination_path}")

                # Using distutils.dir_util.copy_tree for copying directories
                copy_tree(item_path, destination_path)

                list_folders_and_files()
                copied_item = None
                print(f"Copy action successful: {item_path} to {destination_path}")

            except Exception as e:
                print(f"Error during paste action (copy): {e}")
        else:
            print("No item to paste.")

    rename_window=None
    def rename_action():

        try:
            rename_window.destroy()
        except:
            print("rename_window does not exist")
        finally:
            selected_item_index = File_List.curselection()

            if selected_item_index:
                selected_item = File_List.get(selected_item_index)
                selected_path = os.path.join(os.getcwd(), selected_item)

                
                rename_window =Frame(File_Frame, width=300, height=110, bg="light gray", bd=2, relief="solid")
                rename_window.place(x=50, y=450)
                folder_name_label = Label(rename_window, text="New Name:", bg="Light gray", font=("Purisa 12 bold"))
                folder_name_label.place(x=26, y=15)
                
                new_name_entry = Entry(rename_window, width=20, font=("Purisa 10"), bd=1, relief="solid")
                new_name_entry.insert(0, selected_item)
                new_name_entry.place(x=120, y=17)

                
                def confirm_rename():
                    new_name = new_name_entry.get()
                    new_path = os.path.join(os.getcwd(), new_name)

                    try:
                        os.rename(selected_path, new_path)
                        print(f"Renamed '{selected_item}' to '{new_name}'")
                        list_folders_and_files()
                        rename_window.destroy()
                    except FileExistsError:
                        folder_name_warning = Label(rename_window, text=f"Folder '{new_name}' already exists.",
                                               font=("Purisa 10 bold"), bg="Light Gray", fg="red")
                        folder_name_warning.place(x=50, y=37)
                        print(f"Error: '{new_name}' already exists.")
                    except Exception as e:
                        print(f"Error creating folder: {e}")
                        folder_name_warning = Label(rename_window, text=f"Error creating folder: {e}",
                                               font=("Purisa 10 bold"), bg="Light Gray", fg="red")
                        folder_name_warning.place(x=10, y=37)

                
                confirm_button = Button(rename_window, text="Confirm", font=("Purisa 10 bold"), command=confirm_rename, bd=1,
                                        relief="solid")
                confirm_button.place(x=175, y=65)

                
                cancel_button = Button(rename_window, text="Cancel", font=("Purisa 10 bold"), command=rename_window.destroy,
                                       bd=1, relief="solid")
                cancel_button.place(x=50, y=65)

    confirm_frame = None       

    def delete_action(selected_item):
        global confirm_frame
        try:
            if os.path.isfile(selected_item):
                # If it's a file, send the file to trash
                send2trash(selected_item)
            elif os.path.isdir(selected_item):
                # If it's a directory, delete it along with its contents
                shutil.rmtree(selected_item)
            else:
                try:
                    warning_label.destroy()
                except:
                    print("No warning Label")
                finally:
                    warning_label=Label(File_Frame,text=f"Unsupported item type: {selected_item}",font=("Purisa 10 bold"),fg="red",bg="White")
                    warning_label.place(x=50,y=450)
                    win.after(2000,warning_label.destroy())
                    print(f"Unsupported item type: {selected_item}")
                return
            try:
                warning_label.destroy()
            except:
                print("No warning Label")
            finally:
                warning_label=Label(File_Frame,text=f"Item deleted: {selected_item}",font=("Purisa 10 bold"),fg="red",bg="White")
                warning_label.place(x=50,y=450)
                win.after(2000,warning_label.destroy())
            print(f"Item deleted: {selected_item}")
        except Exception as e:
            try:
                warning_label.destroy()
            except:
                print("No warning Label")
            finally:
                warning_label=Label(File_Frame,text=f"Error deleting item: {e}",font=("Purisa 10 bold"),fg="red",bg="White")
                warning_label.place(x=50,y=450)
                win.after(2000,warning_label.destroy())
            print(f"Error deleting item: {e}")

        if confirm_frame:
            confirm_frame.destroy()  
        list_folders_and_files()  
        
    def delete_confirmation(event=None):
        global confirm_frame
        try:
            confirm_frame.destroy()
        except:
            print("confirm_frame does not exist")
        finally:
            selected_item_index = File_List.curselection()

            if selected_item_index:
                selected_item = File_List.get(selected_item_index)
                confirm_frame = Frame(File_Frame, width=300, height=110, bg="light gray", bd=2, relief="solid")
                confirm_frame.place(x=50, y=450)

                confirm_label = Label(confirm_frame, text=f"Do you really want to delete \n '{selected_item}'?", bg="Light gray",
                                      font=("Purisa 10 bold"))
                confirm_label.place(x=50, y=15)

                confirm_yes_button = Button(confirm_frame, text="Yes",width=5, font=("Purisa 10 bold"), command=lambda: delete_action(selected_item), bd=1, relief="solid")
                confirm_yes_button.place(x=195, y=65)

                confirm_no_button = Button(confirm_frame, text="No",width=5, font=("Purisa 10 bold"), command=lambda: confirm_frame.destroy(), bd=1, relief="solid")
                confirm_no_button.place(x=50, y=65)

    def show_new_folder_frame():
        global folder_name_entry, New_Folder_Frame
        try:
            New_Folder_Frame.destroy()
        except:
            print("New_Folder_Frame does not exist")
        finally:

            New_Folder_Frame = Frame(File_Frame, width=300, height=110, bg="light gray", bd=2, relief="solid")
            New_Folder_Frame.place(x=50, y=450)
            folder_name_label = Label(New_Folder_Frame, text="New Folder Name:", bg="Light gray", font=("Purisa 9 bold"))
            folder_name_label.place(x=14, y=15)

            folder_name_entry = Entry(New_Folder_Frame, width=20, font=("Purisa 10"), bd=1, relief="solid")
            folder_name_entry.place(x=130, y=15)

            confirm_Button = Button(New_Folder_Frame, text="Confirm", font=("Purisa 10 bold"), command=create_new_folder,
                                    bd=1, relief="solid")
            confirm_Button.place(x=175, y=65)

            cancel_Button = Button(New_Folder_Frame, text="Cancel", font=("Purisa 10 bold"),
                                   command=lambda: New_Folder_Frame.destroy(), bd=1, relief="solid")
            cancel_Button.place(x=50, y=65)
    perma_path = "path_of_folder"    #replace path with the location of folder
    path = " "
    os.chdir(perma_path + path)

    current_path = os.getcwd()

    file_operation_menubar = Menu(win)
    File_Frame = Frame(win, width=400, height=600, bg="#EEE")
    File_Frame.place(x=0, y=0)
    file_menu = Menu(file_operation_menubar, tearoff=0)
    file_menu.add_command(label="New Folder", command=show_new_folder_frame)
    file_menu.add_separator()
    file_menu.add_command(label="Cut", command=cut_action)
    file_menu.add_command(label="Copy", command=copy_action)
    file_menu.add_command(label="Paste", command=paste_action)
    file_menu.add_command(label="Rename", command=rename_action)
    file_menu.add_separator()
    file_menu.add_command(label="Delete", command=lambda event=None: delete_confirmation(event))
    file_operation_menubar.add_cascade(label="File", menu=file_menu)

    
    Exit_menu = Menu(file_operation_menubar, tearoff=0)
    Exit_menu.add_command(label="Do you want to exit? Yes", command=lambda:{File_Frame.destroy(),file_operation_menubar.destroy()})
    
    file_operation_menubar.add_cascade(label="Exit", menu=Exit_menu)

    win.config(menu=file_operation_menubar)
    cwd_Label = Entry(File_Frame, width=50, font=("Purisa 10 "),bd=1,relief="solid")
    cwd_Label.place(x=20, y=10)

    update_cwd_label()

    canvas = Canvas(File_Frame, width=398, height=1, bg="black", highlightthickness=0)
    canvas.place(x=1, y=49)
    
    canvas = Canvas(File_Frame, width=5, height=500, bg="#EEE", highlightthickness=0)
    canvas.place(x=115, y=50)

    canvas.create_line(0, 0, 0, 385, fill="black")

    canvas = Canvas(File_Frame, width=5, height=500, bg="#EEE", highlightthickness=0)
    canvas.place(x=398, y=50)

    canvas.create_line(0, 0, 0, 385, fill="black")

    canvas = Canvas(File_Frame, width=5, height=500, bg="#EEE", highlightthickness=0)
    canvas.place(x=1, y=50)

    canvas.create_line(0, 0, 0, 385, fill="black")

    canvas = Canvas(File_Frame, width=398, height=1, bg="black", highlightthickness=0)
    canvas.place(x=1, y=434)

    Home_storage_button = Button(File_Frame, width=12, text="Home", font=("Purisa 10 bold"), fg="white", bg="red",
                                 command=go_to_home, relief=FLAT)
    Home_storage_button.place(x=5, y=53)

    Back_button = Button(File_Frame,width=5, text="<", font=("Purisa 10 bold"), fg="gray", bg="white",relief="solid",bd=1,
                     command=go_back)
    Back_button.place(x=5, y=90)
    
    Forward_button = Button(File_Frame,width=5, text=">", font=("Helvetica 10 bold"), fg="white", bg="Blue",relief="solid",bd=1,
                     command=lambda event=None:{open_selected_folder(event)})
    Forward_button.place(x=60, y=90)
    
    File_ListFrame = Frame(File_Frame, width=300, height=320, bg="#EEE")
    File_ListFrame.place(x=118, y=53)

    y_scrollbar = Scrollbar(File_ListFrame, orient="vertical")
    y_scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")

    x_scrollbar = Scrollbar(File_ListFrame, orient="horizontal")
    x_scrollbar.place(relx=0, rely=1, relheight=1, anchor="sw")

    File_List = Listbox(File_ListFrame, width=45, height=23, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
    File_List.pack(fill="both", expand=True)

    y_scrollbar.config(command=File_List.yview)
    x_scrollbar.config(command=File_List.xview)

    list_folders_and_files()




    File_List.bind("<Double-1>", open_selected_folder)
    File_List.bind("<Return>", open_selected_folder)
    win.bind("<Control-x>", lambda event: cut_action())
    win.bind("<Control-n>", lambda event: show_new_folder_frame())
    win.bind("<Control-v>", lambda event: paste_action())
    win.bind("<Control-c>", lambda event: copy_action())
    win.bind("<Control-d>", lambda event: delete_confirmation(event))
    win.bind("<Delete>", lambda event: delete_confirmation(event))
    win.bind("<Control-r>", lambda event: rename_action())
    win.bind('<Button-3>', show_popup)


#store app    
def store_startup():
    del_apps()
    del_nav()
    win.config(bg="SlateBlue3")
    Logo_1a = Label(win, bg="SlateBlue3", fg="lavender", text="sTore", font=("Purisa 20 bold"))
    Logo_1a.pack(pady=250)
    win.after(2000, lambda: Logo_1a.destroy())
    
    win.after(2000, lambda: win.config(bg="SlateBlue4"))
    Logo_2a = Label(win, bg="SlateBlue4", fg="light goldenrod", text="sof-sTore", font=("Purisa 20 bold"))
    Logo_2a.pack(pady=250)
    win.after(3000, lambda: Logo_2a.destroy())

    win.after(3000, lambda: win.config(bg="Black"))
    Logo_3a = Label(win, bg="Black", fg="gold", text="Software-Store", font=("Purisa 20 bold"))
    Logo_3a.pack(pady=250)
    win.after(5000, lambda: Logo_3a.destroy())
    win.after(5000, lambda: win.config(bg="white"))
    win.after(5000, store_interface)

def store_interface():
    from tkinter import ttk

    global app_data,navframe,app_download_Frame,installed_apps
    
    navframe = Frame(win, bg="black",height=50)
    navframe.pack(side="top", fill=X)
    
    nav_label=Label(navframe,bg="black",fg="Gold",text="Software-Store",font=("Purisa 20 bold"))
    nav_label.place(x=20,y=10)
    
    
    app_download_Frame = Frame(win, bg="White")
    app_download_Frame.pack(fill=BOTH, expand=YES, padx=2, pady=0)

    exit_store_button = Button(navframe, bg="black", fg="red", text="Exit", bd=0, font=("Purisa 15 bold"), command=del_store_app)
    exit_store_button.place(x=300,y=10)
    
    ttk.Separator(app_download_Frame, orient="horizontal").pack(pady=10, fill=X)

    Chat_app_download_Icon = Label(app_download_Frame, width=6, height=3, bg="Red")
    Chat_app_download_Icon.place(x=30, y=30)

    Chat_app_download_Label_1 = Label(app_download_Frame, bg="white", text="CommSync", font=("ariel 15 bold"), justify=LEFT)
    Chat_app_download_Label_1.place(x=82, y=30)

    Chat_app_download_Label_2 = Label(app_download_Frame, text="Conversations elevated", font=("ariel 8"), justify=LEFT)
    Chat_app_download_Label_2.place(x=82, y=60)

    Chat_app_download_Button = Button(app_download_Frame,bg="green",fg="white",text="↓",font=("Purisa 17 bold underline"),width=3,anchor=CENTER,relief=FLAT,command=lambda: (Chat_app_download_Button.config(bg="white",fg="black",width=7,text="Installed",font=("Purisa 10 bold underline"),anchor=CENTER,relief=FLAT),Chat_app_download_Button.place(x=280, y=32),installed_apps.append({"name": "CommSync", "func":chat_app})))
    Chat_app_download_Button.place(x=280, y=32)


    ttk.Separator(app_download_Frame, orient="horizontal").pack(pady=80, fill=X)

    BMI_app_download_Icon = Label(app_download_Frame, width=6, height=3, bg="Gray",relief=GROOVE)
    BMI_app_download_Icon.place(x=30, y=120)

    BMI_app_download_Label_1 = Label(app_download_Frame, bg="white", text="Fit_Cal", font=("ariel 15 bold"), justify=LEFT)
    BMI_app_download_Label_1.place(x=82, y=120)

    BMI_app_download_Label_2 = Label(app_download_Frame, text="A personalized path to wellness!", font=("ariel 8"), justify=LEFT)
    BMI_app_download_Label_2.place(x=82, y=150)

    BMI_app_download_Button = Button(app_download_Frame, bg="green", fg="white", text="↓", font=("Purisa 17 bold underline"), width=3, anchor=CENTER, relief=FLAT, command=lambda: (BMI_app_download_Button.config(bg="white",fg="black",width=7,text="Installed",font=("Purisa 10 bold underline"),anchor=CENTER,relief=FLAT),BMI_app_download_Button.place(x=280, y=122),installed_apps.append({"name": "Fit_Cal", "func":fitness_app})))
    BMI_app_download_Button.place(x=280, y=122)

    ttk.Separator(app_download_Frame, orient="horizontal").pack(pady=10, fill=X)

    Bank_app_download_Icon = Label(app_download_Frame, width=6, height=3, bg="orange")
    Bank_app_download_Icon.place(x=30, y=210)

    Bank_app_download_Label_1 = Label(app_download_Frame, bg="white", text="Bank", font=("ariel 15 bold"), justify=LEFT)
    Bank_app_download_Label_1.place(x=82, y=210)

    Bank_app_download_Label_2 = Label(app_download_Frame, text="Manage Your Bank Account seemlessly", font=("ariel 8"), justify=LEFT)
    Bank_app_download_Label_2.place(x=82, y=240)

    Bank_app_download_Button = Button(app_download_Frame, bg="white", fg="black", text="Installed", font=("Purisa 10 bold underline"), anchor=CENTER, relief=FLAT)
    Bank_app_download_Button.place(x=280, y=212)

    ttk.Separator(app_download_Frame, orient="horizontal").pack(pady=75, fill=X)

    Fliptra_app_download_Icon = Label(app_download_Frame, width=6, height=3, bg="AntiqueWhite1",relief=GROOVE)
    Fliptra_app_download_Icon.place(x=30, y=300)

    Fliptra_app_download_Label_1 = Label(app_download_Frame, bg="white", text="Fliptra", font=("ariel 15 bold"), justify=LEFT)
    Fliptra_app_download_Label_1.place(x=82, y=300)

    Fliptra_app_download_Label_2 = Label(app_download_Frame, text="Experience shopping from home", font=("ariel 8"), justify=LEFT)
    Fliptra_app_download_Label_2.place(x=82, y=330)

    Fliptra_app_download_Button = Button(app_download_Frame, bg="white", fg="black", text="Installed", font=("Purisa 10 bold underline"), anchor=CENTER, relief=FLAT)
    Fliptra_app_download_Button.place(x=280, y=302)

    ttk.Separator(app_download_Frame, orient="horizontal").pack(pady=20, fill=X)

def del_store_app():
    global navframe,app_download_Frame
    navframe.destroy()
    app_download_Frame.destroy()
    show_nav()

#opening apps from more apps folder
def open_selected_app():
    global More_listbox
    selected_index = More_listbox.curselection()

    if selected_index:
        selected_app = installed_apps[selected_index[0]]
        selected_app["func"]() 
        print(f"Opening {selected_app['name']}")
    else:
        print("No app selected")


def exit_more_apps():
    global More_apps_frame,More_apps_close
    More_apps_frame.destroy()

#more apps folder        
def More_apps():
    global More_apps_frame, installed_apps,More_listbox
    try:
        More_apps_frame.destroy()
    except:
        print("doesnt exist")
    finally:
        More_apps_frame = Frame(App_frame, bg="light gray", width=200, height=300)
        More_apps_frame.place(x=100, y=50)

        More_apps_label=Label(More_apps_frame, bg="black", fg="white", text="   More Apps",font=("purisa 14 bold"),width=20,anchor="w")
        More_apps_label.place(x=00,y=00)

        More_apps_close = Button(More_apps_frame, bg="red", fg="white", text="X", width=1, relief=FLAT, command=exit_more_apps)
        More_apps_close.place(x=183, y=0)

        More_listbox = Listbox(More_apps_frame, selectmode=SINGLE, width=30, height=13,relief=FLAT)
        More_listbox.place(x=8, y=40)

        More_listbox_select_button = Button(More_apps_frame, bg="Green", fg="white", text="Open",font=("Purisa 10 bold"), relief=FLAT, command=open_selected_app)   
        More_listbox_select_button.place(x=75, y=260)

        for app in installed_apps:
            if (len(installed_apps))==0:
                break
            else:
                More_listbox.insert(END, app["name"])
            
        drag = DragManager()
        drag.add_dragable_widget(More_apps_frame)

    
    
#list of apps   
app_button_pressed=False
app_data = [
    { "bg": "Orange", "fg": "White","name": "Bank", "func": Bank_APPS, "x": 45, "y": 40},
    { "bg": "White", "fg": "Red","name": "Shop", "func": Shopping_App_start, "x": 155, "y": 40},
    { "bg": "Black", "fg": "Red","name": "+/-", "func":Calculator_app, "x": 265, "y": 40},
    { "bg": "Black", "fg": "Gold","name": "Store", "func": store_startup, "x": 45, "y": 120},
    { "bg": "Gray", "fg": "White","name": "More", "func": More_apps,"x":155,"y":120}
]

def del_apps():
    global App_frame,app_button_pressed
    App_frame.destroy()
    app_button_pressed=False
    
    
def switch_setting():
    global btn_state, SettingFrame, SettingBar,noti
    try:
        del_apps()
    except:
        print("Apps Doesnt exist")
    finally:
        if btn_state:
            for y in range(601):
                SettingBar.place(x=0, y=-y)
                SettingFrame.update()
            noti.config(text="↓")
            btn_state = False
        else:
            for y in range(-560, 0):
                SettingBar.place(x=0, y=y)
                SettingFrame.update()
            noti.config(text="↑")
            btn_state = True

#app drawer
def apps():
    global app_data, App_frame,app_button_pressed
    if btn_state:
        switch_setting()
    app_button_pressed=True
    App_frame = Frame(win, bg=win.cget('bg'), height=558, width=402)
    App_frame.pack(fill=BOTH)

    for app in app_data:
        button = Button(App_frame, bg=app["bg"], fg=app["fg"],text=app["name"], font=("Bold", 20), width=5, bd=2, command=app["func"])
        button.place(x=app["x"], y=app["y"])

#check for toggle if app drawer is already open or not
def check_app_button_pressed():
    global app_button_pressed
    if app_button_pressed==True:
        del_apps()
    else:
        apps()
        
#to change bg color
def change_color_bg(selected_color):
    global App_frame
    color_label_bg.config(bg=selected_color)
    win.config(bg=selected_color)

#to change transparency
def change_opacity(value):
    try:
        opacity = float(value) / 100.0
        win.attributes('-alpha', opacity)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric value.")

installed_apps = [{"name": "File Manager", "func":file_manager}]

btn_state = False

SettingFrame = Frame(win, bg="black")
SettingFrame.pack(side='top', fill=X)

SettingBar = Frame(win, bg="black", height=560, width=402)
SettingBar.place(x=0, y=-560)

SettingBar_Label=Label(SettingBar,text="Settings",font=("Purisa 20 bold"),anchor="w",width=402,bg="Black",fg="white")
SettingBar_Label.place(x=10,y=10)

background_color_Label=Label(SettingBar,text="Background Color:",font=("Purisa 15 bold"),fg="white",bg="black")
background_color_Label.place(x=30,y=60)

colors = [
    'black', 'blanchedalmond', 'blue', 'yellow','blue2', 'blue3', 'blue4', 'cadetblue', 'cadetblue1', 'cadetblue2', 'cadetblue3', 'cadetblue4', 'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2', 'coral3', 'coral4', 'cornflowerblue', 'cornflowerblue1', 'cornflowerblue2', 'cornflowerblue3', 'cornflowerblue4', 'cyan', 'cyan1', 'cyan2', 'cyan3', 'cyan4', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgoldenrod1', 'darkgoldenrod2', 'darkgoldenrod3', 'darkgoldenrod4', 'darkgray', 'darkgreen', 'darkkhaki', 'darkkhaki1', 'darkkhaki2', 'darkkhaki3', 'darkkhaki4', 'darkmagenta', 'darkmagenta1', 'darkmagenta2', 'darkmagenta3', 'darkmagenta4', 'darkolivegreen', 'darkolivegreen1', 'darkolivegreen2', 'darkolivegreen3', 'darkolivegreen4', 'darkorange', 'darkorange1', 'darkorange2', 'darkorange3', 'darkorange4', 'darkorchid', 'darkorchid1', 'darkorchid2', 'darkorchid3', 'darkorchid4', 'darkred', 'darkred1', 'darkred2', 'darkred3', 'darkred4', 'darksalmon', 'darksalmon1', 'darksalmon2', 'darksalmon3', 'darksalmon4', 'darkseagreen', 'darkseagreen1', 'darkseagreen2', 'darkseagreen3', 'darkseagreen4', 'darkslateblue', 'darkslateblue1', 'darkslateblue2', 'darkslateblue3', 'darkslateblue4', 'darkslategray', 'darkslategray1', 'darkslategray2', 'darkslategray3', 'darkslategray4', 'darkturquoise', 'darkturquoise1', 'darkturquoise2', 'darkturquoise3', 'darkturquoise4', 'darkviolet', 'darkviolet1', 'darkviolet2', 'darkviolet3', 'darkviolet4', 'deeppink', 'deeppink1', 'deeppink2', 'deeppink3', 'deeppink4', 'deepskyblue', 'deepskyblue1', 'deepskyblue2', 'deepskyblue3', 'deepskyblue4', 'dimgray', 'dimgray1', 'dimgray2', 'dimgray3', 'dimgray4', 'dodgerblue', 'dodgerblue1', 'dodgerblue2', 'dodgerblue3', 'dodgerblue4', 'firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floralwhite', 'forestgreen', 'forestgreen1', 'forestgreen2', 'forestgreen3', 'forestgreen4', 'fuchsia', 'fuchsia1', 'fuchsia2', 'fuchsia3', 'fuchsia4', 'gainsboro', 'ghostwhite', 'gold', 'gold1', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2',
]

selected_color_bg = StringVar(SettingBar)
selected_color_bg.set(colors[3])  

color_dropdown_bg = OptionMenu(SettingBar, selected_color_bg, *colors, command=lambda x: change_color_bg(selected_color_bg.get()))
color_dropdown_bg.place(x=220,y=60)

color_label_bg = Label(SettingBar, text="  ", font=("Arial", 7), width=10, height=2)
color_label_bg.place(x=220,y=100)

change_color_bg(selected_color_bg.get())

opacity_scale = Scale(SettingBar, from_=50, to=100, orient=HORIZONTAL, label="Window Opacity",font=("Purisa 15 bold"),command=change_opacity, length=350,bg="black",fg="white", width=20)
opacity_scale.place(x=22,y=160)
opacity_scale.set(100)


photo = PhotoImage(file="path_to_logo.png")         #replace the path to location of logo.png
logo_image =Label(SettingBar, relief="solid",bd=1,image=photo)
logo_image.place(x=150,y=325)

logo_Label=Label(SettingBar, relief="flat",bd=1, bg="black",font=("Segoe Script", "20", "bold"),fg="white",text="Py_OS")
logo_Label.place(x=155,y=435)

#navigation buttons
def show_nav():    
        global back,app,noti
        win.config(bg="yellow")
        button_width = 11
        button_height = 2
        button_gap = 5

        back = Button(win, bg="Gold", fg="black", text="<",relief="solid", font=("Bold", 15), width=10, bd=1)#,command=close_apps())
        back.place(x=275, y=560)

        app = Button(win, bg="Gold", fg="black", text="O", font=("Bold", 15),relief="solid", width=11, bd=1, command=check_app_button_pressed)
        app.place(x=140, y=560)

        noti = Button(win, bg="Gold", fg="black", text="↓", font=("Bold", 15),relief="solid", width=11, bd=1,command=switch_setting)
        noti.place(x=5, y=560)


def del_nav():
    global back,app,noti
    back.destroy()
    app.destroy()
    noti.destroy()
    
'''Start Button Animation Function'''
def start_up():
    win.config(bg="black")
    win.after(1000,start_bt.destroy())
    win.after(1000, add_op)
    
def add_op():
    win.config(bg="white")
    win.after(1050,l())
    
def l():
    logo = Label(win, text="PY Project OS", font=("Bold", 15))
    logo.place(x=150, y=250)
    logo.after(2000, lambda: logo.destroy())
    win.after(1000, lambda:main_win())
    
def main_win():
    win.after(3000, lambda: win.config(bg="yellow"))
    win.after(3000, lambda: show_nav())

# Start Button
start_bt = Button(win, bg="black", fg='gold', text="", width=1, font=("Bold", 30), command=start_up)
start_bt.place(x=0, y=250)
win.config(bg="#36363d")
