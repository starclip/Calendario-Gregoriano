## **********************************************************************
## Tarea Actividad # 4
##
## Programa: Calendario
## Autores :
##         Jason Barrantes Arce  # carnét: 2015048456
##         Randy Morales Gamboa  # carnét: 2015085446
## Fecha : 27 de Febrero del 2018
##
## Programa que realiza una serie de consultas basándose en el calendario
## gregoriano.
##
## ***********************************************************************

class Calendario:
    # Clase calendario que almacena fechas consultadas y permite consultar datos"
    def __init__(self):
        self.fechas = []

    def formatoCorrectoAño(self, año):
        if (año < 1582):
            print("Las fechas anteriores a 1582 no serán consideradas");
            return False;
        return True;

    def formatoCorrectoMes(self, mes):
        if (mes > 12):
            print("Los meses no deben ser mayores a 12");
            return False;
        return True;

    def formatoCorrectoDia(self, dia, diaFinal):
        if (dia > diaFinal):
            print("No hay tantos días ese mes");
            return False;
        return True;

    # Retorna si un mes es bisiesto o no. 
    def esBisiesto(self, año):
        if (not self.formatoCorrectoAño(año)):
            return -1;
        if (año % 400 == 0):
            return True;
        else:
            if (año % 4 == 0 and año % 100 != 0):
                return True;
        return False;

    # Retorna la cantidad de días que tiene un mes específico.
    def diasDelMes(self, mes, año):
        maxDay = 0;
        if (mes == 2):
            if (self.esBisiesto(año)):
                return 29;
            else:
                return 28;
        elif (mes < 8):
            if (mes % 2 == 1):
                return 31;
            else:
                return 30;
        else:
            if (mes % 2 == 0):
                return 31;
            else:
                return 30;


    # Comprueba si una fecha es valida (la fecha es una tupla (yyyy,mm,dd))
    def esFechaValida(self, fecha):
        
        tempAño = fecha[0];
        tempMes = fecha[1];
        tempDia = fecha[2];
        diaFinal = 0;
        # Verifique si el mes y el año son correctos
        if (not self.formatoCorrectoAño(tempAño) or not self.formatoCorrectoMes(tempMes)):
            return False;
        diaFinal = self.diasDelMes(tempMes, tempAño); # Obtengo los días de ese mes.
        # Verifica si el dia es válido.
        if (not self.formatoCorrectoDia(tempDia, diaFinal)):
            return False;
        self.fechas.append(fecha);
        return True;

    # Retorna la tupla del día siguiente.
    def incrementarDia(self, diaFinal, dia, mes, año):
        if (dia == diaFinal):
            mes += 1;
            dia = 1;
        else:
            dia += 1;
        if (mes > 12):
            año += 1;
            mes = 1;

        return (año, mes, dia);


    # Obtiene el día siguiente.
    def diaSiguiente(self, fecha):
        año = fecha[0];
        mes = fecha[1];
        dia = fecha[2];
        diaFinal = 0;
        nuevaFecha = (0,0,0);

        if (not self.esFechaValida(fecha)):
            return (-1, -1, -1);
        diaFinal = self.diasDelMes(mes, año); # Obtengo los días de ese mes.
        nuevaFecha = self.incrementarDia(diaFinal, dia, mes, año); # Aumente un día.
        return nuevaFecha;


    # Contar el número de días que hay desde el primer día de Enero de ese año.
    def contarDiasPasados(self, fecha):
        dias = 0;
        fechaInicial = (0,0,0);
        
        if (not self.esFechaValida(fecha)):
            return -1;
        fechaInicial = (fecha[0], 1, 1);
        while(fecha != fechaInicial):
            dias += 1;
            fechaInicial = self.diaSiguiente(fechaInicial); # Obtiene el día siguiente.
        return dias;


    # Obtener el día de la semana dependiendo del año.
    def diaPrimeroEnero(self, año):
        añoInicio = 1582;
        dia = 2;
        if (not self.formatoCorrectoAño(año)):
            return -1;
        while(añoInicio < año):
            if (self.esBisiesto(añoInicio) or (añoInicio % 100 == 0)):
                dia += 2;
            else:
                dia += 1;
            dia = dia % 7;
            añoInicio += 1;
        return dia;
    

######################################################################################################
# Código de la progra

calendar = Calendario()

# Función que solicita el año, mes, día y los returna en una tupla. O retorna un False.
def solicitaDatos():
    año = mes = dia = 0;
    print("******************************** ");
    try:
        año = int(input("Por favor digite el año: "));
        mes = int(input("Por favor digite el mes: "));
        dia = int(input("Por favor digite el día: "));
        if (año <= 0 or mes <= 0 or dia <= 0):
            print("No se aceptan valores negativos o equivalentes a 0");
            return False;
    except ValueError:
        print("Escribió mal un dato. Vuelva a intentarlo");
        return False;
    print("\n");
    return (año, mes, dia);

