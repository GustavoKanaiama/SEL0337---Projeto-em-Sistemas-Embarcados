# SEL0337---Projeto-em-Sistemas-Embarcados

Praticas da disciplina SEL0337

Gustavo Mariano Kanaiama Pereira - 12547739<br/>
Giovane Rodrigo Cavalcanti Moretto - 12624252

## Pratica 6 - : Interfaces de visão computacional, versionamento de arquivos e controle via Tags

### Controle Via Tags
Nesta parte da prática foi implementado um sistema de "Write" e "Read" das Tags utilizando o módulo da rasp RFID-RC522 e o protocolo de comunicação I2C abstraído pela biblioteca do python mfre522 utilizada no código. Desse modo foi implementado o código de "WriteTag" com a finalidade de escrver um texto na Tag, para que depois possa ser reconhecido e cadastrado no sistema. Já no outro arquivo, o "ReadTag" passa por uma verificação do texto inserido (que foi escrito no "WriteTag") e uma verificação do id da Tag. Assim que ambas verificações são vedadeiras, é acionado um LED verde indicando que foi reconhecida a Tag. Por outro lado, caso uma delas não seja reconhecida, o LED vermelho é acionado simbolizando um acesso negado.

### Reconhecimento Facial por Câmera
Nesta parte da prática foi implementado um sistema de reconhecimento facial utilizando o módulo da rasp __. Para isso, no código, foi utilizado a biblioteca "picamera2" que contém os pacotes para a aquisição da imagem do módulo da câmera, a biblioteca "open-cv" que utiliza métodos de machine learning para abstrair as informações das imagens e gerar o reconhecimento da face (outros pacotes foram usados tabém apenas para dar suporte para esses dois). Assim, a lógica para a construção do código foi a seguinte: primeiro foi configurado a cãmera e uma pasta "detected_faces" para a aquisição das imagens, além disso foi selecionado um arquivo xml que servirá de banco de dados para o método de machine learnig empregado. Para o resto do código 



### Versionamento
O Git juntamente do GitHub são uma das ferramentas mais importantes para o versionamento dos códigos, além de possibilitar o compartilhamento do código entre os desenvolvedores. Desse modo, foi criado um respositório para disciplina e assim pastas relacionadas à cada Prática desta. Pela simplicidade do código, foi utilizada apenas uma branch(main) que recebeu todas as atualizações do código.