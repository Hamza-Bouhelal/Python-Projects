import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import *
from tkinter import messagebox
import threading
import tkinter.ttk
import tkinter.font as tkFont
import json
import customtkinter


def load_settings():
    with open("config.txt", 'r') as file1:
        lines = file1.readlines()
        settings = ""
        for line in lines:
            settings += line
        settings.replace("\n", "")
        return json.loads(settings)


settings = {}
settings["global_email"] = ""
settings["global_password"] = ""
settings["email_to_send"] = ""
settings["name"] = ""
settings["last_name"] = ""
settings["phone"] = ""
settings["address"] = ""
settings["zip"] = ""
settings["city"] = ""
settings["country"] = ""
settings["position"] = ""
settings["Entreprise"] = ""
settings["Secteur"] = ""
settings["Type d'entreprise"] = ""
settings = load_settings()


def set_settings(global_email=settings["global_email"], global_password=settings["global_password"], email_to_send=settings["email_to_send"], name=settings["name"], last_name=settings["last_name"], phone=settings["phone"], address=settings["address"], zip=settings["zip"], city=settings["city"], country=settings["country"], position=settings["position"], entreprise=settings["Entreprise"], secteur=settings["Secteur"], type=settings["Type d'entreprise"]):
    with open("config.txt", 'w') as file11:
        new_settings = '{"global_email":"' + global_email + '","global_password":"' + global_password + '","name":"' + name + '","last_name":"' + last_name + '", "phone":"' + phone + '","address":"' + address + '","zip":"' + zip + \
            '","city":"' + city + '","country":"' + country + '","position":"' + position + '","email_to_send":"' + \
            email_to_send + '","Entreprise":"' + entreprise + '","Secteur":"' + \
            secteur + '","Type d\'entreprise":"' + type + '"}'
        file11.write(new_settings)


def sauvegarder(lst):
    temp = ["global_email", "global_password", "name", "last_name", "phone", "address", "zip",
            "city", "country", "position", "email_to_send", "Entreprise", "Secteur", "Type d'entreprise"]
    i = 0
    for ele in lst:
        settings[temp[i]] = ele.get()
        i += 1
    set_settings(global_email=settings["global_email"], global_password=settings["global_password"], email_to_send=settings["email_to_send"], name=settings["name"], last_name=settings["last_name"], phone=settings["phone"],
                 address=settings["address"], zip=settings["zip"], city=settings["city"], country=settings["country"], position=settings["position"],  entreprise=settings["Entreprise"], secteur=settings["Secteur"], type=settings["Type d'entreprise"])


