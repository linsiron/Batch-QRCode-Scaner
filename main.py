from pyzbar.pyzbar import decode
from PIL import Image


result=open("./result.txt","w",encoding='utf-8')

filepath=open("./filepaths.txt","r",encoding = 'utf-8')
for line in filepath.readlines():
    line=line.replace('\n','')
    decocdeQR = decode(Image.open(line)) 
    
    print(line + "  ", end="")
    result.write(line+"  ")
    if len(decocdeQR)>0:
        ret=decocdeQR[0].data.decode('ascii')
    else:
        result.write("\n")
        continue
    if len(ret)>0:
        print(ret)
    result.write(ret+"\n")

filepath.close()

