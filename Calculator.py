import tkinter as tk
import math

# ======================================================
class Sci_math:
    
    @staticmethod
    def sin(x):
        x = x*math.pi/180
        sum = math.sin(x)
        return sum

    @staticmethod
    def cosin(x):
        x = x*math.pi/180
        sum = math.cos(x)
        return sum

    @staticmethod
    def tang(x):
        x = x*math.pi/180
        sum = math.tan(x)
        return sum

    @staticmethod
    def res_update(txt):
        if txt in list(range(10)) or txt in ['.','(',')']:
            exp = result_ent.get('1.0','2.0')[:-1]
            if exp == str(0):
                result_ent.delete('1.0','2.0')
            result_ent.insert("end",txt)
        elif txt == math.e or txt == math.pi:
            exp = result_ent.get('1.0', 'end')
            if Sci_math.isoper(exp[-1]):
                result_ent.insert("end",txt)
            else:
                result_ent.delete('1.0','end')
                result_ent.insert('1.0',txt)
    @staticmethod
    def pow_call(val):
        exp = result_ent.get('1.0', "end")
        exp = exp[:-1]
        if Sci_math.isoper(exp[-1]):
            exp += ('pow('+','+str(val)+')')
        else:
            exp = 'pow('+exp+','+str(val)+')'
        result_ent.delete('1.0','end')
        result_ent.insert('end',exp)
    
    @staticmethod
    def func_call(wd,val=None):
        exp = result_ent.get('1.0', "2.0")
        exp = exp[:-1]
        if exp=='' or Sci_math.isoper(exp[-1]):
            if val== None:
                exp+= (wd+'(')
            else:
                exp += (wd+ '(' + ',' + str(val) + ')' )
        else:
            if val == None:
                exp = wd+'('+exp+')'
            else:
                exp = wd+ '(' + exp + ',' + str(val) + ')'
        result_ent.delete('1.0','end')
        result_ent.insert('1.0',exp)
            
        
    @staticmethod
    def isoper(wd):
        if wd in ['+','-','/','*','%']:
            return True
        else:
            return False
    
    @staticmethod
    def oper_click(op):
        exp = result_ent.get('1.0', "2.0")[0:-1]
        if exp == '0':
        	exp=op
        else:
        	exp+=op
        result_ent.delete('1.0','end')
        result_ent.insert('end',exp)
        
    @staticmethod    
    def clear(val):
        if val == 1:
            exp = result_ent.get('1.0', "2.0")[0:-2]
            result_ent.delete('1.0','end')
            result_ent.insert('1.0',exp)
            if result_ent.get('1.0', "2.0")[:-1] == '':
                result_ent.insert('end',0)
        else:
            result_ent.delete('1.0','end')
            result_ent.insert('end',0)
            
    @staticmethod
    def eval_exp():
        fun_dic = {'cos':Sci_math.cosin, 'sin':Sci_math.sin, 'tan':Sci_math.tang, 'log':math.log,
                   'pow':math.pow,'fact':math.factorial}
        exp = result_ent.get('1.0', "2.0")
        try:
            result = eval(exp,fun_dic)
        except:
            result = 'ERROR'
        result = '='+str(result)
        result_ent.delete('1.0','end')
        result_ent.insert('end',exp)
        result_ent.insert('2.0',result)
        
# ####### Main Window ###########
main_wind = tk.Tk()
main_wind.geometry('530x410')
main_wind.title('Scientific Calculator-Methatrexate')

main_wind.columnconfigure(0, weight=1)

fram_1 = tk.Frame(main_wind, relief='sunken', bg='black')
fram_1.grid(row=0, column=0)
fram_1['padx'] = 2
fram_1['pady'] = 2

# ########### RESULT BOX ################
result_ent = tk.Text(fram_1, width=52, height=2,relief='solid', font=('GEORGIA',12), bg='#2a9d8f')
result_ent.grid(row=0,column=0) 
result_ent.insert('end',0)  

# ############ fram_2e 1 ##################
fram_2 = tk.Frame(main_wind, relief='raised', width=640, height=318, borderwidth=4, bg='black')
fram_2.grid(row=1, column=0, sticky='nsew')

# ############ Adding Buttons to fram_2e 1 #############
butt_1 = tk.Button(fram_2, text='e', width=10, font=('GEORGIA', 16), bg='#20bf55',
                   command=lambda : Sci_math.res_update(math.e))
butt_1.grid(row=0,column=0)

butt_2 = tk.Button(fram_2, text='pi', width=10, font=('GEORGIA', 16), bg='#20bf55',
                   command=lambda : Sci_math.res_update(math.pi))
butt_2.grid(row=0,column=1)

