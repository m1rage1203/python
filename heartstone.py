import time
import random

cards = [
    {
        'id': 1,
        'name': '🔮 Маг🔮',   
        'damage': 1,
        'cost': 2,
    },
    {
        'id': 2,
        'name': '🏹 Лучник 🏹',   
        'damage': 5,
        'cost': 4,
    },
    {
        'id': 3,
        'name': '🪓 Варвар 🪓',  
        'damage': 8,
        'cost': 6,
    }, 
]

new_cards = [
    
    {
        'id': 4,
        'name': '👸 Валькирия 👸',   
        'damage': 1,
        'cost': 2,
    },
    {
        'id': 5,
        'name': '🤖 Пекка 🤖',  
        'damage': 5,
        'cost': 4,
    },
    {
        'id': 6,
        'name': '⚔️ Меганайт ⚔️',  
        'damage': 8,
        'cost': 6,
    },
    
]

boss = [
    {
        'name': 'Робот',
        'hp': 20,
        'image': '''  ╔═══════╗
  ║ O ╫ O ║
  ║  /¯\  ║
  ╚═╦---╦═╝
    ║   ║
    ▀░░░▀'''
    },
    {
        'name': 'Мегатрон',
        'hp': 30,
        'image': '''       ╔═══════╗
     ██║ @   @ ║██
    ███║   ▴   ║███
   ████╚═╦═╦═╦═╝████
  ██┌───┐║ ║ ║┌───┐██
 ██│╭───╯║ ║ ║╰───╮│██
██││╰────║ ║ ║────╯││██
══╧╧═══════════════╧╧══
   ██ ██   ██ ██   ██'''
    },
    {
        'name': 'Рустам',
        'hp': 40,
        'image': '''
        ╔══════════╗
     ▓▓▓║ @▓▓▓▓▓@ ║▓▓▓
    ▓▓▓▓║   ▴▓▓▴   ║▓▓▓▓
   ▓▓▓▓▓╚═╦═╦▓▓╦═╦═╝▓▓▓▓▓
  ██┌───┐▓║▓▓▓▓▓║▓┌───┐██
 ██│╭───╯▓║▓▓▓▓▓║▓╰───╮│██
██││╰────▓║▓▓▓▓▓║▓────╯││██
══╧╧═════▓▓▓▓▓▓▓▓▓═════╧╧══
   ██▓▓██   ██▓▓██   ██▓▓██
    ▓▓▓▓     ▓▓▓▓     ▓▓▓▓
     ▓▓       ▓▓       ▓▓
    ╦╦╦      ╦╦╦      ╦╦╦
   ║║║║     ║║║║     ║║║║
  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓
 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'''
    }
]


potions = [
    {
        'id': 1,
        'name': '🧪 Усиление 🧪',
        'count': 3,
    },
    {
        'id': 2,
        'name': '🩸 Восстановление 🩸' ,
        'count': 3,
    }
    
]


def start():
    timeText('Вы проснулись в неизвестной вам лочуге... Голова ужасно болит, и слышен легкий звон в ушах. \n', 0.06)
    timeText('Перед вами приоткрытая дверь, и сквозь нее просачивается яркий свет. Вы слышите подозрительные звуки. \n', 0.06)
    print('''
 ______
|      |
|      |
|      |
|     o|
|      |
|______|''')
    open_door = input('Открыть дверь? \n (ДА\НЕТ)')
    if open_door.lower() == 'да':
        level_1(cards, boss[0])
    else:
        timeText('Вы не стали открывать загадочную дверь в Московский приборостроительный техникум. Вы не решились на это уникальное испытание! \n', 0.06)
        return
def finish():
    
    restart = input('Начать заново? ')
    if restart == 'да':
        start()
    else:
        return

def timeText(text, settime):
    new_text = ''
    for i in text:
        time.sleep(settime)
        new_text = new_text + i
        print(i, end="",  flush=0)
    

#level 1
                                                                          
