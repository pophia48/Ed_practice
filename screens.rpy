

################################################################################
## Стили
################################################################################

style default:
    properties gui.text_properties()
    language gui.language



style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Внутриигровые экраны
################################################################################


## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Если есть боковое изображение ("голова"), показывает её поверх текста.
    ## По стандарту не показывается на варианте для мобильных устройств — мало
    ## места.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Делает namebox доступным для стилизации через объект Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False


## Экран выбора ################################################################
##
## Этот экран используется, чтобы показывать внутриигровые выборы,
## представленные оператором menu. Один параметр, вложения, список объектов,
## каждый с заголовком и полями действия.
##


screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 125
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")






################################################################################
## Экраны Главного и Игрового меню
################################################################################

## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Начать") action Start()

        else:
            textbutton _("Сохранить") action ShowMenu("save")

        textbutton _("Загрузить") action ShowMenu("load")




        if not main_menu:

            textbutton _("Главное меню") action MainMenu()




        if renpy.variant("pc"):

            ## Кнопка выхода блокирована в iOS и не нужна на Android и в веб-
            ## версии.
            textbutton _("Выход") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Экран главного меню #########################################################
##
## Используется, чтобы показать главное меню после запуска игры.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Этот тег гарантирует, что любой другой экран с тем же тегом будет
    ## заменять этот.
    tag menu

    add gui.main_menu_background

    imagemap:
        ground "gui/main_menu.png"
        idle "gui/main_normal.png"
        hover "gui/main_light.png"

        hotspot(120,530,360,100) action Start()
        hotspot(120,656,360,200) action ShowMenu("load")
    ## Оператор use включает отображение другого экрана в данном. Актуальное
    ## содержание главного меню находится на экране навигации.



## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None, или "viewport", или "vpgrid", когда этот
## экран предназначается для использования с более чем одним дочерним экраном,
## включённым в него.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Резервирует пространство для навигации.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                else:

                    transclude

    use navigation

    textbutton _("Вернуться"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")




style game_menu_outer_frame:
    bottom_padding 14
    top_padding 56

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 129
    yfill True


style game_menu_label:
    xpos 24
    ysize 56

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -13




## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##


screen save():

    tag menu

    use file_slots(_("Сохранить"))


screen load():

    tag menu

    use file_slots(_("Загрузить"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):

        fixed:

            ## Это гарантирует, что ввод будет принимать enter перед остальными
            ## кнопками.
            order_reverse True

            ## Номер страницы, который может быть изменён посредством клика на
            ## кнопку.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Таблица слотов.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Пустой слот")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 24
    ypadding 2

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")





################################################################################
## Дополнительные экраны
################################################################################


## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет спросить у игрока вопрос
## Да или Нет.
##


screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 14

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 47

                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action

    ## Правый клик и esc, как ответ "Нет".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Экран индикатора пропуска ###################################################
##
## Экран индикатора пропуска появляется для того, чтобы показать, что идёт
## пропуск.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 3

            text _("Пропускаю")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Эта трансформация используется, чтобы мигать стрелками одна за другой.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


## Экран уведомлений ###########################################################
##
## Экран уведомлений используется, чтобы показать игроку оповещение. (Например,
## когда игра автосохранилась, или был сделан скриншот)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Мобильные варианты
################################################################################

style pref_vbox:
    variant "medium"
    xsize 208

## Раз мышь может не использоваться, мы заменили быстрое меню версией,
## использующей меньше кнопок, но больших по размеру, чтобы их было легче
## касаться.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Назад") action Rollback()
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Меню") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 157

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 185

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 277

screen yuna:
    modal True
    add "images/logo dosie3.png"
    text "{color=#FFA500}{size=+7}Юна Такуми{/size}{/color}" xpos 295 ypos 542
    text "{color=#414141}{size=+5}Возраст: 22 года{/size}{/color}" xpos 225 ypos 585
    text "{color=#414141}{size=+5}Пол: женский{/size}{/color}" xpos 225 ypos 615
    text "{size=+6}Жертва преступления. Работала{/size}" xpos 50 ypos 715
    text "{size=+6}моделью. Проживала в своей{/size}" xpos 50 ypos 750
    text "{size=+6}квартире одна.{/size}" xpos 50 ypos 785
    imagebutton:
        yalign 1.0
        idle "gui/nazad.png"
        hover "gui/nazad_hover.png"
        action [Play("sound", "audio/close.wav"), Hide ("yuna")]
    imagebutton:
        xalign 1.0
        yalign 0.55
        idle "gui/bg uliki.png"
        hover "gui/bg uliki_hover.png"
        action [Play("sound", "audio/bleep.wav"), Hide ("yuna"), Hide ("dosie")]

screen etto:
    modal True
    add "images/logo dosie2.png"
    text "{color=#FFA500}{size=+7}Этто Яхари{/size}{/color}" xpos 300 ypos 542
    text "{color=#414141}{size=+5}Возраст: 23 года{/size}{/color}" xpos 225 ypos 585
    text "{color=#414141}{size=+5}Пол: мужской{/size}{/color}" xpos 225 ypos 615
    text "{size=+6}Подсудимый по данному делу.{/size}" xpos 50 ypos 715
    text "{size=+6}Мой школьный друг и просто{/size}" xpos 50 ypos 750
    text "{size=+6}славный малый.{/size}" xpos 50 ypos 785
    imagebutton:
        yalign 1.0
        idle "gui/nazad.png"
        hover "gui/nazad_hover.png"
        action [Play("sound", "audio/close.wav"), Hide ("etto")]
    imagebutton:
        xalign 1.0
        yalign 0.55
        idle "gui/bg uliki.png"
        hover "gui/bg uliki_hover.png"
        action [Play("sound", "audio/bleep.wav"), Hide ("etto"), Hide ("dosie")]

screen mia:
    modal True
    add "images/logo dosie1.png"
    text "{color=#FFA500}{size=+7}Мия Асато{/size}{/color}" xpos 300 ypos 542
    text "{color=#414141}{size=+5}Возраст: 27 лет{/size}{/color}" xpos 225 ypos 585
    text "{color=#414141}{size=+5}Пол: женский{/size}{/color}" xpos 225 ypos 615
    text "{size=+6}Глава адвокатского бюро{/size}" xpos 50 ypos 715
    text "{size=+6}Асато и Ко. Моя начальница,{/size}" xpos 50 ypos 750
    text "{size=+6}весьма талантливый адвокат.{/size}" xpos 50 ypos 785
    imagebutton:
        yalign 1.0
        idle "gui/nazad.png"
        hover "gui/nazad_hover.png"
        action [Play("sound", "audio/close.wav"), Hide ("mia")]
    imagebutton:
        xalign 1.0
        yalign 0.55
        idle "gui/bg uliki.png"
        hover "gui/bg uliki_hover.png"
        action [Play("sound", "audio/bleep.wav"), Hide ("mia"), Hide ("dosie")]


screen otchet:
    modal True
    add "images/logo evidence5.png"
    text "{color=#FFA500}{size=+7}Отчёт об аварии{/size}{/color}" xpos 260 ypos 542
    text "{color=#414141}{size=+5}Тип: документ{/size}{/color}" xpos 225 ypos 585
    text "{color=#414141}{size=+5}Предоставлен{/size}{/color}" xpos 225 ypos 615
    text "{color=#414141}{size=+5}прокурором Мадзо.{/size}{/color}" xpos 225 ypos 645
    text "{size=+6}В день убийства в доме{/size}" xpos 50 ypos 715
    text "{size=+6}г-жи Такуми с 13:00 до 16:00{/size}" xpos 50 ypos 750
    text "{size=+6}отсутствовало электричество.{/size}" xpos 50 ypos 785
    imagebutton:
        yalign 1.0
        idle "gui/nazad.png"
        hover "gui/nazad_hover.png"
        action [Play("sound", "audio/close.wav"), Hide ("otchet")]
    if der9  >= 0:
        imagebutton:
            xalign 1.0
            yalign 0.55
            idle "gui/bg dosie.png"
            hover "gui/bg dosie_hover.png"
            action [Play("sound", "audio/bleep.wav"), Show ("dosie")]
    if der9  >= 1:
        if right2 >= 1:
            imagebutton:
                xalign 1.0
                yalign 0.55
                idle "gui/bg pokazat.png"
                hover "gui/bg pokazat_hover.png"
                action [Play("sound", "audio/bleep.wav"), Hide ("otchet"), Hide ("inventory"), Jump ("right2")]
        else:
            imagebutton:
                xalign 1.0
                yalign 0.55
                idle "gui/bg pokazat.png"
                hover "gui/bg pokazat_hover.png"
                action [Play("sound", "audio/bleep.wav"), Hide ("otchet"), Hide ("inventory"), Jump ("error")]

screen pasport:
    modal True
    add "images/logo evidence4.png"
    text "{color=#FFA500}{size=+7}Паспорт{/size}{/color}" xpos 310 ypos 542
    text "{color=#414141}{size=+5}Тип: улика{/size}{/color}" xpos 225 ypos 585
    text "{color=#414141}{size=+5}Предоставлен{/size}{/color}" xpos 225 ypos 615
    text "{color=#414141}{size=+5}прокурором Мадзо.{/size}{/color}" xpos 225 ypos 645
    text "{size=+6}Потерпевшая вернулась{/size}" xpos 50 ypos 715
    text "{size=+6}домой из Нью-Йорка 30.07,{/size}" xpos 50 ypos 750
    text "{size=+6}за день до своего убийства.{/size}" xpos 50 ypos 785
    imagebutton:
        yalign 1.0
        idle "gui/nazad.png"
        hover "gui/nazad_hover.png"
        action [Play("sound", "audio/close.wav"), Hide ("pasport")]
    if der9  >= 0:
        imagebutton:
            xalign 1.0
            yalign 0.55
            idle "gui/bg dosie.png"
            hover "gui/bg dosie_hover.png"
            action [Play("sound", "audio/bleep.wav"), Show ("dosie")]
    if der9  >= 1:
        imagebutton:
            xalign 1.0
            yalign 0.55
            idle "gui/bg pokazat.png"
            hover "gui/bg pokazat_hover.png"
            action [Play("sound", "audio/bleep.wav"), Hide ("pasport"), Hide ("inventory"), Jump ("error")]

screen mislitel:
    modal True
    add "images/logo evidence3.png"
    text "{color=#FFA500}{size=+7}Статуэтка{/size}{/color}" xpos 310 ypos 542
    text "{color=#414141}{size=+5}Тип: оружие{/size}{/color}" xpos 225 ypos 585
    text "{color=#414141}{size=+5}Предоставлена{/size}{/color}" xpos 225 ypos 615
    text "{color=#414141}{size=+5}прокурором Мадзо.{/size}{/color}" xpos 225 ypos 645
    text "{size=+6}Миниатюрная копия скульптуры{/size}" xpos 50 ypos 715
    text "{size=+6}{color=#FF7F50}Мыслитель{/color}. Весьма увесиста.{/size}" xpos 50 ypos 750
    imagebutton:
        yalign 1.0
        idle "gui/nazad.png"
        hover "gui/nazad_hover.png"
        action [Play("sound", "audio/close.wav"), Hide ("mislitel")]
    if der9  >= 0:
        imagebutton:
            xalign 1.0
            yalign 0.55
            idle "gui/bg dosie.png"
            hover "gui/bg dosie_hover.png"
            action [Play("sound", "audio/bleep.wav"), Show ("dosie")]
    if der9  >= 1:
        if right3 >= 1:
            imagebutton:
                xalign 1.0
                yalign 0.55
                idle "gui/bg pokazat.png"
                hover "gui/bg pokazat_hover.png"
                action [Play("sound", "audio/bleep.wav"), Hide ("mislitel"), Hide ("inventory"), Jump ("right3")]
        else:
            imagebutton:
                xalign 1.0
                yalign 0.55
                idle "gui/bg pokazat.png"
                hover "gui/bg pokazat_hover.png"
                action [Play("sound", "audio/bleep.wav"), Hide ("mislitel"), Hide ("inventory"), Jump ("error")]

screen protokol:
    modal True
    add "images/logo evidence2.png"
    text "{color=#FFA500}{size=+7}Протокол вскрытия{/size}{/color}" xpos 240 ypos 542
    text "{color=#414141}{size=+5}Тип: отчёт{/size}{/color}" xpos 225 ypos 585
    text "{color=#414141}{size=+5}Получен от{/size}{/color}" xpos 225 ypos 615
    text "{color=#414141}{size=+5}Мии Асато.{/size}{/color}" xpos 225 ypos 645
    text "{size=+6}Дата смерти: 31.07, 16:00-17:00.{/size}" xpos 50 ypos 715
    text "{size=+6}Причина смерти: потеря крови{/size}" xpos 50 ypos 750
    text "{size=+6}в результате тупой травмы.{/size}" xpos 50 ypos 785
    imagebutton:
        yalign 1.0
        idle "gui/nazad.png"
        hover "gui/nazad_hover.png"
        action [Play("sound", "audio/close.wav"), Hide ("protokol")]
    if der9  >= 0:
        imagebutton:
            xalign 1.0
            yalign 0.55
            idle "gui/bg dosie.png"
            hover "gui/bg dosie_hover.png"
            action [Play("sound", "audio/bleep.wav"), Show ("dosie")]
    if der9  >= 1:
        if right >= 1:
            imagebutton:
                xalign 1.0
                yalign 0.55
                idle "gui/bg pokazat.png"
                hover "gui/bg pokazat_hover.png"
                action [Play("sound", "audio/bleep.wav"), Hide ("protokol"), Hide ("inventory"), Jump ("right1")]
        else:
            imagebutton:
                xalign 1.0
                yalign 0.55
                idle "gui/bg pokazat.png"
                hover "gui/bg pokazat_hover.png"
                action [Play("sound", "audio/bleep.wav"), Hide ("protokol"), Hide ("inventory"), Jump ("error")]


screen znachok:
    modal True
    add "images/logo evidence1.png"
    text "{color=#FFA500}{size=+7}Значок адвоката{/size}{/color}" xpos 260 ypos 542
    text "{color=#414141}{size=+5}Тип: другое{/size}{/color}" xpos 225 ypos 585
    text "{color=#414141}{size=+5}Личное.{/size}{/color}" xpos 225 ypos 615
    text "{size=+6}Без него мне бы было сложно{/size}" xpos 50 ypos 715
    text "{size=+6}доказать, что я адвокат.{/size}" xpos 50 ypos 750
    imagebutton:
        yalign 1.0
        idle "gui/nazad.png"
        hover "gui/nazad_hover.png"
        action [Play("sound", "audio/close.wav"), Hide ("znachok")]
    imagebutton:
        xalign 1.0
        yalign 0.55
        idle "gui/bg dosie.png"
        hover "gui/bg dosie_hover.png"
        action [Play("sound", "audio/bleep.wav"), Show ("dosie")]
    if der9  >= 1:
        imagebutton:
            xalign 1.0
            yalign 0.55
            idle "gui/bg pokazat.png"
            hover "gui/bg pokazat_hover.png"
            action [Play("sound", "audio/bleep.wav"), Hide ("znachok"), Hide ("inventory"), Jump ("error")]

screen dosie:
    modal True
    add "logo base1.png"
    imagebutton:
        xalign 1.0
        yalign 0.55
        idle "gui/bg uliki.png"
        hover "gui/bg uliki_hover.png"
        action [Play("sound", "audio/bleep.wav"), Hide ("dosie")]
    imagebutton:
        yalign 1.0
        idle "gui/nazad.png"
        hover "gui/nazad_hover.png"
        action [Play("sound", "audio/close.wav"), Hide ("dosie")]
    imagebutton:
        xalign 0.16
        yalign 0.754
        idle "images/mia.png"
        hover "images/mia_hover.png"
        action [Play("sound", "audio/evidenceshoop.wav"), Show ("mia")]
        hovered Play("sound", "audio/selectblip.wav")
    imagebutton:
        xalign 0.388
        yalign 0.754
        idle "images/etto.png"
        hover "images/etto_hover.png"
        action [Play("sound", "audio/evidenceshoop.wav"), Show ("etto")]
        hovered Play("sound", "audio/selectblip.wav")
    imagebutton:
        xalign 0.616
        yalign 0.754
        idle "images/yuna.png"
        hover "images/yuna_hover.png"
        action [Play("sound", "audio/evidenceshoop.wav"), Show ("yuna")]
        hovered Play("sound", "audio/selectblip.wav")


screen inventory:
    modal True
    add "logo base.png"
    imagebutton:
        xalign 1.0
        yalign 0.55
        idle "gui/bg dosie.png"
        hover "gui/bg dosie_hover.png"
        action [Play("sound", "audio/bleep.wav"), Show ("dosie")]
    imagebutton:
        xalign 0.16
        yalign 0.754
        idle "images/znachok.png"
        hover "images/znachok_hover.png"
        action [Play("sound", "audio/evidenceshoop.wav"), Show ("znachok")]
        hovered Play("sound", "audio/selectblip.wav")

    imagebutton:
        yalign 1.0
        idle "gui/nazad.png"
        hover "gui/nazad_hover.png"
        action [Play("sound", "audio/close.wav"), Hide ("inventory")]

    imagebutton:
        xalign 0.388
        yalign 0.754
        idle "images/protokol.png"
        hover "images/protokol_hover.png"
        action [Play("sound", "audio/evidenceshoop.wav"), Show ("protokol")]
        hovered Play("sound", "audio/selectblip.wav")

    if evidence1:
        imagebutton:
            xalign 0.616
            yalign 0.754
            idle "images/mislitelidle.png"
            hover "images/mislitel_hover.png"
            action [Play("sound", "audio/evidenceshoop.wav"), Show ("mislitel")]
            hovered Play("sound", "audio/selectblip.wav")

    if evidence2:
        imagebutton:
            xalign 0.844
            yalign 0.754
            idle "images/pasport.png"
            hover "images/pasport_hover.png"
            action [Play("sound", "audio/evidenceshoop.wav"), Show ("pasport")]
            hovered Play("sound", "audio/selectblip.wav")

    if evidence3:
        imagebutton:
            xalign 0.16
            yalign 0.895
            idle "images/otchet.png"
            hover "images/otchet_hover.png"
            action [Play("sound", "audio/evidenceshoop.wav"), Show ("otchet")]
            hovered Play("sound", "audio/selectblip.wav")


screen materiali:
    imagebutton:
        xalign 1.0
        yalign 0.55
        idle "gui/bg materiali.png"
        hover "gui/bg materiali_hover.png"
        action [Play("sound", "audio/bleep.wav"), Show ("inventory")]

screen pokazat:
    if der9:
        imagebutton:
            xalign 1.0
            yalign 0.55
            idle "gui/bg pokazat.png"
            hover "gui/bg pokazat_hover.png"
            action [Play("sound", "audio/bleep.wav"), Show ("inventory")]


screen crossex1:
    imagebutton:
        yalign 0.55
        idle "gui/bg perebit.png"
        hover "gui/bg perebit_hover.png"
        action [Play("sound", "audio/close.wav"), Jump ("cross_ex1")]
        if der:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex2")]
        if der1:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex3")]
        if der2:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex4")]
        if der3:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex5")]
        if der4:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex6")]
        if der5:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex7")]
        if der6:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex8")]
        if der7:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex9")]
        if der8:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex10")]
        if der21:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex21")]
        if der22:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex22")]
        if der23:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex23")]
        if der24:
            action [Play("sound", "audio/close.wav"), Jump ("cross_ex24")]








############################################################
############################################################

label cross_ex1:
    $der9 = 0
    hide screen pokazat
    show screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show  phoenix thinking
    r "Что может быть подозрительного в том, что человек уходит из квартиры?"
    r "По-моему, странно, что вы обратили на это внимание."
    hide phoenix
    show onuvu normal
    o "Ну, э-э-э..."
    o "Не знаю, он мне показался подозрительным, вот и всё."
    o "Он был сердитым и в то же время напуганным."
    o "Почти как преступник, убегающий с места преступления!"
    hide onuvu
    show phoenix slaming
    play sound deskslam
    pause 0.7
    r "Защита просит свидетеля не заниматься домыслами!"
    hide phoenix
    show mudzo neutral
    ma "Не возражаю. Свидетель всего-навсего подчеркнул, что тот человек выглядел подозрительно."
    hide onuvu
    show mudzo neutral
    ma "Защита, не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    jump dopros

label cross_ex2:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show  phoenix thinking
    r "Говорите, не до конца запер?"
    hide phoenix
    show onuvu normal
    o "Да, дверь осталась приоткрыта."
    o "Я подождал немного, но никто не вернулся её закрыть."
    o "Я подумал, что это очень странно, учитывая нынешние времена."
    hide onuvu
    show mudzo neutral
    ma "Защита, не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    jump dopros

label cross_ex3:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show  phoenix thinking
    r "Что вас вынудило так поступить?"
    hide phoenix
    show onuvu normal
    o "Ну, дверь же была приоткрыта."
    o "Заглянуть внутрь - вполне естественное желание."
    o "Почему люди играют в игры? Потому, что им это интересно. Так и тут."
    hide onuvu
    show mudzo neutral with hpunch
    ma "Золотые слова - лучше и не скажешь! Любой бы так поступил!"
    hide mudzo
    show  phoenix thinking
    r "{color=#87CEFA}(Хм, почему Мадзо так резко его прервал?){/color}"
    hide phoenix
    show mudzo neutral
    ma "Защита, не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    jump dopros

label cross_ex4:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show  phoenix slaming1
    r "Вы точно уверены, что она была мертва?"
    hide phoenix
    show onuvu normal
    o "Н-ну, нет, не совсем."
    o "Но она не двигалась, и вокруг всё было в крови."
    hide onuvu
    show  phoenix thinking
    r "{color=#87CEFA}(Ну да, увидев место преступления, любой человек на его месте пришёл бы к такому выводу.){/color}"
    hide phoenix
    show mudzo neutral
    ma "Защита, не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    jump dopros

label cross_ex5:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show  phoenix thinking
    r "Значит, в квартире вы {color=#FF7F50}ни к чему{/color} не прикасались?"
    hide phoenix
    show onuvu normal
    o "Нет. В смысле да - ни к чему!"
    hide onuvu
    show mudzo neutral
    ma "Защита, не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    jump dopros

label cross_ex6:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show  phoenix slaming
    pause 0.5
    show phoenix slaming1
    r "Вы подумали вызвать полицию? Выходит, это не вы её вызвали?"
    hide phoenix
    show mudzo neutral
    ma "Защита, сначала дослушайте до конца."
    ma "И не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    jump dopros

label cross_ex7:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show  phoenix thinking
    r "Телефон в квартире не работал?"
    hide phoenix
    show onuvu normal
    o "Нет. В смысле да, не работал."
    hide onuvu
    show phoenix blink
    r "Но вы же ранее заявляли, что не заходили в квартиру?"
    hide phoenix
    show onuvu normal
    o "А, это легко объяснить!"
    o "В коридоре на полке лежал радиотелефон."
    o "Я потянулся за ним и попытался набрать номер. Но телефон не работал."
    hide onuvu
    show mudzo neutral
    ma "Защита, не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    jump dopros

label cross_ex8:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show phoenix thinking
    r "Почему вы пошли в парк?"
    hide phoenix
    show onuvu normal
    o "Видите ли, у меня нет мобильного телефона."
    o "Ну а поскольку был полдень, в соседних квартирах никого не оказалось."
    hide onuvu
    show phoenix thinking
    r "Понятно."
    show mudzo neutral
    ma "Защита, не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    jump dopros

label cross_ex9:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show  phoenix slaming
    pause 0.5
    show phoenix slaming1
    r "Ровно два часа? \nВы уверены?!"
    hide phoenix
    show onuvu normal
    o "Да, абсолютно."
    hide onuvu
    show  phoenix thinking
    r "{color=#87CEFA}(Хм, он в этом совершенно уверен.){/color}"
    hide phoenix
    scene bg desk
    show mia blink3
    m "Ровно {color=#FF7F50}два часа{/color}?"
    m "Рю, тебе это не кажется немного подозрительным?"
    m "Покажи ему {color=#FF7F50}улику{/color}, {color=#FF7F50}противоречащую{/color} его словам!"
    jump dopros

label cross_ex10:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show  phoenix slaming
    pause 0.5
    show phoenix slaming1
    r "Вы в этом полностью уверены?"
    hide phoenix
    show onuvu normal
    o "Да, это был он, несомненно."
    hide onuvu
    show mudzo neutral
    ma "Свидетель не сомневается!"
    jump dopros

label cross_ex21:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show phoenix thinking
    r "Вы сказали {color=#FF7F50}услышал{/color}... то есть вы его не видели?"
    hide phoenix
    show onuvu normal
    o "Да, услышал. Увидел я лишь тело."
    o "Я был не в том состоянии, чтобы куда-то глядеть, в частности на свои часы."
    hide onuvu
    show phoenix thinking
    r "Хм, как-то странно, не находите?"
    show phoenix blink
    r "Вы утверждаете, что вы что-то {color=#FF7F50}услышали{/color}."
    r "Но если бы вы были шокированы увиденным, вы бы не обратили внимание на голос."
    play sound objection
    play sound payne
    show objection_  zorder 100 with hpunch
    pause 0.7
    hide objection_
    hide phoenix
    show mudzo sweat
    ma "Свидетель сказал, что он слышал время."
    ma "Глупо утверждать, что он не обратил внимание на голос."
    hide mudzo
    show judge blink1
    j "Хм... пожалуй соглашусь с обвинением."
    hide judge
    show mudzo sweat
    ma "Так что, защита, не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    hide mudzo
    jump dopros1

label cross_ex22:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show phoenix blink
    r "Вы точно уверены, что это был телевизор, а не, скажем, радио?"
    hide phoenix
    show onuvu normal
    o "Ну, не совсем. Может быть, это было и радио."
    hide onuvu
    show mudzo neutral
    r "Спешу сообщить, что следствие не обнаружило в квартире каких-либо радиоприёмников."
    hide mudzo
    show cross2
    ma "Там был лишь большой телевизор."
    hide cross2
    show mia blink3
    m "Рю, у меня нет доказательств, но я чую, здесь что-то не так. Вот это {color=#FF7F50}услышал телевизор{/color}..."
    show mudzo neutral
    ma "Защита, не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    hide mudzo
    jump dopros1

label cross_ex23:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show phoenix thinking
    r "Видео...запись?"
    hide phoenix
    show onuvu normal
    o "Да, вот поэтому я и перепутал время."
    hide onuvu
    show phoenix blink
    r "Действительно."
    hide phoenix
    show mudzo neutral
    ma "Защита, не перебивайте свидетеля по чём зря. Прослушаем показания заново."
    hide mudzo
    jump dopros1

label cross_ex24:
    hide screen pokazat
    hide screen materiali
    hide screen crossex1
    play sound objection
    play sound hold_it
    show hold_it_  zorder 100 with hpunch
    pause 0.7
    hide onuvu
    hide hold_it_
    show phoenix blink
    r "Вы уверены, что голос произнес {color=#FF7F50}два часа{/color}?"
    hide phoenix
    show onuvu normal
    o "Да, я прямо как сейчас помню. Голос был вполне четким."
    hide onuvu
    show judge blink1
    r "Господин Мадзо, вы можете подтвердить данный факт?"
    hide judge
    show mudzo sweat
    ma "Извините, Ваша честь: я, как и все, только сейчас узнал, что свидетель {color=#FF7F50}услышал{/color} время."
    hide mudzo
    show onuvu normal
    o "Ой, прошу прощения, я вспомнил об этом лишь недавно."
    jump dopros1

label error:
    hide screen pokazat
    hide screen materiali
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
    r "Ваша честь, что вы думаете о данном утверждении?"
    if right3 >= 1:
        hide phoenix
        show judge blink1
        j "Не вижу тут ничего существенного, защита."
        jump bad_end
    hide phoenix
    show judge blink1
    j "Хм, я вас не совсем понимаю."
    hide judge
    show phoenix slaming1
    r "Оно же явно, э-э-э, противоречит ул... в смысле, я думал..."
    hide phoenix
    show judge blink1
    j "Вы даже сами не уверены в своих словах, господин Хорасё."
    j "Протест отклонён."
    r "{color=#87CEFA}(Так я вряд ли завоюю симпатию судьи.){/color}"
    if error1 >= 1:
        jump dopros1
    else:
        jump dopros




#################################################################

















    ##
