

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))




        elif event == "slow_done" or event == "end":
            renpy.sound.stop()



define m = Character(" Мия", callback=type_sound, color="#ffffff")
define r = Character('Рюити',  callback=type_sound, color="#ffffff")
define no = Character ('  ???', callback=type_sound, color="#ffffff")
define e = Character ('Яхари', callback=type_sound, color="#ffffff")
define j = Character("Судья", callback=type_sound, color="#ffffff")
define ma = Character("Мадзо", callback=type_sound, color="#ffffff")
define o = Character("Онуву", callback=type_sound, color="#ffffff")
define sounds = ['audio/A1.ogg', 'audio/A2.ogg']
define audio.So_it_Begins = "audio/So it Begins.mp3"
define audio.Court_is_Now_in_Session = "audio/Court is Now in Session.mp3"
define audio.Cross_Examination = "audio/Cross Examination.mp3"
define audio.The_Truth_Revealed = "audio/The Truth Revealed.mp3"
define audio.Type1 = "audio/Type1.mp3"
define audio.whack = "audio/whack.mp3"
define audio.courtroomb = "audio/courtroomb.wav"
define audio.slamb = "audio/slamb.wav"
define audio.selectjingle = "audio/selectjingle.wav"
define audio.deskslam = "audio/deskslam.wav"
define audio.objection = "audio/objection.wav"
define audio.payne = "audio/payne_objection.wav"
define audio.phoenix = "audio/phoenix_objection.wav"
define audio.hold_it = "audio/hold_it.wav"
default evidence1 = False
default evidence2 = False
default evidence3 = False
default der = False
default der1 = False
default der2 = False
default der3 = False
default der4 = False
default der5 = False
default der6 = False
default der7 = False
default der8 = False
default der9 = 0
default right = 0
default right2 = 0
default right3 = 0
default der21 = False
default der22 = False
default der23 = False
default der24 = False
default error1 = 0


# Игра начинается здесь:
label start:


    scene black with fade
    pause (1)
    $ renpy.movie_cutscene('videos/1delo.ogv')
    scene black
    play sound Type1
    "{cps=14}{space=200} {color=#00FF00} 3 августа, 9:47 \n {space=195} Окружной суд \n {space=195}Зал ожидания №2{/color}{/cps}"

    scene bg room
    play music So_it_Begins
    show screen materiali

    r "{color=#87CEFA}(Ух, как же я волнуюсь!){/color}"

    m "Рю!"
    show mia blink with Dissolve (1.0)
    r "А, з-здрасте, шеф."
    m "Фух, чудом не опоздала."
    show mia blink1
    m "Ну, ты как? Всё-таки это твое первое дело."
    r "Т-так сильно я нервничал лишь во время своего школьного суда."
    show mia blink2
    m "Но ведь это, наверное, было давно?"
    show mia blink
    r "Ну да. Э-э-э, шеф? Извините, что отнимаю у вас сегодня время."
    m "Ай, не бери в голову. Как-никак сегодня у моего ученика важный день."
    show mia blink1
    m "Кстати, Рю, должна заметить, ты меня поразил!"
    m "Мало кто вот так сразу берётся за клиентов, обвиняемых в убийстве."
    m "Это многое говорит о тебе и твоём отношении к клиентам."
    r "А, д-да."
    r "Вообще-то я перед ним в долгу."
    show mia blink2
    m "В долгу?"
    m "Так ты, выходит, знаком с подсудимым?"
    r "Да. Как ни странно, но своей профессией я отчасти обязан ему."
    show mia blink1
    m "Что же, для меня это новость!"
    show mia blink
    r "Мне надо постараться его выручить."
    r "Я... очень хочу ему помочь. \nЯ реально перед ним в долгу."
    stop music
    play sound whack
    show mia blink2
    no "{color=#00FF00}(Это конец!){/color}"
    no "{color=#00FF00}(Конец всего, конец моей жизни!){/color}"
    m "А это, часом, не твой клиент там кричит?"
    show mia blink
    r "Угу, он самый."
    no "{color=#00FF00}(Смерть! Отчаяние! А-а-ах!){/color}"
    show mia blink2
    no "{color=#00FF00}(Все, я решил, пора умирать!){/color}"
    m "Такое впечатление, что он хочет... умереть."
    show mia blink1
    r "Э-э-э, ага. \n *вздыхает*"
    hide mia with dissolve
    play music So_it_Begins
    show etto crying with dissolve
    e "Рю!"
    r "Привет, Этто."
    show etto sweating
    e "Друг, вина полностью лежит на мне! Так им и скажи: это всё он, это он виноват!"
    e "Пусть мне вынесут смертный приговор! Я не боюсь умирать!"
    r "Чего?! Этто, что случилось?"
    show etto crying
    e "Ай, всему конец. Мне... уже нет смысла жить!"
    e "Я не могу без неё! Не могу!"
    e "Кто... кто отнял её у меня, Рю? \nКто этот гад?!"
    e "А-а-а, Рю-ю, ну скажи-и-и! \nКто лишил меня любимой?"
    r "{color=#87CEFA}(Хм, кто виноват в смерти твоей девушки?){/color}"
    r "{color=#87CEFA}(В газетах пишут, что это {/color}{color=#FF7F50}твоих рук дело{/color}{color=#87CEFA}.){/color}"
    stop music
    scene bg black with fade
    r "Меня зовут Рюити Хорасё. \nПрошло три месяца с тех пор как я стал адвокатом."
    r "Сегодня я впервые буду представлять своего клиента."
    r "Моё первое дело оказалось достаточно простым."
    window hide
    show girl blooding
    pause 2
    r "Молодую девушку убили в собственной квартире."
    r "Арестованным оказался её незадачливый ухажёр."
    hide girl blooding with dissolve
    show etto sweating
    r "Этто Яхари. Мой лучший школьный друг."
    r "Он вечно попадает во всякие неприятности."
    show etto crying
    r "Но я однозначно могу сказать: обычно он ни в чём не виноват. Ему просто хронически не везёт."
    hide etto with dissolve
    r "Но кому, как не мне, известно, что в душе он хороший человек."
    r "Кроме того, я перед ним в долгу. Поэтому я и взялся за это дело - чтобы оправдать его."
    r "Вот так всё и началось."
    window hide
    pause 2
    play sound Type1
    "{cps=14}{space=200} {color=#00FF00} 3 августа, 10:00 \n {space=195} Окружной суд \n {space=195}Зал ожидания №2{/color}{/cps}"
    show courtroom begin
    play sound courtroomb
    pause 2.5
    show slam b
    play sound slamb
    pause 1
    play music Court_is_Now_in_Session
    show judge blink

    j "Суд приступает к рассмотрению дела гражданина Этто Яхари."
    show mudzo neutral
    ma "Сторона обвинения готова, Ваша честь."
    hide mudzo neutral
    show animatik:
        xalign 1.0
        linear 0.4 xalign 0.0
    pause 0.5
    hide animatik
    show phoenix blink
    r "Э-эм, с-сторона защиты готова, Ваша честь."
    hide phoenix blink
    show judge close1
    j "Кхе-кхе."
    show judge blink1
    j "Господин Хорасё, если не ошибаюсь, это ваше первое судебное заседание, верно?"
    hide judge blink1
    show phoenix blink
    r "Д-да, Ваша честь. \nЯ, э-эм, немного волнуюсь."
    hide phoenix blink
    show judge blink1
    j "От ваших действий во время прений будет зависеть судьба вашего клиента."
    j "Обвинения в убийстве просто так не выдвигаются."
    show judge blink
    j "Надеюсь, что вы справитесь с волнением."
    hide judge blink
    show phoenix blink
    r "С-спасибо, Ваша честь."
    hide phoenix blink
    show judge blink1
    j "..."
    j "Хорошо, но перед тем как перейти к слушаниям, нам нужно удостовериться в вашей готовности."
    hide judge blink1
    show phoenix blink
    r "К-конечно."
    show phoenix sweating
    r "{color=#87CEFA}(От неожиданности меня аж в пот бросило. И коленки затряслись.){/color}"
    hide phoenix sweating
    show judge blink1
    j "Я вам задам несколько простых вопросов."
    j "Будьте добры, назовите {color=#FF7F50}имя подсудимого{/color} в этом деле."
    jump question1

