import os, sys
import time

class Imessage(object):
    class handleErr(Exception):
        pass

    def __init__(self, Number, message):
       self.Number = Number
       self.message = message

    def create_isms(self):
        text = open('isms.txt', 'w')
        text.writelines('recipients="%s" \nmessage="%s"' % (self.Number, self.message))
        text.close()

    def execute(self):
       time.sleep(1)
       os.system("./read_text.sh")
     

def send(n, m):
    os.system('chmod +x read_text.sh')
    msg = Imessage(n, m)
    msg.create_isms()
    msg.execute()
    return 0
  

if __name__ == "__main__": 
    send("12019522808", "Nasil islerini hallede bildin mi  ??")
