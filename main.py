import os # https://docs.python.org/3/library/os.html
import subprocess as sub # https://docs.python.org/3/library/subprocess.html


if __name__=="__main__":
    # Nombre del dispositivo
    awus_str = "RTL8812AU"
    awus_id = None
        
    sub.run(["clear"])    
    
    lsusb_aux = sub.run(["lsusb"], capture_output=True, text=True, universal_newlines=True) # text=True 
    
    lsusb = lsusb_aux.stdout.splitlines()
    del lsusb_aux
    
    
    for l in lsusb:
        if l.find(awus_str) >= 0: # busca la línea de la tarjeta wifi
            list_line = l.split(" ")
            for i, t in enumerate(list_line): # busca el trozo del literal "ID" y el siguiente es el que contiene el id
                if list_line[i].lower() == "id":
                    awus_id = list_line[i+1] # guardamos el ID en memoria
                    
    print(awus_id)
    
    sub.run(["sudo","usbreset", awus_id])