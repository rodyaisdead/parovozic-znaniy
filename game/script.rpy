
# Определение персонажей игры.
define cond = Character('Кондуктор', color="#970026")
define znach = 10 

# Создание кнопок для конечного меню
screen butt:
    imagebutton:
        xalign 0.665
        yalign 0.86
        idle "images/as.png"
        hover "images/ass.png"
        action MainMenu(confirm=True) 

screen butyt:

    imagebutton:
        xalign 0.93
        yalign 0.89
        idle "images/kek.png"
        hover "images/keek.png"
        action Quit(confirm=True)
        
#окно с выводом перемнной 1
screen info_panel:
    frame:
        padding(100,100)
        xalign 0.89
        yalign 0.2
        
        vbox:
            text "{size=+10}{color=#000000}Итоговый результатат:{/color}{/size}" xalign 0.5
            text "{size=+10}{color=#000000}[znach]{/color}" xalign 0.5
 
 
#окно с выводом перемнной 2
screen info_rab:
    frame:
        padding(100,100)
        xalign 0.98
        yalign 0.4
        
        vbox:
            text "{size=+10}{color=#000000}Рекомендции для работодателя:{/color}{/size}"
            if znach >= -90:
                text "{color=#000000}Сотрудник прошел тест успешно.{/color}" 
            #elif znach >= 4:
                #text "{color=#000000}Сотрудник прошел тест успешно.{/color}"
            #elif (znach < 4) and (znach > 1):
                #text "{color=#000000}Сотрудник прошел тест успешно, однако стоит повторить материал.{/color}"
            #else:
                #text "{color=#000000}Сотрудник не прошел тест. Рекомендуем пройти экзамен заново.{/color}"

init:
    $ right2 = Position(xalign = 0.7, yalign = 1.1)
    
label start:
    scene poezd
    with fade
    
    #voice "sound/mainmenu.OGG"
    
    show conductor3

    cond "Добро пожаловать в виртуальный тренажёр Поезд Знаний"
    hide conductor3
    
    show conductor3 at right2
    with dissolve

    cond "Удачного прохождения тестирования!"
    
    hide conductor3
    jump test1
        
    return 
 
#Вопрос 1 
label test1:

    scene poezd_pj1
    with dissolve
    
    scene poezd_pj2
    with dissolve
    
    
    "ID-1" "Вопрос 1. {w}При обнаружении пожара на локомотиве запрещается остановка:"
    
    menu:
        "При обнаружении пожара на локомотиве запрещается остановка:"
        
        "На ж/д мостах, в тоннелях, под мостами, вблизи трансформаторов и тяговых подстанций.":
            $ znach = znach + 1
            jump per
        
        "На перегоне, вблизи сгораемых строений.":
            $ znach = znach - 1
            jump p1
        
        "На переезде, в тоннеле.":
            $ znach = znach - 1
            jump p1
            
        "Пропустить вопрос.":
            $ znach = znach - 2
            jump test2
    return
       
#Подсказка 1
label p1:

    scene poezd_pj2

    show conductor3
    with fade
    
    voice "sound/ps1.OGG"
    cond "Ваш ответ неверный. {w}Подсказка: Остановка около объектов, которые могут получить значительный ущерб от огня. {w}Попробуйте еще раз."
    
    jump test1
    
    return
       
label per:

    scene perehod
    with dissolve
    
    cond "Поезд едет дальше."
    jump test2
    
    return
 
#Вопрос 2   
label test2:

    scene poezd_m1
    with dissolve
    
    scene poezd_m2
    with dissolve
    
    "ID-2" "Вопрос 2. {w}Порядок действий в случае угрозы наезда на автотранспортное средство, механизмы, работников дистанции пути:"
    
    menu:
        "Порядок действий в случае угрозы наезда на автотранспортное средство, механизмы, работников дистанции пути:"
        
        "Подавать оповестительный сигнал. В случае возникновения угрозы наезда – применить экстренное торможение.":
            $ znach = znach - 1
            jump p2
        
        "Подавать оповестительный сигнал, применить экстренное торможение только в случае наезда.":
            $ znach = znach - 1
            jump p2
        
        "Подавать оповестительный сигнал. В случае возникновения угрозы наезда – применить служебное торможение.":
            jump per2
            
        "Пропустить вопрос.":
            $ znach = znach - 2
            jump test3
    
    return
    
