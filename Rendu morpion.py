import network #import des fonctions liés au wifi
from machine import Pin #importe la lib pour gérer les pins
import urequests # import des fonctions liés aux requêtes http
import utime # import des fonctions liés au temps
import ujson #import des fonctions liés à la conversion en json



#leds
import machine
import time

red_led1 = machine.Pin(0, machine.Pin.OUT)
blue_led1 = machine.Pin(1, machine.Pin.OUT)

red_led4 = machine.Pin(2, machine.Pin.OUT)
blue_led4 = machine.Pin(3, machine.Pin.OUT)

red_led7 = machine.Pin(4, machine.Pin.OUT)
blue_led7 = machine.Pin(5, machine.Pin.OUT)

red_led2 = machine.Pin(6, machine.Pin.OUT)
blue_led2 = machine.Pin(7, machine.Pin.OUT)

red_led5 = machine.Pin(8, machine.Pin.OUT)
blue_led5 = machine.Pin(9, machine.Pin.OUT)

red_led8 = machine.Pin(10, machine.Pin.OUT)
blue_led8 = machine.Pin(11, machine.Pin.OUT)

red_led3 = machine.Pin(12, machine.Pin.OUT)
blue_led3 = machine.Pin(13, machine.Pin.OUT)

red_led6 = machine.Pin(14, machine.Pin.OUT)
blue_led6 = machine.Pin(15, machine.Pin.OUT)

red_led9 = machine.Pin(16, machine.Pin.OUT)
blue_led9 = machine.Pin(17, machine.Pin.OUT)


led_dict = {
0: (red_led1, blue_led1),
1: (red_led2, blue_led2),
2: (red_led3, blue_led3),
3: (red_led4, blue_led4),
4: (red_led5, blue_led5),
5: (red_led6, blue_led6),
6: (red_led7, blue_led7),
7: (red_led8, blue_led8),
8: (red_led9, blue_led9),
}




wlan = network.WLAN(network.STA_IF) #met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'HUAWEI P30 lite'
password = '12345678'
wlan.connect(ssid, password) #connecte la raspi au réseau
#url = "http://date.jsontest.com/"
url = "http://192.168.43.19:3000/"
#box chesnay : 192.168.1.72
#huawei : 192.168.43.19
print(wlan.isconnected())

while not wlan.isconnected():
    print("no co")
    utime.sleep(0.3)
    pass

i=0
while(True):
   # red_led1.toggle()
  #  red_led4.toggle()
    try:
        #print("GET")
        r = urequests.get(url) #lance une requete sur l'url
       # if r.headers.get("Content-Type") == "application/json": # Vérifiez si la réponse est au format JSON
        json_response = r.json() # Décompressez la réponse en JSON
            #print(json_response["date"]) # traitez sa réponse en Json
        tableau = json_response["data"]
        print(tableau)
        #print(json_response["joueur"])
        joueur = json_response["joueur"]
        if joueur == "X":
            joueur ="O"
        else:
            joueur = "X"
        print(joueur)
        
        jeu = json_response["jeu"]
        print(jeu)
        
        
  
        for j in range(len(tableau)):
            if tableau[j] == "X":
                led_dict[j][1].value(1)
               # led_dict[j][0].value(1)                
            elif tableau[j] == "O":
                led_dict[j][0].value(1)
                #led_dict[j][1].value(1)                
            elif tableau[j] == "":
                led_dict[j][0].value(0)
            
        if(jeu == False):
            
            
            while i<=50:
                                
                if joueur == "X":
                    for t in range(len(tableau)):
                        #led_dict[t][0].value(0)
                        led_dict[t][1].value(1)
                        led_dict[t][1].toggle()
                        utime.sleep(0.2)
                        i=i+1

                elif joueur == "O":
                    for t in range(len(tableau)):
                       # led_dict[t][1].value(0)
                        led_dict[t][0].value(1) 
                        led_dict[t][0].toggle()
                        utime.sleep(0.2)
                        i=i+1
            
            for j in range(len(tableau)):
           
                    
                
                    
                
                if tableau[j] == "X" or tableau[j] == "O":
                    led_dict[j][0].value(0)
                    
                    led_dict[j][1].value(0)
                elif tableau[j] == "O":
                    led_dict[j][0].value(0)

                    
            
        r.close()
        
        utime.sleep(1)

    except Exception as e:
        print(e)
        
    #utime.sleep(1)
