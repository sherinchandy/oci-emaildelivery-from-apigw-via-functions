# python script for sending SMTP configuration with Oracle Cloud Infrastructure Email Delivery
import io
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

def handler(ctx, data: io.BytesIO = None):
    body = json.loads(data.getvalue())
    SENDER = body.get("senderAddress")
    SENDERNAME = body.get("senderName")
    RECIPIENT = body.get("recipientAddress")
    SUBJECT = body.get("emailSubject")
    # Replace the USERNAME_SMTP value with your Email Delivery SMTP username.
    USERNAME_SMTP = 'ocid1.user.oc1..aaaaaaaacx2udxqxqsek2z3zy7yuf6lmen4voq@ocid1.tenancy.oc1..aaaaaaaac3l6hgylozzuh2b5u2kejplzalhgk4nzka.jj.com'
    # Replace the PASSWORD_SMTP value with your Email Delivery SMTP password.
    PASSWORD_SMTP = '#OO1ymw{Z!h{Vp5}'
    # If you're using Email Delivery in a different region, replace the HOST value with an SMTP endpoint. Use port 25 or 587 to connect to the SMTP endpoint.
    HOST = "smtp.us-ashburn-1.oraclecloud.com"
    PORT = 587

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Email Delivery Test\r\n"
                 "This email was sent through the Email Delivery SMTP "
                 "Interface using the Python smtplib package from OCI Fn."
                 )
    # The HTML body of the email.

    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Email Delivery SMTP Email Test</h1>
      <p>This email was sent with Email Delivery using the
        <a href='https://www.python.org/'>Python</a>
        <a href='https://docs.python.org/3/library/smtplib.html'>
        smtplib</a> library.</p>
         <img src="http://www.tizag.com/pics/htmlT/sunset.gif" alt="alternatetext"> 
    </body>
    </html>"""

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
    msg['To'] = RECIPIENT
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(BODY_TEXT, 'plain')
    part2 = MIMEText(BODY_HTML, 'html')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Try to send the message.
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        # smtplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
    # Display an error message if something goes wrong.
    except Exception as e:
        print("Error: ", e)
    else:
        print("Email successfully sent !")