def change_settings():
    ws = Tk()
    ws.title("Jobteaser Automatisation")
    f = ('Times', 12)
    f2 = ('Bombshell Pro', 14)
    f3 = ('Bombshell Pro', 1)
    lst = []
    Label(
        ws,
        text="\t ",
        font=f3).pack()
    Label(
        ws,
        text="Configuration des identifiant",
        font=f2).pack()
    Label(
        ws,
        text="\t ",
        font=f3).pack()
    left_frame = Frame(
        ws,
        bd=2,
        bg='#CCCCCC',
        relief=SOLID,
        padx=10,
        pady=10
    )
    a = Label(
        left_frame,
        text="Détail du compte:",
        bg='#CCCCCC',
        font=f2)
    ab = tkFont.Font(a, a.cget("font"))
    ab.configure(underline=True)
    a.configure(font=ab)
    a.grid(row=0, column=1, sticky=W, pady=10)
    Label(
        left_frame,
        text="Adresse Email:",
        bg='#CCCCCC',
        font=f
    ).grid(row=1, column=0, pady=10)

    email = Entry(
        left_frame,
        font=f
    )
    email.grid(row=1, column=1, pady=10, padx=20)
    email.insert(0, settings["global_email"])
    lst.append(email)
    Label(
        left_frame,
        text="\tMot de passe:",
        bg='#CCCCCC',
        font=f
    ).grid(row=1, column=3, pady=10)

    password = Entry(
        left_frame,
        font=f
    )
    password.grid(row=1, column=4, pady=10, padx=20)
    lst.append(password)
    password.insert(0, settings["global_password"])

    Label(
        left_frame,
        text="\tPrénom:",
        bg='#CCCCCC',
        font=f
    ).grid(row=2, column=3, pady=10)

    name = Entry(
        left_frame,
        font=f
    )
    name.grid(row=2, column=4, pady=10, padx=20)
    name.insert(0, settings["name"])
    lst.append(name)
    Label(
        left_frame,
        text="Nom:",
        bg='#CCCCCC',
        font=f
    ).grid(row=2, column=0, pady=10)

    last_name = Entry(
        left_frame,
        font=f
    )
    last_name.grid(row=2, column=1, pady=10, padx=20)
    last_name.insert(0, settings["last_name"])
    lst.append(last_name)

    Label(
        left_frame,
        text="Numero de téléphone:",
        bg='#CCCCCC',
        font=f
    ).grid(row=3, column=0, pady=10)

    phone = Entry(
        left_frame,
        font=f
    )
    phone.grid(row=3, column=1, pady=10, padx=20)
    phone.insert(0, settings["phone"])
    lst.append(phone)
    Label(
        left_frame,
        text="\tAdresse: ",
        bg='#CCCCCC',
        font=f
    ).grid(row=3, column=3, pady=10)

    address = Entry(
        left_frame,
        font=f
    )
    address.grid(row=3, column=4, pady=10, padx=20)
    address.insert(0, settings["address"])
    lst.append(address)
    Label(
        left_frame,
        text="Code postal:",
        bg='#CCCCCC',
        font=f
    ).grid(row=4, column=0, pady=10)

    zip = Entry(
        left_frame,
        font=f
    )
    zip.grid(row=4, column=1, pady=10, padx=20)
    zip.insert(0, settings["zip"])
    lst.append(zip)
    Label(
        left_frame,
        text="\tVille:",
        bg='#CCCCCC',
        font=f
    ).grid(row=4, column=3, pady=10)

    city = Entry(
        left_frame,
        font=f
    )
    city.grid(row=4, column=4, pady=10, padx=20)
    lst.append(city)
    city.insert(0, settings["city"])
    Label(
        left_frame,
        text="Pays:",
        bg='#CCCCCC',
        font=f
    ).grid(row=5, column=0, pady=10)

    country = Entry(
        left_frame,
        font=f
    )
    country.grid(row=5, column=1, pady=10, padx=20)
    country.insert(0, settings["country"])
    lst.append(country)
    Label(
        left_frame,
        text="\tPoste:",
        bg='#CCCCCC',
        font=f
    ).grid(row=5, column=3, pady=10)

    position = Entry(
        left_frame,
        font=f
    )
    position.grid(row=5, column=4, pady=10, padx=20)
    lst.append(position)
    position.insert(0, settings["position"])
    Label(
        left_frame,
        text="Email recevant les postes:",
        bg='#CCCCCC',
        font=f
    ).grid(row=6, column=0, pady=10)

    emailto = Entry(
        left_frame,
        font=f
    )
    emailto.grid(row=6, column=1, pady=10, padx=20)
    emailto.insert(0, settings["email_to_send"])
    lst.append(emailto)

    sep = tkinter.ttk.Separator(left_frame, orient=tkinter.HORIZONTAL)
    sep.grid(row=7, columnspan=5, sticky="ew")

    Label(
        left_frame,
        text="Entreprise:",
        bg='#CCCCCC',
        font=f
    ).grid(row=8, column=0, pady=10)

    ent = Entry(
        left_frame,
        font=f
    )
    ent.grid(row=8, column=1, pady=10, padx=20)
    ent.insert(0, settings["Entreprise"])
    lst.append(ent)
    Label(
        left_frame,
        text="\tSecteur:",
        bg='#CCCCCC',
        font=f
    ).grid(row=8, column=3, pady=10)

    secteur = Entry(
        left_frame,
        font=f
    )
    secteur.grid(row=8, column=4, pady=10, padx=20)
    lst.append(secteur)
    secteur.insert(0, settings["Secteur"])
    optionList = ["", "Grande entreprise", "PME", "Start-up", "Association/institution publique/Laboratoire",
                  "Collectif"]

    Label(
        left_frame,
        text="Type d'entreprise:",
        bg='#CCCCCC',
        font=f
    ).grid(row=9, column=0, pady=10)

    dropVar = StringVar()
    dropVar.set(settings["Type d'entreprise"])
    dropmenu = OptionMenu(left_frame, dropVar, *optionList)
    dropmenu.config(width=35, anchor="w")
    dropmenu.grid(row=9, column=1)
    lst.append(dropVar)

    Button(
        left_frame,
        width=18,
        text='Sauvegarder',
        font=f,
        relief=SOLID,
        cursor='hand2',
        command=lambda: [sauvegarder(lst)],
    ).grid(row=10, column=4, pady=10, padx=15)

    Button(
        left_frame,
        width=18,
        text="Retourner à l'accueil",
        font=f,
        relief=SOLID,
        cursor='hand2',
        command=lambda: [ws.destroy(), main_menu()],
    ).grid(row=10, column=0, pady=10, padx=15)
    left_frame.pack()
    ws.mainloop()