label question1:

    menu:
        "Рюити Хорасё":
            show phoenix thinking
            r "Хм, подсудимый... это я, да?"
            hide phoenix thinking
            show mia blink3
            m "Рю, что с тобой случилось?! \nТы заболел? Соберись!"
            m "Подсудимый - это человек, которому предъявлены обвинения!"
            m "Ты его адвокат!"
            r "Э-эм, разве? А, ну да, конечно! Ха-ха..."
            m "Это не смешно."
            m "Тебе точно выдали лицензию адвоката?"
            hide mia blink3
            show judge blink
            j "Извините, я не расслышал ваш ответ. Ещё раз задам вопрос."
            j "Будьте добры, назовите {color=#FF7F50}имя подсудимого{/color} в этом деле."
            jump question1
        "Этто Яхари":
            show phoenix blink
            r "Подсудимый? Это... Этто Яхари, Ваша честь."
        "Мия Асато":
            show phoenix blink
            r "Э-эм, подсудимый? \nЭто, э-э-э... Мия Асато?"
            scene bg black
            show mia blink3
            m "Ты притворяешься? Знаешь, мне уже пора... пора домой. Я... ожидаю важный звонок."
            r "Да чего вы, шеф, вам ещё рано уходить."
            m "Рю, подсудимый - это тот, кто находится под судом!"
            m "Сейчас судят твоего клиента! \nЭто же элементарно!"
            r "{color=#87CEFA}(Вот это я дал маху! \nНадо успокоиться!){/color}"
            hide mia blink3
            show judge blink
            j "Извините, я тут отвлекся. Еще раз задам вопрос."
            j "Будьте добры, назовите {color=#FF7F50}имя подсудимого{/color} в этом деле."
            jump question1

    hide phoenix blink
    show judge blink
    j "Верно."
    j "Вы, главное, не волнуйтесь, и у вас всё получится."
    j "Следующий вопрос."
    hide judge blink
    show judge blink1
    j "Сегодня суд рассматривает дело об убийстве. Назовите {color=#FF7F50}имя потерпевшей{/color}."
    hide judge blink1
    show phoenix blink
    r "{color=#87CEFA}(Фух, с этим порядок: я эти несчастные материалы уже до дыр зачитал.){/color}"
    show phoenix sweating
    r "{color=#87CEFA}(Это... стоп... блин!){/color}"
    r "{color=#87CEFA}(Нет... неужели... я забыл! Вообще ничего не лезет в голову.){/color}"
    hide phoenix
    show mia blink3
    m "Рю, ты точно уверен, что справишься?!"
    m "Как ты умудрился забыть имя потерпевшей?!"
    r "А, потерпевшей! К-конечно же я знаю имя потерпевшей!"
    r "Я всего-навесго забыл его. Капельку."
    m "Кажется, у меня разболелась голова."
    m "Вся важная информация содержится в {color=#FF7F50}материалах дела{/color}."
    m "Ты можешь просмотреть их в любой момент, достаточно нажать на кнопку {color=#FF7F50}Материалы{/color}."
    m "Старайся почаще их проверять. А теперь найди в них имя потерпевшей, умоляю тебя."
    hide mia blink3
    show judge blink1
    j "Назовите {color=#FF7F50}имя потерпевшей{/color}."
    jump question2

