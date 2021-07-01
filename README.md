# Notficações Windows via RabbitMQ e API REST

Aplicação para comunicação via notificação do Windows simples.
Utilizando RabbitMQ e API REST.


## desktop

A aplicação desktop consome a fila no servidor RabbitMQ em que o usúario especifica através do login no console.

## server

A aplicação server possui um método POST para receber mensagem identificando o destinatário e produzindo a mensagem no servidor RabbitMQ para fila do usuário de destino.