def register_page_from_login_link(url1, email_address):
    return url1.split("recr")[0] + "backend/recruiter_profile/new?user[email]=" + email_address.replace('@', '%40')


def jobteaser_automatisation_sign_up(driver, name=settings["name"], last_name=settings["last_name"], password=settings["global_password"], phone=settings["phone"], address=settings["address"], zip=settings["zip"], city=settings["city"], country=settings["country"], position=settings["position"], entreprise=settings["Entreprise"], secteur=settings["Secteur"], type=settings["Type d'entreprise"]):
    driver.find_element_by_id('user_password').send_keys(password)
    driver.find_element_by_id('user_password').send_keys(Keys.RETURN)
    driver.find_element_by_id('user_password_confirmation').send_keys(password)
    driver.find_element_by_id(
        'user_password_confirmation').send_keys(Keys.RETURN)
    driver.find_element_by_id('user_first_name').send_keys(name)
    driver.find_element_by_id('user_last_name').send_keys(last_name)
    driver.find_element_by_id('user_phone_number').send_keys(phone)
    driver.find_element_by_id('user_address').send_keys(address)
    driver.find_element_by_id('user_zip_code').send_keys(zip)
    driver.find_element_by_id('user_city').send_keys(city)
    driver.find_element_by_id('user_country').send_keys(country)
    driver.find_element_by_id('user_position').send_keys(position)
    driver.find_element_by_id('terms').click()
    driver.find_element_by_id('recruiter_form_go_to_step2').click()
    driver.find_element_by_id(
        'user_recruiter_profile_company_name').send_keys(entreprise)
    select = driver.find_elements_by_class_name("select2-choice")
    select[0].click()
    driver.find_element_by_id('s2id_autogen1_search').send_keys(secteur)
    driver.find_element_by_id('s2id_autogen1_search').send_keys(Keys.RETURN)
    select[1].click()
    lst = ["Grande entreprise", "PME", "Start-up",
           "Association/institution publique/Laboratoire", "Collectif"]
    options = driver.find_elements_by_class_name("select2-result-label")
    for i in range(len(lst)):
        if type == lst[i]:
            options[i].click()
            break
    driver.find_element_by_id('submit').click()
    driver.find_element_by_link_text("Passer cette étape").click()


def jobteaser_automatisation_login(driver, email_address, password):
    driver.find_element_by_xpath(
        '//*[@id="user_email"]').send_keys(email_address)
    driver.find_element_by_link_text("Suivant").click()
    time.sleep(0.5)
    driver.find_element_by_id('user_password').send_keys(password)
    driver.find_element_by_id('user_password').send_keys(Keys.RETURN)


