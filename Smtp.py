import smtplib
from email.mime.text import MIMEText

#SMTP Bilgileri
#64.233.184.108 google.smtp
#213.180.193.38 yandex.smtp
#40.101.53.242  outlook.smtp

platform = input("Platform ?(Other, Gmail, Yandex, Outlook)").lower()
if(platform == "gmail"):
    smtp_adres = "64.233.184.108"
    smtp_port = 587
elif(platform == "yandex"):
    smtp_adres = "213.180.193.38"
    smtp_port = 587
elif(platform == "outlook"):
    smtp_adres = "40.101.53.242"
    smtp_port = 587
elif(platform == "other"):
    smtp_adres = input("Enter SMTP adress")
    smtp_port = input("Enter Port No")
else:
    print("Wrong Key")

username = input("Mail adress ? ")
pwd = input("Password ? ")

#Mail Bilgileri

gonderilecek_adresler = input("To : ")
konu = input("Subject : ")
icerik = """ <h1> Deneme </h1> """
try:
    #Mail İçeriğinin html ve utf8 e gore çevrilmesi
    mail = MIMEText(icerik, "html", "utf-8")

    #Maili gönderen kişi 
    mail["From"] = username
    mail["Subject"] = konu
    mail["To"] = gonderilecek_adresler

    #Mail bilgilerinin derlenmesi
    mail = mail.as_string()
    print("Please Wait...")
    
    #s = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
    s = smtplib.SMTP(smtp_adres, smtp_port)
    #Şifreli bağlantıyı açıyoruz
    s.starttls()
    #Giriş yaptırıyoruz
    s.login(username, pwd)

    #Gönder
    s.sendmail(username, gonderilecek_adresler, mail)
    print("Success")
except Exception  as e:
    print(str(e))
