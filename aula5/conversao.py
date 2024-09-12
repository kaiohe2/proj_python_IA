class conversao:
    
    def velocidade():
        Kmh = [75.4,30.6,120,32.8,20.8]
        Mph = [round(x/1.61,2) for x in Kmh]
        return Mph
    
    def temperatura():
        celsius = [45,30,12.5,32.6,50]
        fahrenheit = [round((x*1.8)+32,2) for x in celsius]
        return fahrenheit
    
    def altura():
        pes = [32,45,65,76,87]
        metros = [round((x*1)*0.3048,2 ) for x in pes]
        return metros
    
    def idade():
        anos = [12,29,45,2,5,18]
        meses = [round (x*12,2) for x in anos]
        x = 0
        while(x<5) :
            print(anos[x],"anos em meses são meses"[x])
            x+= 1
             
        