def jobteaser_automatisation_create_offer(driver, email_address, list_for_offer, otherfile):
    if list_for_offer[4].replace("\n", "") == "":
        if otherfile:
            driver.find_element_by_link_text("Accueil").click()
            driver.find_element_by_link_text("Offres").click()
        return False
    time.sleep(0.5)
    driver.find_element_by_link_text("Ajouter une offre").click()

    dropdown_btn = driver.find_element_by_xpath(
        '//*[@id="job_offer"]/div[2]/div[5]/div/button')
    dropdown_btn.click()
    state = False
    for ele in list_for_offer[4].split(","):
        if len(list_for_offer[4].split(",")) == 0:
            break
        state = False
        try:
            c = driver.find_element_by_link_text(ele)
        except:
            state = True
        if not state:
            c.click()
            break
    if state:
        print("Fonctionalité indisponible!")
        if otherfile:
            driver.find_element_by_link_text("Accueil").click()
            driver.find_element_by_link_text("Offres").click()
        return False
    else:
        driver.find_element_by_xpath(
            '//*[@id="job_offer_title"]').send_keys(list_for_offer[0])
        lieu = driver.find_element_by_xpath(
            '//*[@id="job_offer"]/div[2]/div[1]/div[1]/input')
        lieu.send_keys(list_for_offer[1])
        time.sleep(1)
        lieu.send_keys(Keys.DOWN)
        lieu.send_keys(Keys.RETURN)

        if list_for_offer[2] == "Non spécifié":
            modalite_de_teletravail = driver.find_element_by_xpath(
                '//*[@id="job_offer_remote_type_not_specified"]')
        elif list_for_offer[2] == "Télétravail non autorisé":
            modalite_de_teletravail = driver.find_element_by_xpath(
                '//*[@id="job_offer_remote_type_remote_not_allowed"]')
        elif list_for_offer[2] == "Télétravail ponctuel autorisé":
            modalite_de_teletravail = driver.find_element_by_xpath(
                '//*[@id="job_offer_remote_type_remote_partial_allowed"]')
        elif list_for_offer[2] == "Poste ouvert au télétravail à temps plein":
            modalite_de_teletravail = driver.find_element_by_xpath(
                '//*[@id="job_offer_remote_type_remote_full_allowed"]')
        elif list_for_offer[2] == "Uniquement en télétravail":
            modalite_de_teletravail = driver.find_element_by_xpath(
                '//*[@id="job_offer_remote_type_remote_only"]')
        modalite_de_teletravail.click()

        select_job_offer = Select(
            driver.find_element_by_id('job_offer_contract_type'))
        if list_for_offer[3] == "CDI" or list_for_offer[3] == "Job étudiant":
            select_job_offer.select_by_visible_text(list_for_offer[3])
        else:
            select_job_offer.select_by_visible_text(
                list_for_offer[3].split(" ")[0])

        if list_for_offer[3] != "CDI" and list_for_offer[3] != "Job étudiant":
            time.sleep(2)
            sliders = driver.find_element_by_class_name(
                'slider-handles-container').find_elements_by_tag_name('div')

            lower_bound = driver.execute_script('return arguments[0].value;', driver.find_element_by_xpath(
                '//*[@id="job_offer"]/div[2]/div[4]/div/div/input[1]'))
            upper_bound = driver.execute_script('return arguments[0].value;', driver.find_element_by_xpath(
                '//*[@id="job_offer"]/div[2]/div[4]/div/div/input[2]'))

            wanted_lower_bound = list_for_offer[3].split(" ")[1]
            wanted_upper_bound = list_for_offer[3].split(" ")[2]

            move_upper_right = ActionChains(driver)
            move_upper_right.click_and_hold(sliders[1])
            move_upper_right.move_by_offset(75, 0)
            move_upper_right.release(sliders[1])
            if upper_bound != wanted_upper_bound:
                while int(upper_bound) < 36:
                    move_upper_right.perform()
                    upper_bound = driver.execute_script('return arguments[0].value;', driver.find_element_by_xpath(
                        '//*[@id="job_offer"]/div[2]/div[4]/div/div/input[2]'))
                    if int(upper_bound) == 36:
                        break

            move_lower_left = ActionChains(driver)
            move_lower_left.click_and_hold(sliders[0])
            move_lower_left.move_by_offset(-75, 0)
            move_lower_left.release(sliders[0])
            if lower_bound != wanted_lower_bound:
                while int(lower_bound) > 2:
                    move_lower_left.perform()
                    lower_bound = driver.execute_script('return arguments[0].value;', driver.find_element_by_xpath(
                        '//*[@id="job_offer"]/div[2]/div[4]/div/div/input[1]'))
                    if int(lower_bound) == 2:
                        break

            move_lower_right = ActionChains(driver)
            move_lower_right.click_and_hold(sliders[0])
            move_lower_right.move_by_offset(75, 0)
            move_lower_right.release(sliders[0])
            if int(lower_bound) != int(wanted_lower_bound):
                while int(lower_bound) < int(wanted_lower_bound):
                    move_lower_right.perform()
                    lower_bound = driver.execute_script('return arguments[0].value;', driver.find_element_by_xpath(
                        '//*[@id="job_offer"]/div[2]/div[4]/div/div/input[1]'))
                    if int(lower_bound) == int(wanted_lower_bound):
                        break

            move_upper_left = ActionChains(driver)
            move_upper_left.click_and_hold(sliders[1])
            move_upper_left.move_by_offset(-75, 0)
            move_upper_left.release(sliders[1])
            upper_bound = driver.execute_script('return arguments[0].value;', driver.find_element_by_xpath(
                '//*[@id="job_offer"]/div[2]/div[4]/div/div/input[2]'))
            while int(upper_bound) > int(wanted_upper_bound):
                move_upper_left.perform()
                upper_bound = driver.execute_script('return arguments[0].value;', driver.find_element_by_xpath(
                    '//*[@id="job_offer"]/div[2]/div[4]/div/div/input[2]'))
                if int(upper_bound) == int(wanted_upper_bound):
                    break

        select_job_offer = Select(
            driver.find_element_by_id('job_offer_work_experience'))
        select_job_offer.select_by_value('3')

        driver.find_element_by_xpath(
            '//*[@id="job_offer"]/div[3]/div[2]/div/div[3]/div').send_keys(list_for_offer[5])

        driver.find_element_by_xpath(
            '//*[@id="job_offer_notification_email"]').send_keys(email_address)

        elem = driver.find_element_by_xpath(
            '//*[@id="job_offer"]/div[2]/div[4]/div/div/input[1]')

        driver.find_element_by_xpath(
            "//*[@id='new_job_offer']/fieldset[1]/div/div[2]/input").click()
        return True


