from lenguajes.serializers import PostSerializer
import json
from lenguajes.models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#####
import re 
from lenguajes.maquina import TuringMachine
from lenguajes.gramatica import conjuntosal
from lenguajes.automataconjunto import automataconjunto
from lenguajes.automataparticiones import automataparticiones
import json, os
tm = TuringMachine.parse(os.path.join('turing','transicion.tm'))

arregloparticion = []
matriz_uno =[["A"]]

matriz_dos = [["B"], 
              ["C"]]

matriz_tres = [["D"], 
               ["E"], 
               ["F"], 
               ["G"], 
               ["H"]]

matriz_cuatro = [["I"], 
                 ["J"],  
                 ["K"], 
                 ["Z"],
                 ["M"],
                 ["N"],
                 ["O"],
                 ["P"],
                 ["Q"],
                 ["T"],
                 ["U"],        
                 ["V"],
                 ["W"],
                 ["X"],    
                 ["Y"]]
cadena = []


def main():
    senal = "personalisado"
    
    if senal == "personalisado":
        conjunto = "{a,c}"
        ingresado = automataconjunto.automata(conjunto)
        crearparticiones(ingresado)
       
        
        
    elif senal == "aletorio":
        resultado = conjuntosal.conjunto()
        crearparticiones(resultado)
        
        
     
def crearparticiones(entrada): 
    i = 0
    while i < len(entrada):
         #se remplazan valores para limpiar el texto            
         lin = entrada
         lin = lin.replace("{","")
         lin = lin.replace(",","")
         lin = lin.replace("}","")
         #print(lista[i])
         i = i + 1
    for i in range(len(lin)):
         for j in lin:
               for x in j:
                  cadena.append(x)

    if len(lin) == 1:
        dato = limpiarvalores(matriz_uno[0])
        data = tm.accepts(dato)
        data = str(data)
        particiones(data)
       
        
    if len(lin) == 2:
       for i in range(len(matriz_dos)):  
            dato = limpiarvalores(matriz_dos[i])
            data = tm.accepts(dato)
            data = str(data)
            particiones(data)
            
    if len(lin) == 3:
         for i in range(len(matriz_tres)):  
            dato = limpiarvalores(matriz_tres[i])
            data = tm.accepts(dato)
            data = str(data)
            particiones(data)
        
    if len(lin) == 4:
         for i in range(len(matriz_cuatro)):  
            dato = limpiarvalores(matriz_cuatro[i])
            data = tm.accepts(dato)
            data = str(data)
            particiones(data)   
  
        
def limpiarvalores(entrada):
    i=0 
    parseo = str(entrada)
    while i < len(parseo):
            #se remplazan valores para limpiar el texto            
            lin = parseo
            lin = lin.replace("[","")
            lin = lin.replace(",","")
            lin = lin.replace("]","")
            lin = lin.replace("'","")
            lin = lin.replace("'","")
            #print(lista[i])
            i = i + 1
    
    lin = lin.replace(" ","")
    #print(lin)
    
    return lin

def particiones(val):
    i=0 
    parseo = val
    while i < len(parseo):
            #se remplazan valores para limpiar el texto            
            lin = parseo
            lin = lin.replace("[","")
            
            lin = lin.replace("]","")
            lin = lin.replace("'","")
            lin = lin.replace("'","")
            lin = lin.replace("q2:","")
            lin = lin.replace("#","")
            
            #print(lista[i])
            i = i + 1
    cont = ""
    
    
    for j in lin:
        
        if j == "{":
            cont += j
        elif j == "0" or j == "1" or j == "2" or j=="3":
            val = int(j)
            cont  += cadena[val]
        elif j == ",":
            cont += j
        elif j == "}":
            cont += j 
             
    arregloparticion.append(cont)
    


class ReloadPague(APIView):
    main()

class GetParticiones(APIView):
    def get(self, response):
       
        array_json = json.dumps(arregloparticion)
        print(array_json)
        i=0
        while i < len(array_json):           
            lin = array_json
            lin = lin.replace("[","")
            lin = lin.replace('"','')
            lin = lin.replace("]","")
            i = i + 1
        
        return Response(lin, status=status.HTTP_200_OK)
    
class GetConjunto(APIView):
    def get(self, response): 
        
        conjunto1 = arregloparticion[0]
        i=0
        while i < len(conjunto1):           
            lin = conjunto1
            lin = lin.replace("[","")
            lin = lin.replace('"','')
            lin = lin.replace("]","")
            i = i + 1
            
        
        return Response(lin, status=status.HTTP_200_OK)
    
# class PostParticiones(APIView):
#     def post(self, response):
  
class PostParticiones(APIView): 
    
    def post(self, request):
        
        print(request.data)
        serializer = PostSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response("Bien", status=status.HTTP_200_OK)

        return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)