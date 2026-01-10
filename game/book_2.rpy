init offset = 1

init -1 python:
    from renpy.text.text import Text

    def get_nvl_dialogue_height(dialogue_list, width):
        """Вычисляет общую высоту списка NVL реплик."""
        if not dialogue_list:
            return 0
        
        total_h = 0
        spacing = 15 # Должно совпадать с vbox spacing
        
        for i, d in enumerate(dialogue_list):
            t = Text(d.what, 
                     font="gui/fonts/Lora-Regular.ttf", 
                     size=24, 
                     line_spacing=7, 
                     xmaximum=width)
            
            # Рендерим текст для получения реальных размеров
            w, h = renpy.render(t, width, 2000, 0, 0).get_size()
            total_h += h
            if i < len(dialogue_list) - 1:
                total_h += spacing
        return total_h

    def split_nvl_by_height(dialogue, width, max_height):
        """Разбивает список диалогов на две страницы по высоте."""
        left = []
        right = []
        
        for d in dialogue:
            temp_left = left + [d]
            if get_nvl_dialogue_height(temp_left, width) <= max_height:
                left.append(d)
            else:
                right.append(d)
                
        return left, right

# 2. ПЕРЕМЕННЫЕ УПРАВЛЕНИЯ
default book_nvl_mode = False
default book_page_side = "left"
default book_two_columns = False

# 3. СТИЛЬ - СБРОС ВСЕГО
# Мы принудительно сбрасываем xpos и xsize, чтобы они не наследовались от стандартного NVL
style book_nvl_text:
    xpos 0
    xanchor 0
    xsize None
    xmaximum 500
    
    # Визуал
    font "gui/fonts/Lora-Regular.ttf"
    size 24
    line_spacing 7
    color "#2b1d0e"
    xalign 0.0
    text_align 0.0
    layout "tex"
    subpixel True

# 4. ПЕРСОНАЖ
# Явно указываем what_style, чтобы id "what" использовал наш чистый стиль
define book_nvl = Character(None, kind=nvl, what_style="book_nvl_text")

# 5. ТРАНСФОРМЫ
transform book_img_left:
    subpixel True
    anchor (0.5, 0.5)
    pos (0.25, 0.5)

transform book_img_right:
    subpixel True
    anchor (0.5, 0.5)
    pos (0.65, 0.5)

transform book_img_left_small:
    subpixel True
    anchor (0.25, 0.25)
    pos (0.25, 0.25)


image ilustration_cat = Transform("cat_jump.png", xsize=600, ysize=800)
image illustration_cat_angry = Transform("cat_angry.png", xsize=600, ysize=800)
image illustration_girl = Transform("girl.png", xsize=600, ysize=800)
image illustration_girl_room = Transform("sсene2_3.jpg", xsize=600, ysize=800)
image illustration_lonely = Transform("images/illustrations/scene_02_01.png", xsize=600, ysize=800)

image illustration_cat_angry_small = Transform("cat_angry.png", xsize=600, ysize=300)
image scene_01_01 = Transform("images/illustrations/scene_01_01.png", xsize=600, ysize=800)
image scene_02_01 = Transform("images/illustrations/scene_02_01.png", xsize=600, ysize=800)
image scene_02_02 = Transform("images/illustrations/scene_02_02.png", xsize=600, ysize=600)
image scene_03_01 = Transform("images/illustrations/scene_03_01.png", xsize=600, ysize=500)
image scene_04_01 = Transform("images/illustrations/scene_04_01.png", xsize=600, ysize=800)
image scene_05_01 = Transform("images/illustrations/scene_05_01.png", xsize=600, ysize=800)
image scene_06_01 = Transform("images/illustrations/scene_06_01.png", xsize=600, ysize=450)
image scene_07_01 = Transform("images/illustrations/scene_07_01.png", xsize=600, ysize=800)
image scene_08_01 = Transform("images/illustrations/scene_08_01.png", xsize=600, ysize=800)
image scene_10_01 = Transform("images/illustrations/scene_10_01.png", xsize=600, ysize=800)
image scene_11_01 = Transform("images/illustrations/scene_11_01.png", xsize=600, ysize=800)
image scene_12_01 = Transform("images/illustrations/scene_12_01.png", xsize=600, ysize=800)
image scene_13_01 = Transform("images/illustrations/scene_13_01.png", xsize=600, ysize=800)
image scene_14_01 = Transform("images/illustrations/scene_14_01.png", xsize=600, ysize=800)
image scene_15_01 = Transform("images/illustrations/scene_15_01.png", xsize=600, ysize=800)
image scene_16_01 = Transform("images/illustrations/scene_16_01.png", xsize=600, ysize=800)
image scene_17_01 = Transform("images/illustrations/scene_17_01.png", xsize=600, ysize=800)
image scene_18_01 = Transform("images/illustrations/scene_18_01.png", xsize=600, ysize=800)
image scene_19_01 = Transform("images/illustrations/scene_19_01.png", xsize=600, ysize=800)
image scene_20_01 = Transform("images/illustrations/scene_20_01.png", xsize=600, ysize=800)
image scene_21_01 = Transform("images/illustrations/scene_21_01.png", xsize=600, ysize=800)
image scene_23_01 = Transform("images/illustrations/scene_23_01.png", xsize=600, ysize=800)
image scene_25_01 = Transform("images/illustrations/scene_25_01.png", xsize=600, ysize=800)
image scene_26_01 = Transform("images/illustrations/scene_26_01.png", xsize=600, ysize=800)
image scene_29_01 = Transform("images/illustrations/scene_29_01.png", xsize=600, ysize=800)
image scene_31_01 = Transform("images/illustrations/scene_31_01.png", xsize=600, ysize=800)

