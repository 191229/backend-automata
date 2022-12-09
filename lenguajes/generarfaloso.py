import random
    
class generafalso():
    def generarfalsos():
        val = random.randint(1,4)
        dato = random.randint(1,99)
        dato = str(dato)
        randlowercase = chr(random.randint(ord('a'), ord('z')))
        
        if val == 1:
            particion = "{{"+ randlowercase + ","+ dato + ","+randlowercase + dato+"}"
            return particion
            
        elif val ==2:
            particion = "{{"+ randlowercase +"}}}"
            return particion
            
        elif val == 3:
            particion = randlowercase+"}"+","+dato+"]"+randlowercase
            
            return particion
        elif val == 4:
            particion = "{{"+ randlowercase + ","+ dato +","+ ","+ dato +"}"+"," +"{"+randlowercase+"}"+"}}"
            
            return particion
            

