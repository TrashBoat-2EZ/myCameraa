import smtplib

email = "goodshepherdiot@gmail.com"  # Sending email
password = "P@ssword#1"  # Sending email password
recipient = "finnsampson@gmail.com"  # email recipient
message = "This is Sir's message"

server = smtplib.SMTP("smtp.gmail.com", 587)  # connect to gmail server
server.starttls()  # use TLS (Transport Layer Security)
server.login(email, password)
server.sendmail(email, recipient, message)
server.quit()
