'''
import win10toast
import six
import appdirs
import packaging.requirements

toaster = win10toast.ToastNotifier()


def notificarUsuario(msg):
    toaster.show_toast('Nova Mensagem', msg.decode("utf-8"), duration=10)
'''
import plyer.platforms.win.notification
from plyer import notification

def notificarUsuario(msg):
    notification.notify('Nova Mensagem', 
                    msg.decode("utf-8"),
                    'HPSMQ-Message',
                    'message_mailing2.ico')