def from_file_path_to_list(file_offer_path):
    file_offer_path_without_new_line = file_offer_path.replace("\n", "")
    with open("./Jobteaser Offres/"+file_offer_path_without_new_line, 'r', encoding='utf8') as file1:
        lines = file1.readlines()
        lines_without_new_line = [line.replace("\n", "") for line in lines[:5]]
        description = ""
        for idx in range(5, len(lines)):
            description += lines[idx]
        lines_without_new_line.append(description)
        return lines_without_new_line


def multiconditional_running():
    try:
        start_tread()
    except RuntimeError:
        messagebox.showinfo('Lancement Impossible',
                            'Fermez et rouvrez l\'application')


global list_of_offres
list_of_offres = [filename for filename in os.listdir("./Jobteaser Offres")]
list_of_schools = []
global config, config_with_cat, listofkeys, globkey
listofkeys = []
config, config_with_cat = {}, {}
global lines
with open("jobteaser_links.txt", 'r', encoding='utf8') as file1:
    for ele in file1.readlines():
        stritemp = ele.split(" ")[0]
        config[stritemp] = []
        for ele1 in [x.replace('_', ' ').replace("\n", "") for x in ele.split(" ")[1].split('/')]:
            config_with_cat[ele1] = []
with open("jobteaser_links.txt", 'r', encoding='utf8') as file1:
    for ele in file1.readlines():
        for ele1 in [x.replace('_', ' ').replace("\n", "") for x in ele.split(" ")[1].split('/')]:
            for key in config_with_cat.keys():
                if key == ele1:
                    config_with_cat[key].append(ele.split(" ")[0])
    for key in config_with_cat.keys():
        config_with_cat[key] = list(set(config_with_cat[key]))
    lines = [ele.replace("\n", "").split(" ")[0] for ele in file1.readlines()]
    for line in lines:
        if line != "" and line != "\n":
            config[line] = []
            list_of_schools.append(line.split(
                ':')[1].split(".")[0].replace("/", ''))
for key in config_with_cat.keys():
    listofkeys.append(key)
    key = "https://" + key + ".jobteaser.com/fr/recruiter_account/sign_in"


def add_config(lib1, lst2):
    for key in lib1.keys():
        for i in range(len(lib1[key])):
            if lib1[key][i].get():
                for ele in range(len(lst2)):
                    if lst2[ele].get():
                        config[config_with_cat[key][i]].append(
                            list_of_offres[ele])
    for key in lib1.keys():
        for ele in lib1[key]:
            ele.set(False)
    for ele in lst2:
        ele.set(False)


class val:
    def __init__(self):
        self.valu = 0

    def inc(self):
        self.valu += 1

    def dinc(self):
        self.valu -= 1

    def get(self):
        return self.valu

    def reset(self):
        self.valu = 0

    def set(self, n):
        self.valu = n


def change_right_cat(lst_to_change, globkey, lst_for_checkbutton_cat, lab, i):
    if i.get() != len(listofkeys)-1:
        i.inc()
        globkey = listofkeys[i.get()]
        lab.config(text=f"  {globkey}")
        for but in lst_to_change:
            but.config(text="",  variable=None)
            but.grid_remove()
        idx = 0
        for ele in config_with_cat[globkey]:
            lst_to_change[idx].config(text=ele.split(':')[1].split(".")[0].replace("/", ''),
                                      variable=lst_for_checkbutton_cat[globkey][idx])
            lst_to_change[idx].grid(**lst_to_change[idx]._grid_info)
            idx += 1
    else:
        i.reset()
        globkey = listofkeys[i.get()]
        lab.config(text=f"  {globkey}")
        for but in lst_to_change:
            but.config(text="", variable=None)
            but.grid_remove()
        idx = 0
        for ele in config_with_cat[globkey]:
            lst_to_change[idx].config(text=ele.split(':')[1].split(".")[0].replace("/", ''),
                                      variable=lst_for_checkbutton_cat[globkey][idx])
            lst_to_change[idx].grid(**lst_to_change[idx]._grid_info)
            idx += 1


