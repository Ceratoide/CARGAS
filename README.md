# Simulador
Se trata de un proyecto universitario el cual tiene como objetivo realizar simulaciones de eventos f�sicos, tales como el movimiento 
de cuerpo masivos alrededor de una estrella, movimiento de particulas atraves de un campo, entre otros. Este ultimo, el movimiento de 
particulas, se esta llevando acabo y por el momento es el unico que tiene algun desarrollo.

Se esta trabajando en la interfaz de modo que aparezca un men� de manera que el jugador pueda interactuar directamente con la simulaci�n
sea el quien decida caracteristicas de la carga tales como: su signo, su posici�n, si va a ser una carga estacionario o de prueba, entre 
otros aspectos que son fundamentales dentro de lo que se tiene planeado para la simulaci�n.

## Funcionamiento
Cabe aclarar que el funcionamiento del programa se encuentra en constantes cambios, esto debido a que se trabaja de manera continua,
a�adiendo cosas que lo complementen.

Lo primero que se ver� al iniciar el simulador ser� la pantalla de inicio, donde encontraremos una imagen que hace alusi�n a James Clerk
Maxwell, f�sico que dedujo las leyes del electromagnetismo, en esta se encontrar� el boton de comenzar, el cual conducir� al simulador.
Una vez dentro nos encontraremos con la interfaz ( a�n en desarrollo ), esta nos permitir� dotar de varias caracteristicas a las cargas
con las cuales se trabajar�. En el primer recuadro se encuentran las dos opciones de cargas: estacionarias y de prueba, despu�s se encuentra
dos espacios que indican el valor del campo el�ctrico y el potencial respectivamente, por ultimo, hay 3 casillas donde es posible intrudicr
la magnitud y los componentes de la velocidad de la carga.

Al a�adir cargas se pinta inmediatamente el fondo con el potencial, siendo el color amarillo un potencial positivo y el color morado un 
potencial negativo.

### Controles y botones
  * Tecla q: da pausa al juego.
  * Bot�n izquierdo del mouse: Introduce cargas al campo. Su magnitud y su velocidad se pueden modificar introduciendo valores en los 
  espacios debajo donde se encuentra el nombre de esa caracteristica. 
  
  La velocidad presenta dos casillas debido a que el primero da la componente del vector velocidad en el eje x y el segundo al eje y. si
  no se introduce ningun valor a la magnitud aparecer� un neutron, el cual no interactua con el campo al no tener carga.


### Cargas

  * Cargas estacionarias: Estas no se moveran y generaran un campo que afectar� el moviento de las cargas de prueba.
  * Cargas de prueba: Estas cargas ser�n introducidas por el empleador del programa y su movimiento se ve definido por el campo que 
   generan las cargas estacionarias.

Tanto las cargas estacionarias como las cargas de prueba pueden ser positivas o negativas, de manera que las cargas de mismo signo
se repelen y las de signo contrario se atraen. 


## Trabajo en proceso
 Se sabe como introducir el potencial como fondo, sin embargo, establecerlo vuelve muy lento el programa por lo que se estan mirando 
 maneras de optimizar este problema. Con esto solucionado a�adir como opci�n la visualizaci�n del campo electrico ser� muy similar.

## Autores
- Jean Pierre Cifuentes
- Juan Diego Zuniga 
