import os
import datetime
import shutil

#directory = '/hd/postgres.bkp/bkpcore/'
directory = 'C:\\bkp\\'

dataExec = str(datetime.datetime.now())
diaExec = str(datetime.date.today())
caminhobkp = os.path.join(directory, 'oldbkp/')
caminholog = os.path.join(directory, 'log/')
#caminhobkp = os.path.join(directory, 'oldbkp\\')
#print (caminhobkp)

texto =''
if not os.path.exists(caminholog):
     os.makedirs(caminholog)
if os.path.exists(caminholog+'lista_de_arquivos_removidos_'+diaExec+'.log'):
    with open(caminholog+'lista_de_arquivos_removidos_'+diaExec+'.log', 'r') as log:
        texto = log.read()

arq = open(caminholog+'lista_de_arquivos_removidos_'+diaExec+'.log', 'w',encoding='utf-8')
arq.write(texto+'\n\n')

if not os.path.exists(caminhobkp):
     os.makedirs(caminhobkp)
#else:
#    print (f'Caminho já existe no diretório {caminhobkp}')
ext = ['bkp']
def getExtension(filename):
    filename,fileExtension = os.path.splitext(filename)
    return fileExtension

def inArray(array,to_look):
    for x in array:
        if(to_look[1:] == x):
            return True
    return False
def isExt(filename):
    extensions = ext
    extencion = getExtension(filename)
    if(inArray(extensions,extencion)):
        return True
    return False

def lookupDirectory(directory):
    arquivos = sorted(os.listdir(os.path.expanduser(directory)))
    arquivosbkp = []


    for a in arquivos:
        if isExt(a):
            print(a)
            arquivosbkp.append(a)

    #print(arquivosbkp)
    fim = len(arquivosbkp) - 5
    if(fim>0):
        print ('Mais de 10 arquivos! Removendo esses!!')
        arq.write('Removendo em -> '.upper() + dataExec + '\n\n')
        for i in range(0,fim):
            print(arquivosbkp[i])
            arq.write("ARQUIVOS NA PASTA '" + str(arquivosbkp[i]).upper() + "': \n")
            shutil.move(os.path.join(directory,arquivosbkp[i]),caminhobkp)
            # os.remove(os.path.join(caminhobkp,arquivosbkp[i]))

lookupDirectory(directory)
arq.close()