import requests
from bs4 import BeautifulSoup


def response_data():
    try:
        response = requests.get('https://finance.rambler.ru/currencies/')
        if response.status_code != 200:
            return 
    except:
        return
    result_dict = {}
    soup = BeautifulSoup(response.text, 'lxml')
    result = soup.find_all('div', class_='finance__currency-block')
    for i in result:
        if 'USD' in i.text:
            result_dict['USD'] = i.find('div', class_='currency-block__marketplace-value').text.split()[0]
        elif 'EUR' in i.text:
            result_dict['EUR'] = i.find('div', class_='currency-block__marketplace-value').text.split()[0]
    return result_dict
