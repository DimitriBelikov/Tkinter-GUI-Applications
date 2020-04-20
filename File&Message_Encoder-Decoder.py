import tkinter as tk
import time
from tkinter.filedialog import askopenfilename as aof
from cryptography.fernet import Fernet

# ==========================ENCRYPT_DECRYPT=======================================
class encr_decr:
    
    @staticmethod
    def encrypt_data(data,value,path=None):
        encr_msg = ""
        key_gen = Fernet.generate_key()
        cryp_obj = Fernet(key_gen)
        encr_msg = cryp_obj.encrypt(data.encode())
            
        if(value == 1):
            key_ent.insert(0,key_gen.decode())
            res_ent.insert('1.0',encr_msg.decode())
        else:
            file_key_ent.insert(0,key_gen.decode())
            new_file = path[0:path.rindex('/')+1]+'encrypt_'+path[path.rindex('/')+1:]
            with open(new_file,'w') as encr_fl:
                print(encr_msg.decode(), file=encr_fl)
         
            new_path.set(new_file)
    
    @staticmethod
    def decrypt_data(key, encr_data, value, path=None):
        decr_msg = ""
        key_gen = key.encode()
        cryp_obj = Fernet(key_gen)
        decr_msg = cryp_obj.decrypt(encr_data.encode())
        
        if(value == 1):
            res_ent.insert('1.0',decr_msg.decode())
        else:
            new_file = path[0:path.rindex('/')+1]+'decrypt_'+path[path.rindex('/')+1:]
            with open(new_file,'w') as decr_fl:
                print(decr_msg.decode(), file=decr_fl)
         
            new_path.set(new_file)
    
    @staticmethod
    def clear_msg_box(value):
        if(value == 1):
            msg_ent.delete('1.0', tk.END)
            key_ent.delete(0, tk.END)
            res_ent.delete('1.0', tk.END)
        else:
            path_file.delete(0, tk.END)
            data_ent.delete('1.0', tk.END)
            file_key_ent.delete(0, tk.END)
            new_path_ent.delete(0, tk.END)
#==============================================================================================    
#================================Main Window and Widgets=======================================
main_wind = tk.Tk()
main_wind.geometry('690x640')
main_wind.title('Word Encoder Decoder')
main_wind.configure(bg='#14ffcc')
main_wind.columnconfigure(0, weight=1)
main_wind.rowconfigure(1, weight=1)
main_wind.rowconfigure(2, weight=1)
main_wind.rowconfigure(3, weight=1)
main_wind.rowconfigure(4, weight=3)
# ---------------------------------FRAME 1------------------------------------
fram_1 = tk.Frame(main_wind,width=640, height=320, bg='#14ffcc')
fram_1.grid(row=0,column=0)

#----------------------------------HEADING------------------------------------ 
hd_lab = tk.Label(fram_1, text='Welcome !!! Now Encrypt and Decrypt Messages on your Own', 
                  font=('GEORGIA',16), fg='blue', bg='#14ffcc')
hd_lab.grid(row=0, column=0, sticky='nsew')

# ---------------------------------MESSAGE ENCRYPT----------------------------
wd_encr_lab = tk.Label(main_wind, text='Encrypt a Message', font=('Georgia',15), bg='green')
wd_encr_lab.grid(row=1,column=0, sticky='nsew')
wd_encr_lab['pady'] = 10

# ---------------------------------FRAME 2------------------------------------
fram_2 = tk.Frame(main_wind, width=320,bg='#14ffcc')
fram_2.grid(row=2, column=0, sticky = 's')
fram_2['pady'] = 10
fram_2.columnconfigure(0, weight=1)
fram_2.columnconfigure(1, weight=3)
fram_2.rowconfigure(0, weight=1)
fram_2.rowconfigure(1, weight=1)
fram_2.rowconfigure(2, weight=1)
fram_2.rowconfigure(3, weight=2, minsize=40)

# ---------------------------------FRAME 3------------------------------------
# =============================================================================
# fram_3 = tk.Frame(main_wind, width=320, height=120, relief='groove',bg='#14ffcc')
# fram_3.grid(row=3, column=0, sticky='nsew')
# fram_3['pady'] = 10
# fram_3.columnconfigure(1, weight=3)
# fram_3.rowconfigure(0, weight=1)
# fram_3.rowconfigure(1, weight=4)
# 
# =============================================================================

# ---------------------------------FILE ENCRYPT LABEL-------------------------
wd_encr_lab = tk.Label(main_wind, text='Encrypt a File', font=('Georgia',15), bg='green')
wd_encr_lab.grid(row=3,column=0, sticky='nsew')
wd_encr_lab['pady'] = 10

# ---------------------------------FILE FRAME---------------------------------
file_fram = tk.Frame(main_wind, relief='raised', width=12,bg='#14ffcc')
file_fram.grid(row=4,column=0, sticky='nsew')
file_fram['pady'] = 15
file_fram.columnconfigure(0, weight=1)
file_fram.columnconfigure(1, weight=3)
file_fram.columnconfigure(2, weight=2)
file_fram.rowconfigure(0, weight=0)
file_fram.rowconfigure(1, weight=2)
file_fram.rowconfigure(2, weight=2)
file_fram.rowconfigure(3, weight=1)
file_fram.rowconfigure(4, weight=2)

#=====================================TIME WIDGET================================================
dat_tm = time.localtime()
act_time = time.strftime('%a, %d %b %Y %H:%M:%S',dat_tm)
tm_lab = tk.Label(fram_1, text=act_time, font=('CENTURY'), anchor='center', fg='red',bg='#14ffcc')
tm_lab.grid(row=1, column=0)

