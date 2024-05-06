MINIBINGO
========================================================================================================================================================================================
MiniBingo es un juego que he programado en Python basado en el tradicional Bingo con el objetivo de aprender las bases de Python.

📋 Normas de MiniBingo
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- Los cartones se conforman de 5 casillas de acho y 6 de alto.
- Se pueden hacer una linea vertical y una horizontal por partida.
- Gana el jugador que haga Bingo antes (el que complete antes el cartón)

🎮 ¿Cómo jugar?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Datos a tener en cuenta antes de jugar:
  - Es un juego de terminal de comandos.
  - Recomiendo jugar en ventana máximizada.
  - Recomiendo indicarle una vez por lo menos que no te gusta el cartón que te ha generado.

1- Seleccionar cuantos jugadores van a jugar (max. 5)

2- Nombrar al jugador pertinente.

3- Elegir cartón.

4- Dejar que el programa juegue solo.

⚙️ Datos sobre el funcionamiento
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
La ejecución del programa se divide en dos fases:

1- Fase de preparación
  - Se define el número de jugadores.
  - Se inicia un bucle por jugador en el que se pregunta el nombre de cada uno y se le genera un cartón.
  - Se guarda el número y nombre de los jugadores en un archivo para que durante la próxima preparación no se tenga que volver a poner el número y nombre de jugadores.
  - Finaliza la fase de preparación.
   
2- Fase de partida
  - Una vez ha terminada la preparación del juego inicia la partida y esta acaba cuando algúno de los jugadores hace Bingo.
  - En cada ronda de forma aleatoria se "canta" un número que no se volverá a repetir durante el resto de la partida.
  - Se pinta en pantalla una interfaz dínamica en la que se pintan todos los cartones, el número "cantado", cual de los jugadores va ganado y el progreso de la partida.
  - Al finalizar cada ronda se comprueba que cartones contienen el número "cantado", se tacha y se se comprueba si hay algúna linea o Bingo. Además tambien se calcula el progreso de la partida y quien va ganando.
  - La partida finaliza una vez se canta el primer Bingo.
