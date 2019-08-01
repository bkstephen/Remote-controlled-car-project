import urllib.request, json 
import car

def direction():
    with urllib.request.urlopen("http://192.168.1.100:3000/") as url:
        data = json.loads(url.read().decode())
        return data['d']
        #print(data['d'])

check = 0
while(True):
    d = direction()    
    if d == 'Forward':
        car.forward()        
        print ('F')
    elif d == 'Backward':
        car.backward()
        print ('B')
    elif d == 'Right':
        car.right()
        print ('R')
    elif d == 'Left':
        car.left()
        print ('L')
    elif d == 'Stop':
        car.clean()        


input()