butt_3 = tk.Button(fram_2, text='C', width=10, font=('GEORGIA', 16), bg='#20bf55',
                   command= lambda : Sci_math.clear(2))
butt_3.grid(row=0,column=2)

butt_4 = tk.Button(fram_2, text='<--', width=10, font=('GEORGIA', 16), bg='#20bf55',
                   command= lambda : Sci_math.clear(1))
butt_4.grid(row=0,column=3)

butt_5 = tk.Button(fram_2, text='x^2', width=10, font=('GEORGIA', 16), bg='#20bf55',
                   command=lambda :Sci_math.func_call('pow',val=2))
butt_5.grid(row=1,column=0)

butt_6 = tk.Button(fram_2, text='x^3', width=10, font=('GEORGIA', 16), bg='#20bf55',
                   command=lambda :Sci_math.func_call('pow',val=3))
butt_6.grid(row=1,column=1)

butt_7 = tk.Button(fram_2, text='x^y', width=10, font=('GEORGIA', 16), bg='#20bf55',
                   command=lambda :Sci_math.func_call('pow',val='y'))
butt_7.grid(row=1,column=2)

butt_8 = tk.Button(fram_2, text='log', width=10, font=('GEORGIA', 16), bg='#20bf55',
                   command=lambda : Sci_math.func_call('log'))
butt_8.grid(row=1,column=3)

butt_9 = tk.Button(fram_2, text='(', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update('('))
butt_9.grid(row=2,column=0)

butt_10 = tk.Button(fram_2, text=')', width=10, font=('GEORGIA', 16), bg='#20bf55',
                   command=lambda : Sci_math.res_update(')'))
butt_10.grid(row=2,column=1)

butt_11 = tk.Button(fram_2, text='cos', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.func_call('cos'))
butt_11.grid(row=2,column=2)

butt_12 = tk.Button(fram_2, text='sin', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.func_call('sin'))
butt_12.grid(row=2,column=3)

butt_13 = tk.Button(fram_2, text='tan', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.func_call('tan'))
butt_13.grid(row=3,column=0)

butt_14 = tk.Button(fram_2, text='n!', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda :Sci_math.func_call('fact'))
butt_14.grid(row=3,column=1)

butt_15 = tk.Button(fram_2, text='%', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.oper_click('%'))
butt_15.grid(row=3,column=2)

butt_16 = tk.Button(fram_2, text='/', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.oper_click('/'))
butt_16.grid(row=3,column=3)

butt_17 = tk.Button(fram_2, text='7', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update(7))
butt_17.grid(row=4,column=0)

butt_18 = tk.Button(fram_2, text='8', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update(8))
butt_18.grid(row=4,column=1)

butt_19 = tk.Button(fram_2, text='9', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update(9))
butt_19.grid(row=4,column=2)

butt_20 = tk.Button(fram_2, text='x', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.oper_click('*'))
butt_20.grid(row=4,column=3)

butt_21 = tk.Button(fram_2, text='4', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update(4))
butt_21.grid(row=5,column=0)

butt_22 = tk.Button(fram_2, text='5', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update(5))
butt_22.grid(row=5,column=1)

butt_23 = tk.Button(fram_2, text='6', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update(6))
butt_23.grid(row=5,column=2)

butt_24 = tk.Button(fram_2, text='-', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.oper_click('-'))
butt_24.grid(row=5,column=3)

butt_25 = tk.Button(fram_2, text='1', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update(1))
butt_25.grid(row=6,column=0)

butt_26 = tk.Button(fram_2, text='2', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update(2))
butt_26.grid(row=6,column=1)

butt_27 = tk.Button(fram_2, text='3', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update(3))
butt_27.grid(row=6,column=2)

butt_28 = tk.Button(fram_2, text='+', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.oper_click('+'))
butt_28.grid(row=6,column=3)

butt_29 = tk.Button(fram_2, text='0', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update(0))
butt_29.grid(row=7,column=0)

butt_30 = tk.Button(fram_2, text='.', width=10, font=('GEORGIA', 16), bg='#20bf55',
                    command=lambda : Sci_math.res_update('.'))
butt_30.grid(row=7,column=1)

butt_31 = tk.Button(fram_2, text='=', width=21, font=('GEORGIA', 16), bg='#01baef',
                    command=lambda : Sci_math.eval_exp())
butt_31.grid(row=7,column=2, columnspan=2)


main_wind.minsize(530,405)
main_wind.maxsize(530,405)
main_wind.mainloop()



# dhjgfhjhj dgahjdh  hdashdjhaskjdhkjashdj hdashdjhaskjdhkjashdjsdghjasgdhjgdh
# asdg hjasdghjasgdhjasdhjash dghjasgdhasg dhjgasd
# dhasgdhjg ashdghjasd