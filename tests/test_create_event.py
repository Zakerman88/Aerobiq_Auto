from pages.applications import Applications
from pages.event_program import Program
from pages.judges import Judges
from pages.brigades import Brigades
import time

baseURL = 'https://juds-client-admin-stage.aldera-soft.ru'
port = '8084'
category = 'events'
eventID = '856fac8a-7cf2-4072-9d3b-c1f84e75c1fd'
URL = f'{baseURL}:{port}/{category}/{eventID}'
IndWomanTrainers = ['Павлова', 'Зверева', 'Хасикян', 'Гусева', 'Хандов']
IndManTrainers = ['Хандов', 'Гусева', 'Павлова', 'Зверева']
TrioTrainers = ['Харужева', 'Хандов']
GPTrainers = ['Хандов', 'Зверева']
TGTrainers = ['Хандов', 'Пашкова']
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

def test_add_IndWoman1(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[0]) #выбор тренера
    time.sleep(2)
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1) #задержка без которой поля для клика перерываются уведомлениями об успешном добавлении

def test_add_IndWoman2(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[1]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(small) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndWoman3(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[2]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndWoman4(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[3]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(high) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndWoman5(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[4]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(small) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndWoman6(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[4]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndWoman7(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndWomanTrainers[4]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(high) #выбор возрастной группы
    app.choose_disc(IndWoman) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndMan1(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndManTrainers[0]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(high) #выбор возрастной группы
    app.choose_disc(IndMan) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndMan2(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndManTrainers[1]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(IndMan) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndMan3(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndManTrainers[2]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(small) #выбор возрастной группы
    app.choose_disc(IndMan) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_IndMan4(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(IndManTrainers[3]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(small) #выбор возрастной группы
    app.choose_disc(IndMan) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_Trio1(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(TrioTrainers[0]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(Trio) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_Trio2(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(TrioTrainers[1]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(Trio) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_TG1(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(TGTrainers[0]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(high) #выбор возрастной группы
    app.choose_disc(TG) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_4_sportik()
        app.add_5_sportik()
        app.add_6_sportik()
        app.add_7_sportik()
        app.add_8_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_TG2(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(TGTrainers[1]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(high) #выбор возрастной группы
    app.choose_disc(TG) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_4_sportik()
        app.add_5_sportik()
        app.add_6_sportik()
        app.add_7_sportik()
        app.add_8_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_GP1(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(GPTrainers[0]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(small) #выбор возрастной группы
    app.choose_disc(GP) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        app.add_1_sportik()
        app.add_2_sportik()
        app.add_3_sportik()
        app.add_4_sportik()
        app.add_5_sportik()
        app.add_6_sportik()
        app.add_7_sportik()
        app.add_8_sportik()
        app.add_next_sports()
        time.sleep(0.1)

def test_add_GP2(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.open_create_application_window()
    app.choose_trainer(GPTrainers[1]) #выбор тренера
    app.choose_organisation()
    app.save_application()
    app.open_add_nomination_window()
    app.choose_age(middle) #выбор возрастной группы
    app.choose_disc(GP) #выбор номинации
    app.save_nomination()
    app.open_add_sports_window()
    while (1): #бесконечно добавляет
        i = 1
        while i != 8:
            app.add_1_sportik()
            i = i + 1
        app.add_next_sports()
        time.sleep(0.1)

def test_accept_all_applications(driver):
    app = Applications(driver)
    app.authorization() #авторизация
    app.open(URL)
    app.send_applications()
    app.accept_applications()

def test_start_program(driver):
    prog = Program(driver)
    prog.authorization()
    prog.open(URL)
    prog.start_program()

def test_add_judges(driver):
    jud = Judges(driver)
    jud.authorization()
    jud.open(URL)
    i=0
    while i != 29:
        jud.add_judges()
        i = i + 1

def test_judges_teams(driver):
    br = Brigades(driver)
    br.authorization()
    br.open(URL)
    br.open_edit_brigades()
    br.create_brigades(4)

def test_set_program_plan(driver):
    prog = Program(driver)
    prog.authorization()
    prog.open(URL)
    prog.set_event_program()

def test_start_event(driver):
    print('Not ready')