label question2:

    menu:
        "Мия Асато":
            show phoenix thinking
            r "Мия Асато?"
            hide phoenix thinking
            show mia blink3
            m "Чего?! Как яя могу быть жертвой преступления?!"
            r "Ой, точно, извини! Я, это, твоё имя первым взбрело мне в голову, поэтому..."
            m "Нажми на кнопку {color=#FF7F50}Материалы{/color}! Всегда обращайся к ним в случае затруднений."
            hide mia blink3
            show judge blink
            j "Ещё раз вас спрашиваю."
            j "Назовите {color=#FF7F50}имя потерпевшей{/color}."
            jump question2
        "Юма Ранэти":
            show phoenix thinking
            r "Это вроде госпожа Ранэти? Госпожа Юма Ранэти?"
            hide phoenix thinking
            show judge blink1
            j "Господин Хорасё, потерпевшая была жертвой преступления, а не жертвой вашего юмора."
            hide judge blink1
            show mia blink3
            m "Рю, если ты чего-то не помнишь, нажми на кнопку {color=#FF7F50}Материалы{/color} и просмотри их."
            m "Ошибка, допущенная во время суда, может дорого обойтись твоему клиенту."
            hide mia blink3
            show judge blink
            j "Ещё раз вас спрашиваю."
            j "Назовите {color=#FF7F50}имя потерпевшей{/color}."
            jump question2
        "Юна Такуми":
            show phoenix blink
            r "Хм, потерпевшая - Юна Такуми."
            hide phoenix blink
            show judge blink
            j "Верно."

    j "Что ж, вы ответили на все мои вопросы. Думаю, можно приступать к слушаниям."
    hide judge blink1
    show phoenix sweating
    r "Д-да. \n{color=#87CEFA}(Вот именно, немного. А не совсем){/color}"
    hide phoenix blink
    show judge blink
    j "Итак."
    j "Хочу обратиться к прокурору. Господин Мадзо?"
    hide judge
    show mudzo neutral
    ma "Да, ваша честь?"
    hide mudzo
    show judge blink1
    j "Из материалов дела ясно, что потерпевшей был нанесён удар тупым предметом."
    j "Объясните, пожалуйста, что это был за предмет?"
    hide judge
    show mudzo neutral
    show mislitel
    ma "Орудием убийства была статуэтка {color=#FF7F50}Мыслитель{/color}."
    ma "Её нашли на полу рядом с телом потерпевшей."
    hide mudzo
    show judge blink1
    j "Хорошо, суд принимает её в качестве улики."
    $evidence1 += True
    play sound selectjingle
    "{color=#87CEFA}Статуэтка приобщена к материалам дела.{/color}"
    hide judge
    show mia blink3
    m "Рю, обязательно обращай внимание на все предъявляемые улики."
    m "Они - твоё единственное орудие во время прений."
    m "Почаще {color=#FF7F50}проверяй материалы дела{/color} с помощью соответствующей кнопки на экране."
    stop music
    show slam b
    play sound slamb
    pause 1
    hide mia blink3
    show judge blink
    j "Господин Мадзо, разрешаю вызвать своего первого свидетеля."
    hide judge
    show mudzo neutral
    ma "Обвинение просит вызвать подсудимого, Этто Яхари, для дачи показаний."
    hide mudzo
    show mia blink3
    r "Э-э-э, шеф, что теперь делать?"
    m "Будь внимателен. Запоминай любые факты, которые могут помочь твоему клиенту."
    m "У тебя будет возможность ответить на обвинения, так что приготовься."
    m "Будем надеяться, что он... не ляпнет ничего лишнего."
    r "{color=#87CEFA}(Ой-ой-ой, Этто очень легко заводится. Плохо дело.){/color}"
    play music Court_is_Now_in_Session
    hide mia
    show mudzo neutral
    ma "Кхе-кхе."
    ma "Этто Яхари, это правда, что незадолго до убийства потерпевшая вас бросила?"
    hide mudzo
    show animatik1:
        xalign 1.0
        linear 0.4 xalign 0.0
    pause 0.5
    hide animatik
    scene bg desk
    show etto smiling
    show desk zorder 100
    e "..."
    show etto crying with hpunch
    e "Эй, аккуратнее на поворотах!"
    e "Не смей так говорить о самой лучшей паре этого столетия!"
    hide etto
    hide desk
    show phoenix sweating with hpunch
    r "{color=#87CEFA}(Чего?! Первый раз об этом слышу.){/color}"
    hide phoenix
    show desk zorder 100
    show etto smiling
    e "Меня никто не бросал! Да, она не брала трубку. И не виделась со мной. Ну и что?"
    show etto sweating
    e "Чего ты суёшь нос куда не следует?!"
    hide desk
    show animatik1:
        xalign 0.0
        linear 0.4 xalign 1.0
    pause 0.5
    hide animatik1
    show mudzo neutral
    ma "Этто Яхари, под {color=#FF7F50}бросили{/color} я подразумевал именно то, что вы нам рассказали."
    ma "Мало того, что она вас бросила окончательно и бесповоротно: у неё были другие мужчины."
    ma "Накануне убийства она как раз вернулась из-за границы с одним из своих кавалеров."
    show animatik1:
        xalign 1.0
        linear 0.4 xalign 0.0
    pause 0.5
    hide animatik1
    scene bg desk
    show desk zorder 100
    show etto crying with hpunch
    e "Стоп, как это с одним из своих кавалеров?!"
    e "Ложь! Наглая ложь! Ни единому слову не верю!"
    hide desk
    show animatik1:
        xalign 0.0
        linear 0.4 xalign 1.0
    pause 0.5
    hide animatik1
    show mudzo neutral
    show pasport_icon
    ma "Ваша честь, это паспорт жертвы."
    ma "Обратите внимание, за день до смерти потерпевшая вернулась из Нью-Йорка."
    $evidence2 += True
    play sound selectjingle
    "{color=#87CEFA}Паспорт приобщен к материалам дела.{/color}"
    hide pasport_icon
    hide mudzo
    show judge blink1
    j "Так-так-так, действительно, она вернулась за день до убийства."
    hide judge
    show desk zorder 100
    show etto crying with hpunch
    e "Не может быть."
    hide desk
    hide etto
    show mudzo neutral
    ma "Жертва работала моделью, но она имела скромные дохода."
    ma "Похоже, что у неё было несколько т. н. {color=#FF7F50}папиков{/color}."
    scene bg desk
    show desk zorder 100
    show etto crying with hpunch
    e "Папиков?"
    hide desk
    show animatik1:
        xalign 0.0
        linear 0.4 xalign 1.0
    pause 0.5
    hide animatik1
    show mudzo neutral
    ma "Да, богатые пожилые мужчины задаривали её деньгами и подарками."
    ma "Именно поэтому она и могла вести такой образ жизни."
    scene bg desk
    show desk zorder 100
    show etto crying
    e "Чего?"
    hide desk
    hide etto
    show mudzo neutral
    ma "Думаю, вполне ясно, кем была госпожа Такуми."
    ma "Скажите, Яхари, {color=#FF7F50}какого вы теперь о ней мнения{/color}?"
    show mia blink3
    m "Рю, лучше ему на этот вопрос не отвечать."
    scene bg desk
    show desk zorder 100
    show etto crying
    r "{color=#87CEFA}(Да, Этто вечно мелет невпопад. Как мне поступить?){/color}"
    jump question3

