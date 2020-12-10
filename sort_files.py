import os 
import shutil 

path = 'path'
  
def sort(path):
    list_ = os.listdir(path) 
       
    for file_ in list_: 
        name, ext = os.path.splitext(file_) 
      
        ext = ext[1:] 
      
        if ext == '':
            if os.path.isdir(path+"/"+file_):
                print(f"sorting {file_}")
                sort(path+"/"+file_+'/')
            
            elif os.path.isfile(path+"/"+file_) and os.path.dirname(path).split("/")[-1] != "no_ext":
                if os.path.exists(path+'/'+'no_ext'):
                    shutil.move(path+'/'+file_, path+'/'+"no_ext"+'/'+file_)
                else:
                    os.makedirs(path+'/'+"no_ext")
                    shutil.move(path+'/'+file_, path+'/'+"no_ext"+'/'+file_)
            
            continue

        if os.path.dirname(path).split("/")[-1] != ext:
            if os.path.exists(path+'/'+ext):
                    shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 
            else: 
                os.makedirs(path+'/'+ext) 
                shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)

    print(f"Finished with {path}")

if __name__ == "__main__":
    sort(path)
    
print("done")
