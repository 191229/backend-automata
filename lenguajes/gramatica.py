from nltk import CFG
from nltk.parse.generate import generate
from nltk.corpus import words
import random

conjuntos = []

class conjuntosal():
    
    def conjunto():
        conjunto = random.randint(1,4)
        if conjunto == 1:
            vran1=random.randint(1,36)
            correctos = CFG.fromstring("""
                        A -> KE VC  KS 
                        KE -> '{' 
                        VC -> V C
                        KS -> '}'
                        V -> ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0' | ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' g' | ' h' | ' i' | ' j' | ' k' | ' l' | ' m' | ' n' | ' o' | ' p' | ' q' | ' r'| ' s' | ' t' | ' u' | ' v' | ' w' | ' x' | ' y' | ' z' 
                        C -> ''
                    """)
                
            for s in generate(correctos,n=999):
                        valor = ''.join(s)
                        conjuntos.append(valor)
            resultado = conjuntos[vran1]
            resultado = resultado.replace(" ","")
            
            return resultado
            
            
        elif conjunto == 2:
            vran1=random.randint(1,999)
            correctos = CFG.fromstring("""
                        A -> KE VC V KS 
                        KE -> '{' 
                        VC -> V C
                        KS -> '}'
                        V -> ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0' | ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' g' | ' h' | ' i' | ' j' | ' k' | ' l' | ' m' | ' n' | ' o' | ' p' | ' q' | ' r'| ' s' | ' t' | ' u' | ' v' | ' w' | ' x' | ' y' | ' z' 
                        C -> ','
                    """)
            for s in generate(correctos,n=999):
                        valor = ''.join(s)
                        conjuntos.append(valor)

            resultado = conjuntos[vran1]
            resultado = resultado.replace(" ","")
            return resultado
            
            
        elif conjunto == 3:
            vran1=random.randint(1,999)
            correctos = CFG.fromstring("""
                        A -> KE VC VC V KS 
                        KE -> '{' 
                        VC -> V C
                        KS -> '}'
                        V -> ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0' | ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' g' | ' h' | ' i' | ' j' | ' k' | ' l' | ' m' | ' n' | ' o' | ' p' | ' q' | ' r'| ' s' | ' t' | ' u' | ' v' | ' w' | ' x' | ' y' | ' z' 
                        C -> ','
                    """)
            for s in generate(correctos,n=9999):
                        valor = ''.join(s)
                        conjuntos.append(valor)

            resultado = conjuntos[vran1]
            resultado = resultado.replace(" ","")
            return resultado
            
        elif conjunto == 4:
            vran1=random.randint(1,9999)
            correctos = CFG.fromstring("""
                        A -> KE VC VC VC V KS 
                        KE -> '{' 
                        VC -> V C
                        KS -> '}'
                        V -> ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0' | ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' g' | ' h' | ' i' | ' j' | ' k' | ' l' | ' m' | ' n' | ' o' | ' p' | ' q' | ' r'| ' s' | ' t' | ' u' | ' v' | ' w' | ' x' | ' y' | ' z' 
                        C -> ','
                    """)
            
            for s in generate(correctos,n=99999):
                        valor = ''.join(s)
                        conjuntos.append(valor)

            resultado = conjuntos[vran1]
            resultado = resultado.replace(" ","")
            return resultado
            
            
            
    

                        

            
  