label question3:
    menu:
        "Подождать и понаблюдать":
            hide desk
            hide etto
            show phoenix thinking
            r "{color=#87CEFA}(Наверное, сейчас лучше не вмешиваться.){/color}"
            hide phoenix
            show mudzo neutral
            ma "Ну, Этто Яхари."
            hide mudzo
            show desk zorder 100
            show etto crying with hpunch
            e "Не может такого быть! Вот... вот блудная стерва, а!"

        "Перебить его":
            hide desk
            hide etto
            play sound deskslam
            show phoenix slaming
            pause 0.7
            r "Мой клиент совершенно не знал, что потерпевшая встречалась с другими мужчинами."
            show phoenix slaming1
            r "Этот вопрос не касается данного дела!"
            hide phoenix
            show mudzo shocked with hpunch
            ma "Ь-ь-ь!"
            hide mudzo
            show desk zorder 100
            show etto crying with hpunch
            e "Рю...ити! Как это так, не относится?!"
            show etto smiling
            e "Вот блудная стерва, а."
            show etto crying with hpunch



    e "Я умру! Меня щас хватит кондрашка!"
    stop music
    hide etto
    hide desk
    show courtroometto
    e "И тогда мы встретимся в загробной жизни..."
    e "И я устрою ей такой разнос!"
    show slam b
    play sound slamb
    pause 1
    hide mia blink3
    show judge blink
    j "Может вернемся к нашим прениям?"
    hide judge
    show mudzo neutral
    ma "Полагаю, теперь всем ясна мотивация подсудимого."
    hide mudzo
    show judge blink
    j "Да, вполне."
    hide judge
    show phoenix sweating
    r "{color=#87CEFA}(Ой-ой-ой, плохи мои дела.){/color}"
    play music Court_is_Now_in_Session
    hide phoenix
    show mudzo neutral
    ma "Следующий вопрос."
    ma "В день убийства вы ходили к потерпевшей, верно?"
    hide mudzo
    scene bg desk
    show desk zorder 100
    show etto crying with hpunch
    e "Ь-ь-ь!"
    hide desk
    hide etto
    show mudzo neutral
    ma "Ну, так ходили или нет?"
    hide mudzo
    show desk zorder 100
    show etto smiling
    e "Заладил же, ну да ну... Баранки гну!"
    hide desk
    hide etto
    show phoenix sweating
    r "{color=#87CEFA}(По лицу вижу - ходил. Как поступить?){/color}"
    jump question4

