# SEL0337---Projeto-em-Sistemas-Embarcados

Praticas da disciplina SEL0337

Gustavo Mariano Kanaiama Pereira - 12547739<br/>
Giovane Rodrigo Cavalcanti Moretto - 12624252

## Pratica 4 - Modulação PWM

Para a Prática 4 foram montados 2 circuitos diferentes, o primeiro referente à modulação PWM utilizando um LED e um osciloscópio para avaliar a variação do Duty Cycle. O Segundo referente à implementação do Sensor Ultrassônico para medir distância.

### Circuito de Modulação PWM com LED

A montagem do circuito de controle da luminosidade do LED via PWM foi realizada de acordo com as instruções do site [gpiozero(pwm)](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html) dessa forma o objetivo foi alterar o duty cycle constantemente(de 0 a 100%) para vizualizar a mudança de luminosidade do LED na protoboard.

![montagem_pwm_LED](Pratica_4\images\Montagem_pwm.jpeg?raw=true "montagem_pwm_LED")

    Na primeira prática, utilizamos em série um LED e um resistor de 110Ω, conectados no GND e no pino 3 da Raspberry Pi.

O código primeiro define o pino 3 como saída GPIO do circuito(asim consegue enviar informação). Depois é definido o PWM no pino 3 começando de 0 e indo até 100 de Duty Cycle, para isso é utilziado um laço for que intercalado com um sleep de 0.01s modifica o Duty Cycle(incrementa) até os 100%.

#### Imagens do Osciloscópio

Com o PWM alterado para Duty Cycle = 0
![PWM_0](Pratica_4\images\PWM_0.jpeg?raw=true "PWM_0")

Com o PWM no momento em que o Duty Cycle está entre 0 e 100%
![PWM_1](Pratica_4\images\PWM_1.jpeg?raw=true "PWM_1")

### Circuito com Sensor Ultrassonico

A montagem do circuito ultrassonico foi feita de acordo com as instruções do site da [gpiozero(distance sensor)](https://gpiozero.readthedocs.io/en/stable/recipes.html?highlight=distance%20sensor#distance-sensor) dessa forma o objetivo é de construir um sensor de distância que, em uma determinada frequência, avalia a distância e printa ela no terminal.

![montagem_ultrassonico](Pratica_4\images\Montagem_ultrasonico.jpeg?raw=true "montagem_ultrassonico")

    Para a segunda prática, utilizamos um sensor ultrassônico, para realizar a medida de distâncias que vão até 1m, utilizando o sensor, um resistor de 220Ω e um resistor de 470Ω, utilizando o pino 23 no Echo e o pino 24 no Trigger

O código começa definindo os pinos de Echo e Trigger nos pinos 23 e 24 reespecitvamente com a função `DistanceSensor()`, esta função cria um objeto(sensor) que possue a propriedade "distance" que é utilizada para verificar a distância. Portanto, utilizamos `sensor.distance` para acessar a distância e printar na tela do terminal.