def change_left_cat(lst_to_change, globkey, lst_for_checkbutton_cat, lab, i):
    if i.get() != 0:
        i.dinc()
        globkey = listofkeys[i.get()]
        lab.config(text=f"  {globkey}")
        for but in lst_to_change:
            but.config(text="",  variable=None)
            but.grid_remove()
        idx = 0
        for ele in config_with_cat[globkey]:
            lst_to_change[idx].config(text=ele.split(':')[1].split(".")[0].replace("/", ''),
                                      variable=lst_for_checkbutton_cat[globkey][idx])
            lst_to_change[idx].grid(**lst_to_change[idx]._grid_info)
            idx += 1
    else:
        i.set(len(listofkeys)-1)
        globkey = listofkeys[i.get()]
        lab.config(text=f"  {globkey}")
        for but in lst_to_change:
            but.config(text="", variable=None)
            but.grid_remove()
        idx = 0
        for ele in config_with_cat[globkey]:
            lst_to_change[idx].config(text=ele.split(':')[1].split(".")[0].replace("/", ''),
                                      variable=lst_for_checkbutton_cat[globkey][idx])
            lst_to_change[idx].grid(**lst_to_change[idx]._grid_info)
            idx += 1


def post_it():
    i = val()
    globkey = listofkeys[i.get()]
    ws = Tk()
    ws.title("Jobteaser Automatisation")
    ws.config()
    f = ('Times', 14)
    f4 = ('Times', 10)
    f2 = ('Bombshell Pro', 16)
    Label(
        ws,
        text="\t",
        font=f).pack()
    Label(
        ws,
        text="Jobteaser Automatisation",
        font=f2).pack()
    Label(
        ws,
        text="\t",
        font=f).pack()
    left_frame = Frame(
        ws,
        bd=2,
        bg='#CCCCCC',
        relief=SOLID,
        padx=10,
        pady=10
    )

    login_btn1 = Button(
        left_frame,
        width=15,
        text='Lancer',
        font=f,
        relief=SOLID,
        cursor='hand2',
        command=lambda: [multiconditional_running()],
    )
    Label(
        left_frame,
        text="       ",
        bg='#CCCCCC',
        font=f).grid(row=3, column=0, sticky=W, pady=10)
    idx = 4
    lst_for_checkbutton_cat = {}
    for key in listofkeys:
        lst_for_checkbutton_cat[key] = [BooleanVar()
                                        for _ in range(len(config_with_cat[key]))]
    pdx = 0
    count = 0
    tempidx = 0
    lst_to_change = []
    lengthi = 0
    for key in config_with_cat.keys():
        if lengthi < len(config_with_cat[key]):
            lengthi = len(config_with_cat[key])

    for ran in range(lengthi):
        if count == 12:
            pdx += 1
            count = 0
            idx -= 12
        if len(config_with_cat[globkey]) > ran:
            but = Checkbutton(
                left_frame,
                text=config_with_cat[globkey][tempidx].split(':')[1].split(".")[
                    0].replace("/", ''),
                bg='#CCCCCC',
                variable=lst_for_checkbutton_cat[globkey][tempidx],
                font=f)
            but._grid_info = but.grid_info()
            but.grid(row=idx+1, column=0+pdx, sticky=W, pady=10)
        else:
            but = Checkbutton(
                left_frame,
                bg='#CCCCCC',
                font=f)
            but.grid(row=idx + 1, column=0 + pdx, sticky=W, pady=10)
            but._grid_info = but.grid_info()
            but.grid_remove()
        lst_to_change.append(but)
        count += 1
        idx += 1
        tempidx += 1
    if pdx == 0:
        pdx += 1

    if len(list_of_schools) < 8 and len(list_of_offres) < 8:
        lenght = max(len(list_of_schools), len(list_of_offres))
    else:
        lenght = 12
    pdx += 1
    sep = tkinter.ttk.Separator(left_frame, orient=VERTICAL)
    sep.grid(column=pdx+1, row=5, rowspan=lenght, sticky='ns')
    a = Label(
        left_frame,
        text="Écoles:",
        bg='#CCCCCC',
        font=f)
    ab = tkFont.Font(a, a.cget("font"))
    ab.configure(underline=True)
    a.configure(font=ab)
    a.grid(row=3, column=0, sticky=W, pady=10)
    lab = Label(
        left_frame,
        text=f"  {globkey}",
        bg='#CCCCCC',
        font=f)
    lab.grid(row=4, column=1, sticky=W, pady=10)
    b = Label(
        left_frame,
        text="Offres à poster:",
        bg='#CCCCCC',
        font=f)
    bc = tkFont.Font(b, b.cget("font"))
    bc.configure(underline=True)
    b.configure(font=bc)
    b.grid(row=3, column=pdx+2, sticky=W, pady=10)
    jdx = 5
    lst_for_checkbutton_for_offre = [BooleanVar()
                                     for _ in range(len(list_of_offres))]
    count = 0
    tempidx = 0
    for ele in list_of_offres:
        if count == 12:
            count = 0
            pdx += 1
            jdx -= 12
        but = Checkbutton(
            left_frame,
            text=ele.replace(".txt", "").replace("(HF)", ""),
            bg='#CCCCCC',
            variable=lst_for_checkbutton_for_offre[tempidx],
            font=f)
        but.grid(row=jdx, column=2+pdx, sticky=W, pady=10)
        count += 1
        jdx += 1
        tempidx += 1
    if count == 12:
        temp0 = 17
        temp1 = pdx+1
    else:
        temp0 = 16
        temp1 = pdx+2

    Button(
        left_frame,
        width=18,
        text='Ajouter configuration',
        font=f,
        relief=SOLID,
        cursor='hand2',
        command=lambda: [add_config(
            lst_for_checkbutton_cat, lst_for_checkbutton_for_offre)],
    ).grid(row=temp0, column=temp1, pady=10, padx=20)
    login_btn1.grid(row=17, column=2+pdx, pady=10, padx=20)
    Button(
        left_frame,
        width=18,
        text='Creation de compte',
        font=f,
        relief=SOLID,
        cursor='hand2',
        command=lambda: [ws.destroy(), set_it()],
    ).grid(row=17, column=2, pady=10, padx=15)
    Button(
        left_frame,
        width=18,
        text='Catégorie suivante',
        font=f4,
        relief=SOLID,
        cursor='hand2',
        command=lambda: [change_right_cat(
            lst_to_change, globkey, lst_for_checkbutton_cat, lab, i)],
    ).grid(row=4, column=2, pady=8, padx=11)
    Button(
        left_frame,
        width=18,
        text='Catégorie précedente',
        font=f4,
        relief=SOLID,
        cursor='hand2',
        command=lambda: [change_left_cat(
            lst_to_change, globkey, lst_for_checkbutton_cat, lab, i)],
    ).grid(row=4, column=0, pady=8, padx=11)
    left_frame.pack()
    ws.mainloop()


