from subprocess import call

comando = ['ls','-l']
call(comando)

from subprocess import Popen
proceso = Popen(['ls','-l'])
proceso.wait()