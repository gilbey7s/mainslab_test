import random


service_dict = { 
    1: 'консультация',
    2: 'лечение',
    3: 'стационар',
    4: 'диагностика',
    5: 'лаборатория'
}

def detector(str):
    return random.random()

def classifier(str):
    service_class, service_name = random.choice(list(service_dict.items()))
    result = { service_class:service_name,
    }
    return result
