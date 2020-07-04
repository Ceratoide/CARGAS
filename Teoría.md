# TEORÍA
Es de aclarar que toda la simulación trabaja con vectores dos-dimensionales para la posición, velocidad y magnitudes que se obtengan a partir de estas como la Fuerza y el Campo eléctricos.

El programa funciona bajo la ley de interacción de cargas de Coulomb; existen dos grandes grupos en la arquitectura de la simulación, las cargas estacionarias <img src="https://latex.codecogs.com/svg.latex?\Large&space;Q_c" title="\Large Coulomb" /> que producen campo eléctrico, y las cargas de prueba <img src="https://latex.codecogs.com/svg.latex?\Large&space;q_p" title="\Large Coulomb" /> que lo perciben y se mueven siguiendo la segunda ley de Newton:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\sum\vec{F}=m\vec{a}" title="\Large Newton" />

Para la simulación se considero el valor de la masa igual para todas las particulas a 1, por lo que el unico factor determinante para la fuerza fue la aceleración, además, se ultilizó la expresión de la ley de Coulomb:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\vec{F}_e=k\frac{Q_cq_p}{r^2}\hat{r}" title="\Large Coulomb" />

Para determinar el valor de fuerza en cada punto; el proceso que se realiza es que la carga de prueba itera el valor producido por el campo de una lista de cargas estacionarias y las multiplica por su carga, esto ya que la expresión para el campo electrico de una carga puntual viene dado por:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\vec{E}=k\frac{Q_c}{r^2}\hat{r}=\vec{F}_eq_p" title="\Large Campo" />

De esta forma se va calculando para cada iteración en el bucle principal de Pygame, el valor de la fuerza, extrapolando esto bajo el principio de superposición al haber toda una lista de cargas de campo, estas tendrán su contribución al movimiento de las cargas de prueba, para algunas pantallas, por ejemplo la del campo contante, se ve como es posible modelar distribuciones continuas de carga. 
El campo y el Potencial, el cual se rige por la expresión:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\Phi=k\frac{Q_c}{r}" title="\Large Potencial" />

Son calculados para cada punto en la pantalla como ya se dijo bajo el principio de superposición, y se muestran en los paneles correspondientes.

Las adiciones de velocidad se hacen a partir de la suma de tuplas que van sumando el valor de la fuerza en cada punto (Al la masa ser 1 la aceleración, es decir el cambio de la velocidad es equivalente a la fuerza) y esta se le va sumando a la tupla de posición de la particula de prueba, este proceso va realizando el calculo y actualizando la pantalla conforme transcurren las iteraciones; el tiempo esta ajustado de modo que el programa corra a maximo 10 fps, las escalas de posición estan puestas para que 1m=80pix, esta escala se muestra en la esquina inferior derecha de la pantalla, para que el usuario sea capaz de tener un completo conocimiento del fenómeno que esta tratando de modelar.