def updat_tm():
    nw_time = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())
    if nw_time != act_time:
        tm_lab.config(text=nw_time)
        
    tm_lab.after(100, func=updat_tm)
#=================================================================================================

usr_key = tk.StringVar()

msg_lab = tk.Label(fram_2, text='Message', font=('GEORGIA',10), bg='#14ffcc')
msg_ent = tk.Text(fram_2, width=50, height=2, borderwidth=2, relief='sunken', font=('Georgia',10))
msg_lab.grid(row=0,column=0, sticky='nw')
msg_ent.grid(row=0,column=1, sticky='nw')
msg_lab['padx'] = 7

key_lab = tk.Label(fram_2, text='Key(For Decrypt)', font=('GEORGIA',10), bg='#14ffcc')
key_ent = tk.Entry(fram_2, textvar=key_lab, borderwidth=2, relief='sunken', font=('Georgia',10), 
                   width=40)
key_lab.grid(row=1,column=0, sticky='nw')
key_ent.grid(row=1,column=1, sticky='w')
key_lab['pady'] = 10
key_lab['padx'] = 7

res_lab = tk.Label(fram_2, text='Result', font=('GEORGIA',10), bg='#14ffcc')
res_ent = tk.Text(fram_2, width=50, height=2, relief='sunken', font=('Georgia',10), borderwidth=2)
res_lab.grid(row=2, column=0, sticky='w')
res_ent.grid(row=2, column=1, sticky='nsew')

encrypt_but = tk.Button(fram_2, text='Encrypt', font=('GEORGIA',10), 
                        command = lambda : encr_decr.encrypt_data(msg_ent.get('1.0',tk.END),1))
decrypt_but = tk.Button(fram_2, text='Decrypt', font=('GEORGIA',10), 
                        command = lambda : encr_decr.decrypt_data(key_ent.get(),
                                                                  msg_ent.get('1.0',tk.END),1))
clear_but = tk.Button(fram_2, text='Clear', font=('GEORGIA',10), 
                      command = lambda : encr_decr.clear_msg_box(1))
encrypt_but.grid(row=3,column=0, sticky='s')
decrypt_but.grid(row=3, column=1, sticky='s')
clear_but.grid(row=3, column=2, sticky='s')
encrypt_but['padx'] = 10

# ===========================FILE WIDGETS==========================================================
def path_file_disp(): # function to display filepath and File Data
    filename = aof()
    path_var.set(filename)
    try:
        with open(filename, 'r') as ec_file:
            str_data = ec_file.read()
            data_ent.delete('1.0', tk.END)
            data_ent.insert('1.0',str_data) # insert function to enter data to Text Widget 
    except:
            data_ent.delete('1.0', tk.END)
            data_ent.insert("1.0",'File not Found or File not Selected')

file_sel_lab = tk.Label(file_fram, text='Select File', font=('Georgia',11), bg='#14ffcc')
file_sel_lab.grid(row=0,column=0,sticky='n')
file_sel_lab['padx'] = 10

path_var = tk.StringVar()
path_file = tk.Entry(file_fram, width=50, textvariable=path_var, relief='sunken', borderwidth=2, 
                     font=('Georgia',11))
path_file.grid(row=0,column=1, sticky='new')

butt_file = tk.Button(file_fram, text='Browse', command=path_file_disp)
butt_file.grid(row=0, column=2, sticky='nsew')

data_file_lab = tk.Label(file_fram, text='Data', font=('Georgia',10), bg='#14ffcc')
data_file_lab.grid(row=1, column=0, sticky='nsew')
data_ent = tk.Text(file_fram, width=50, height=5, borderwidth=2, relief='sunken', font=('Georgia',
                                                                                        10))
data_ent.grid(row=1,column=1, sticky='nsew')


data_scbar = tk.Scrollbar(file_fram, orient='vertical', command=data_ent.yview)
data_scbar.grid(row=1, column=2, sticky='nsw')
data_ent['yscrollcommand'] = data_scbar.set

file_key = tk.Label(file_fram, text='KEY(For Decrypt)', bg='#14ffcc', font=('Georgia',10))
file_key_ent = tk.Entry(file_fram, width=50, borderwidth=2, relief='sunken', font=('Georgia',10))
file_key.grid(row=2, column=0)
file_key_ent.grid(row=2, column=1,sticky='w')
                    
new_path = tk.StringVar()
new_path_lab = tk.Label(file_fram, text='New Path', bg='#14ffcc', font=('Georgia',10))
new_path_ent = tk.Entry(file_fram, width=50, textvariable=new_path, relief='sunken', 
                        borderwidth=2, font=('Georgia',10))
new_path_lab.grid(row=3, column=0)
new_path_ent.grid(row=3, column=1, sticky='nsew')

encrypt_file_but = tk.Button(file_fram, text='Encrypt File', font=('GEORGIA',10), 
                             command = lambda : encr_decr.encrypt_data(data_ent.get('1.0',tk.END),2,
                                                                  path_file.get()))
decrypt_file_but = tk.Button(file_fram, text='Decrypt File', font=('GEORGIA',10),
                             command = lambda : encr_decr.decrypt_data(file_key_ent.get(),
                                                                  data_ent.get('1.0',tk.END),2,
                                                                       path_file.get()))
clear_file_but = tk.Button(file_fram, text='Clear File', font=('GEORGIA',10),
                           command = lambda : encr_decr.clear_msg_box(2))
encrypt_file_but.grid(row=4,column=0, sticky='s')
decrypt_file_but.grid(row=4, column=1, sticky='s')
clear_file_but.grid(row=4, column=2, sticky='s')
encrypt_file_but['padx'] = 10


main_wind.minsize(690,640)
main_wind.maxsize(690,640)
updat_tm()
main_wind.mainloop()
