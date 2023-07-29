from multiprocessing import context
import sqlite3
import paho.mqtt.client as mqtt
import json
import random
import os
import smtplib
import imghdr
from email.message import EmailMessage

from paho.mqtt import client as mqtt_client


EMAIL_ADDRESS = "ohmni.iaas@gmail.com"
EMAIL_PASSWORD = "bbdxrpwsflmyjwkk"

broker = '192.168.178.36'
port = 1883
topic = "home/mail"
# generate client ID with pub prefix randomly
username = 'ohmni'
password = 'root'




dbase = sqlite3.connect('Our_data.db') # Open a database File
print('Database opened')

dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_email(
     id, name, email) ''')

def insertVaribleIntoTable(id, name, email):
    try:
        dbase = sqlite3.connect('Our_data.db')
        cursor = dbase.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO employee_email
                          (id, name, email) 
                          VALUES (?, ?, ?);"""

        data_tuple = (id, name, email)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        dbase.commit()
        print("Python Variables inserted successfully into employee_email table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if dbase:
            dbase.close()
            print("The SQLite connection is closed")


insertVaribleIntoTable(1, 'SHARATH', 'sharathbhushan18@gmai.com')
insertVaribleIntoTable(2, 'NASIRU ABOKI', 'nasiru.aboki@iaas.uni-stuttgart.de')
insertVaribleIntoTable(3, 'MARCO AIELLO', 'marco.aiello@iaas.uni-stuttgart.de')

def getDeveloperInfo(name):
    try:
        dbase = sqlite3.connect('Our_data.db')
        cursor = dbase.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from employee_email where name = ?"""
        cursor.execute(sql_select_query, (name,))
        records = cursor.fetchone()
        print("Printing email:", records[2])
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if dbase:
            dbase.close()
            print("The SQLite connection is closed")
            return records[2]
name = "Sharath Nataraj"
getDeveloperInfo(name.upper())


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client()
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        email_gen = json.loads(msg.payload)
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        param = email_gen.get('queryResult').get('parameters')
        username = param.get('username').get('name')
        mail_to = param.get('name').get('name')
        date = param.get('date')
        email_id_user = param.get('email')
        email_id_to = getDeveloperInfo(mail_to.upper())
        print("user ", username)
        print("name to ", mail_to)
        print("date ", date)
        print("email_id of user ", email_id_user)
        print("email_ to ", email_id_to)
        context = "Hello " + mail_to + " this is appointment scheduler messege from Ohmni, " + username + " requested to set an appointment with you on " + date + " kindly respond with suitable slot to: " + email_id_user
        send_mail(email_id_to, context)
    client.subscribe(topic)
    client.on_message = on_message

def send_mail(email_id, context):

    msg = EmailMessage()
    msg['Subject'] = 'Ohmni Appointment Request'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email_id

    msg.set_content(context)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

