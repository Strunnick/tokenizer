#-------------------------------------------------------------------------------
# Name:        Аббревиатуры
# Author:      ash-911
# Created:     01.07.2016
#-------------------------------------------------------------------------------

class abb(object):
    # свойства аббревиатуры
    # - требуется ли перед ней слово (сокращение)
    def __init__(self,ab="",ful="",frst=False):
        self.abb = ab
        self.full = ful
        self.first = frst
    def __str__(self):
        return self.abb
# словарь стандартных аббревиатур
ABBList = {}

def Init():
    # кириллические
    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
    ABBList["МУП"]=abb("МУП","муниципальное унитарное предприятие",False)
    ABBList["с.г.с."]=abb("с.г.с.","система государственных стандартов",False)
    ABBList["ИТАР"]=abb("ИТАР","Информационное телеграфное агентство России",False)
    ABBList["ЦСКА"]=abb("вуз","Центральный спортивный клуб армии",False)
    ABBList["НИИ"]=abb("НИИ","научно-исследовательский институт",False)
    ABBList["СНГ"]=abb("СНГ","содружество независимых государств",False)
    ABBList["КПД"]=abb("КПД","коэффициент полезного действия",False)
    ABBList["ЭВМ"]=abb("ЭВМ","электронно-вычислительная машина",False)
    ABBList["ГАБТ"]=abb("ГАБТ","государственный академический Большой театр",False)
    ABBList["ПТУ"]=abb("ПТУ","профессиональное техническое училище",False)
    ABBList["ССУЗ"]=abb("ССУЗ","среднее специальное учебное заведение",False)
    ABBList["ГЭС"]=abb("ГЭС","гидро-электростанция",False)
    ABBList["ТЭЦ"]=abb("ТЭЦ","теплоэлектроцентраль",False)
    ABBList["ТЭС"]=abb("ТЭС","высшее учебное заведение",False)
    ABBList["АЭС"]=abb("АЭС","высшее учебное заведение",False)
    ABBList["ГТЭС"]=abb("ГТЭС","высшее учебное заведение",False)
    ABBList["ГАЭС"]=abb("ГАЭС","высшее учебное заведение",False)
    ABBList["ПЭС"]=abb("ПЭС","высшее учебное заведение",False)
    ABBList["СЭС"]=abb("СЭС","высшее учебное заведение",False)
    ABBList["КЗоТ"]=abb("КЗоТ","кодекс законов о труде",False)
    ABBList["МХАТ"]=abb("МХАТ","московский художественный академический театр",False)
    # по словарю аббревиатур "Циклопедии"
