import csv

def salvar(path,dados):
    data = []
    f = open(path,'r')
    leitor = csv.reader(f)
    for row in leitor:
        #print(row)
        data.append(row)
    f.close()
    data.append((dados))
    #print(data)
    
    #print(data)
    file = open(path,'w')
    writer = csv.writer(file)
    for newdata in data:
        writer.writerow(newdata)
    file.close()

    
def saveDataRAM(link,giga,nome,lat):
    print('SALVANDO DADOS...')
    path = "./data/ram.csv"
    dados = []
    dados.append(nome)
    dados.append(giga)
    dados.append(lat)
    dados.append(link)
    salvar(path,dados)
    print('SALVO')

def saveDataCPU(data1):
    print('SALVANDO DADOS...')
    path = "./data/cpus.csv"
    dados = []
    for key, value in data1.iteritems():
        temp = value
        dados.append(temp)
    salvar(path,dados)
    print('SALVO')
    
#saveData()