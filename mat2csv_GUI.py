
from csv import writer
from tkinter import Tk, StringVar, Button, Button, Entry
from tkinter.filedialog import askopenfilename
from scipy.io import loadmat
from pandas import Series 

def find_kernal_item(check_item):
  temp=[]
  for each_item in check_item :
    temp.append(each_item[0])
  return temp

def Select_file():

    path = askopenfilename()
    print(path)
    select_file_path.set(path)


def transfer_mat():
    matfn = str(select_file_path.get())
    try:
        data = loadmat(matfn)
    except:
        print('Data load error!')

    data_keys = data.keys()
    Result = Series(data,index = data_keys)

    with open('output.csv','w',newline="") as csvfile:
        write = writer(csvfile)
        for each_key in data_keys :
            write.writerow([each_key])
            if each_key == "__header__" :
             write.writerow([str(Result[each_key],encoding='utf-8')])
            elif each_key == "__globals__" :
                write.writerow([Result[each_key]])
            elif each_key == "Units" :
                for each_colum in range(len(Result[each_key][0])) :
                    temp=[]
                    for each_row in range(len(Result[each_key])) :
                        try:
                            temp.append(Result[each_key][each_row][each_colum][0])
                        except :
                            temp.append(" ")
                    write.writerow(temp)
            else : 
                if len(Result[each_key]) == 1:
                    write.writerow(Result[each_key][0])
                elif len(Result[each_key]) > 1:
                    write.writerow(find_kernal_item(Result[each_key]))


    print("transfer successed!")

#從同資料夾中尋找mat檔
#for dirpath, dirname, files in os.walk('.'):
#    for each_file in files:
#        file_name = os.path.join(dirpath,each_file)
#        if file_name.split('.')[-1] == 'mat':
#            mat_file=file_name
#            print(mat_file)

#建立主視窗跟frame
window = Tk()
window.title("Mat2Csv APP")
window.geometry('400x200')
select_file_path = StringVar()

#設定選取檔案按鈕
button = Button(window,text = "Select File",command = Select_file,width = 10,font=('Arial',14))
button.pack()
button.place(x = 50,y = 50,anchor = 'w')

#設定顯示選取結果
path_enter = Entry(window, textvariable = select_file_path,width = 30, font=('Arial',14))
path_enter.pack()
path_enter.place(x=50,y=100,anchor='w')

#設定轉換檔案按鈕
transfer_buttom = Button(window,text = 'Transfer',command = transfer_mat,font=('Arial',14))
transfer_buttom.pack()
transfer_buttom.place(x=50,y=150,anchor='w')

window.mainloop()

# matfn = str(select_file_path.get())
# data = sio.loadmat(matfn)

# data_keys = data.keys()
# Result = Series(data,index = data_keys)

# with open('output.csv','w',newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     for each_key in data_keys :
#       writer.writerow([each_key])
#       if each_key == "__header__" :
#         writer.writerow([str(Result[each_key],encoding='utf-8')])
#       elif each_key == "__globals__" :
#         writer.writerow([Result[each_key]])
#       elif each_key == "Units" :
#         for each_colum in range(len(Result[each_key][0])) :
#           temp=[]
#           for each_row in range(len(Result[each_key])) :
#             try:
#               temp.append(Result[each_key][each_row][each_colum][0])
#             except :
#               temp.append(" ")
#           writer.writerow(temp)
#       else : 
#         if len(Result[each_key]) == 1:
#             writer.writerow(Result[each_key][0])
#         elif len(Result[each_key]) > 1:
#             writer.writerow(find_kernal_item(Result[each_key]))