##    ABBList["ААНИИ"]=abb("ААНИИ","Арктический и антарктический научно-исследовательский институт",False)
##    ABBList["АБС"]=abb("АБС""Анти-блокировочная система
##    ABBList["АВД"]=abb("All Wheel Drive,полный привод
##    ABBList["АВМ"]=abb("аналоговая вычислительная машина
##    ABBList["АВР"]=abb("Автоматический ввод резерва
##    ABBList["АДЭ"]=abb("Ассоциация документальной электросвязи
##    ABBList["АНОЮ"]=abb("Антифашистское вече народного освобождения Югославии
##    ABBList["АДГ"]=abb("эндокринолог. Антидиуретический гормон
##    ABBList["АДД"]=abb("Авиация дальнего действия
##    ABBList["аддд"]=abb("Авиационная дивизия дальнего действия
##    ABBList["АЗ"]=abb("Аварийная Защита
##    ABBList["АЗЛК"]=abb("Автомобильный завод имени Ленинского комсомола
##    ABBList["АЗС"]=abb("Автозаправочная станция
##    ABBList["АИЖК"]=abb("Агентство по ипотечному жилищному кредитованию
##    ABBList["АИК"]=abb("Аппарат искусственного кровообращения
##    ABBList["АиФ"]=abb("Аргументы и факты
##    ABBList["АКА"]=abb("Архив кабинета археологии
##    ABBList["АКБ"]=abb("АКкумуляторная Батарея , Акционерный коммерческий банк
##    ABBList["АКМ"]=abb("Автомат Калашникова ( модернизированный)
##    ABBList["АКП"]=abb("Автоматическая Коробка Передач
##    ABBList["АКТГ"]=abb("эндокринолог. Адренокортикотропный гормон
##    ABBList["Альп. корп."]=abb("	Альпийский корпус
##    ABBList["АМ
##    ABBList["АМГОТ	англ. AMGOT, Allied Military Government of Occupied Territory	Союзная военная администрация на оккупированных территориях
##    ABBList["АМЗ
##    ABBList["АМН	Академия медицинских наук
##    ABBList["АМО ЗИЛ	Открытое акционерное московское общество «Завод имени И. А. Лихачёва»
##    ABBList["АХЛ
##    ABBList["АН	Академия наук, Агентство недвижимости
##    ABBList["АНЗЮС	англ. ANZUS Security Treaty — Australia, New Zealand, United States	Тихоокеанский пакт безопасности	Военный союз Австралии, Новой Зеландии и США
##    ABBList["АНО	Автономная некоммерческая организация
##    ABBList["АНП
##    ABBList["АНСА	итал. ANSA, Agenzia Nazionale Stampa Associata	Национальное агентство объединённой печати	Итальянское информационное агентство
##    ABBList["АНХ
##АО	Акционерное общество
##АОА
##АОЗТ	Акционерное общество закрытого типа
##АОК
##АОН	Академия общественных наук, Автоматический определитель номера
##АООТ	Акционерное общество открытого типа
##АП
##АПА
##АПБ	Архитектурно-планировочное бюро
##АПК	Аграрно-промышленный комплекс, Агропромышленный комплекс, Арский педагогический колледж
##АПЛ
##АПН	Агентство печати «Новости»
##АПН РФ	Академия Педагогических Наук Российской Федерации
##АПР	Аграрная партия России
##АПРА	кас. APRA, Alianza Popular Revolucionaria Americana	Американский народно-революционный альянс	Перуанская политическая партия
##АПЭ (значения)
##АПЧ	Автоматическая подстройка частоты
##АПЧиФ	Автоматическая подстройка частоты и фазы
##АРА	англ. ARA, American Relief Administration	Американская администрация помощи
##АРБЕД	Aciéries Réunies de Burbach — Eich — Dudelange	Объединённые сталеплавильные заводы Бурбах — Эйх — Дюделанж	Люксембург
##АРЕ	Арабская Республика Египет
##АРК	Автономная Республика Крым
##АРКОС	англ. en:All Russian Co-operative Society, с 1922 — Arcos Ltd		Акционерное торговое общество
##АРМ (значения)
##АРМКО	англ. ARMCO, American Rolling Mill Corporation, AK Steel Holding		Американская фирма
##АРМУ		Ассоциация революционного искусства Украины
##АРУ	Автоматическая регулировка усиления		Объединение архитекторов-урбанистов
##АРФ
##АС	Автомат стабилизации, акустическая система
##АСГЭ	Археологический сборник Государственного Эрмитажа
##АСЕАН		Ассоциация государств Юго-Восточной Азии
##АСКУЭ	энерг. Автоматизированные системы контроля и учета энергии
##АСНОВА	Ассоциация новых архитекторов
##АСП
##АССР	Автономная Советская Социалистическая Республика
##АСТ
##АСУ	Автоматизированная система управления, Ассоциация смоленских учёных
##АСУП	Автоматизированная система управления предприятием
##АСУ ТП	Автоматизированная система управления технологическим процессом
##АТ
##АТС	Автоматическая телефонная станция
##АТФ	Аденозинтрифосфорная кислота	англ. аббр. ATP	Универсальный аккумулятор и переносчик энергии в живых организмах
##АТЭС	Азиатско-Тихоокеанское экономическое сотрудничество
##АУ
##АУМ	Ассоциация учащейся молодёжи
##АУПРБ (АУпПРБ)	Академия управления при Президенте Республики Беларусь	англ. Academy of Public Administration under the aegis of the President of the Republic of Belarus	ведущий вуз в национальной системе образования Республики Беларусь
##АУПТ	пож. Автоматические установки пожаротушения
##АУРШ	Ассоциация учителей русских школ
##АФК
##АФТ	Американская федерация труда
##АФТ—КПП	Американская федерация труда — Конгресс производственных профсоюзов
##АХ	Академия художеств
##АХЛ	Американская хоккейная лига
##АХР
##АХРР	Ассоциация художников революционной России
##АХО	Административно хозяйственный отдел
##АХЧУ	укр. Асоцiaцiя художниюв Червоної України	Ассоциация художников Красной Украины
##АХОВ	Аварийно химически опасное вещество
##АШ
##«АЭГ—Телефункен»	нем. AEG, Allgemeine Elektricitats-Gesellschaft-Telefunken, Allgemeine Electricitats-Gesellschaft		ФРГ
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)

    # латинские
    ABBList["N.A.T.O."]=abb("N.A.T.O.","Nord Atlantic Trust Organisation",False)
    ABBList["NATO"]=abb("NATO","Nord Atlantic Trust Organisation",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
##    ABBList["вуз"]=abb("вуз","высшее учебное заведение",False)
