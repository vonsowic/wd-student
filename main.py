# -*- coding: utf-8 -*-
u"""Main script"""
from crawler import WdCrawler as Crawler
from notification import send_email as send
import pickle
from os import path as pth


def load_configuration(filename=pth.dirname(pth.abspath(__file__))+"/config.pickle"):
    u"""Loads configuration data from file"""
    login_data = {}
    try:
        with open(filename, 'rb') as handle:
            login_data = pickle.load(handle)
    except IOError:
        accept = False
        while not accept:
            login_data["login_d"] = input("Login do wirtualnej uczelnii: ")
            login_data["password_d"] = input("Haslo do wirtualnej uczelnii: ")
            login_data["login_m"] = input("Login do studenckiego maila(wpisz razem z @stud...): ")
            login_data["password_m"] = input("haslo do mail: ")
            login_data["notification_address"] = input("Na jaki mail wysylac powiadomienia?: ")
            if input("Czy dane sa poprawne[T/N]: ") == "T":
                accept = True

        with open(filename, 'wb') as f:
            pickle.dump(login_data, f, protocol=pickle.HIGHEST_PROTOCOL)

    return login_data


if __name__ == "__main__":
    login_data = load_configuration()
    c = Crawler(login_data.get("login_d"), login_data.get("password_d"))
    local_path = pth.dirname(pth.abspath(__file__))
    old_marks_file_name = local_path + "/old_marks.html"

    tmp_marks = c.getMarksInHtmlTable()

    # TODO: utf-8 should be default
    marks = str(tmp_marks.encode('utf-8'))
    try:
        f = open(old_marks_file_name, 'r')
        old_marks = f.read()
        if old_marks != marks:
            send(
                login_data.get("login_m"),
                login_data.get("notification_address"),
                login_data.get("password_m"),
                marks)
            f.close()
            f = open(old_marks_file_name, 'w')
            f.write(marks)
        f.close()

    except IOError:
        print("Error: this is initial usage or another error occurred")
        with open(old_marks_file_name, 'w') as f:
            send(
                login_data.get("login_m"),
                login_data.get("notification_address"),
                login_data.get("password_m"),
                marks,
                "Pierwsza wiadomosc")
            f.write(marks)