def submit(email=settings["email_to_send"]):
    for key in config.keys():
        config[key] = list(set(config[key]))
    for key in config.keys():
        if len(config[key]) == 0:
            continue
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(key)
        driver.maximize_window()
        jobteaser_automatisation_login(
            driver, settings["global_email"], settings["global_password"])
        idx = 0
        name = key.split(".")[0].split("://")[1].replace('\n', '')
        for file_offer_path in config[key]:
            if idx != len(config[key]) - 1:
                status = jobteaser_automatisation_create_offer(driver, email, from_file_path_to_list(file_offer_path),
                                                               True)
            else:
                status = jobteaser_automatisation_create_offer(driver, email, from_file_path_to_list(file_offer_path),
                                                               False)
            if status:
                print(
                    f"{file_offer_path.replace('.txt', '' )} a été posté sur {name}.")
            else:
                print(
                    f"L'offre {file_offer_path.replace('.txt', '' )} n'a pas été posté sur {name}.")
            if idx != len(config[key]) - 1:
                driver.find_element_by_link_text("Accueil").click()
                driver.find_element_by_link_text("Offres").click()
            print()
            idx += 1
        driver.close()
    for key in config.keys():
        config[key] = []


def start_tread():
    for key in config.keys():
        if len(config[key]) != 0:
            newtread = threading.Thread(target=submit, daemon=True)
            newtread.start()
            return
    messagebox.showinfo('', 'Ajoutez configuration!')