label question4:
    menu:
        "Пусть ответит честно":
            show phoenix blink
            r "{color=#87CEFA}(Придумал: я ему маякну!){/color}"
            play sound deskslam
            show phoenix slaming
            pause 1.0
            show phoenix thinking
            r "{color=#87CEFA} \n{space=110} (ГОВОРИ{/color}"
            show phoenix sweating
            r "{cps=0}{space=200} {color=#87CEFA}  \n{space=110} (ГОВОРИ{/color}{/cps} {color=#87CEFA} ТОЛЬКО{/color}"
            show phoenix blink
            r "{cps=0}{space=200} {color=#87CEFA}  \n{space=110} (ГОВОРИ ТОЛЬКО{/color}{/cps}{color=#87CEFA} ПРАВДУ){/color}"
            hide phoenix
            show desk zorder 100
            show etto smiling with hpunch
            e "Э-э-э, да! Да, я ходил к ней, верно!"
            hide desk
            hide etto
            play sound courtroomb
            show courtroom e
            pause 2
            show judge blink
            j "Тишина в зале суда!"
            show judge blink1
            j "И, господин Яхари?"
            scene bg desk
            hide judge
            show desk zorder 100
            show etto smiling
            e "Да расслабьтесь вы!"
            e "Её не было дома. \nКороче, я её не застал."
            play sound objection
            play sound payne
            show objection_  zorder 100 with hpunch
            pause 0.7
            hide desk
            hide objection_
            show mudzo neutral
            ma "Ваша честь, подсудимый врёт."
            hide mudzo
            show judge blink
            j "Врёт?"
            hide judge
            show mudzo neutral
            stop music
            ma "Сторона обвинения просит вызвать {color=#FF7F50}свидетеля{/color}. Он докажет, что г-н Яхари врёт."



        "Перебить его":
            show phoenix blink
            r "{color=#87CEFA}(Я ему маякну.){/color}"
            play sound deskslam
            show phoenix slaming
            pause 1.0
            show phoenix thinking
            r "{color=#87CEFA} \n{space=180} (ВРИ{/color}"
            show phoenix sweating
            r "{cps=0}{space=200} {color=#87CEFA}  \n{space=180} (ВРИ{/color}{/cps} {color=#87CEFA} ОБО ВСЁМ){/color}"
            scene bg desk
            show desk zorder 100
            show etto smiling with hpunch
            e "Ну, э-эм, видите ли... я не помню."
            hide etto
            hide desk
            show mudzo neutral
            ma "Как это так, не помните?"
            ma "Хорошо, тогда мы вам напомним."
            hide mudzo
            show phoenix blink
            r "{color=#87CEFA}(Нехорошее у меня предчувствие.){/color}"
            hide phoenix
            show mudzo neutral
            stop music
            ma "У нас есть {color=#FF7F50}свидетель{/color}, который может доказать, что подсудимый посещал квартиру потерпевшей."


    hide mudzo
    show judge blink
    j "Тогда это существенно упрощает нашу задачу. Кто ваш свидетель?"
    hide judge
    show mudzo neutral
    ma "Этот человек обнаружил труп потерпевшей."
    ma "Буквально за минуту до того, как он обнаружил тело..."
    hide mudzo
    show desk zorder 100
    show etto crying with hpunch
    ma "Он видел, как подсудимый убегал с места преступления!"
    hide desk
    play sound courtroomb
    show courtroom e
    pause 2
    show slam b
    play sound slamb
    pause 1
    show judge blink
    j "Тишина! Тишина в зале суда!"
    show judge blink1
    j "Господин Мадзо, разрешаю вам вызвать своего свидетеля."
    hide judge
    show mudzo neutral
    ma "Да, Ваша честь."
    play music Court_is_Now_in_Session
    hide mudzo
    show phoenix sweating
    r "{color=#87CEFA}(Ох, не к добру это.){/color}"
    hide phoenix
    show mudzo neutral
    ma "В день убийства мой свидетель распространял газеты в доме потерпевшей."
    ma "Пожалуйста, пригласите господина Риото Онуву."
    show onuvu normal with fade
    pause 2
    hide onuvu
    show mudzo neutral
    ma "Господин Онуву, вы продаёте газеты, верно?"
    show onuvu normal
    o "Ах, газеты! Продаю, конечно!"
    hide onuvu
    show judge blink
    j "Господин Онуву, в таком случае засвидетельствуйте о случившемся перед судом."
    show judge blink1
    j "Пожалуйста, расскажите, что вы видели в день убийства."
    stop music
    show onuvu normal with fade
    "{color=#FF7F50} \n{space=170}-Рассказ свидетеля-{/color}"
    pause 2
    play music Cross_Examination
    show crossexamination zorder 100
    o "{color=#00FF00}Я ходил по квартирам, предлагая оформить подписку,- и вдруг кто-то выбежал из квартиры.{/color}"
    show cross1
    o "{color=#00FF00}Я предположил, что человек очень спешил, так как он не до конца запер дверь.{/color}"
    hide cross1
    show cross2
    o "{color=#00FF00}Мне это показалось странным, поэтому я заглянул в саму квартиру.{/color}"
    o "{color=#00FF00}Там...неподвижно лежала женщина. Она уже была мертва!{/color}"
    o "{color=#00FF00}От страха у меня подкосились ноги, поэтому я не зашел туда.{/color}"
    o "{color=#00FF00}Я подумал, что надо сразу вызвать полицию!{/color}"
    o "{color=#00FF00}Однако телефон в квартире не работал.{/color}"
    o "{color=#00FF00}Я отправился в близлежащий парк, где и нашел таксофон.{/color}"
    hide cross2
    show onuvu normal
    o "{color=#00FF00}Я запомнил точное время: два часа дня.{/color}"
    o "{color=#00FF00}Сбежавшим оказался - я в этом не сомневаюсь - подсудимый.{/color}"
    hide crossexamination
    hide onuvu
    stop music
    show judge close1 with fade
    j "Хм..."
    hide judge
    show phoenix slaming1
    r "{color=#87CEFA}(Этто, почему ты не рассказал мне всю правду?){/color}"
    r "{color=#87CEFA}(Ну и как мне тебя защищать после таких показаний?!){/color}"
    hide phoenix
    show judge blink1
    j "Кстати, а почему в квартире потерпевшей не работал телефон?"
    hide judge
    show mudzo neutral
    ma "Ваша честь, в момент убийства во всём доме отсутствовал свет."
    hide mudzo
    show judge blink
    j "Но, насколько я знаю, отсутствие электричества не должно влиять на работу телефонов, да?"
    hide judge
    show mudzo neutral
    ma "Верно, Ваша честь, однаков радиотелефоны не могут без него работать."
    hide mudzo
    show cross2
    ma "Телефон, которым попытался воспользоваться свидетель, был как раз таким."
    hide cross2
    show mudzo neutral
    ma "Ваша честь..."
    show otchet_icon
    ma "Хочу предоставить вам документ, подтверждающий факт отсутствия электричества."
    $evidence3 += True
    play sound selectjingle
    "{color=#87CEFA}Отчёт об аварии приобщен к материалам дела.{/color}"
    hide otchet_icon
    hide mudzo
    show judge close1
    j "Итак, сторона защиты."
    hide judge
    show phoenix blink
    r "Да, ваша честь?"
    hide phoenix
    show judge blink1
    j "Можете начать {color=#FF7F50}перекрёстный допрос{/color} свидетеля."
    hide judge
    show phoenix thinking
    r "{color=#FF7F50}Д-допрос{/color}, говорите?"
    play music The_Truth_Revealed
    hide phoenix
    show mia blink3
    m "Хорошо, Хорасё, пора браться за работу."
    r "Э-э-э, и что от меня требуется?"
    m "Как что - искать {color=#FF7F50}ложь{/color} в показаниях свидетеля."
    r "Ложь? \nТак он врёт?!"
    m "Твой клиент невиновен, да?"
    m "Значит, свидетель врал во время дачи показаний."
    m "Ты-то хоть сам веришь, что твой клиент невиновен?"
    r "!.. \nИ как мне это доказать?"
    m "Всё необходимое находится в {color=#FF7F50}материалах дела{/color}."
    m "Сравни показания свидетеля с имеющимися у тебя уликами."
    m "Они должны где-то {color=#FF7F50}противоречить{/color} друг другу."
    m "Сперва найди несоответствие между {color=#FF7F50}материалами дела{/color} и свидетельскими показаниями."
    m "Как только ты найдешь {color=#FF7F50}улику{/color}, противоречащую показаниям..."
    m "{color=#FF7F50}Покажи её{/color} свидетелю!"
    r "А-а-а, ну хорошо."
    m "Нажми на кнопку {color=#FF7F50}Материалы{/color} и укажи на {color=#FF7F50}противоречие{/color} в показаниях!"
    show onuvu normal with fade
    stop music
    "{color=#FF7F50} \n{space=170}-Рассказ свидетеля-{/color}"
    play music Cross_Examination
    jump dopros

