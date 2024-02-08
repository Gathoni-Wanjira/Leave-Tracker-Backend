# importing libraries 
from flask import Flask ,request
from flask_mail import Mail, Message 
from flask_cors import CORS



app = Flask(__name__) 
CORS(app)


# configuration of mail 
# Mail server to link the email between the sender and hr 
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '921198b40eda6e'
app.config['MAIL_PASSWORD'] = 'c19ea17cc955ea'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app) # instantiate the mail class  

# message object mapped to a particular URL ‘/’ 

@app.route("/", methods = ['POST'])
def index():
    data = request.get_json() 
    full_name = data["fullName"]
    department = data["department"]
    reason =data["reason"]
    start_date = data["startDate"]
    end_date =data["endDate"]
    email_address = data["email"]
    days_Number = data["daysNumber"]


    leave_request_email = f"""
    
    Dear HR,

    Good day, I hope this message finds you well.
    
    I would like to request leave from the {department} department for {days_Number} days.
    
    - Reason for Leave: {reason}
    - Start Date: {start_date}
    - End Date: {end_date}


    Kind regards,

    {full_name}
    {email_address}
    """

    print(leave_request_email)

# recipients = hr's image
# Sender = internal email address
    msg = Message(f'Subject: Leave Request - {full_name}', sender =   'peter@mailtrap.io', recipients = ['paul@mailtrap.io'])
    msg.body = leave_request_email
    mail.send(msg)
    return "Message sent!"

if __name__ == '__main__': 
    app.run(debug = True) 