def level_1(cards, selectBoss):
    
    my_hp = 10
    start_mana = 15
    timeText('ДОБРО ПОЖАЛОВАТЬ НА ПЕРВЫЙ УРОВЕНЬ \n', 0.06)
    timeText(f"Босс: {selectBoss['name']} \n", 0.05)
    
    print(selectBoss['image'])
    while my_hp > 0 and selectBoss['hp'] > 0 and start_mana > 0:
        print('🔵 Доступная мана 🔵', start_mana)
        print('🃏 Доступные карты 🃏')
        for i in cards:
            print(i['name'], '- выбор:', i['id'], 'Цена:', i['cost'])
        can_play = False    
        for card in cards:
            if card['cost'] < start_mana:
                can_play = True
                break
        if can_play == False:
            timeText('❌ НЕ ХВАТАЕТ МАНЫ НА ЛЮБУЮ КАРТУ! \n' , 0.05)
            timeText('💀 ВЫ ПРОИГРАЛИ 💀 \n', 0.05)
            break
        selected_card = int(input('Выберите карту '))  
        
        
        for card in cards:
            
            if card['id'] == selected_card:
                if card['cost'] > start_mana:
                    timeText("Не хватает МАНЫ!!!!!!\n", 0.05)
                    continue
                timeText(f"Выбор: {card['name']} \n", 0.05)
                selectBoss['hp'] -= card['damage']
                timeText(f"Вы наносите {card['damage']} урона \n", 0.05)
                timeText(f"💀 У босса осталось {selectBoss['hp']} HP 💀 \n", 0.05)
                if selectBoss['hp'] <= 0:
                    print('🏆 ПОБЕДА 🏆')
                    new_card = random.randint(0, 2)
                    cards.append(new_cards[new_card])
                    new_cards.pop(new_card)
                    if new_card == 2:
                        timeText('🔥ЛЕГЕНДАРНАЯ КАРТА 🔥 \n', 0.05)
                        print(cards[-1]['name'])
                    level_2(cards, boss[1])
                    
                    break
                start_mana -= card['cost'] 
                timeText(f"🔵 У вас осталось {start_mana} маны 🔵 \n", 0.05)
                timeText("...\n", 0.5)
                timeText(f'🗡️  БОСС АТАКУЕТ!!!🗡️ \n', 0.05)
                boss_damage = random.randint(1, 4)
                my_hp -= boss_damage
                timeText(f"🗡️  Он наносит {boss_damage} урона 🗡️ \n", 0.05) 
                timeText(f"💖 У вас осталось {my_hp} HP 💖 \n", 0.05)
                start_mana += 1
                timeText('+ 1 маны за ход \n', 0.05)
                print('--------')
                if start_mana <= 0 or my_hp <= 0:
                    print('💀 ВЫ ПРОИГРАЛИ 💀')   

#level 2
def level_2(cards, boss):
    my_hp = 15
    start_mana = 20
    
    
    timeText('ОТКРЫТ ВТОРОЙ УРОВЕНЬ \n', 0.06)
    timeText(f"Босс: {boss['name']} \n", 0.05)
    
    print(boss['image'])
    
    while my_hp > 0 and boss['hp'] > 0 and start_mana > 0:
        print('🔵 Доступная мана 🔵', start_mana)
        print('🃏 Доступные карты 🃏')
        for i in cards:
            print(i['name'], '- выбор:', i['id'], 'Цена:', i['cost'])
        can_play = False    
        for card in cards:
            if card['cost'] < start_mana:
                can_play = True
                break
        if can_play == False:
            timeText('❌ НЕ ХВАТАЕТ МАНЫ НА ЛЮБУЮ КАРТУ! \n' , 0.05)
            timeText('💀 ВЫ ПРОИГРАЛИ 💀 /')
            break
        selected_card = int(input('Выберите карту '))  
        
        
        for card in cards:
            if card['id'] == selected_card:
                if card['cost'] > start_mana:
                    timeText("Не хватает МАНЫ!!!!!!\n", 0.05)
                    continue
                timeText(f"Выбор: {card['name']} \n", 0.1)
                boss['hp'] -= card['damage']
                timeText(f"Вы наносите {card['damage']} урона \n", 0.05)
                timeText(f"💀 У босса осталось {boss['hp']} HP 💀 \n", 0.05)
                if boss['hp'] <= 0:
                    print('🏆 ПОБЕДА 🏆')
                    
                    new_card = random.randint(0, 2)
                    cards.append(new_cards[new_card])
                    new_cards.pop(new_card)
                    level_3(cards, boss[2])
                    
                    break
                start_mana -= card['cost'] 
                timeText(f"🔵 У вас осталось {start_mana} маны 🔵 \n", 0.05)
                timeText("...\n", 0.5)
            
                spells = random.randint(1, 2)
                if spells == 1:
                    timeText(f'🗡️  БОСС АТАКУЕТ!!!🗡️ \n', 0.05)
                    boss_damage = random.randint(1, 4)
                    my_hp -= boss_damage
                    timeText(f"🗡️  Он наносит {boss_damage} урона 🗡️ \n", 0.05) 
                    timeText(f"💖 У вас осталось {my_hp} HP 💖 \n", 0.05)
                else:
                    timeText(f'🩹 БОСС ВОССТАНАВЛИВАЕТ ЗДОРОВЬЕ!!🩹 \n', 0.05)
                    boss['hp'] += 2
                    timeText(f"💀 У босса стало {boss['hp']} HP 💀 \n", 0.05)
                start_mana += 1
                timeText('+ 1 маны за ход \n', 0.05)
                print('--------')
                if start_mana <= 0 or my_hp <= 0:
                    print('💀 ВЫ ПРОИГРАЛИ 💀')
                