label dopros:
    $der9 = 1
    show screen pokazat
    show onuvu normal with fade
    show screen crossex1
    o "{color=#00FF00}Я ходил по квартирам, предлагая оформить подписку,- и вдруг кто-то выбежал из квартиры.{/color}"
    $der += True
    o "{color=#00FF00}Я предположил, что человек очень спешил, так как он не до конца запер дверь.{/color}"
    $der1 += True
    o "{color=#00FF00}Мне это показалось странным, поэтому я заглянул в саму квартиру.{/color}"
    $der2 += True
    o "{color=#00FF00}Там...неподвижно лежала женщина. Она уже была мертва!{/color}"
    $der3 += True
    o "{color=#00FF00}От страха у меня подкосились ноги, поэтому я не зашел туда.{/color}"
    $der4 += True
    o "{color=#00FF00}Я подумал, что надо сразу вызвать полицию!{/color}"
    $der5 += True
    o "{color=#00FF00}Однако телефон в квартире не работал.{/color}"
    $der6 += True
    o "{color=#00FF00}Я отправился в близлежащий парк, где и нашел таксофон.{/color}"
    $der7 += True
    $right = 1
    o "{color=#00FF00}Я запомнил точное время: два часа дня.{/color}"
    $right = 0
    $der8 += True
    o "{color=#00FF00}Сбежавшим оказался - я в этом не сомневаюсь - подсудимый.{/color}"
    hide onuvu
    $der9 = 0
    show mia blink3
    hide screen crossex1
    m "Он закончил давать показания."
    m "Где-то в его словах находится неувязка."
    m "Просмотри {color=#FF7F50}материалы дела{/color}, если у тебя что-то вызываает подозрение."
    m "Затем найди улику, противоречащую его словам, и {color=#FF7F50}покажи{/color} её ему!"

    jump dopros

