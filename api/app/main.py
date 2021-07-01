import pika
from flask import Flask,request,abort
from app import dadosconn
import configparser
import urllib

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/mensagem/<username>', methods=['POST'])
def enviarmsg(username):
    key_1 = request.args.get('key')
    if key_1 :
        sendMensagem(username, request.data.decode("utf-8"))
        return "OK - Success"
    abort(401)


def sendMensagem(usuario, msg):
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

    channel.basic_publish(exchange='', routing_key=usuario, body=msg)
    connection.close()

def getRabbitMQUrl():
    cfg = configparser.ConfigParser(allow_no_value=True)
    cfg.read('app/config.ini')
    dadosrmq = dadosconn.DadosConexao(cfg.get('rabbitmq','protocol'),
                                      cfg.get('rabbitmq','username'),
                                      urllib.parse.quote_plus(cfg.get('rabbitmq','password')),
                                      cfg.get('rabbitmq','host'),
                                      cfg.get('rabbitmq','vhost'))
    print(' [*] DADOS = %r %r' % (dadosrmq.protocol,dadosrmq.username))
    if dadosrmq.host == '' :
        print(' [*] Falha ao pegar URL da mensageria')
    return dadosrmq
