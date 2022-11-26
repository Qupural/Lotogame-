from cards import Cards
import random
cards_player = Cards()
cards_comp1 = Cards()
cards_comp2 = Cards()
cards_player2 = Cards()
while True:
    print('1. игра против ПК')
    print('2. игра ПК против ПК')
    print('3. игра Игрок против Игрока')
    print('4. ВЫход')

    num = input('Введите номер:')
    if num == '1':
        player = cards_player.cards()
        print('                                       ')
        comp_num2 = cards_comp2.cards()
        count = 90
        numbers = []
        one = 0
        count_player = 0
        count_comp_2 = 0
        while len(numbers) != 90:
            one += 1
            numbers.append(one)
        while count_comp_2 != 15 and count_player != 15:

            player = cards_player.cards_form('Игрок!')
            print('                                       ')
            comp2 = cards_comp2.cards_form('Компьютер!')
            print(player)
            print(comp2)
            count = count - 1
            qwe = random.choice(numbers)
            numbers.remove(qwe)

            print(f'Номер бочонка {qwe}, (осталось: {count}) ')
            otvet  = input(' Удалить число? + / - ')


            if otvet == '+':
                if qwe in cards_player.data:
                    c =cards_player.data.index(qwe)
                    cards_player.data[c]= -1
                    player = cards_player.cards_form('Игрок!')
                    count_player +=1

                else:
                    print('You Lose ')
                    break
            elif otvet == '-':
                if qwe in cards_player.data:
                    print('You Lose ')
                    break
            else:
                print('Ты испортил бланк  и проиграл ')
                break


            if qwe in cards_comp1.data:
                c = cards_comp2.data.index(qwe)
                cards_comp2.data[c] = -1
                comp = cards_comp2.cards_form('Компьютер!')
                count_comp_2 += 1

        if count_player == 15:
            print('Победа Игрока!')
        elif count_comp_2 == 15:
            print('Победа Компьютера ')
        else:
            break


    elif num == '2':
        comp_num1 = cards_comp1.cards()
        print('                                       ')
        comp_num2 = cards_comp2.cards()
        count = 90
        numbers = []
        one = 0
        count_comp_1 = 0
        count_comp_2 = 0
        while len(numbers) != 90:
            one += 1
            numbers.append(one)

        while count_comp_2 != 15 and count_comp_1 != 15:

            comp1 = cards_comp1.cards_form('Компьютер1')
            print('                                       ')
            comp2 = cards_comp2.cards_form('Компьютер2')
            print(comp1)
            print(comp2)
            count = count - 1
            qwe = random.choice(numbers)
            numbers.remove(qwe)

            print(f'Номер бочонка {qwe}, (осталось: {count}) ')

            if qwe in cards_comp1.data:
                c = cards_comp1.data.index(qwe)
                cards_comp1.data[c] = -1
                comp = cards_comp1.cards_form('Компьютер1')
                count_comp_1 += 1

            if qwe in cards_comp2.data:
                c = cards_comp2.data.index(qwe)
                cards_comp2.data[c] = -1
                comp = cards_comp2.cards_form('Компьютер2')
                count_comp_2 += 1

        if count_comp_1== 15:
            print('Победа Компа 1')
        elif count_comp_2 == 15:
            print('Победа Компа 2 ')
        else:
            break
    elif num == '3':
        player = cards_player.cards()
        print('                                       ')
        player2 = cards_player2.cards()
        count = 90
        numbers = []
        one = 0
        count_player = 0
        count_player2 = 0
        while len(numbers) != 90:
            one += 1
            numbers.append(one)
        while count_player2 != 15 and count_player != 15:
            player = cards_player.cards_form('Игрок1')
            print('                                       ')
            player2 = cards_player2.cards_form('Игрок2')
            print(player)
            print(player2)
            count = count - 1
            qwe = random.choice(numbers)
            numbers.remove(qwe)

            print(f'Номер бочонка {qwe}, (осталось: {count}) ')

            otvet = input('1 Игрок, Удалить число? + / - ')

            if otvet == '+':
                if qwe in cards_player.data:
                    c = cards_player.data.index(qwe)
                    cards_player.data[c] = -1
                    player = cards_player.cards_form('Игрок1')
                    count_player += 1

                else:
                    print('You Lose, Win 2 player ')
                    break
            elif otvet == '-':
                if qwe in cards_player.data:
                    print('You Lose, Win 2 player')
                    break
            else:
                print('Ты испортил бланк  и проиграл ')
                break

            otvet = input('2 Игрок, Удалить число? + / - ')

            if otvet == '+':
                if qwe in cards_player2.data:
                    c = cards_player2.data.index(qwe)
                    cards_player2.data[c] = -1
                    player = cards_player2.cards_form('Игрок2')
                    count_player2 += 1

                else:
                    print('You Lose, Win 1 player  ')
                    break
            elif otvet == '-':
                if qwe in cards_player2.data:
                    print('You Lose, Win 1 player')
                    break
            else:
                print('Ты испортил бланк  и проиграл ')
                break
        if count_player == 15:
            print('Победа Игрока 1 ')
        elif cards_player2 == 15:
            print('Победа Игрока 2 ')
        else:
            break
    elif num == '4':
        break