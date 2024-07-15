from functools import reduce
import os

def genArrTemp(filename):
    newArr = []
    with open(filename , 'r') as city1rec:
        temps = city1rec.read()
        temps = temps.split('\n')
    for item in temps:
        if (item !=  ''):
            item = float(item)
            newArr.append(item)
    return newArr        
   

city1Arr = genArrTemp('cities/city3.txt')

def getAVG(filename):
    temps_arr = genArrTemp(filename)
    average_temp = sum(temps_arr)/len(temps_arr)
    return str(average_temp)
 

def checkEndTxt(name):
    if(name.endswith('.txt') == True):
        return name

file_arr = os.listdir('cities')
ress = filter(checkEndTxt , file_arr)
citi_names = list(ress)


with open('summarrry.txt' , 'w') as sumary_temp:
    for x in citi_names:
        cityavg = getAVG(f'cities/{x}')
        sumary_temp.write(cityavg + '\n')





def generteAvg(cityfile):
    with open(cityfile , 'r') as city1:
        city1Temp = city1.read()
        acc =0
        newArr = []
        for x in city1Temp.split('\n'):
            if x != "":
                newArr.append(x)
        for y in newArr:
            acc = acc + float(y)        
        return (acc/len(newArr)) 
       

generteAvg('city1.txt')

newAverages  = [round( generteAvg('city1.txt') ,2)  , round(generteAvg('city2.txt'), 2) , round(generteAvg('city3.txt') , 2)]

# print(newAverages)

with open('summary.txt' , 'a') as summary:
    for index,average in enumerate(newAverages):
        report = summary.write(f'city{index} : {average} \n') 



    