label right1:
    $der9 = 0
    stop music
    hide screen pokazat
    show screen materiali
    scene bg desk
    hide screen crossex1
    play sound objection
    play sound phoenix
    show objection_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide objection_
    show  phoenix slaming
    pause 0.5
    show phoenix slaming1
    r "Вы нашли тело в два часа дня. Вы точно не ошибаетесь?"
    hide phoenix
    show onuvu normal
    o "Да, было ровно два часа."
    hide onuvu
    show  phoenix slaming
    pause 0.5
    show phoenix slaming1
    r "В таком случае возникает явная проблема!"
    show protokol_icon
    show phoenix thinking
    r "Ваше утверждение полностью противоречит протоколу вскрытия."
    r "В нём указано, что смерть наступила около {color=#FF7F50}четырёх часов дня{/color}."
    hide protokol_icon
    r "Вы не могли обнаружить тело в указанное вами время!"
    show phoenix blink
    r "Чем вы объясните разницу в два часа?"
    hide phoenix
    show onuvu sweating
    o "!.."
    o "Э-э-э, м-м-м... э-это-о..."
    hide onuvu
    play sound objection
    play sound payne
    show objection_  zorder 100 with hpunch
    pause 0.7
    hide objection_
    show mudzo sweat
    ma "Это несущественно! Свидетель просто перепутал время!"
    hide mudzo
    show judge blink
    j "Учитывая его слова, мне в это сложно поверить."
    show judge blink1
    j "Господин Онуву."
    j "Почему вы так уверены в том, что вы нашли тело в два часа?"
    hide judge
    show onuvu sweating
    o "Я... э-э-э... ну-у-у... я... Действительно, почему?"
    hide onuvu
    show mia blink3
    m "Молодец, Хорасё!"
    m "Вот так и надо действовать: находить противоречия!"
    m "Ложь порождает ложь!"
    m "Раскуси её - и всё враньё рассыплется как карточный домик!"
    hide mia
    show onuvu normal
    o "Подождите, я вспомнил!"
    hide onuvu
    show judge blink1
    j "Пожалуйста объяснитесь."
    stop music
    show onuvu normal with fade
    "{color=#FF7F50} \n{space=170}-Не то время-{/color}"
    pause 2
    play music Cross_Examination
    show crossexamination zorder 100
    o "{color=#00FF00}Видите ли, когда я обнаружил тело, я услышал время.{/color}"
    hide onuvu
    show cross2
    o "{color=#00FF00}Его озвучил некий голос. Наверное это был телевизор.{/color}"
    o "{color=#00FF00}Возможно жертва смотрела видеозапись, потому время и было неправильное.{/color}"
    hide cross2
    show onuvu normal
    o "{color=#00FF00}Вот поэтому я и подумал, что это было в два часа!{/color}"
    hide crossexamination
    hide onuvu
    stop music
    show judge close1 with fade
    j "Хм, теперь понятно. Вы услышали время, умоминавшееся в видеозаписи."
    show judge blink1
    j "Защита, можете приступать к допросу свидетеля."
    hide judge
    show mia blink3
    m "Хорасё, ты уже знаешь, что делать."
    r "Да."
    show onuvu normal with fade
    "{color=#FF7F50} \n{space=170}-Не то время-{/color}"
    play music Cross_Examination
    jump dopros1

label dopros1:
    $error1 = 1
    $der9 = 1
    $right = 0
    show screen pokazat
    show onuvu normal with fade
    show screen crossex1
    $der21 += True
    o "{color=#00FF00}Видите ли, когда я обнаружил тело, я услышал время.{/color}"
    $right2 = 1
    $der22 += True
    o "{color=#00FF00}Его озвучил некий голос. Наверное это был телевизор.{/color}"
    $right2 = 0
    $der23 += True
    o "{color=#00FF00}Возможно жертва смотрела видеозапись, потому время и было неправильное.{/color}"
    $der24 += True
    o "{color=#00FF00}Вот поэтому я и подумал, что это было в два часа!{/color}"
    $der9 = 0
    hide onuvu
    show mia blink3
    hide screen crossex1
    m "Заметил противоречие?"

    jump dopros1

label right2:
    $der9 = 0
    stop music
    hide screen pokazat
    show screen materiali
    scene bg desk
    hide screen crossex1
    play sound objection
    play sound phoenix
    show objection_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide objection_
    show  phoenix slaming
    pause 0.5
    show phoenix slaming1
    r "Подождите минутку!"
    r "Прокурор утверждал, что когда свидетель обнаружил тело, в здании не было света!"
    show otchet_icon2
    show phoenix thinking
    r "Отчет это подтверждает."
    hide phoenix
    show onuvu sweating
    o "!.."
    hide onuvu
    show  phoenix slaming
    pause 0.5
    show phoenix slaming1
    r "Запись тут не при чем. Дело в телевизоре! Он никоим образом не мог работать!"
    hide phoenix
    show onuvu sweating
    o "Ь-ь-ь!"
    o "Я... это... ы-ы-ы!"
    hide onuvu
    show judge blink1
    j "Не могу не согласиться. Господин Онуву, как вы это объясните?"
    hide judge
    show onuvu sweating
    o "Не знаю, мне это самому крайне удивительно. Крайне!"
    o "..."
    o "В-вот оно что! \nЯ вспомнил!"
    hide onuvu
    show judge blink1
    j "Свидетель, было бы желательно, если бы вы с самого начала давали точные показания."
    show judge blink
    j "Эти постоянные оговорки подрывают к вам доверие."
    hide judge
    show onuvu sweating
    j "Вас словно что-то... тревожит."
    o "Ь-Ь-Ь!"
    o "П-прошу прощения, Ваша честь! Скорее всего, это... последствия пережитого мной стресса!"
    hide onuvu
    show judge blink1
    j "Тогда объясните."
    hide judge
    show onuvu sweating
    o "На самом деле я не услышал, а увидел время!"
    o "На настольных часах!"
    o "Да, орудие убийства! Убийца ударил ими свою жертву!"
    o "Вот их то я и увидел."
    hide onuvu
    show judge blink1
    j "Вы увидели часы? А, ну тогда понятно."
    j "Защита, у вас есть возражения?"

label end_:
    menu:
        "Да!":
            $der9 = 1
            $right = 0
            $right2 = 0
            $right3 = 1
            show screen pokazat
            j "Тогда покажите улику, указывающую на несостыковку."
            $der9 = 0
            jump end_


        "Вообще-то нет":
            jump bad_end


