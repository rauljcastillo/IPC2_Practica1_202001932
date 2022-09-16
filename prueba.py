import os 

cadena='digraph { '
cadena+='label="Periodo"\n'
cadena+='node [shape=none]\n'
cadena+="n1 [label =\n"
cadena+='<<TABLE cellspacing="3" cellpadding="10" bgcolor="white">\n'



cadena+=" <TR>\n"
cadena+='<TD>Hola</TD>\n'
cadena+='<TD bgcolor="lightgreen">'
cadena+="Hola"
cadena+="<BR/>Que"
cadena+='</TD>'           
cadena+="</TR>\n"
cadena+="</TABLE>>]"
cadena+='}'
        
file=open("./nodo.dot","w+") #Escribo un archivo dot
file.write(cadena) 
file.close()

os.system("dot -Tpng ./nodo.dot -o ./Ordenes.png")