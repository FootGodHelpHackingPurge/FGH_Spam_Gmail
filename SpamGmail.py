import smtplib
import os


RED= '\033[101m'
GREEN= '\033[102m'
YELLOW= '\033[103m'
BLUE= '\033[104m'
PURPLE= '\033[105m'
AQUA= '\033[106m'
WHITE= '\033[107m'
red= '\033[91m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
normal= '\033[0m'

os.system("clear")


print("     ___ ")
print("    __H__")
print("     ["+'\033[102m'+" "+'\033[0m'+"]")
print ('\033[91m'+"Desarollador: Alejo_FGH"+'\033[0m')
print("     ["+'\033[102m'+" "+'\033[0m'+"]")
print("     ["+'\033[102m'+" "+'\033[0m'+"]")
print("     ["+'\033[102m'+" "+'\033[0m'+"]")
print("      V ")


gmail = input ("--Tu Correo: ")
contraceña = input ("--Contraceña: ")
para = input ("--Para: ")
asunto = input ("---Asunto: ")
mensaje = input ("---Mensaje: ")
print("Para Parar CTRL+C ")

message = mensaje
subject = asunto

message = 'Subject: {}\n\n{}'.format(subject, message)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail, contraceña)
while True:
    server.sendmail(gmail, para, message)

server.quit()

print ("SE ENVIO CORRECTAMENTE")