label right3:
    $der9 = 0
    hide screen pokazat
    show screen materiali
    scene bg desk
    hide screen crossex1
    play sound objection
    play sound phoenix
    show objection_  zorder 100 with hpunch
    pause 0.7
    hide judge
    hide objection_
    show  phoenix slaming
    pause 0.5
    show phoenix slaming1
    r "Орудием убийства были вовсе не часы."
    play music The_Truth_Revealed
    r "Это была статуэтка!"
    r "Ну и где вы здесь видите часы?"
    hide phoenix
    show onuvu sweating
    o "Чего?"
    o "К-как ты надоел со своими протестами и со своими уликами. Чего ты себе позволяешь?!"
    hide onuvu
    show phoenix slaming1
    r "Отвечайте на вопрос, господин Онуву."
    hide phoenix
    show onuvu sweating
    o "Я...я... их видел, ясно тебе?! Это часы!"
    hide onuvu
    show mudzo sweat
    ma "Свидетель прав, эта статуэтка на самом деле является часами."
    ma "Её голова служит кнопкой. Если её наклонить, она громким голосом озвучит время."
    ma "Так как она не похожа на часы, я заявил ее в качестве статуэтки."
    hide mudzo
    show judge blink1
    j "Выходит, орудием убийства были настольные часы."
    j "Давайте проверим.."
    stop music
    scene bg black with fade
    show mislitel with dissolve
    pause 1
    "{cps=14}{color=#00FF00}\n {space=150}Я думаю, сейчас 9:25.{/color}{/cps}"
    hide mislitel
    show judge blink
    j "Как-то странно они объявляют время!"
    hide judge
    show phoenix blink
    r "Ну, статус мыслителя обязывает."
    hide phoenix
    show judge blink
    j "Защита, похоже, что показания свидетеля были точными - это часы."
    hide judge
    show phoenix slaming1
    r "В показаниях свидетеля содержится противоречие!"
    show phoenix blink
    r "Он мог узнать, что это часы, лишь в одном случае: если бы он держал их в руках."
    r "Но по его же словам, он никогда не переступал порога квартиры."
    show  phoenix slaming
    pause 0.5
    show phoenix slaming1
    play music The_Truth_Revealed
    r "Это явное противоречие!"
    r "Свидетель знал, что это, часы потому, что он был внутри!"
    r "Звук произвёл на господина Онуву невероятное впечатление."
    r "Оно и понятно. Оружие вдруг заговорило!"
    hide phoenix
    show judge blink
    j "И какой ваш вывод защита?"
    hide judge
    show phoenix blink
    r "Господин Мадзо, который сейчас час?"
    hide phoenix
    show mudzo sweat
    ma "11:25."
    show mudzo shocked
    ma "Ь-ь-ь!"
    hide mudzo
    show phoenix slaming1
    r "Как вы помните, ранее часы объявили 9:25."
    r "То есть часы отстают ровно на 2 часа."
    stop music
    r "Время, которое услышал Онуву, и время смерти отличаются на те же два часа!"
    hide phoenix
    play sound courtroomb
    show courtroom e
    pause 2
    show slam b
    play sound slamb
    pause 1
    hide courtroom e
    hide slam b
    show judge blink
    j "П-порядок!"
    show judge blink1 with fade
    pause 1.5
    play music So_it_Begins
    j "Господин Мадзо?"
    j "Где господин Онуву?"
    hide judge
    show mudzo sweat
    ma "Э-э-э.. Он вышел и сдался. Его арестовали."
    hide mudzo
    show judge blink1
    j "Понятно."
    j "В таком случае допрос окончен."
    hide judge
    show mudzo sweat
    r "Стойте, я-"
    hide mudzo
    show judge blink1
    j "Пришло время вынести вердикт."
    j "У защиты есть комментарии?"
    hide judge
    show phoenix blink
    ma "Нет, Ваша честь."
    hide phoenix
    show judge blink1
    j "Хорошо, что все разрешилось."
    j "Позовите господина Яхари."
    hide judge
    scene bg desk with fade
    show desk zorder 100 with dissolve
    show etto crying with dissolve
    pause 1
    j "Спасибо, Ваша честь."
    hide etto
    hide desk
    show phoenix sweating
    r "{color=#87CEFA}(А мне ничего..?){/color}"
    r "{color=#87CEFA}(Нет?){/color}"
    hide phoenix
    show judge blink
    stop music
    j "Подведем итоги."
    show slam b
    play sound slamb
    pause 1
    hide slam b
    show judge blink
    j "Гражданин Этто Яхари.."
    pause 1
    play sound deskslam
    show not_ with dissolve
    pause 0.5
    play sound deskslam
    show not_guilty with dissolve
    pause 1.5
    play sound courtroomb
    show courtroom e
    pause 2
    hide screen materiali with dissolve
    scene black with dissolve
    pause 2
    r "Таков был исход моего первого дела."
    r "Я помог своему другу, как он помог мне много лет тому назад."
    return








label bad_end:
    j "В таком случае допрос окончен."
    hide judge
    show phoenix slaming1
    r "Стойте, я-"
    hide phoenix
    show judge blink1
    j "Пришло время вынести вердикт."
    j "У обвинения есть комментарии?"
    hide judge
    show mudzo neutral
    ma "Нет, Ваша честь."
    hide mudzo
    show judge blink1
    j "Хорошо, что все разрешилось, господин Онуву."
    show onuvu normal
    o "Спасибо за понимание, Ваша честь."
    hide onuvu
    play sound courtroomb
    show courtroom e
    pause 2
    show slam b
    play sound slamb
    pause 1
    hide courtroom e
    hide slam b
    show judge blink
    j "Подведем итоги."
    j "Гражданин Этто Яхари.."
    pause 1
    play sound deskslam
    show guilty with dissolve
    pause 2
    hide screen materiali with dissolve
    scene black with dissolve
    r "Таков был исход моего первого дела."
    pause 1
    r "Прости, Этто."




















    return
