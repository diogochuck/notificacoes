import pika, sys, os
import notificacao
import configparser
import urllib
import dadosconn

def callback(ch, method, properties, body):
    notificacao.notificarUsuario(body)
        
def start_consume(usuario):
    userrmq = getRabbitMQUrl()
    urlencodestr = "%s://%s:%s@%s/%s" % (userrmq.protocol,
                                         userrmq.username,
                                         userrmq.password,
                                         userrmq.host,
                                         userrmq.vhost)
    print(' [*] URL = %s' % urlencodestr)

    parameters = pika.URLParameters(urlencodestr)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue=usuario)

    
    channel.basic_consume(queue=usuario,
                      auto_ack=True,
                      on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    channel.start_consuming()

def getRabbitMQUrl():
    cfg = configparser.ConfigParser(allow_no_value=True)
    cfg.read('config.ini')
    dadosrmq = dadosconn.DadosConexao(cfg.get('rabbitmq','protocol'),
                                      cfg.get('rabbitmq','username'),
                                      urllib.parse.quote_plus(cfg.get('rabbitmq','password')),
                                      cfg.get('rabbitmq','host'),
                                      cfg.get('rabbitmq','vhost'))
    print(' [*] DADOS = %r %r' % (dadosrmq.protocol,dadosrmq.username))
    if dadosrmq.host == '' :
        print(' [*] Falha ao pegar URL da mensageria')
    return dadosrmq