def add_account(lst):
    state = True
    for idx in range(len(lst)):
        if lst[idx].get():
            state = False
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(register_page_from_login_link(
                lines[idx], settings["global_email"]))
            driver.maximize_window()
            jobteaser_automatisation_sign_up(driver)
            driver.close()
            lst[idx].set(False)
    if state:
        messagebox.showinfo('', 'Aucune organisation n\'a été selectionnée!')


def start_it(argi):
    threading.Thread(target=lambda: add_account(argi)).start()


def set_it():
    ws = Tk()
    ws.title("Jobteaser Automatisation")
    f = ('Times', 14)
    f2 = ('Bombshell Pro', 16)
    Label(
        ws,
        text="\t",
        font=f).pack()
    Label(
        ws,
        text="Jobteaser Automatisation",
        font=f2).pack()
    Label(
        ws,
        text="\t",
        font=f).pack()
    left_frame = Frame(
        ws,
        bd=2,
        bg='#CCCCCC',
        relief=SOLID,
        padx=10,
        pady=10
    )

    idx = 0
    pdx = 0
    count = 0
    tempidx = 0
    state = False
    list_of_schools = []
    with open("jobteaser_links.txt", 'r', encoding='utf8') as file1:
        lines1 = [ele.replace("\n", "").split(" ")[0]
                  for ele in file1.readlines()]
        for line in lines1:
            if line != "" and line != "\n":
                lines.append(line)
                list_of_schools.append(line.split(
                    ':')[1].split(".")[0].replace("/", ''))
    lst_for_checkbutton_sign_up = [BooleanVar()
                                   for _ in range(len(list_of_schools))]
    for ele in list_of_schools:
        if count == 12:
            state = True
            pdx += 1
            count = 0
            idx -= 12
        but = Checkbutton(
            left_frame,
            text=ele,
            bg='#CCCCCC',
            variable=lst_for_checkbutton_sign_up[tempidx],
            font=f)
        but.grid(row=idx, column=0 + pdx, sticky=W, pady=10)
        count += 1
        idx += 1
        tempidx += 1
    left_frame.pack()
    if state:
        temp0 = 13
    else:
        temp0 = idx + 1
    if pdx != 0:
        Button(
            left_frame,
            width=18,
            text='Creation de poste',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=lambda: [ws.destroy(), post_it()],
        ).grid(row=temp0, column=0, pady=10, padx=15)
    if pdx > 3:
        Button(
            left_frame,
            width=18,
            text='  Crée Comptes Jobteaser  ',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=lambda: start_it(lst_for_checkbutton_sign_up),
        ).grid(row=temp0, column=pdx-1, pady=10, padx=20)
    else:
        Button(
            left_frame,
            width=18,
            text='  Crée Comptes Jobteaser  ',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=lambda: start_it(lst_for_checkbutton_sign_up),
        ).grid(row=temp0, column=pdx, pady=10, padx=20)
    ws.mainloop()


def main_menu():
    # Modes: system (default), light, dark
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    ws = customtkinter.CTk()
    ws.title("Jobteaser Automatisation")
    ws.geometry('684x200')
    f = ('Times', 14)
    f2 = ('Bombshell Pro', 16)
    f3 = ('Bombshell Pro', 3)
    customtkinter.CTkLabel(
        ws,
        text="\t",
    ).pack()

    customtkinter.CTkLabel(
        ws,
        text="Jobteaser Automatisation",
    ).pack()
    customtkinter.CTkLabel(
        ws,
        text="\t ",
    ).pack()
    customtkinter.CTkLabel(
        ws,
        text="\t ",
    ).pack()
    left_frame = Frame(
        ws,
        bd=2,
        bg='#CCCCCC',
        relief=SOLID,
        padx=10,
        pady=10
    )
    customtkinter.CTkButton(
        left_frame,
        width=18,
        text='Création de compte',
        relief=SOLID,
        cursor='hand2',
        command=lambda: [ws.destroy(), set_it()],
    ).grid(row=3, column=3, pady=10, padx=15)
    customtkinter.CTkButton(
        left_frame,
        width=18,
        text='Changer les identifiants',
        relief=SOLID,
        cursor='hand2',
        command=lambda: [ws.destroy(), change_settings()],
    ).grid(row=3, column=4, pady=10, padx=15)
    customtkinter.CTkButton(
        left_frame,
        width=18,
        text='Création de poste',
        relief=SOLID,
        cursor='hand2',
        command=lambda: [ws.destroy(), post_it()],
    ).grid(row=3, column=5, pady=10, padx=15)
    left_frame.pack()
    ws.mainloop()


main_menu()
