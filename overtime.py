#!/usr/bin/python3
import smtplib,sys,os
from datetime import datetime
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-p","--password", dest="password")
parser.add_option('-l',"--login", dest="login", default=None)
parser.add_option("--to", dest="to", default='chefe@empresa.com,gerente@empresa.com')
parser.add_option("--smtp", dest="smtp", default="mail.vivapixel.com.br")
parser.add_option("--port", dest="port", default="25")
parser.add_option("-t","--time", dest="time", default=18)
parser.add_option("-s","--subject", dest="subject",default="Hora extra")

(options,args) = parser.parse_args()

if options.login is None:
    options.login = args[0]

options.to = options.to.split(',')

if (datetime.now().hour == options.time and datetime.now().minute > 0) or datetime.now().hour > options.time:
    print('Enviando e-mail...')
    now = datetime.now().time().strftime("%H:%M")
    body = 'Saindo as %s' % now

    body = "" + body + ""
    headers = ["From: " + args[0],
               "subject: " + options.subject,
               "To: " + options.to[0]]

    if len(options.to) > 1:
        headers += ["CC: " + options.to[1]]

    headers += ["MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    session = smtplib.SMTP()
    session.connect(options.smtp, options.port)
    session.login(options.login, options.password)
    session.sendmail(args[0], options.to, headers + "\r\n\r\n" + body)
    session.quit()

    print('E-mail enviado!')

print('Desligando...')

plataform = sys.platform
if 'linux' in plataform:
    os.system('sudo shutdown -h now "Até amanhã"')
elif 'windows':
    os.system('shutdown -s -t 3 -c "Até amanhã"')

print('Bye...')
exit(0)