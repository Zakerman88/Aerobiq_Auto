from pages.applications import Applications
from pages.event_program import Program
from pages.judges import Judges
import time

WebAddress = 'https://juds-client-admin-stage.aldera-soft.ru:8084/events/b83b62b1-5b66-4850-b286-856b12d02512'
IndWomanTrainer1 = 'Павлова' # middle
IndWomanTrainer2 = 'Зверева' # small
IndWomanTrainer3 = 'Хасикян' # middle
IndWomanTrainer4 = 'Гусева' # high
IndWomanTrainer5 = 'Хандов' # small middle high
IndManTrainer1 = 'Хандов'
IndManTrainer2 = 'Гусева'
IndManTrainer3 = 'Павлова'
IndManTrainer4 = 'Зверева'
TrioTrainer1 = 'Харужева'
TrioTrainer2 = 'Хандов'
GPTrainer1 = 'Хандов'
GPTrainer2 = 'Зверева'
TGTrainer1 = 'Хандов'
TGTrainer2 = 'Пашкова'
# woman - Павлова, Зверева, Хасикян, Гусева, Хандов; man - Хандов, Гусева, Павлова, Зверева; trio - Харужева, Хандов; gruppa - ,,; GP - Хандов, Зверева; TG - Хандов, Пашкова;
small = 1
middle = 2
high = 3
# в зависимости от выбранных на соревнования возрастных групп (при 10-12, 15-17, 18+ - 1=10-12, 2=15-17, 3=18+)
IndWoman = 1
IndMan = 2
Trio = 3
Gruppa = 4
TG = 5
GP = 6
SmeshPara = 7
# номинации 1=ИЖ, 2=ИМ, 3=трио, 4=группа-5, 5=ТГ, 6=ГП, 7=смеш.пара

def test_start_program(driver):
    prog = Program(driver)
    prog.authorization()
    prog.open(WebAddress)
    #prog.open_edit_event_program()
    prog.dnd_example()