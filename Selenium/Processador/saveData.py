import csv

def saveData(data1):
    print('SALVANDO...')
    path = "./data/cpus.csv"
    data = []
    f = open(path,'r')
    leitor = csv.reader(f)
    for row in leitor:
        #print(row)
        data.append(row)
    dados = []
    f.close()
    for key, value in data1.iteritems():
        temp = value
        dados.append(temp)
    data.append((dados))
    #print(data)
    
    #print(data)
    file = open(path,'w')
    writer = csv.writer(file)
    for newdata in data:
        writer.writerow(newdata)
    file.close()
    
    print('SALVO')
    
#saveData()