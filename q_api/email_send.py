# https://hyunmin1906.tistory.com/276
import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "보내는 사람 이메일"
receiver_email = "받는 사람 이메일"
password = "앱 비밀번호"
message = "<h1>내용</h1>"

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

