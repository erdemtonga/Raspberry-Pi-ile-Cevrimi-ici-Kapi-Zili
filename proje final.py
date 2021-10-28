import RPi.GPIO as GPIO
from time import sleep
import smtplib
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(26,False)


while True:
    GPIO.output(26,False)
    
               
    
  
    try:

        while  GPIO.input(18) == True:
            continue
            
       
        if GPIO.input(18) == False:
            print("butona basildi")                      
                                                           # Hesap bilgilerimiz
            kullanici="gonderen mail"
            kullanici_sifresi = 'sifre'
            alici = 'alici mail'              # alıcının mail adresi
            konu = 'KAPI CALDI'
            msj = 'KAPIDA BIRI VAR'
                                                         # bilgileri bir metinde derledik
            email_text = """
            From: {}
            To: {}
            Subject: {}
            {}
            """ .format(kullanici,alici, konu, msj)
            
            server = smtplib.SMTP('smtp.gmail.com:587')   #servere bağlanmak için gerekli host ve portu belirttik
            server.starttls() #serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
            server.login(kullanici, kullanici_sifresi)   # Gmail SMTP server'ına giriş yaptık
            server.sendmail(kullanici, alici, email_text) # Mail'imizi gönderdik 
            server.close()     # SMTP serverimizi kapattık
            print ('email gönderildi')
            GPIO.output(26,True)
            sleep(2)
           
           
            
    
    except:
        print("bir hata oluştu")
        sleep(0.1)