#level 3
def level_3(cards, boss):
    my_hp = 20
    start_mana = 30
    
    timeText('ОТКРЫТ ТРЕТИЙ УРОВЕНЬ \n', 0.06)
    timeText(f"Босс: {boss['name']} \n", 0.05)
    
    print(boss['image'])
    move = 1
    
    while my_hp > 0 and boss['hp'] > 0 and start_mana > 0:
        deleted_potions = []
        for potion in potions:
            if potion['count'] == 0:
                deleted_potions.append(potion)
        for potion in deleted_potions:
            potions.remove(potion)
            
        print(f'---- Ход {move} ---- \n' )
        
        print(' 💖 Ваше здоровье 💖', my_hp)
        
        print(' 🔵 Доступная мана 🔵', start_mana)
        
        print(' 🃏 Доступные карты 🃏')
        for i in cards:
            print(i['name'], '- выбор:', i['id'], 'Цена:', i['cost'])
            
        print('\n 🃏 Доступные зелья 🃏')
        if potions:  
            for i in potions:
                print(i['name'])
        else:
            print("❌ Зелья закончились")
            
        can_play = False    
        
        for card in cards:
            if card['cost'] <= start_mana:
                can_play = True
                break
        if can_play == False:
            timeText('❌ НЕ ХВАТАЕТ МАНЫ НА ЛЮБУЮ КАРТУ! \n' , 0.05)
            timeText('💀 ВЫ ПРОИГРАЛИ 💀 ' , 0.05)
            break
        is_potion = input('Использовать зелье (ДА/НЕТ) ')
        
        selected_potion = None 
            
        if is_potion.lower() == 'да':
            if potions:
                while True:
                    
                    for potion in potions:
                        print(potion["name"], '- выбор:', potion['id'])
                    selected_potions = input('Выберите зелье: ')
        
                    for potion in potions:
                        if str(potion['id']) == selected_potions:
                            selected_potion = potion
                            break
                    if selected_potion is None:
                        timeText("❌ Такого зелья не существует!\n", 0.05)
                        continue
                    elif selected_potion['count'] == 0:
                        timeText("❌ Это зелье закончилось!\n", 0.05)
                        selected_potion = None
                        continue
                    else:
                        timeText(f"✅ Выбрано зелье: {selected_potion['name']}\n", 0.05)
                        break
            else:
                timeText("❌ У вас нет зелий для использования!\n", 0.05)       
                
                
        selected_card = int(input('Выберите карту '))
               
        for card in cards:
            if card['id'] == selected_card:
                if card['cost'] > start_mana:
                    timeText("Не хватает МАНЫ!!!!!!\n", 0.05)
                    continue
                
                timeText(f"Выбор: {card['name']} \n", 0.1)
                
                damage = card['damage']
                
                if is_potion.lower() == 'да':
                    
                    if selected_potion and selected_potion['count'] > 0:
                        if selected_potions == '1':
                            damage += 3
                            selected_potion['count'] -= 1 
                            timeText('🗡️ Урон вашей выбранной карты увеличен на 3! 🗡️ \n' , 0.05)
                        elif selected_potions == '2':
                            my_hp += 2
                            selected_potion['count'] -= 1 
                            timeText('💖 Вы увеличили свое HP на 2! 💖 \n' , 0.05)
                            timeText(f"💖 У вас стало {my_hp} HP 💖 \n", 0.05)
                              
                    else: 
                        timeText("❌ Зелье закончилось!\n", 0.05) 
                boss['hp'] -= damage
                timeText(f"Вы наносите {card['damage']} урона \n", 0.05)
                timeText(f"💀 У босса осталось {boss['hp']} HP 💀 \n", 0.05)
                if boss['hp'] <= 0:
                    print('🏆 ПОБЕДА 🏆')
                    finish()
                    cards.append(new_cards[0])

                    break
                start_mana -= card['cost'] 
                timeText(f"🔵 У вас осталось {start_mana} маны 🔵 \n", 0.05)
                timeText("...\n", 0.5)
                available = len(cards) > 1
                spells = random.randint(1, 3)
                if spells == 1:  
                    timeText(f'🗡️  БОСС АТАКУЕТ!!!🗡️ \n', 0.05)
                    boss_damage = random.randint(1, 4)
                    my_hp -= boss_damage
                    timeText(f"🗡️  Он наносит {boss_damage} урона 🗡️ \n", 0.05)
                    timeText(f"💖 У вас осталось {my_hp} HP 💖 \n", 0.05)
                elif spells == 2 and available:
                    delete_card = random.randint(0,1)
                    cards.pop(delete_card)
                    timeText(f"☠  Босс принес в жертву вашу карту под номером... {delete_card + 1} ☠  \n", 0.05)
                else:
                    timeText(f'🩹 БОСС ВОССТАНАВЛИВАЕТ ЗДОРОВЬЕ!!🩹 \n', 0.05)
                    boss['hp'] += 2
                    timeText(f"💀 У босса стало {boss['hp']} HP 💀 \n", 0.05)
                start_mana += 1
                timeText('+ 1 маны за ход \n', 0.05)
                print('-------- \n')
                move += 1
                if start_mana <= 0 or my_hp <= 0:
                    print('💀 ВЫ ПРОИГРАЛИ 💀')
                               
start()






