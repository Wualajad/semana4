#No se como agregar los valores al excel sin que se borre los anteriores aiura xd
#Sera con json noma
from json import load, decoder, dump
from time import sleep
from uuid import uuid4
import pandas as pd #Fail pandas :( 


dat1 = {'Alumnos en el registro': []}
dat2 = {'Docentes en el registro' :[]}
alumni={}
profe={}
cali=[]
ocupacion=0
class  Persona :
    def  __init__(self,nombre,edad,dni,notas):
        self.nombre= nombre
        self.edad= edad
        self.notas=notas
        self.dni=dni
        #self.ocupacion=ocupacion

    def inicio(self):
        while True:
            print('''
                Bienvenido al Registro de personas : 
                ¿Que deseas hacer?
                1) Ingresar una nueva persona
                2) Ver registro de alumno
                3) ver registro de profesores
                4) Salir del registro\n
            ''')
            op = input("-> ")
            if op == "1":
                self.configurar_persona()
            elif op == "2": 
                print(dat1['Alumnos en el registro'])
            elif op == '3':
                print(dat2['Docentes en el registro'])
            elif op == "4":
                print("\nGracias por usar la aplicacion")
                sleep(1)
                quit()
            else:
                print("\nIntroduciste una opcion incorrecta")
    
    def configurar_persona(self):
        print('''\n¿Que persona deseas crear?\n
            1) Alumno
            2) Docente''')
        ocupacion = input("-> ")
        if ocupacion == "1":
            self.modulo_alumno('Ingrese el nombre del alumno:',4)
        elif ocupacion == "2":
            self.modulo_docente('Ingrese el nombre del docente:','Ingrese la edad :', 'DNI :')
        else:
            print("\nHas introducido una ocupación erronea")
    
    def modulo_alumno(self,texto,cantidad):
        print(texto)
        nombre=input('->')
        n=1
        while cantidad >=n:
            try:
                nota=int(input("Ingrese la nota : "))
            except:
                print("Ingrese un valor numerico valido para notas")
            if nota<= 20 and nota >=0:
                cali.append(nota)
                n=n+1
            else:
                print("Ingrese un valor valido para notas")
        promedio=sum(cali)/len(cali)
        maxi=max(cali)
        mini=min(cali)
        alumni={'nombre': nombre,'promedio': promedio ,'mayor nota':maxi,'menor nota': mini,'nota 1':cali[0],'nota 2':cali[1],
        'nota 3':cali[2],'nota 4':cali[3]}
        self.guardar(alumni,'1')


        pass
    def modulo_docente(self,txt1,txt2,txt3):
        print(txt1)
        nombre=input('\n->')
        print(txt2)
        edad=input('\n->')
        print(txt3)
        dni=input('\n->')
        profe={'Nombre ': nombre ,'Edad ':edad, 'DNI ':dni }
        self.guardar(profe,'2')

    def cargar_data(self,ocupacion):
        if ocupacion=='1':
            try:
                archivo=open('alumnos.json','r')
                dat1['Alumnos en el registro'] =load(archivo)
                archivo.close()
            except FileNotFoundError:
                print("\n Creando registro de Alumnos...")
                sleep(1)
                archivo = open("alumnos.json", "w")
                archivo.close()
            except decoder.JSONDecodeError:
                print("\nNo hay alumnos en le registro, se puede crear desde ahora")
        elif ocupacion=='2':
            try:
                archivo=open('docentes.json','r')
                dat2['Docentes en el registro'] =load(archivo)
                archivo.close()
            except FileNotFoundError:
                print("\n Creando registro de Docentes...")
                sleep(1)
                archivo = open("docentes.json", "w")
                archivo.close()
            except decoder.JSONDecodeError:
                print("\nNo hay docentes en le registro, se puede crear desde ahora")           

    def guardar(self,diccionario,ocupacion):
        if ocupacion=='1':
            dat1['Alumnos en el registro'].append(diccionario)
            nose1=dat1['Alumnos en el registro']
            archivo=open('alumnos.json','w')
            dump(nose1,archivo,indent=4)
            archivo.close()
            alumni={}
            profe={}
            cali=[]
            ocupacion=0
        elif ocupacion=='2':
            dat2['Docentes en el registro'].append(diccionario)
            nose1=dat2['Docentes en el registro']
            archivo=open('docentes.json','w')
            dump(nose1,archivo,indent=4)
            archivo.close()
            alumni={}
            profe={}
            cali=[]
            ocupacion=0




class Start(Persona):
    def __init__(self):
        try:
            self.cargar_data('1')
            self.cargar_data('2')
            self.inicio()
        except KeyboardInterrupt:
            print('\nAplicacion interrumpida')

Start()