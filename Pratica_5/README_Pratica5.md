# SEL0337---Projeto-em-Sistemas-Embarcados

Praticas da disciplina SEL0337

Gustavo Mariano Kanaiama Pereira - 12547739<br/>
Giovane Rodrigo Cavalcanti Moretto - 12624252

## Pratica 5 - Comunicação I2C entre Arduino e Raspberry Pi

Este projeto exemplifica a troca de dados entre um Arduino e uma Raspberry Pi usando o protocolo de comunicação Serial Peripheral Interface (SPI) e o barramento I2C. O objetivo é ler informações analógicas do Arduino e transmiti-las para a Raspberry Pi para exibição ou processamento.

### Código do Arduino

O código do Arduino configura o dispositivo para funcionar como um escravo no barramento I2C, respondendo a solicitações da Raspberry Pi para enviar dados analógicos lidos de um pino específico (no caso, o A0). O código também aguarda comandos da Raspberry Pi para controlar um LED integrado.

### Código da Raspberry Pi (Python)

O script em Python utiliza a biblioteca smbus para estabelecer comunicação via barramento I2C com o Arduino. Ele solicita continuamente os dados analógicos ao Arduino e os interpreta para uso na Raspberry Pi, como exibição em tela ou processamento adicional.