#Подсказка 2
label p2:

    scene poezd_m2
    
    show conductor3 at right2
    with fade
    
    voice "sound/ps2.MP3"
    cond "Ваш ответ неверный. {w}Подсказка: В определенном случае применяем торможение. {w}Попробуйте еще раз."
    jump test2
    
    return 
    
label per2:

    scene perehod
    with dissolve
    
    cond "Поезд едет дальше."
    jump test3
    
    return
    
#Вопрос 3 
label test3:

    scene poezd_op1
    with dissolve
    
    scene poezd_op2
    with dissolve
    
    scene poezd_op3
    with dissolve
    
    scene poezd_op2
    with dissolve
    
    scene poezd_op3
    with dissolve
    
    
    "ID-3" "Вопрос 3. {w}После получения информации о наличии в составе неисправности, угрожающей безопасности движения, машинисту запрещается:"
    
    menu:
        "После получения информации о наличии в составе неисправности, угрожающей безопасности движения, машинисту запрещается:"
        
        "Выключать приоры безопасности.":
            $ znach = znach + 1
            jump p3
        
        "Продолжать движение.":
            jump per3
        
        "Применять экстренное торможение.":
            $ znach = znach - 1
            jump p3
            
        "Пропустить вопрос.":
            $ znach = znach - 2
            jump test4
    return
 
#Подсказка 3
label p3:

    scene poezd_op3
    with dissolve
    
    show conductor3 at right2
    with fade
    
    voice "sound/ps3.MP3"
    cond "Ваш ответ неверный. {w}Подсказка: Движение состава. {w}Попробуйте еще раз."
    jump test3
    
    return 
    
label per3:

    scene perehod
    with dissolve
    
    cond "Поезд едет дальше."
    jump test4
    
    return
    
#Вопрос 4 
label test4:

    scene poezd_top1
    with dissolve
    
    scene poezd_top2
    with dissolve
    
    scene poezd_top3
    with dissolve
    
    
    
    "ID-4" "Вопрос 4. {w}Для экономии топлива необходимо:"
    
    menu:
        "Для экономии топлива необходимо:"
        
        "Вести вопросы при максимальных точках на тяговом двигателе.":
            $ znach = znach + 1
            jump p4
        
        "Учитывать поездную обстановку.":
            jump per4
        
        "При движении на подъем применять ослабление поля.":
            $ znach = znach - 1
            jump p4
            
        "Пропустить вопрос.":
            $ znach = znach - 2
            jump test5
    return 
    
#Подсказка 4   
label p4:

    scene poezd_top2
    with dissolve
    
    show conductor3 
    with fade
    
    voice "sound/ps4.MP3"
    cond "Ваш ответ неверный. {w}Подсказка: Следить за ситуацией. {w}Попробуйте еще раз."
    jump test4
    
    return 
    
label per4:

    scene perehod
    with dissolve
    
    cond "Поезд едет дальше."
    jump test5
    
    return
    
#Вопрос 5 
label test5:

    scene poezd_it1
    with dissolve
    
    scene poezd_it2
    with dissolve
    
    scene poezd_it3
    with dissolve
    
    scene poezd_it2
    with dissolve
    
    scene poezd_it3
    with dissolve
    
    scene poezd_it4
    with dissolve
    
    scene poezd_it5
    with dissolve
    
    
    
    "ID-5" "Вопрос 5. {w}Порядок проверки сцепления локомотива с первым вагоном в пассажирском поезде:"
    
    menu:
        "Порядок проверки сцепления локомотива с первым вагоном в пассажирском поезде:"
        
        "Кратковременным движением от состава. Если вагоны закреплены механическим упором, то по сигнальным отросткам автосцепок.":
            $ znach = znach + 1
            jump p5
        
        "По сигнальным отросткам автосцепок.":
            jump itog
        
        "По сигнальным отросткам автосцепок или специальным шаблонам, находящегося у вагонника.":
            $ znach = znach - 1
            jump p5
            
        "Пропустить вопрос.":
            $ znach = znach - 2
            jump itog
    return 
    
#Подсказка 5   
label p5:

    scene poezd_it1
    with dissolve
    
    show conductor3 
    with fade
    
    voice "sound/ps5.MP3"
    cond "Ваш ответ неверный. {w}Подсказка: По отросткам. {w}Попробуйте еще раз."
    jump test5
    
    return 
    

label itog:
    scene bg
    
    show screen butt
    show screen butyt
    show screen info_rab
    show screen info_panel

    
    show conductor3 at left
    cond "Результаты теста"
   
    return 