label start_book:
    scene black
    show room_bg
    show book_bg:
        align (0.35, 0.5)
    with fade

    $ book_nvl_mode = True

    # maket 1
    $ book_page_side = "left"
    $ book_two_columns = False
    show scene_01_01 at book_masked, book_img_right with dissolve

    book_nvl "4 брошенных\nдуши"
    book_nvl "В последний вечер декабря,\nКогда Москва в огнях тонула,\nИ, светом праздничным горя,\nЗима в проулках прикорнула," 
    book_nvl "Шла Лада по тропе одна,\nМинуя людные кварталы.\nЕй не нужна была толпа,\nОна от праздника устала." 

    window hide
    nvl clear
    hide scene_01_01
    with dissolve

    # maket 2
    $ book_page_side = "right"
    show scene_02_01 at book_masked, book_img_left with dissolve
    show scene_02_02 at book_masked, book_img_right with dissolve

    book_nvl "В её квартире — блеск и шарм,\nГирлянд слепящие изломы,\nНо там царил иной пожар —\nПожар бездушья, всем знакомый." 
    book_nvl "Там мама, глядя в телефон,\nЛистала ленту раз за разом,\nА папа, позабыв про сон,\nРабочие решал заказы." 

    window hide
    nvl clear
    hide scene_02_01
    hide scene_02_02
    with dissolve

    # maket 3
    $ book_page_side = "right"
    show scene_03_01 at book_masked, book_img_left with dissolve

    book_nvl "Никто не звал её играть,\nНе слышал тихие вопросы,\nИ Лада вышла погулять,\nВдыхая снежный вихрь носом." 
    book_nvl "Она не знала, почему\nЕё влекло в ночную стужу,\nНо прорезая взглядом тьму,\nОна нашла тех, кому хуже." 
    book_nvl "Свернув за угол, в старый двор,\nГде арки высились угрюмо,\nОна поникла сквозь укор,\nВдохнувши воздух без парфюма." 

    window hide
    nvl clear
    hide scene_03_01
    with dissolve

    # maket 4
    $ book_page_side = "left"
    show scene_04_01 at book_masked, book_img_right with dissolve

    book_nvl "Там, в подворотне, у стены,\nГде ветер выл в пустых проёмах,\nЛежали те, кто лишены\nТепла и ласки в стенах дома." 
    book_nvl "Две кошки, пёс — один клубок,\nЕдва дыша в морозном прахе.\nИх путь был горек и жесток,\nОни дрожали в вечном страхе." 

    window hide
    nvl clear
    hide scene_04_01
    with dissolve

    # maket 5
    $ book_page_side = "right"
    show scene_05_01 at book_masked, book_img_left with dissolve

    book_nvl "Породный лоск ещё сиял\nНа шёрстке, спутанной и грязной,\nИх взгляд как выцветший кристалл —\nСветился горестью несчастья." 
    book_nvl "Они породисты, стройны,\nНо голод высушил их жилы.\nВ тени полуночной луны\nОни искали крохи силы." 

    window hide
    nvl clear
    hide scene_05_01
    with dissolve

    # maket 6
    $ book_page_side = "right"
    show scene_06_01 at book_masked, book_img_left with dissolve

    book_nvl "Шагнула девочка вперёд,\nСнежком под обувью хрустя,\nИ вздрогнул маленький комок,\nВ беду поверив не шутя." 
    book_nvl "Они метнулись по углам,\nШипя и прячась в тени зданий.\nУже не веря ни словам,\nНи горькой правде ожиданий." 

    window hide
    nvl clear
    hide scene_06_01
    with dissolve

    # maket 7
    $ book_page_side = "left"
    show scene_07_01 at book_masked, book_img_right with dissolve

    book_nvl "Но Лада, вынув свой запас —\nПеченья горсть из-под пальто,\nИх приманила в этот час\nТеплом, что не дарил никто." 
    book_nvl "«Не бойтесь, милые мои,\nЯ не обижу, я не трону.\nПусть в этом мире нет любви,\nЯ принесла тепла немного»." 

    window hide
    nvl clear
    hide scene_07_01
    with dissolve

    # maket 8
    $ book_page_side = "right"
    show scene_08_01 at book_masked, book_img_left with dissolve

    book_nvl "Она рассыпала еду\nНа ледяном, глухом бетоне,\nИ звери, чуя доброту,\nСмягчились в робком полутоне." 
    book_nvl "Они поели, и в тиши,\nГде снег ложился на ресницы,\nОткрылись тайны их души,\nЛистая прошлого страницы." 

    window hide
    nvl clear
    hide scene_08_01
    with dissolve

    # maket 9
    $ book_page_side = "left"

    book_nvl "«Спасибо», — вдруг раздался бас,\nПёс поклонился ей смиренно.\nСлеза застыла возле глаз\nОт этой речи сокровенной." 
    $ book_page_side = "right"
    book_nvl "Она пустилась со двора,\nДомой неслась в немом испуге,\nЧтоб маме с папой всё сказать\nО говорящем, странном друге." 

    window hide
    nvl clear
    with dissolve

    # maket 10
    $ book_page_side = "left"
    show scene_10_01 at book_masked, book_img_right with dissolve

    book_nvl "Влетела в зал: «Мамуля! Там —\nТам трое мёрзнут у порога!\nПёс говорил... Клянусь я вам!\nИх нужно покормить немного!»" 
    book_nvl "Но мама, вперившись в экран,\nГде мишура и блеск мелькали,\nСквозь сеть своих душевных ран,\nНе видела её печали." 
    book_nvl "Сказала скользко: «Не мешай!\nУ нас готовки выше крыши.\nИди к себе, воображай,\nИ будь, пожалуйста, потише»." 

    window hide
    nvl clear
    hide scene_10_01
    with dissolve

    # maket 11
    $ book_page_side = "left"
    show scene_11_01 at book_masked, book_img_right with dissolve

    book_nvl "«С работы папиной придут\nСегодня значимые люди.\nПорядок важен там и тут,\nЗакуски ждут уже на блюде." 
    book_nvl "«Ему сулят большой скачок,\nСудьба вот-вот преобразится.\nА ты несёшь какой-то вздор...\nИди-ка в комнату, девица!»" 
    book_nvl "Отец мелькнул в тени дверей,\nВ плену отчётов и созвонов:\n«Потом обсудим тех зверей,\nГорят дедлайны договоров»." 

    window hide
    nvl clear
    hide scene_11_01
    with dissolve

    # maket 12
    $ book_page_side = "right"
    show scene_12_01 at book_masked, book_img_left with dissolve

    book_nvl "Ушла девчонка в темноту,\nК своим пластмассовым игрушкам.\nХраня на сердце пустоту,\nПрипала к мягеньким подушкам." 
    book_nvl "Но образ тех, кто на снегу\nДрожал, прижавшися друг к другу,\n“Их позабыть я не смогу,\nВ последний день земного круга." 

    window hide
    nvl clear
    hide scene_12_01
    with dissolve

    # maket 13
    $ book_page_side = "left"
    show scene_13_01 at book_masked, book_img_right with dissolve

    book_nvl "Она решилась. В тишине,\nКогда на кухне стихли звуки,\nПри бледном, лунном полотне,\nСмиряя дрожь и сердца стуки." 
    book_nvl "Сама достала весь запас\nМясных нарезок и колбаски,\nЗабыв про страх в полночный час,\nПоверив в истинность той сказки." 
    book_nvl "Взяла пакет еды с собой,\nЗабыв про праздничный запрет,\nИ вновь шагнула в мрак ночной,\nОставив в доме тусклый свет." 

    window hide
    nvl clear
    hide scene_13_01
    with dissolve

    # maket 14
    $ book_page_side = "right"
    show scene_14_01 at book_masked, book_img_left with dissolve

    book_nvl "Скрывал бетон промёрзших плит\nТроих несчастных в снежной пыли.\nЗнакомый силуэт манит,\nО ком давно все позабыли." 
    book_nvl "С руки кормила — по куску,\nИ лапы к пальцам льнули смело.\nИз самых дальних уголков\nЖивое слово зазвенело." 

    window hide
    nvl clear
    hide scene_14_01
    with dissolve

    # maket 15
    $ book_page_side = "left"
    show scene_15_01 at book_masked, book_img_right with dissolve

    book_nvl "Сказал сперва печальный пёс,\nЧьи уши падали на лапы,\nКто сквозь всю жизнь обиду нёс\nИ знал предательства ухабы." 
    book_nvl "Меня в коробку положили,\nОбвили лентой золотой.\nРодители щенка купили,\nЧтоб сын не мучил их мольбой." 
    book_nvl "Он ждал породистого зверя,\nЧтоб гордо за собой вести.\nА я в любовь его поверил,\nЕдва успев порог пройти." 

    window hide
    nvl clear
    hide scene_15_01
    with dissolve

    # maket 16
    $ book_page_side = "right"
    show scene_16_01 at book_masked, book_img_left with dissolve

    book_nvl "Для них я был — декор на праздник,\nИгрушка, чтоб занять досуг.\nНе ведал маленький проказник,\nЧто я — живой, что я — их друг." 
    book_nvl "Но время шло — я стал не нужен,\nОбузой лишней на пути.\nИ вот, мороз, в ночи застужен,\nУслышал краткое: «Уйди»." 

    window hide
    nvl clear
    hide scene_16_01
    with dissolve

    # maket 17
    $ book_page_side = "left"
    show scene_17_01 at book_masked, book_img_right with dissolve

    book_nvl "Им стало в тягость ежедневно\nМеня на улицу водить.\nСказала мать: «Он слишком нервный,\nПора его нам проводить»." 
    book_nvl "Меня за шкирку — и в метели,\nСквозь двери, в ледяной оскал.\nПонять меня не захотели,\nПока я преданно кивал." 

    window hide
    nvl clear
    hide scene_17_01
    with dissolve

    # maket 18
    $ book_page_side = "right"
    show scene_18_01 at book_masked, book_img_left with dissolve

    book_nvl "Вторым раздался тихий звук —\nТо кошка белая вздохнула.\nСквозь череду полночных мук\nОна в былое заглянула." 
    book_nvl "Сказала кошка, что бела,\nКак снег на утреннем рассвете:\n«Я с доброй бабушкой жила,\nМы были счастливы, как дети." 
    book_nvl "Она поила молоком,\nДелила кресло и подушку.\nНо опустел внезапно дом,\nНикто не гладил по макушке." 

    window hide
    nvl clear
    hide scene_18_01
    with dissolve

    # maket 19
    $ book_page_side = "left"
    show scene_19_01 at book_masked, book_img_right with dissolve

    book_nvl "Её не стало. В тот же миг\nНаследник в дом вошёл, ликуя.\nОн подавил победный крик,\nНаживу жадную почуяв." 

    window hide
    nvl clear
    hide scene_19_01
    with dissolve

    # maket 20
    $ book_page_side = "right"
    show scene_20_01 at book_masked, book_img_left with dissolve

    book_nvl "Меня он втиснул в свой пакет,\nИ мир вокруг пошёл вращаться.\nПогас навеки тёплый свет,\nВелев с надеждой распрощаться." 
    book_nvl "Очнулась я среди ведра,\nВ помойной яме, в грязной жиже.\nТеперь ничья я здесь, сестра,\nКонец судьбы моей всё ближе»." 

    window hide
    nvl clear
    hide scene_20_01
    with dissolve

    # maket 21
    $ book_page_side = "left"
    show scene_21_01 at book_masked, book_img_right with dissolve

    book_nvl "Был третьим кот — сплошная мгла,\nС глазами, полными раздора.\nЕго душа, как сталь, была,\nВ плену людского приговора." 
    book_nvl "«Я заперт был в плену квартир,\nГде миска сутками пустела.\nИ мой кошачий, хрупкий мир\nОбида жгучая задела." 

    window hide
    nvl clear
    hide scene_21_01
    with dissolve

    # maket 22
    $ book_page_side = "right"

    book_nvl "Я мебель рвал, чтоб не завыть,\nЧтоб голос голода умерить.\nНо не могли меня простить,\nВ мой зов не пожелав поверить." 
    book_nvl "Меня лупили за протест,\nЗа каждый след на коже кресел.\nСреди пустых и мёртвых мест\nМир был до ужаса невесел." 

    window hide
    nvl clear
    with dissolve

    # maket 23
    $ book_page_side = "right"
    show scene_23_01 at book_masked, book_img_left with dissolve

    book_nvl "Но ветер вдруг окно открыл,\nМаня в ночную бесконечность.\nЯ прыгнул вниз, набравшись сил,\nШагнув из этой клетки в вечность." 
    book_nvl "Я одинок, я зол, я дик,\nНе верю больше вашим ласкам.\nНо этот хлеб, и этот миг,\nОн для меня подобен сказке»." 

    window hide
    nvl clear
    hide scene_23_01
    with dissolve

    # maket 24
    $ book_page_side = "left"

    book_nvl "Девчонка слушала, и в ней\nСквозь холод истина росла.\nМир стал прозрачней и больней,\nОна их к сердцу привлекла." 
    book_nvl "«Я тоже лишняя для них,\nВ своей игрушечной неволе.\nСреди подарков золотых\nНе нахожу любви ни доли." 
    book_nvl "Они не видят моих глаз,\nЗабыв про близость и про дом.\nВсе заняты своим «сейчас»,\nОставив счастье на «потом»." 

    window hide
    nvl clear
    with dissolve

    # maket 25
    $ book_page_side = "right"
    show scene_25_01 at book_masked, book_img_left with dissolve

    book_nvl "Четыре сердца в унисон\nСтучали робко под навесом.\nМир погружался в зимний сон,\nСкрывая горе за завесой." 
    book_nvl "Ударил в полночь громкий бой,\nИ небо вспыхнуло огнями.\nСалют над сонной головой\nРассыпал искры над домами." 
    book_nvl "В смятенье души содрогнулись,\nТеряя в грохоте покой,\nНо к Ладе робко потянулись,\nНайдя защиту под рукой." 

    window hide
    nvl clear
    hide scene_25_01
    with dissolve

    # maket 26
    $ book_page_side = "left"
    show scene_26_01 at book_masked, book_img_right with dissolve

    book_nvl "Она их крепко обнимала,\nШепча заветные слова.\nИ боль бесследно исчезала\nВ лучах ночного торжества." 
    book_nvl "И вдруг — шаги. И чей-то зов\nПронзил безлюдье полуночи.\nСредь беспощадных холодов\nОна взглянула маме в очи." 
    book_nvl "В глазах у мамы — дикий страх,\nСтальной, как отблеск на свинце.\nДрожали слёзы на глазах,\nи застывали на лице." 

    window hide
    nvl clear
    hide scene_26_01
    with dissolve

    # maket 27
    $ book_page_side = "right"

    book_nvl "И мать увидела дитя,\nЧто греет брошенных зверей.\nОт холодов едва дыша,\nСреди сугробов и теней." 
    book_nvl "А звери, сбившись в тесный круг,\nИ от мороза защищали,\nЗабыв про холод и испуг\nСвоё тепло ей отдавали." 
    book_nvl "Застыли взрослые. И стыд\nИм горло стиснул изнутри.\nСломался прежний строгий вид —\nИ стало слышно: «Мы свои»." 

    window hide
    nvl clear
    with dissolve

    # maket 28
    $ book_page_side = "left"

    book_nvl "И осознали в этот миг,\nКак много счастья проглядели.\nИ каждый здесь душой постиг\nВсю ценность данного мгновенья." 
    book_nvl "«Прости нас, Лада. Мы отныне\nИначе будем жить с тобой.\nПусть лёд в сердцах навеки сгинет,\nПриняв и ласку, и покой»." 
    book_nvl "И мама, плача, их обняла —\nЖивых, загубленных бедой.\nИм нежностью всю свою отдала,\nЗакрыв дорогу в мрак былой." 
    book_nvl "Всех трёх — измученных, больных —\nИх дома приняли с любовью.\nИсчезла горечь дней былых,\nВсе попрощались с прошлой болью." 

    window hide
    nvl clear
    with dissolve

    # maket 29
    $ book_page_side = "right"
    show scene_29_01 at book_masked, book_img_left with dissolve

    book_nvl "Жизнь забурлила в тех стенах,\nСтал дом светлее и чудесней.\nУшёл из мыслей горький страх,\nСменившись звонкой, доброй песней." 
    book_nvl "Теперь с собакой в дождь и снег\nСпешат на улицу гурьбою.\nИ слышен лапок звонкий бег\nНад предрассветною землёю." 

    window hide
    nvl clear
    hide scene_29_01
    with dissolve

    # maket 30
    $ book_page_side = "left"

    book_nvl "Котам — деликатесов ряд,\nИх балуют нарезкой вкусной.\nИ звери преданно глядят,\nЗабыв о доле своей грустной." 
    book_nvl "А ночью, в звёздной тишине,\nКогда пурга стучит в окошко,\nОни приходят как во сне —\nИ верный пёс, и две их кошки." 
    book_nvl "Свернувшись в тесный, тёплый круг,\nОни заснут с девчушкой рядом.\nКак в час полночных зимних вьюг,\nСогреты верным, добрым взглядом." 

    window hide
    nvl clear
    with dissolve

    # maket 31
    $ book_page_side = "right"
    show scene_31_01 at book_masked, book_img_left with dissolve

    book_nvl "Прошли года. И повзрослев\nДорогу Лада обрела.\nТеперь она — защита тех,\nЧья жизнь всем стала не мила." 
    book_nvl "В приюте лечит и спасает,\nМир воскресшая добротой.\nОна о прошлом вспоминает,\nС той новогоднею судьбой." 
    book_nvl "Она запомнила метель,\nИ как шептало ей зверьё.\nОдна ночная канитель\nСменила прежнюю её." 

    window hide
    nvl clear
    hide scene_31_01
    with dissolve

    $ book_nvl_mode = False
    return
