import pandas as pd
from flask import Flask, request
import plotly.express as px
import multiprocessing as mp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep

data = pd.read_csv('transactions_1.CSV')


def check_anomalies(data):
    # Define rules to check for anomalies
    failed_threshold = 0.1
    reversed_threshold = 0.05
    denied_threshold = 0.2

    # Calculate the number of failed, reversed and denied transactions
    failed_count = data['status'].value_counts().get('failed', 0)
    reversed_count = data['status'].value_counts().get('reversed', 0)
    denied_count = data['status'].value_counts().get('denied', 0)

    # Check if any of the rules are violated
    if failed_count > len(data) * failed_threshold:
        return True
    if reversed_count > len(data) * reversed_threshold:
        return True
    if denied_count > len(data) * denied_threshold:
        return True

    # No anomalies found
    return False


def send_notification(sender_email: object, sender_password: object, recipient_email: object, subject: object,
                      message: object) -> object:
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Set up the message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send the message
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()


pass

sender_email = f'josejunior3979@gmail.com'
sender_password = f'nvxzpwzxxuasgxfj'
recipient_email = f'josejunior3979@gmail.com'
subject = f'Transaction Alert'
message = f'There have been abnormal transactions. Please check the dashboard.'

app = Flask(__name__)


@app.route('/check_anomalies', methods=['POST'])
def check_anomalies_endpoint():
    # Get the transaction data from the request
    data = pd.read_csv(request.data)

    # Check for anomalies
    if check_anomalies(data):
        # Send a notification to the team

        send_notification(sender_email, sender_password, recipient_email, subject, message)

    # Return a response indicating whether anomalies were found or not
    return {'anomalies_found': check_anomalies(data)}


def plot_transaction_data(data):
    fig = px.scatter(data, x='time', y='f0_', color='status')
    fig.show()


if __name__ == '__main__':
    # Create a separate process for the dashboard
    dashboard_process = mp.Process(target=plot_transaction_data, args=(data,))
    dashboard_process.start()

    while True:
        # Check for anomalies every minute
        if check_anomalies(data):
            send_notification(sender_email, sender_password, recipient_email, subject, message)

        # Update the data every minute
        data = pd.read_csv('transactions_1.CSV')

        sleep(60)