def solicitaUnDato():
    año = 0;
    print("******************************** ");
    try:
        año = int(input("Por favor digite el año: "));
        if (año <= 0):
            print("No se aceptan valores negativos o equivalentes a 0");
            return False;
    except ValueError:
        print("Escribió mal el año. Vuelva a intentarlo");
        return False;
    print("\n");
    return año;

def consultarBisiestos():
    bisiesto = False;
    año = solicitaUnDato(); # Solicita al usuario que escriba el año.
    if (año == False):
        return False;
    # Obtenga el  estado para comprobar si es un año bisiesto.
    bisiesto = calendar.esBisiesto(año);
    if (bisiesto == True):
        print("El año es bisiesto \n");
    elif (bisiesto == False):
        print("El año no es bisiesto \n");
    return True;

def consultarFecha():
    fechaValida = (0, 0, 0);
    año = mes = dia = 0;
    valida = False;
    fechaValida = solicitaDatos() # Solicita al usuario que escriba los datos.
    if (fechaValida == False):
        return False;
    # Obtenga el  estado para comprobar si es una fecha valida.
    valida = calendar.esFechaValida(fechaValida);
    if (valida):
        print("Es una fecha válida.")
        return True;
    return False;

def siguiente():
    fechaValida = (0, 0, 0);
    nuevaFecha = (0, 0, 0);
    año = mes = dia = 0;
    valida = False;
    fechaValida = solicitaDatos() # Solicita al usuario que escriba los datos.
    if (fechaValida == False):
        return False;
    # Obtenga una nueva fecha.
    nuevaFecha = calendar.diaSiguiente(fechaValida);
    if (nuevaFecha == (-1, -1, -1)):
        return False;
    print("El siguiente día es: " + str(nuevaFecha));
    return True;

def contarDias():
    fechaValida = (0, 0, 0);
    año = mes = dia = diasTotales = 0;
    valida = False;
    fechaValida = solicitaDatos() # Solicita al usuario que escriba los datos.
    if (fechaValida == False):
        return False;
    # Obtenga los días que han pasado.
    diasTotales = calendar.contarDiasPasados(fechaValida);
    if (diasTotales >= 0):
        print("El número de días que han pasado son: " + str(diasTotales));
        return True;
    return False;

def diaSemana():
    dia = 0;
    text = "El primero de la semana del ";
    año = solicitaUnDato(); # Solicita al usuario que escriba el año.
    if (año == False):
        return False;
    text += "(" + str(año) + ")";
    # Obtenga el día de la semana del primero de Enero
    dia = calendar.diaPrimeroEnero(año); 
    if (dia == 0):
        text += " es domingo \n"
    elif (dia == 1):
        text += " es lunes \n"
    elif (dia == 2):
        text += " es martes \n"
    elif (dia == 3):
        text += " es miércoles \n"
    elif (dia == 4):
        text += " es jueves \n"
    elif (dia == 5):
        text += " es viernes \n"
    elif (dia == 6):
        text += " es sábado \n"
    else:
        return False;
    print(text);
    return True;

state = True;
inputX = 0;
print("Bienvenido a la aplicación Calendario Gregoriano \n");

while(state):
    print(" --------------------------------------------------------------- ");
    print("Por favor, elija la opción que desea: \n");
    print("1) Consultar años bisiestos ");
    print("2) Saber si una fecha es válida ");
    print("3) Obtener el día siguiente de una fecha ");
    print("4) Obtener los días que han pasado desde el primero de ese año. ");
    print("5) Obtener el dia específico del primero de enero dado un año. ");
    print("0) Salir del programa. ");
    print(" --------------------------------------------------------------- ");
    try:
        inputX = int(input("Digite el número que desea: "));
        print("\n");
        if (inputX == 1):
            estadoConsulta = consultarBisiestos();
            while(not estadoConsulta):
                estadoConsulta = consultarBisiestos();
        elif (inputX == 2):
            estadoConsulta = consultarFecha();
            while (not estadoConsulta):
                estadoConsulta = consultarFecha();
        elif (inputX == 3):
            estadoConsulta = siguiente();
            while (not estadoConsulta):
                estadoConsulta = siguiente();
        elif (inputX == 4):
            estadoConsulta = contarDias();
            while (not estadoConsulta):
                estadoConsulta = contarDias();
        elif (inputX == 5):
            estadoConsulta = diaSemana();
            while (not estadoConsulta):
                estadoConsulta = diaSemana();
        elif (inputX == 0):
            state = False;
        else:
            print("Por favor lea las instrucciones y digite un número del rango \n");
    except ValueError:
        print("¡Oops! Qué pena pero el digito no es válido. \n")

print("***********************************");        
print("Gracias por haber usado el programa");
print("***********************************"); 
