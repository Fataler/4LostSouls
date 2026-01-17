init python:
    def show_book_img(img_name):
        if store.book_text_side == "left":
            pos_transform = book_img_right()
        else:
            pos_transform = book_img_left()
            
        store.book_current_img = img_name
        renpy.show(img_name, at_list=[book_masked(), pos_transform])
        renpy.with_statement(dissolve)

    def book_clear():
        if store.book_current_img:
            renpy.hide(store.book_current_img)
            store.book_current_img = None
        nvl_clear()

        renpy.sound.play(renpy.random.choice([sfx_page_1, sfx_page_2, sfx_page_3, sfx_page_4, sfx_page_5]))
        renpy.with_statement(dissolve)

label start_book:
    play music music_amberlight fadein 1.0 fadeout 1.0
    scene black
    show bg_book
    show bg_book_elka zorder 10:
        align (-0.01, -0.01)
        zoom 1.1

    show bg_book_svet onlayer screens zorder 101:
        anchor (1.0, 0.0)
        align (1.0, 0.0)
    with fade

    show book_logo:
        pos (0.30, 0.32)
        anchor (0.5, 0.5)
        zoom 0.8

    $ book_nvl_mode = True
    $ quick_menu = True

    # p 1
    $ book_text_side = "left"
    $ book_page_stanzas = 2
    $ show_book_img("scene_1_image")
    
    play sfx3 sfx_winter_wind loop fadein 2.0
    play sfx2 sfx_snow_steps_1

    book_nvl "{vspace=200}В последний вечер декабря,\nКогда Москва в огнях тонула,\nИ, светом праздничным горя,\nЗима в проулках прикорнула," 
    
    play sfx sfx_crowd fadein 1.0
    book_nvl "Шла Лада по тропе одна,\nМинуя людные кварталы.\nЕй не нужна была толпа,\nОна от праздника устала."

    stop sfx3 fadeout 1.0
    stop sfx2 fadeout 1.0
    stop sfx fadeout 1.0

    hide book_logo 
    with dissolve

    $ book_clear()

    # p 2
    $ book_text_side = "right"
    $ show_book_img("scene_2_image")
    $ book_page_stanzas = 3

    book_nvl "В её квартире — всё «как надо»:\nГирлянды, ленты, мишура,\nНо в этом праздничном фасаде\nЛишь отстранённость и хандра." 
    book_nvl "Там каждый угол был согрет\nЛишь электрическим сияньем,\nНо правды в том сиянье нет —\nОдно холодное молчанье." 
    book_nvl "Где мама, глядя в телефон,\nЛистала ленту раз за разом,\nА папа, позабыв про сон,\nРабочие решал заказы." 
    
    $ book_clear()

    # p 3
    $ book_text_side = "right"
    $ show_book_img("scene_3_image")
    $ book_page_stanzas = 2
    play sfx2 sfx_winter_wind loop fadein 2.0
    play sfx3 sfx_snow_steps_2
    play sfx sfx_crowd

    book_nvl "Никто не звал её играть,\nНе слышал тихие вопросы,\nИ Лада вышла погулять,\nВдыхая зимний воздух носом." 
    stop sfx fadeout 1.0
    play sfx2 sfx_dog_whine
    book_nvl "Скрываясь от людского гула,\nОна вошла в притихший двор,\nНо вдруг у баков, в глубине,\nСкребнулся кто-то, словно вор." 
    
    $ book_clear()

    # p 4
    $ book_text_side = "left"
    $ show_book_img("scene_4_image")
    $ book_page_stanzas = 3

    play sfx2 sfx_cat_cry
    book_nvl "Там, в подворотне, у стены,\nГде ветер выл в пустых проёмах,\nЛежали те, кто лишены\nТепла и ласки в стенах дома." 
    book_nvl "Две кошки, пёс — один клубок,\nЕдва дыша в морозной стуже.\nИх путь был горек и жесток,\nИм с каждым мигом только хуже." 
    book_nvl "Природный лоск ещё сиял\nНа шёрстке, спутанной и грязной,\nА взгляд, как выцветший кристалл —\nСветился горестью несчастья." 

    stop sfx2 fadeout 1.0
    $ book_clear()

    # p 5
    $ book_text_side = "right"
    $ show_book_img("scene_5_image")
    $ book_page_stanzas = 2
    play sfx sfx_cat_meow
    play sfx2 sfx_snow_step

    book_nvl "Шагнула девочка вперёд,\nСтупая робко, как по льду.\nИ вздрогнул маленький комок…\nИ сжался, чувствуя беду." 
    play sfx3 sfx_cat_angry_2
    book_nvl "Они метнулись по углам,\nШипя и прячась в тени зданий.\nУже не веря ни словам,\nНи горькой правде ожиданий." 

    stop sfx3 fadeout 1.0
    stop sfx2 fadeout 1.0
    stop sfx fadeout 1.0
    $ book_clear()

    # p 6
    $ book_text_side = "right"
    $ show_book_img("scene_6_image")
    $ book_page_stanzas = 2

    book_nvl "Но Лада, вынув свой запас\nПеченья горсть со дна кармана,\nСказала тихо: «Это вам»,\nБез капли фальши и обмана." 
    book_nvl "«Не бойтесь, милые мои,\nЯ не обижу, я не трону.\nВы в этом мире не одни,\nЯ принесла тепла немного»." 

    $ book_clear()

    # p 7
    $ book_text_side = "left"
    $ show_book_img("scene_7_image")
    $ book_page_stanzas = 3

    book_nvl "Рассыпав крошки на бетон,\nОна ждала, не шевелясь.\nИ тихий, недовольный рык\nЗатих, доверием сменясь." 
    play sfx2 sfx_dog_bark
    book_nvl "«Спасибо», — вдруг раздался бас,\nПёс поклонился ей смиренно.\nИ Лада вздрогнула тотчас,\nУшам не веря совершенно." 
    play sfx sfx_snow_run
    book_nvl "Она пустилась со двора,\nДомой неслась в немом испуге,\nЧтоб маме с папой рассказать\nО говорящем, странном друге." 

    stop sfx2 fadeout 1.0
    stop sfx fadeout 1.0

    $ book_clear()

    # p 8
    $ book_text_side = "right"
    $ show_book_img("scene_8_image")
    $ book_page_stanzas = 3

    play music music_hope fadein 1.0 fadeout 1.0

    play sfx2 [ "<silence 3.0>", sfx_door_open ]

    book_nvl "Влетела в зал: «Мамуля! Там —\nТам трое мёрзнут у порога!\nПёс говорил... Клянусь я вам!\nИх нужно покормить немного!»" 
    book_nvl "Но мама, вперившись в экран,\nГде мишура и блеск мелькали,\nСквозь сеть своих душевных ран,\nНе видела её печали." 
    book_nvl "Сказала сухо: «Не мешай!\nУ нас готовки выше крыши.\nИди к себе, воображай,\nИ будь, пожалуйста, потише»." 

    $ book_clear()

    # p 9
    $ book_text_side = "left"
    $ show_book_img("scene_9_image")
    $ book_page_stanzas = 3
    
    book_nvl "«С работы папиной придут\nСегодня значимые люди.\nПорядок важен там и тут,\nЗакуски ждут уже на блюде!" 
    book_nvl "Ему сулят большой скачок,\nСудьба вот-вот преобразится.\nА ты несёшь какой-то вздор...\nИди-ка в комнату, девица!»" 
    book_nvl "Отец мелькнул в тени дверей,\nВ плену отчётов и созвонов:\n«Потом обсудим тех зверей,\nГорят дедлайны договоров»." 

    $ book_clear()

    # p 10
    $ book_text_side = "left"
    $ show_book_img("scene_10_image")
    $ book_page_stanzas = 2

    play sfx sfx_door_open
    book_nvl "Ушла девчонка в темноту,\nК своим пластмассовым игрушкам.\nХраня на сердце пустоту,\nПрипала к мягеньким подушкам." 
    book_nvl "Но зов зверей, что на снегу,\nПронзал её сквозь стены дома.\n«Я бросить их там не смогу»,\nЕй эта боль до слёз знакома." 
    
    $ book_clear()

    # p 11
    $ book_text_side = "left"
    $ show_book_img("scene_11_image")
    $ book_page_stanzas = 3

    book_nvl "Она решилась. В тишине,\nКогда на кухне стихли звуки,\nПри бледном, лунном полотне,\nСмиряя дрожь и сердца стуки," 
    play sfx sfx_door_open
    book_nvl "Сама достала весь запас\nМясных нарезок и колбаски,\nЗабыв испуг в полночный час,\nНе зная страха и опаски." 
    
    book_nvl "Взяла пакет еды с собой,\nЗабыв родительский запрет,\nИ вновь шагнула в мрак ночной,\nОставив в доме тусклый свет." 

    $ book_clear()

    # p 12
    $ book_text_side = "right"
    $ show_book_img("scene_12_image")
    $ book_page_stanzas = 2

    play sfx sfx_winter_wind loop fadein 3.0
    play sfx2 sfx_snow_run
    book_nvl "Спешила Лада, что есть сил,\nЗабыв про холод и покой.\nТот самый двор её манил,\nСвоей привычной темнотой." 
    book_nvl "Скрывал бетон промёрзших плит\nТроих несчастных в снежной пыли.\nИх холод насмерть леденит,\nО них совсем все позабыли." 
    
    $ book_clear()

    # p 13
    $ book_text_side = "left"
    $ show_book_img("scene_13_image")
    $ book_page_stanzas = 2
    stop sfx2 fadeout 1.0
    play sound sfx_dog_eating loop

    book_nvl "Под рыжим светом фонаря,\nРассыпав мясо по плите,\nОна смотрела, не таясь,\nКак ели трое в темноте." 
    stop sound fadeout 1.0
    book_nvl "Когда окончился обед,\nИ смолк последний тихий хруст,\nРаздался девочке в ответ\nЛюдской язык из зверьих уст." 
    
    $ book_clear()

    # p 14
    $ book_text_side = "right"
    $ show_book_img("scene_14_image")
    $ book_page_stanzas = 3

    stop sfx fadeout 1.0
    
    play sfx sfx_dog_bark
    play music music_snow_plains fadein 1.0 fadeout 1.0

    book_nvl "Сказал сперва печальный пёс,\nЧьи уши падали на лапы,\nКто сквозь всю жизнь обиду нёс\nИ знал предательства ухабы." 
    book_nvl "«Меня под ёлку положили,\nОбвили лентой золотой.\nРодители щенка купили,\nЧтоб сын не мучил их мольбой." 
    book_nvl "Он ждал породистого зверя,\nЧтоб гордо за собой вести.\nА я в любовь его поверил,\nЕдва успев порог пройти." 

    $ book_clear()

    # p 15
    $ book_text_side = "left"
    $ show_book_img("scene_15_image")
    $ book_page_stanzas = 2

    play sfx sfx_dog_bark
    book_nvl "Для них я был — декор на праздник,\nИгрушка, чтоб занять досуг.\nНе ведал маленький проказник,\nЧто я — живой, что я — их друг." 
    book_nvl "Шло время, и запал угас,\nМальчишке стало всё равно.\nК такой ответственности разом\nПривыкнуть не было дано." 

    $ book_clear()

    # p 16
    $ book_text_side = "right"
    $ show_book_img("scene_16_image")
    $ book_page_stanzas = 2

    book_nvl "Им стало в тягость ежедневно\nСо мной на улице гулять.\nСказала мать: «Он слишком нервный,\nПора его нам прогонять»." 
    book_nvl "Меня за шкирку — и в метели,\nСквозь двери, в ледяной оскал.\nПонять меня не захотели,\nПока я преданно кивал»." 

    $ book_clear()

    # p 17
    $ book_text_side = "left"
    $ show_book_img("scene_17_image")
    $ book_page_stanzas = 3
    play audio sfx_cat_meow

    book_nvl "Вторым раздался тихий звук —\nТо кошка белая вздохнула.\nСквозь череду душевных мук\nОна в былое заглянула." 

    play audio sfx_cat_purr
    book_nvl "Сказала кошка, что бела,\nКак снег на утреннем рассвете:\n«Я с доброй бабушкой жила,\nМы были счастливы, как дети." 
    book_nvl "Она поила молоком,\nДелила кресло и подушку.\nНо опустел внезапно дом,\nНикто не гладил по макушке." 
    
    $ book_clear()

    # p 18
    $ book_text_side = "right"
    $ show_book_img("scene_18_image")
    $ book_page_stanzas = 2

    play sfx sfx_cat_cry
    book_nvl "Её не стало. В тот же миг\nНаследник в дом вошёл, ликуя.\nОн подавил победный крик,\nНаживу жадную почуяв." 
    book_nvl "Он обводил жильё глазами,\nПрикинув ценник за добро.\nИ, встретясь взглядом вдруг со мною,\nПронзил мне страхом всё нутро." 
    
    $ book_clear()

    # p 19
    $ book_text_side = "left"
    $ show_book_img("scene_19_image")
    $ book_page_stanzas = 2

    book_nvl "Меня он втиснул в свой пакет,\nИ мир вокруг пошёл вращаться.\nПогас навеки тёплый свет,\nВелев с надеждой распрощаться." 
    book_nvl "И вот среди гнилья, тряпья,\nЯ в яме той, в помойной жиже.\nТеперь я здесь совсем ничья,\nКонец судьбы моей всё ближе»." 
    stop sfx fadeout 1.0
    
    $ book_clear()

    # p 20
    $ book_text_side = "right"
    $ show_book_img("scene_20_image")
    $ book_page_stanzas = 2

    play sfx2 sfx_cat_angry_1
    book_nvl "Был третьим кот — сплошная мгла,\nС глазами, полными раздора.\nЕго душа, как сталь, была,\nВ плену людского приговора." 
    book_nvl "«Я заперт был в плену квартир,\nГде миска сутками пустела.\nИ мой кошачий, хрупкий мир\nОбида жгучая задела." 
    
    $ book_clear()

    # p 21
    $ book_text_side = "left"
    $ show_book_img("scene_21_image")
    $ book_page_stanzas = 2

    play sfx2 sfx_cat_angry_2
    book_nvl "Я мебель рвал, чтоб не завыть,\nЧтоб голос голода умерить.\nНо не могли меня простить,\nВ мой зов не пожелав поверить." 
    play sfx sfx_slap
    book_nvl "Меня лупили за протест,\nЗа каждый шрам на коже кресел.\nТвердили: «Злой, кусучий бес»,\nИ от того я был невесел." 
    
    stop sfx fadeout 1.0
    stop sfx2 fadeout 1.0
    $ book_clear()

    # p 22
    $ book_text_side = "right"
    $ show_book_img("scene_22_image")
    $ book_page_stanzas = 3

    book_nvl "Я затаился, план берёг,\nСмиряя дрожь в когтистых лапах.\nТерпеть я больше их не мог —\nНи этот дом, ни этот запах." 
    play sfx sfx_winter_wind
    book_nvl "Но ветер вдруг окно открыл,\nМаня в ночную бесконечность.\nЯ прыгнул вниз, набравшись сил,\nШагнув из этой клетки в вечность." 
    book_nvl "Я одинок, я зол, я дик,\nНе верю больше вашим ласкам.\nНо этот пир, и этот миг,\nОн для меня подобен сказке»." 
    stop sfx fadeout 1.0
    $ book_clear()

    # p 23
    $ book_text_side = "right"
    $ show_book_img("scene_23_image")
    $ book_page_stanzas = 3

    play music music_lost_in_the_quiet fadein 1.0 fadeout 1.0

    book_nvl "Девчонка слушала, и в ней\nСквозь холод истина росла.\nМир стал прозрачней и ясней,\nОна всю боль их поняла." 
    book_nvl "«Я тоже лишняя для них,\nВ своей игрушечной неволе.\nСреди подарков дорогих\nНе нахожу себе я роли." 
    book_nvl "Они не видят моих глаз,\nЗабыв про близость и про дом.\nВсе заняты своим «сейчас»,\nОставив жизнь на «потом»»." 
    
    $ book_clear()

    # p 24
    $ book_text_side = "left"
    $ show_book_img("scene_24_image")
    $ book_page_stanzas = 2

    book_nvl "Четыре сердца в унисон\nСтучали робко под луной.\nМир погружался в зимний сон,\nУкрыв их белой пеленой." 
    book_nvl "Они сидели чуть дыша,\nНе слыша ветра злой порыв.\nЗабыв обиды снежный ком,\nСвои печали позабыв." 
    
    $ book_clear()

    # p 25
    $ book_text_side = "right"
    $ show_book_img("scene_25_image")
    $ book_page_stanzas = 3
    play sfx sfx_fireworks loop fadein 1.0

    book_nvl "Ударил в полночь громкий бой,\nИ небо вспыхнуло огнями.\nСалют вверху над головой\nРассыпал искры над домами." 
    play sfx2 sfx_cat_angry_1 
    book_nvl "Гремел как гром, как плеть по нервам,\nУдар в лицо, небесный шквал.\nКлубок друзей в порыве этом\nСвою погибель ожидал." 
    book_nvl "Но Лада робко их обняла,\nДаря покой своей рукой,\nИ темнота двора вдруг стала\nНадёжной крепостью, стеной." 

    stop sfx fadeout 1.0
    stop sfx2 fadeout 1.0
    $ book_clear()

    # p 26
    $ book_text_side = "left"
    $ show_book_img("scene_26_image")
    $ book_page_stanzas = 3

    book_nvl "И вдруг — шаги. И чей-то зов\nПронзил затишье в этот час.\nСредь беспощадных холодов\nМать шла, не закрывая глаз." 
    book_nvl "И мать увидела дитя,\nЧто греет брошенных зверей.\nОт холодов едва дыша,\nСреди сугробов и теней." 
    book_nvl "Застыли взрослые. И стыд\nСтеснил дыханье в тишине.\nИ каждый был теперь открыт,\nПризнав свою вину вполне." 
    
    $ book_clear()

    # p 27
    $ book_text_side = "right"
    $ show_book_img("scene_27_image")
    $ book_page_stanzas = 3

    play sfx sfx_dog_bark_happy
    book_nvl "И осознали в этот миг,\nЧто всё не то они ценили.\nВ душе у каждого — тупик,\nО самом важном позабыли." 
    book_nvl "«Прости нас, Лада. Обещаем,\nЧто станет всё у нас иным.\nМы лёд из сердца убираем,\nНаполним дом теплом живым»." 
    play sfx sfx_cat_meow
    book_nvl "«Мам, можно?..» — но пресёк мольбу\nУ папы голос, ставший мягким:\n«Всех заберём! Свою судьбу\nРазделим с ними в доме ярком»." 

    $ book_clear()

    # p 28
    $ book_text_side = "left"
    $ show_book_img("scene_28_image")
    $ book_page_stanzas = 3
    
    stop sound fadeout 3.0
    play sfx2 sfx_dog_bark_happy
    play sfx sfx_cat_purr fadein 1.0

    book_nvl "{vspace=-50}{space=200}***\nВсех трёх — измученных, больных —\nВ семью их приняли с любовью.\nИсчезла горечь дней былых,\nВсе попрощались с прошлой болью." 
    book_nvl "Жизнь забурлила в тех стенах,\nСтал дом светлее и чудесней.\nУшёл из мыслей горький страх,\nСменившись доброй звонкой песней." 
    book_nvl "Теперь с собакой в дождь и снег\nСпешат на улицу гурьбою.\nИ слышен лапок звонкий бег\nНад предрассветною землёю." 

    $ book_clear()

    # p 29
    $ book_text_side = "right"
    $ show_book_img("scene_29_image")
    $ book_page_stanzas = 2
    play sfx sfx_dog_eating

    book_nvl "Котам — деликатесов ряд,\nИх балуют нарезкой вкусной.\nИ звери преданно глядят,\nЗабыв о жизни своей грустной." 
    stop sfx fadeout 1.0

    play sfx sfx_cat_purr
    book_nvl "Когда в квартире гаснет свет,\nОни всегда ложатся рядом.\nДля них теперь несчастья нет,\nИм больше ничего не надо." 
    
    stop sfx fadeout 1.0
    $ book_clear()

    # p 30
    $ book_text_side = "left"
    $ show_book_img("scene_30_image")
    $ book_page_stanzas = 3
   
    book_nvl "Прошли года. И, повзрослев,\nДорогу Лада обрела.\nТеперь она — защита тех,\nЧья жизнь всем стала не мила." 
    book_nvl "В приюте лечит и спасает,\nМир наполняя добротой.\nОна о прошлом вспоминает,\nС той новогоднею судьбой." 
    book_nvl "Она запомнила метель,\nИ как шептало ей зверьё.\nОдна ночная канитель\nСменила прежнюю её." 
    
    $ book_clear()

    # p 31
    $ book_text_side = "right"
    $ show_book_img("scene_31_image")
    $ book_page_stanzas = 3

    book_nvl "Но это знание теперь\nВедёт её сквозь тьму и свет.\nОткрыло в жизнь иную дверь,\nГде равнодушью места нет." 
    book_nvl "Хоть мир бывает слеп и глух,\nИ гаснет в нём священный пыл.\nНо не исчезнет верный дух,\nРаз ты кого-то полюбил." 
    book_nvl "Ты помни истину одну,\nПока в груди горит огонь:\nХрани в душе своей весну\nИ грей озябшую ладонь." 
    
    $ book_clear()

    # p 32
    $ book_text_side = "left"
    $ show_book_img("scene_32_image")
    $ book_page_stanzas = 3

    book_nvl "Кого ты в жизни приручил,\nТого в беде не оставляй.\nЗаботься, не жалея сил,\nОт всех невзгод их укрывай." 
    book_nvl "Не на минуту, не на час —\nНавек, пока стучат сердца.\nПусть доброта не гаснет в нас,\nВедя по жизни до конца." 
    book_nvl "Любовь — не слово, не хвала,\nА то, что греет нас в пути.\nИ только добрые дела\nПомогут правду обрести." 

    $ book_nvl_mode = False
    $ quick_menu = False
    stop sound fadeout 4.0
    scene bg_black with Dissolve(4.0)
    $ renpy.pause(2, hard=True)
    return
