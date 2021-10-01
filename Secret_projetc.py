import time
import sys
import os
import shutil
import webbrowser


def main():

    def yes_no(link):
        print("1: Igen".center(middle()))
        if link == 1:
            print("2: Nem, de szerintem most passzolom :)".center(middle()))
            print("3: Nem, és kíváncsi vagyok a Trailer-re ;)".center(middle()))
        elif link == 2:
            print("2: Nem, de szerintem most passzolom :)".center(middle()))
        else:
            print("2: Nem.".center(middle()))

    def middle():
        return shutil.get_terminal_size().columns

    def quit():
        print("Akkor legyen szép hétvégéd :)".center(middle()))
        sys.exit()

    def clear():
        os.system('clear')

    def nick_name():
        clear()
        print("Mi a codecool beceneved?".center(middle()))
        name = input(" " * (int(middle() / 2)))
        return name

    def movie_or_not():
        clear()
        print("Szeretsz moziba járni?".center(middle()))
        yes_no(link=0)
        first_choice = input(" " * (int(middle() / 2)))
        clear()
        if first_choice == "2":
            print(':"('.center(middle()))
            quit()
        elif first_choice == "1":
            return first_choice
        else:
            print("mellé nyomtál. Próbáljuk meg újra :)".center(middle()))
            time.sleep(2)
            movie_or_not()

    def seen_or_not():
        clear()
        print('Láttad a Free Guy-t?'.center(middle()))
        yes_no(link=1)
        choice = input(" " * (int(middle() / 2)))
        clear()
        if choice == "2":
            quit()
        elif choice == "3":
            print("Juhééééé".center(middle()))
            time.sleep(1)
            print("Paszolom neked a magyar tarilert :)...".center(middle()))
            time.sleep(2)
            webbrowser.open('https://www.youtube.com/watch?v=1xGs9fhzQoI')
            time.sleep(2)
            print("Ha megnézted, csapj egy entert:)".center(middle()))
            input(" " * (int(middle() / 2)))
            choice = "1"
            return choice

        elif choice == "1":
            return choice
        else:
            print("mellé nyomtál. Próbáljuk meg újra :)".center(middle()))
            time.sleep(2)
            seen_or_not()

    def again_or_not():
        clear()
        print('Van kedved megnézni szombaton velünk moziban?'.center(middle()))
        yes_no(link=3)
        wanna_watch_it = input(" " * (int(middle() / 2)))
        if wanna_watch_it == "2":
            quit()
        elif wanna_watch_it == "1":
            return wanna_watch_it
        print("mellé nyomtál. Próbáljuk meg újra :)".center(middle()))
        time.sleep(2)
        again_or_not()

    def alone_or_not():
        clear()
        print("Egyedül jönnél, vagy hoznál valakit?".center(middle()))
        print("1: Most egyedül".center(middle()))
        print("2: Ketten jönnénk".center(middle()))
        partner = input(" " * (int(middle() / 2)))
        if partner != '1' and partner != '2':
            print("mellé nyomtál. Próbáljuk meg újra :)".center(middle()))
            time.sleep(2)
            alone_or_not()
        if partner == '1':
            partner = "Egyedül érkezem"
        elif partner == "2":
            partner = "Párban érkezünk"
        return partner

    def which_saturday():
        clear()
        print("Melyik nap lenne jó Neked?".center(middle()))
        print("1: Most vasárnap(október 3)".center(middle()))
        print("2: Jövő hét szombat(október 9)".center(middle()))
        print("3: Mind 2 időpont jó nekem".center(middle()))
        saturday = input(" " * (int(middle() / 2)))
        if saturday != "1" and saturday != "2" and saturday != "3":
            print("mellé nyomtál. Próbáljuk meg újra :)".center(middle()))
            time.sleep(2)
            which_saturday()
        if saturday == "1":
            saturday = "Jövő hét szombat(október 9)"
        elif saturday == "3":
            saturday = "Mind 2 időpont jó nekem"
        else:
            saturday = "Most vasárnap(október 3)"
        return saturday

    def which_date():
        def names_dates():
            variable = []
            with open('.secret_list/list.txt', 'r') as file:
                menu = file.read().splitlines()
                for line in menu:
                    variable.append(line)
            return variable

        clear()
        variable = names_dates()
        print('Többiek, akik jönnek:'.center(middle()))
        for line in variable:
            print("\n")
            print(f'{line}'.center(middle()))
        print('\n\n')
        print('Neked melyik időpont lenne a jó?'.center(middle()))
        print('Westend:'.center(middle()))
        print('1: 12:40'.center(middle()))
        print('2: 15:00'.center(middle()))
        print('\n\n')
        print('Mammut:'.center(middle()))
        print('3: 17:30'.center(middle()))
        print('\n\n')
        print("Egyszerre többet is megadhatsz, pl.: 123, vagy 12".center(middle()))
        date = input(" " * (int(middle() / 2)))
        for string in date:
            if string != "1" and string != "2" and string != "3":
                print("mellé nyomtál. Próbáljuk meg újra :)".center(middle()))
                time.sleep(2)
                which_saturday()
        return(date)

    def date_iterator(dates):
        date_counter = []
        for date in dates:
            if date == "1":
                date_counter.append("Westend: 12:40")
            if date == "2":
                date_counter.append("Westend: 15:00")
            if date == "3":
                date_counter.append("Mammut: 17:30")
        return date_counter

    def appender(nickname, partner, date, saturday):
        new_line = ("\n")
        with open(".secret_list/list.txt", "a") as válasz:
            válasz = open(".secret_list/list.txt", "a")
            válasz.write(f'{nickname.capitalize()}: {partner},  {saturday},{" | ".join(date)}')
            válasz.write(new_line)
        clear()

    def invite():
        nickname = nick_name()
        movie_or_not()
        seen_or_not()
        again_or_not()
        partner = alone_or_not()
        saturday = which_saturday()
        date = which_date()
        date_or_dates = date_iterator(date)
        appender(nickname, partner, date_or_dates, saturday)
        print("Köszönöm, hogy kitöltötted. Kérlek told vissza gitre :)".center(middle()))

    invite()


main()