label start_book_2:
    scene black
    show room_bg
    show book_bg:
        align (0.35, 0.5)
    with fade

    $ book_nvl_mode = True

    # --- СТРАНИЦА 1 ---
    $ book_page_side = "left"
    $ book_two_columns = False
    show illustration_girl at book_masked, book_img_right with dissolve
    
    book_nvl "В последний вечер декабря,\nКогда Москва в огнях тонула,"
    book_nvl "И, светом праздничным горя,\nЗима в проулках прикорнула,"
    book_nvl "Шла Лада по тропе одна,\nМинуя людные кварталы."
    
    window hide
    nvl clear
    hide illustration_girl
    with dissolve

    # --- СТРАНИЦА 2 ---
    $ book_page_side = "right"
    show illustration_lonely at book_masked, book_img_left with dissolve
    
    book_nvl "Там мама, глядя в телефон,\nЛистала ленту раз за разом,"
    book_nvl "А папа, позабыв про сон,\nРабочие решал заказы."
    
    window hide
    nvl clear
    hide illustration_lonely
    with dissolve

    # --- СТРАНИЦА 3 ---
    $ book_page_side = "left"
    show illustration_girl_room at book_masked, book_img_right with dissolve
    
    book_nvl "Там мама, глядя в телефон,\nЛистала ленту раз за разом,"
    book_nvl "А папа, позабыв про сон,\nРабочие решал заказы."
    
    window hide
    nvl clear

    # --- СТРАНИЦА 4 ---
    $ book_two_columns = True

    show illustration_cat_angry_small at book_masked, book_img_left_small with dissolve
    book_nvl "{vspace=300}Свернув за угол, в старый двор,\nГде арки высились угрюмо,"
    book_nvl "Она поникла сквозь укор,\nВдохнувши воздух без парфюма."
    book_nvl "Там, в подворотне, у стены,\nГде ветер выл в пустых проёмах,\nЛежали те, кто лишены\nТепла и ласки в стенах дома."

    book_nvl "Свернув за угол, в старый двор,\nГде арки высились угрюмо,"
    book_nvl "Она поникла сквозь укор,\nВдохнувши воздух без парфюма."
    book_nvl "Там, в подворотне, у стены,\nГде ветер выл в пустых проёмах,\nЛежали те, кто лишены\nТепла и ласки в стенах дома."
    hide illustration_cat_angry_small

    window hide
    nvl clear
    $ book_nvl_mode = False
    return
