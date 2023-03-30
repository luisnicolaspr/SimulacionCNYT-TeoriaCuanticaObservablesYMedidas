# SimulacionCNYT-TeoriaCuanticaObservablesYMedidas
Se realizan los retos de programacion del la sección 4 del libro  Quantum Computing for Computer Scientists y el simulador del sistema cuantico de la seccion 4.1 con cada una de sus funciones requeridas.

#### 👨🏻 NOMBRE: Luis Nicolás Pinilla Rodríguez CNYT 2023-1




### ✅ Simulacion del sistema cuántico

Para simular el sistema cuántico descrito en la sección 4.1, se debe crear una matriz que represente al sistema con el número de posiciones especificado por el usuario y un vector ket que asigne las amplitudes de cada posición. Para calcular la probabilidad de encontrar la partícula en una posición en particular, se debe elevar al cuadrado la amplitud correspondiente y sumar todas las amplitudes al cuadrado para obtener la probabilidad total.

Para la amplitud de transición, se deben recibir dos vectores ket y calcular el producto interno entre ellos, elevando el resultado al cuadrado para obtener la probabilidad de transición.

### ✅ Retos de programación capitulo 4

En los retos de programación del capítulo 4, se deben realizar diferentes operaciones en matrices y vectores ket. En el primer reto se debe calcular la amplitud de transición, tal como se explicó anteriormente. En el segundo reto, se debe comprobar que una matriz observable sea hermitiana, y si lo es, calcular la media y la varianza del observable en un estado dado. Para ello, se debe primero calcular la matriz conjugada transpuesta de la matriz observable y luego multiplicarla por el producto entre el vector ket y su conjugada transpuesta, para obtener la media. La varianza se calcula utilizando la fórmula varianza = <A^2> - <A>^2, donde <A^2> es el promedio de la matriz observable al cuadrado, y <A> es el promedio de la matriz observable.

En el tercer reto, se deben calcular los valores propios de una matriz observable y la probabilidad de transitar a alguno de los vectores propios después de la observación. Para ello, se deben calcular los valores propios y vectores propios de la matriz observable utilizando la función np.linalg.eig(). Luego, se debe calcular la probabilidad de transitar a cada vector propio después de la observación utilizando la fórmula probabilidad = |<v propio|psi>|^2.

Finalmente, en el cuarto reto se debe considerar la dinámica del sistema. Se deben recibir una serie de matrices Un y un estado inicial, y calcular el estado final del sistema después de aplicar todas las matrices Un. Para ello, se deben multiplicar todas las matrices Un en orden, empezando desde la izquierda, y luego multiplicar el resultado por el vector ket inicial.

### ✅ Ejercicios adicionales agregados como ejemplo

En los problemas 4.3.1, 4.3.2, 4.4.1 y 4.4.2 se debe aplicar todo lo aprendido anteriormente en ejercicios específicos. En el problema 4.3.1 se deben calcular la probabilidad de encontrar una partícula en una posición específica después de aplicar una operación determinada. En el problema 4.3.2 se deben calcular las probabilidades de transición entre estados de un sistema de dos partículas. En el problema 4.4.1 se debe calcular la probabilidad de que un sistema se encuentre en un estado después de aplicar una serie de matrices de evolución temporal. Y en el problema 4.4.2 se deben calcular las probabilidades de transitar a los vectores propios de una matriz observable específica.





