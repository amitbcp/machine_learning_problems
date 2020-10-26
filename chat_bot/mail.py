from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import pandas as pd
from pretty_html_table import build_table


def send_mail(recipient, body):

    message = MIMEMultipart()
    message['Subject'] = 'Top Suggested Restuarants'
    message['From'] = 'search.foodie@gmail.com'
    message['To'] = recipient

    body_content = body
    message.attach(MIMEText(body_content, "html"))
    msg_body = message.as_string()

    server = SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(message['From'], 'foodie123!')
    server.sendmail(message['From'], message['To'], msg_body)
    server.quit()


def get_gdp_data():
    """
    GDP data
    :return:
    """
    gdp_dict = {
      'Restaurant ': ['United States', 'China', 'Japan', 'Germany', 'India'],
      'Address': [
        'Rooftop jah tu allowed nahi', 'English tere Bas ki nahi',
        'Tu yeh Jagah Zanta Nai', 'Jaha Akasar jatein hai', 'Khopche mai'
      ],
      'Avg. Budget (2 ppl)': [
        'Lootega', 'Mehnga Haggo', 'Yeh Thik ha', 'Chindi jaisa', 'Govt Meal'
      ],
      'Rating': [
        'Poshh Logo ka', 'Show off', 'Middle Class Zindabaad', 'Bekar Bhao',
        'Bakwaas'
      ],
    }
    data = pd.DataFrame(gdp_dict)
    return data


def send_country_list():
    gdp_data = get_gdp_data()
    output = build_table(gdp_data, 'blue_light')
    send_mail("ishant30oct@gmail.com ", output)
    return "Mail sent successfully."


# send_country_list()
