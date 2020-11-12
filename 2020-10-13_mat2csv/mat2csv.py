import os
import csv
#import numpy.random.common
#import numpy.random.bounded_integers
#import numpy.random.entropy

import numpy
import scipy.io as sio
import pandas as pd

def find_kernal_item(check_item):
  temp=[]
  for each_item in Result[each_key] :
    temp.append(each_item[0])
  return temp

for dirpath, dirname, files in os.walk('.'):
    for each_file in files:
        file_name = os.path.join(dirpath,each_file)
        if file_name.split('.')[-1] == 'mat':
            mat_file=file_name
            print(mat_file)


#matfn = ".\Ray.mat"
matfn = mat_file #input("Please input the file path :")
data = sio.loadmat(matfn)


data_keys = data.keys()
Result = pd.Series(data,index = data_keys)

with open('output.csv','w',newline="") as csvfile:
    writer = csv.writer(csvfile)
    for each_key in data_keys :
      writer.writerow([each_key])
      if each_key == "__header__" :
        writer.writerow([str(Result[each_key],encoding='utf-8')])
      elif each_key == "__globals__" :
        writer.writerow([Result[each_key]])
      elif each_key == "Units" :
        for each_colum in range(len(Result[each_key][0])) :
          temp=[]
          for each_row in range(len(Result[each_key])) :
            try:
              temp.append(Result[each_key][each_row][each_colum][0])
            except :
              temp.append(" ")
          writer.writerow(temp)
      else : 
        if len(Result[each_key]) == 1:
          writer.writerow(Result[each_key][0])
        elif len(Result[each_key]) > 1:
          writer.writerow(find_kernal_item(Result[each_key]))
