#-------------------------------------------------------------------------------
# Name:        Списки сокращений
# Author:      ash-911
# Created:     22.06.2016
# Copyright:   (c) ash-911 2016
#-------------------------------------------------------------------------------

class soc(object):
        # свойства сокращений:
    # - может ли стоять на конце предложения
    # - низкая вероетность расположения в конце
    # - высокая вероятность -//-
    # - никогда не стоит в конце предложения
    # - редко бывает с точкой на конце
    # - часто с точкой на конце
    def __init__(self, krt="", ful="", end=True, post=False):
        self.krat = krt
        self.full = ful
        self.maybeEND = end
        self.needPost = post

    def __str__(self):
        return self.krat

class sokr(object):
    """
    список сокращений
    """
    def __init__(self):
        self.SocrList = {}
        self.SocrTips = []
        self.SocrList["адм.-терр."]=soc("адм.-терр.","административно-территориальный",False,True)
        self.SocrList["акад."]=soc("акад.","академик,академия",False,True)
        self.SocrList["а. л."]=soc("а. л.","авторский лист",False,True)
        self.SocrList["авт. л."]=soc("авт. л.","авторский лист",False,True)
        self.SocrList["а/о"]=soc("а/о","автономный округ,автономная область",True,False)
        self.SocrList["б"]=soc("б","байт",True,False)
        self.SocrList["б-ка"]=soc("б-ка","библиотека",False,True)
        self.SocrList["в."]=soc("в.","век",True,False)
        self.SocrList["вв."]=soc("вв.","века",True,False)
        self.SocrList["вкз."]=soc("вкз.","вокзал",False,True)
        self.SocrList["в/о"]=soc("в/о","вечернее отделение",True,False)
        self.SocrList["вост.-европ."]=soc("вост.-европ.","восточноевропейский",True,False)
        self.SocrList["г."]=soc("г.","год,город,гора,господин,госпожа,грамм",True,False)
        self.SocrList["гг."]=soc("гг.","годы, города, горы, господа",True,False)
        self.SocrList["г"]=soc("г","грамм",True,False)
        self.SocrList["г-н"]=soc("г-н","господин",False,True)
        self.SocrList["г-да"]=soc("г-да","господа",False,True)
        self.SocrList["г-жа"]=soc("г-жа","госпожа",False,True)
        self.SocrList["гор."]=soc("гор.","город",False,True)
        self.SocrList["гос."]=soc("гос.","государственный",False,True)
        self.SocrList["гос-во"]=soc("гос-во","государство",True,False)
        self.SocrList["гр."]=soc("гр.","гражданин,гражданка,грамм",False,True)
        self.SocrList["гр-ка"]=soc("гр-ка","гражданка",False,True)
        self.SocrList["гр-н"]=soc("гр-н","гражданин",False,True)
        self.SocrList["гр-не"]=soc("гр-не","граждане",False,True)
        self.SocrList["д."]=soc("д.","деревня",False,True)
        self.SocrList["деп."]=soc("деп.","департамент,депутат",False,True)
        self.SocrList["дисс."]=soc("дисс.","диссертация",False,True)
        self.SocrList["д. о."]=soc("д. о.","дом отдыха",True,False)
        self.SocrList["д.о."]=soc("дом отдыха",True,False)
        self.SocrList["д/о"]=soc("д.о.","дом отдыха,дневное отделение",True,False)
        self.SocrList["дол."]=soc("дол.","долина",True,False)
        self.SocrList["долл."]=soc("долл.","доллар",True,False)
        self.SocrList["доц."]=soc("доц.","доцент",False,True)
        self.SocrList["ежедн."]=soc("ежедн.","ежедневный",True,False)
        self.SocrList["ж."]=soc("ж.","женский",True,False)
        self.SocrList["жен."]=soc("жен.","женский",True,False)
        self.SocrList["ж. д."]=soc("ж. д.","железная дорога",True,False)
        self.SocrList["ж/д"]=soc("ж/д","железная дорога",True,False)
        self.SocrList["ж.-д."]=soc("ж.-д.","железнодорожный",True,False)
        self.SocrList["ж/д"]=soc("ж/д","железнодорожный",True,False)
        self.SocrList["зам."]=soc("зам.","заместитель",False,True)
        self.SocrList["зам"]=soc("зам","заместитель",False,True)
        self.SocrList["зап."]=soc("зап.","западный",False,True)
        self.SocrList["з."]=soc("з.","западный",False,True)
        self.SocrList["зап.-европ."]=soc("зап.-европ.","западноевропейский",True,False)
        # совпадает со словом "заруб"
        #self.SocrList["заруб."]=soc("заруб.","зарубежный",False,True)
        self.SocrList["з. к."]=soc("з. к.","заключенный",True,False)
        self.SocrList["з/к"]=soc("з/к","заключенный",True,False)
        self.SocrList["з/о"]=soc("з/о","заочное отделение",True,False)
        self.SocrList["изд-во"]=soc("изд-во","издательство",True,False)
        self.SocrList["ин."]=soc("ин.","иностранный",False,True)
        self.SocrList["иностр."]=soc("иностр.","иностранный",False,True)
        self.SocrList["ин-т"]=soc("ин-т","институт",True,False)
        self.SocrList["ин-тов"]=soc("ин-тов","институтов",True,False)
        self.SocrList["инст."]=soc("инст.","институт",True,False)
        self.SocrList["и. о."]=soc("и. о.","исполняющий обязанности,имя и отчество",False,True)
        self.SocrList["и.о."]=soc("и.о.","исполняющий обязанности,имя и отчество",False,True)
        self.SocrList["т. д."]=soc("т. д.","так далее",True,False)
        self.SocrList["т.д."]=soc("т.д.","так далее",True,False)
        self.SocrList["тд."]=soc("тд.","так далее",True,False)
        self.SocrList["т. п."]=soc("т. п.","тому подобное,тому подобные",True,False)
        self.SocrList["др."]=soc("др.","другие",True,False)
        self.SocrList["пр."]=soc("пр.","прочие",True,False)
        self.SocrList["им."]=soc("им.","имени",False,True)
        self.SocrList["ил."]=soc("ил.","иллюстрация",False,True)
        self.SocrList["канд."]=soc("канд.","кандидат",False,True)
        self.SocrList["к."]=soc("к.","который,кандидат",False,True)
        self.SocrList["кг"]=soc("кг","килограмм",True,False)
        self.SocrList["кг."]=soc("кг.","кегль",True,False)
        self.SocrList["м."]=soc("м.","мужской, минута",True,False)
        self.SocrList["муж."]=soc("муж.","мужской",True,False)
        self.SocrList["м"]=soc("м","метр",True,False)
        self.SocrList["млн"]=soc("млн","миллион",True,False)
        self.SocrList["млрд"]=soc("млрд","миллиард",True,False)
        self.SocrList["трл"]=soc("трл","триллион",True,False)
        self.SocrList["напр."]=soc("напр.","например",True,False)
        self.SocrList["нач."]=soc("нач.","начальник",False,True)
        self.SocrList["н.э."]=soc("н.э.","нашей эры",True,False)
        self.SocrList["Кб"]=soc("Кб","килобайт",True,False)
        self.SocrList["Кбайт"]=soc("Кбайт","килобайт",True,False)
        self.SocrList["КиБ"]=soc("Кбайт","килобайт",True,False)
        self.SocrList["Кбит"]=soc("Кбит","килобит",True,False)
        self.SocrList["Мб"]=soc("Мб","мегабайт",True,False)
        self.SocrList["Мбайт"]=soc("Мбайт","мегабайт",True,False)
        self.SocrList["МиБ"]=soc("МиБ","мегабайт",True,False)
        self.SocrList["Мбит"]=soc("Мбит","мегабит",True,False)
        self.SocrList["Гб"]=soc("Гб","гигабайт",True,False)
        self.SocrList["Гбайт"]=soc("Гбайт","гигабайт",True,False)
        self.SocrList["ГиБ"]=soc("ГиБ","гигабайт",True,False)
        self.SocrList["Гбит"]=soc("Гбит","гигабит",True,False)
        self.SocrList["Тб"]=soc("Тб","терабайт",True,False)
        self.SocrList["Тбайт"]=soc("Тбайт","терабайт",True,False)
        self.SocrList["Тбит"]=soc("Тбит","терабит",True,False)
        self.SocrList["Пб"]=soc("Пб","петабайт",True,False)
        self.SocrList["Пбайт"]=soc("Пбайт","петабайт",True,False)
        self.SocrList["Пбит"]=soc("Пбит","петабит",True,False)
        self.SocrList["Эб"]=soc("Эб","экзабайт",True,False)
        self.SocrList["Эбайт"]=soc("Эбайт","экзабайт",True,False)
        self.SocrList["Эбит"]=soc("Эбит","экзабит",True,False)
        self.SocrList["Зб"]=soc("Зб","зетабайт",True,False)
        self.SocrList["Збайт"]=soc("Збайт","зетабайт",True,False)
        self.SocrList["Збит"]=soc("Збит","зетабит",True,False)
        self.SocrList["мб"]=soc("мб","миллибар",True,False)
        self.SocrList["лит."]=soc("лит.","литературный",True,False)
        self.SocrList["мин."]=soc("мин.","минута,минимальный,министерство,министр",True,False)
        self.SocrList["мин-во"]=soc("мин-во","министерство",False,True)
        self.SocrList["миним."]=soc("миним.","минимальный",True,False)
        self.SocrList["мм"]=soc("мм","миллиметр",True,False)
        self.SocrList["мк"]=soc("мк","микрон,микрометр",True,False)
        self.SocrList["мкс"]=soc("мкc","микросекунда",True,False)
        self.SocrList["нм"]=soc("нм","нанометр",True,False)
        self.SocrList["пм"]=soc("пм","пикометр",True,False)
        self.SocrList["ам"]=soc("ам","аттометр",True,False)
        self.SocrList["фм"]=soc("фм","фемтометр",True,False)
        self.SocrList["дм"]=soc("дм","дециметр",True,False)
        self.SocrList["см"]=soc("см","сантиметр",True,False)
        self.SocrList["дм"]=soc("дм","децииметр",True,False)
        self.SocrList["км"]=soc("км","километр",True,False)
        self.SocrList["д"]=soc("д","дюйм,дом",True,False)
        self.SocrList["моск."]=soc("моск.","московский",False,True)
        self.SocrList["нед."]=soc("нед.","неделя",True,False)
        self.SocrList["о."]=soc("о.","остров, озеро",False,True)
        self.SocrList["ок."]=soc("ок.","около",False,True)
        self.SocrList["оз."]=soc("оз.","озеро",False,True)
        self.SocrList["п."]=soc("п.","параграф,пункт,переулок",False,True)
        self.SocrList["пп."]=soc("пп.","параграфы,пункты",False,True)
        self.SocrList["п/п"]=soc("п/п","по порядку",True,False)
        self.SocrList["пер."]=soc("пер.","переулок",False,True)
        self.SocrList["пед."]=soc("пед.","педагогический",False,True)
        self.SocrList["п/я"]=soc("п/я","почтовый ящик",False,True)
        self.SocrList["просп."]=soc("просп.","проспект",False,True)
        self.SocrList["пр."]=soc("пр.","проспект",False,True)
        self.SocrList["пр-т"]=soc("пр-т","проспект",False,True)
        self.SocrList["проф."]=soc("проф.","профессор",False,True)
        self.SocrList["р."]=soc("р.","рубль,река",False,True)
        self.SocrList["руб."]=soc("руб.","рубль",True,False)
        self.SocrList["ред."]=soc("ред.","редакция",False,True)
        self.SocrList["рус."]=soc("рус.","русского",False,True)
        self.SocrList["с."]=soc("с","секунда,страница",True,False)
        # сокращение "с" совпадает с предлогом!
        # необходима постобработка
        #self.SocrList["с."]=soc("село,секунда,страница",True,False)
        self.SocrList["сек."]=soc("сек.","секунда",True,False)
        self.SocrList["стр."]=soc("стр.","страница",False,True)
        self.SocrList["сокр."]=soc("сокр.","сокращение",True,False)
        self.SocrList["см"]=soc("см","сантиметр",True,False)
        self.SocrList["см."]=soc("см.","смотри",False,True)
        self.SocrList["сред."]=soc("сред.","средний",False,True)
        self.SocrList["СПб."]=soc("СПб.","Санкт-Петербург",True,False)
        self.SocrList["т."]=soc("т.","том,телефон,товарищ,тысяча",False,True)
        self.SocrList["т"]=soc("т","тонна,том,телефон,товарищ,тысяча",False,True)
        self.SocrList["тт."]=soc("тт.","тома",False,True)
        self.SocrList["т.е."]=soc("т.е.","то есть",True,False)
        self.SocrList["т.к."]=soc("т.к.","так как",True,False)
        self.SocrList["т.о."]=soc("т.о.","таким образом",True,False)
        self.SocrList["тел."]=soc("тел.","телефон",False,True)
        self.SocrList["тов."]=soc("тов.","товарищ",False,True)
        self.SocrList["тыс."]=soc("тыс.","тысяча",True,False)
        self.SocrList["т/к"]=soc("т/к","телеканал",False,True)
        self.SocrList["т/с"]=soc("т/с","телесериал",False,True)
        self.SocrList["т.н."]=soc("т.н.","так называемый",False,True)
        self.SocrList["т.-н."]=soc("т.-н.","так называемый",False,True)
        self.SocrList["т-н"]=soc("т-н","так называемый",False,True)
        self.SocrList["ул."]=soc("ул.","улица",False,True)
        self.SocrList["Учеб."]=soc("Учеб.","Учебное",False,True)
        self.SocrList["Ф. И. О."]=soc("Ф. И. О.","фамилия имя отчество",False,True)
        self.SocrList["Ф.И.О."]=soc("Ф.И.О.","фамилия имя отчество",False,True)
        self.SocrList["ф. и. о."]=soc("ф. и. о.","фамилия имя отчество",False,True)
        self.SocrList["ф.и.о."]=soc("ф.и.о.","фамилия имя отчество",False,True)
        self.SocrList["ф-та"]=soc("ф-та","факультета",False,True)
        self.SocrList["ф-т"]=soc("ф-т","факультет",False,True)
        self.SocrList["ч."]=soc("ч.","час",True,False)
        self.SocrList["экз."]=soc("экз.","экземпляр",True,False)
        self.SocrList["яз."]=soc("яз.","языка",True,False)
        # виды предприятий
        self.SocrList["АООТ"]=soc("АООТ","акционерное общество открытого типа",True,False)
        self.SocrList["АОЗТ"]=soc("АОЗТ","акционерное общество закрытого типа",True,False)
        self.SocrList["ОАО"]=soc("ОАО","открытое акционерное общество",True,False)
        self.SocrList["ЗАО"]=soc("ЗАО","закрытое акционерное общество",True,False)
        self.SocrList["ООО"]=soc("ООО","общество с ограниченной ответственностью",True,False)
        self.SocrList["ТОО"]=soc("ТОО","товарищество с ограниченной ответственностью",True,False)
        self.SocrList["ГП"]=soc("ГП","государственное предприятие",True,False)
        self.SocrList["МП"]=soc("МП","муниципальное предприятие",True,False)
        self.SocrList["ЧП"]=soc("ЧП","частное предприятие",True,False)
        self.SocrList["ИЧП"]=soc("ИЧП","индивидуальное частное предприятие",True,False)
        self.SocrList["СП"]=soc("СП","совместное предприятие",True,False)
        self.SocrList["НПО"]=soc("НПО","научно-производственное объединение",True,False)
        self.SocrList["ОО"]=soc("ОО","общественное объединение",True,False)
        # воинские звания
        self.SocrList["ряд."]=soc("ряд.","рядовой",False,True)
        self.SocrList["мл. сер."]=soc("мл. сер.","младший сержант",False,True)
        self.SocrList["сер."]=soc("сер.","сержант",False,True)
        self.SocrList["прап."]=soc("прап.","прапорщик",False,True)
        self.SocrList["ст. сер."]=soc("ст. сер.","старший сержант",False,True)
        self.SocrList["старш."]=soc("старш.","старшина",False,True)
        self.SocrList["ст. прап."]=soc("мл. прап.","старший прапорщик",False,True)
        self.SocrList["мл. лейт."]=soc("мл. лейт.","младший лейтенант",False,True)
        self.SocrList["мл. л-т"]=soc("мл. л-т.","младший лейтенант",False,True)
        self.SocrList["лейт."]=soc("лейт.","лейтенант",False,True)
        self.SocrList["л-т"]=soc("л-т.","лейтенант",False,True)
        self.SocrList["ст. лейт."]=soc("ст. лейт.","старший лейтенант",False,True)
        self.SocrList["ст. л-т"]=soc("ст. л-т.","старший лейтенант",False,True)
        self.SocrList["кап."]=soc("кап.","капитан",False,True)
        self.SocrList["м-р."]=soc("м-р.","майор",False,True)
        self.SocrList["пп-к."]=soc("пп-к","подполковник",False,True)
        self.SocrList["п-к."]=soc("п-к","полковник",False,True)
        #self.SocrList["ген."]=soc("ген.","генерал",False,True)
        self.SocrList["брик. ген."]=soc("брик. ген.","бригадный генерал",False,True)
        self.SocrList["ген. м-р"]=soc("ген. м-р","генерал-майор",False,True)
        self.SocrList["ген. л-т"]=soc("ген. л-т","генерал-лейтенант",False,True)
        self.SocrList["ген. ар."]=soc("ген. ар.","генерал армии",False,True)

    def isSocr(self, s=""):
        try:
            ss = self.SocrList[s.lower()]
            return True
        except: return False

    def findSocr(self,s=""):
        fin = False
        ss = None
        try:
            ss = self.SocrList[s.lower()]
            fin = True
        except:
            fin = False
        if fin is False:
            try:
                ss = self.SocrList[s.lower()+"."]
                fin = True
            except:
                fin = False
        return ss if fin else ""

    def maybeEND(self, s):
        return self.SocrList[s].maybeEND

    def needPost(self, s):
        return self.SocrList[s].needPost