#!/bin/bash
NOMBRE_USUARIO=$1
EDAD_USUARIO=$2

#Verificamos que no estén vacios
if [ -z "$NOMBRE_USUARIO" ] || [ -z "$EDAD_USUARIO" ] ; then
        echo "ERROR: Debes proporcionar el Nombre y/o la Edad."
        echo "Uso: ./quien-es-rico.sh [Nombre] [Edad]"
else
        #Muestra el valor de la variable en pantalla
        echo "¡Hola, $NOMBRE_USUARIO! tu tienes $EDAD_USUARIO años y eres rico(a)."
fi