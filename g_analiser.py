#-------------------------------------------------------------------------------
# Name:        Модуль графематического анализа
# Author:      ash-911
# Created:     19.06.2016
#-------------------------------------------------------------------------------

from sokrash import sokr
import abbrev as abb
import Cython

class grafema(object):
    def __init__(self):
        self.txt = ""
        self.tokens = []
        self.tip = []
        self.isPart = False
        self.position = 0
    def __str__(self): return self.txt

class promt(object):
    def __init__(self):
        self.Grafems = []
    def __str__(self):
        strs = ""
        for g in self.Grafems:
            strs+=g.txt+" "
        return strs

class Grafem_Analiser(object):
    """
    Класс для графематики
    """
    def __init__(self):
        self.Tokens = []
        self.Grafems = []
        self.Tag = []
        self.Promts = []
        self.LET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
        self.let = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
        self.LAT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lat = "abcdefghijklmnopqrstuvwxyz"
        self.digit = "1234567890"
        self.delem = ",.;:!?–-"
        self.znakB = "<«[({'\""
        self.znakE = "'\"})]»>"
        self.spec = "/\|=+@#$%^&*~_"
        self.Sokr = sokr()
        self.ZnakDict = {}
        self.InitZnak()

    def InitZnak(self):
        self.ZnakDict[","] = "ЗПТ"
        self.ZnakDict["."] = "ТЧК"
        self.ZnakDict["..."] = "МТЧ"
        self.ZnakDict[";"] = "ТЗП"
        self.ZnakDict[":"] = "ДВТ"
        self.ZnakDict["!"] = "ВСЗ"
        self.ZnakDict["?"] = "ВПЗ"
        self.ZnakDict["–"] = "ТИР"
        self.ZnakDict["-"] = "ДЕФ"
        self.ZnakDict["\""] = "КАВ"
        self.ZnakDict["'"] = "ОКВ"
        self.ZnakDict["("] = "О_СКБ"
        self.ZnakDict["{"] = "О_ФСК"
        self.ZnakDict["["] = "О_КСК"
        self.ZnakDict["«"] = "О_ДКВ"
        self.ZnakDict["<"] = "О_ОКВ"
        self.ZnakDict[">"] = "З_ОКВ"
        self.ZnakDict["»"] = "З_ДКВ"
        self.ZnakDict["]"] = "З_КСК"
        self.ZnakDict["}"] = "З_ФСК"
        self.ZnakDict[")"] = "З_СКБ"
        self.ZnakDict["/"] = "КОС"
        self.ZnakDict["\\"] = "ОБР"
        self.ZnakDict["\n"] = "КОН"
        self.ZnakDict["|"] = "ВРТ"
        self.ZnakDict["="] = "РАВ"
        self.ZnakDict["+"] = "ПЛС"
        self.ZnakDict["@"] = "СОБ"
        self.ZnakDict["#"] = "РЕШ"
        self.ZnakDict["$"] = "ДОЛ"
        self.ZnakDict["%"] = "ПРЦ"
        self.ZnakDict["^"] = "ДОМ"
        self.ZnakDict["&"] = "АМП"
        self.ZnakDict["*"] = "ЗВД"
        self.ZnakDict["~"] = "ТИЛ"
        self.ZnakDict["_"] = "ПОД"

    def createGrafem(self,grf="",tp="",tp2=""):
        """
        создание эксземпляра графемы
        """
        G = grafema()
        G.txt = grf
        if tp != "": G.tip.append(tp)
        if tp2 != "": G.tip.append(tp2)
        return G

    def setTag(self):
        self.Tag.append("BEG")

    def getTokens(self,text = ""):
        """
        разбиение строки на слова
        """
        self.Tokens = text.split(" ")

    def isInSet(self,st,arr):
        res = True
        ln = len
        ind = 0
        for ind in range(ln(st)):
            if st[ind] in arr: res = True
            else:
                res = False
                break
        return res

    def isUpperCyr(self,st): return self.isInSet(st,self.LET)
    def isUpperLat(self,st): return self.isInSet(st,self.LAT)
    def isUpper(self,st):
        if self.isInSet(st,self.LET) or self.isInSet(st,self.LAT): return True
    def isLowerCyr(self,st): return self.isInSet(st,self.let)
    def isLowerLat(self,st): return self.isInSet(st,self.lat)
    def isLower(self,st):
        if self.isInSet(st,self.let) or self.isInSet(st,self.lat): return True
    def isMixUpLowCyr(self,st):
        FIN = False
        fin = False
        ln = len
        ind = 0
        if st[0:1] in self.LET and self.isLowerCyr(st[1:]): return False
        else:
            for ind in range(ln(st)):
                if st[ind] in self.LET: FIN = True
                elif st[ind] in self.let: fin = True
                else:
                    fin = False
                    break
        if FIN and fin: return True
        return False
    def isMixUpLowLat(self,st):
        FIN = False
        fin = False
        ln = len
        ind = 0
        if st[0:1] in self.LAT and self.isLowerLat(st[1:]): return False
        else:
            for ind in range(ln(st)):
                if st[ind] in self.LAT: FIN = True
                elif st[ind] in self.lat: fin = True
                else:
                    fin = False
                    break
        if FIN and fin: return True
        return False
    def isDigit(self,st): return self.isInSet(st,self.digit)
    def isAlphaCyr(self,st):
        Let = self.LET + self.let
        if self.isInSet(st,Let): return True
    def isAlphaLat(self,st):
        Lat = self.LAT + self.lat
        if self.isInSet(st,Lat): return True
    def isSim(self,st):
        if self.isAlphaLat(st) or self.isAlphaCyr(st) or self.isDigit(st): return True
    def isZnak(self,st):
        if st in self.znakB or st in self.znakE or st in self.delem or st in self.spec or st=="\n": return True
    def isUP(self,st):
        if st[0] in self.LET or st[0] in self.LAT: return True
    def isEndPromt(self,st):
        if st == "ТЧК" or st == "ВПЗ" or st == "ВСЗ" or st == "МТЧ": return True

    def getGraf(self,s):
        """
        определение типа строки
        создание графемы
        """
        ln = len
        G = grafema()
        G.txt = s
        GT = G.tip.append
        if (s[0:1] in self.LET and self.isLowerCyr(s[1:])): GT("Лек")
        if (s[0:1] in self.LAT and self.isLowerLat(s[1:])): GT("Lex")
        if ln(s) > 1:
            if self.isUpperCyr(s): GT("ЛЕК")
            if self.isUpperLat(s): GT("LAT")
        if self.isLowerCyr(s): GT("лек")
        if self.isLowerLat(s): GT("lex")
        if self.isMixUpLowCyr(s): GT("ЛеК")
        if self.isMixUpLowLat(s): GT("LeX")
        if self.isDigit(s): GT("чис")
        if self.isAlphaCyr(s): GT("бук")
        if self.isAlphaLat(s): GT("chr")
        if ln(G.tip) == 0: GT("НаН")
        return G

    def getTips(self):
        """
        определение типа однословной графемы
        """
        i = 0
        ln = len
        tok = self.Tokens
        lnn = ln(tok)
        app = self.Grafems.append
        gG = self.getGraf
        for i in range(lnn): app(gG(tok[i]))

    def findEOS(self):
        i = 0
        ln = len
        grf = self.Grafems
        gf = []
        app = gf.append
        cG = self.createGrafem
        lnn = ln(grf)
        lnl = lnn - 1
        for i in range(lnn):
            g = grf[i]
            s = g.txt
            if s.find("\n") > 0:
                g.txt = s[:-1]
                app(g)
                app(cG("\n","EOS"))
            elif i == lnl:
                app(g)
                app(cG("\n","EOS"))
            else: app(g)
        self.Grafems = gf

    def getZnakTip(self,s):
        return self.ZnakDict[s[0]]

    def findSim(self):
        """
        поиск разделителей, скобок, кавычек, спец. символов
        в начале и в конце токена
        """
        i = 0
        ii = 0
        pos = 0
        n = 0
        m = 0
        N = 0
        ln = len
        f = False
        word = False
        grf = self.Grafems
        Gr = self.createGrafem
        gZ = self.getZnakTip
        isis = self.isInSet
        isZn = self.isZnak
        gG = self.getGraf
        gf = []
        appen = gf.append
        lnn = ln(grf)
        szB = self.znakB
        szE = self.znakE
        szDel = self.delem
        ssp = self.spec
        for i in range(lnn):
            ss = ""
            g = grf[i]
            s = g.txt
            ll = ln(s)
            tp = g.tip
            f = False
            fin = False
            word = False
            pos = 0
            for N in range(ll):
                if not isZn(s[N]):
                    word = True
            for ii in range(ll):
                sss = s[ii]
                if ll == 1:
                    if s[0] in szB:
                        appen(Gr(s,"SKO",gZ(s)))
                        fin = True
                    elif s[0] in szE:
                        appen(Gr(s,"SKO",gZ(s)))
                        fin = True
                    elif s[0] in szDel:
                        appen(Gr(s,"DEL",gZ(s)))
                        fin = True
                    elif s[0] in ssp:
                        appen(Gr(s,"SPE",gZ(s)))
                        fin = True
                elif not word:
                    if isis(sss,szB):
                        appen(Gr(sss,"SKO",gZ(sss)))
                        fin = True
                    elif isis(sss,szE):
                        appen(Gr(sss,"SKO",gZ(sss)))
                        fin = True
                    elif isis(sss,szDel):
                        appen(Gr(sss,"DEL",gZ(sss)))
                        fin = True
                    elif isis(sss,ssp):
                        appen(Gr(sss,"SPE",gZ(sss)))
                        fin = True
                    else:
                        pos = ii
                        break
                else:
                    if isis(sss,szB):
                        appen(Gr(sss,"B_SKO",gZ(sss)))
                        fin = True
                    elif isis(sss,szE):
                        appen(Gr(sss,"B_SKO",gZ(sss)))
                        fin = True
                    elif isis(sss,szDel):
                        appen(Gr(sss,"B_DEL",gZ(sss)))
                        fin = True
                    elif isis(sss,ssp):
                        appen(Gr(sss,"B_SPE",gZ(sss)))
                        fin = True
                    else:
                        pos = ii
                        break
            if pos == ll-1 and pos != 0:
                ss += s[pos]
                appen(gG(ss))
            else:
                for n in range(ll-1,pos-1,-1):
                    if not isZn(s[n]):
                        appen(gG(s[pos:n+1]))
                        f= True
                        pos = n
                        break
                if f == False and fin == False:
                    print("False: %s" % s[pos:ll])
                    appen(gG(s[pos:ll]))
            for m in range(pos,ll):
                sss = s[m]
                if fin == False or f == True:
                    if isis(sss,szB): appen(Gr(sss,"E_SKO",gZ(sss)))
                    elif isis(sss,szE): appen(Gr(sss,"E_SKO",gZ(sss)))
                    elif isis(sss,szDel): appen(Gr(sss,"E_DEL",gZ(sss)))
                    elif isis(sss,ssp): appen(Gr(sss,"E_SPE",gZ(sss)))
                    elif s[m] == "\n": appen(Gr("КОН","EOS",gZ(sss)))
        self.Grafems = gf

    def process_(self,text):
        self.Grafems.clear()
        self.Tokens.clear()
        self.getTokens(text)
        self.getTips()
        #self.findEOS()
        self.findSim()

    def SokrMayBe(self,s,toch=""):
        GG = self.createGrafem(s,"СОК")
        s +=toch
        if self.Sokr.maybeEND(s.lower()) : GG.tip.append("M_END")
        else: GG.tip.append("N_END")
        if self.Sokr.needPost(s.lower()) : GG.tip.append("M_PST")
        else: GG.tip.append("N_PST")
        return GG

    def findSokr(self):
        """
        поиск сокращений в тексте
        """
        i = 0
        ii = 0
        pos = 0
        ln = len
        grf = self.Grafems
        Gr = self.createGrafem
        gG = self.getGraf
        sM = self.SokrMayBe
        isSC = self.Sokr.isSocr
        gf = []
        appen = gf.append
        lnn = ln(grf)
        fin = False
        double = False
        for i in range(lnn):
            g = grf[i]
            s = g.txt
            part = g.isPart
            ll = ln(s)
            fin = False
            if i+1 < lnn:
                if ln(grf[i+1].tip) > 1 and grf[i+1].tip[0] == "E_DEL" and grf[i+1].tip[1]=="ТЧК":
                    if not part:
                        # тройное сокращение
                        if i+5 < lnn:
                            ts = s+"."+" "+grf[i+2].txt+"."+" "+grf[i+4].txt
                            if ln(grf[i+3].tip) > 1 and grf[i+3].tip[0] == "E_DEL" and grf[i+3].tip[1]=="ТЧК":
                                if ln(grf[i+5].tip) > 1 and grf[i+5].tip[0] == "E_DEL" and grf[i+5].tip[1]=="ТЧК":
                                    if isSC(ts+"."):
                                        grf[i+4].isPart = True
                                        grf[i+3].isPart = True
                                        grf[i+2].isPart = True
                                        grf[i+1].isPart = True
                                        g.isPart = True
                                        appen(sM(ts,"."))
                                        fin = True
                        # двойное сокращение
                        if i+3 < lnn and not fin:
                            ds = s+"."+" "+grf[i+2].txt
                            if ln(grf[i+3].tip) > 1 and grf[i+3].tip[0] == "E_DEL" and grf[i+3].tip[1]=="ТЧК":
                                if isSC(ds+"."):
                                    grf[i+2].isPart = True
                                    grf[i+1].isPart = True
                                    g.isPart = True
                                    appen(sM(ds,"."))
                                    fin = True
                        if isSC(s+".") and not fin and not g.isPart:
                            # одинарное сокращение
                            appen(sM(s,"."))
                            fin = True
                    elif isSC(s) and not part:
                        # стоит в конце строки с точкой, но точки после себя не требует
                        appen(sM(s))
                        fin = True
                elif isSC(s) and not part:
                # без точки на конце
                    appen(sM(s))
                    fin = True
            else:
                # без точки и не в конце текста
                # требует ли сокращение после себя  особых форм слова (заглавные буквы)
                if isSC(s) and not part:
                    appen(sM(s))
                    fin = True
            if not fin and not part: appen(g)
        self.Grafems = gf

    def findSostav(self):
        """
	   = составные слова - серо-зелёный отличие от пере-носов
	   = слова в (скобках), "кавычках"
	   = имена собственные - Интернет(интернет), Россия
	   = математические переменные
	   = формулы - y=x,
	   = выражения
	   = соотношения
	   = операторы x > y, x != y
       = устранение пере-носов
            -- после пере- часто идёт EOS
       = разделение слитнонаписанныхслов, знаков препинания, слов и цифр
        """
        i = 0
        ln = len
        grf = self.Grafems
        gf = []
        app = gf.append
        cG = self.createGrafem
        gG = self.getGraf
        gZ = self.getZnakTip
        isup = self.isUP
        # инициализация массива аббревиатур
        abb.Init()
        ir = self.isUpper
        il = self.isLower
        iU = self.isUpper
        iD = self.isDigit
        iS = self.isSim
        isZ = self.isZnak
        lnn = ln(grf)
        lnl = lnn-1

        # проверка на соответствие имени сайта
        def isAdress(st):
            tmp = False
            adr = st.split(".")
            domens = ["com","ru","net","de","us","rf","fr","uk","cn","ua","org",
                    "xxx","pl","ch","biz","edu","gov","info","jobs","br","be",
                    "ру","рф","бел","by","eu","fi","gr","in","jp","kz","nl","su"]
            for t in st:
                if il(t) or iD(t) or t=="-" or t==".": tmp = True
                else:
                    tmp = False
                    break
            if ln(adr)>1 and ln(adr[-1])<5 and ln(st)>2: tmp = True
            else: tmp = False
            if adr[-1] in domens: tmp = True
            else:  tmp = False
            return tmp

        def isE_name(st):
            tmp = False
            for t in st:
                if il(t) or iD(t) or t=="-" or t==".": tmp = True
                else:
                    tmp = False
                    break
            if ln(st)>2: tmp = True
            else: tmp = False
            return tmp

        def isFile_name(st):
            tmp = False
            point = False
            lng = False
            # имя файла может состоять из любых символов, кроме
            noncor = '\\','/',':','*','?','"','<','>','|'
            fl = []
            for ch in noncor:
                if st.find(ch)>0:
                    tmp=False
                    break
                else:tmp=True
            # всегда есть точка
            if st.find(".")>0: point=True
            else: point=False
            if point: fl = st.split(".")
            # после неё от 1 до 3-х символов, иногда больше
            if ln(fl)>0 and ln(fl[0])>0: lng=True
            else: lng=False
            if tmp and point and lng: return True
            return False

        def isTime(st):
            tmp = False
            tim = st.split(":")
            for i in range(ln(tim)):
                if iD(tim[i]) and ln(tim[i])>1: tmp = True
                else:
                    tmp = False
                    break
            return tmp

        def isDate(st,delim):
            dat2 = False
            dat3 = False
            ss = st.split(delim)
            if ln(ss)==2:
                if iD(ss[0]) and ln(ss[0])<3 and ln(ss[0])>0:dat2=True
                if iD(ss[1]) and ln(ss[1])<3 and ln(ss[1])>0:dat2=True
                else: dat2=False
            if ln(ss)==3:
                if iD(ss[0]) and ln(ss[0])<3 and ln(ss[0])>0:dat2=True
                if iD(ss[1]) and ln(ss[1])<3 and ln(ss[1])>0:dat2=True
                if iD(ss[2]) and ln(ss[2])<5 and ln(ss[2])>1:dat2=True
                else: dat3=False
            if dat2 or dat3: return True
            return False

        def findSlash(st):
            for n in st:
                if n=="\\": return True
            return False

        def adC(ind,st="",tp=""):
            if st!="":
                app(cG(st,tp))
                grf[ind].isPart = True

        def adG(ind,st,tp=""):
            G = gG(st)
            G.tip.append(tp)
            app(G)
            grf[ind].isPart = True

        for i in range(lnn):
            g = grf[i]
            s = g.txt
            sFin = s.find
            part = g.isPart
            ll = ln(s)
            if not part:
            # обработка составных графем:
                # ФИО - Фамилия И.О. | Фамилия И. | Фамилия Имя Отчество
                if i<lnn-2 and (g.tip[0]=="Лек" or g.tip[0]=="Lex") and ln(grf[i+1].txt)>2 and ir(grf[i+1].txt[0]) and grf[i+1].txt[1]=="." and ir(grf[i+1].txt[2]) and ln(grf[i+1].txt)==3:
                    adC(i,g.txt+" "+grf[i+1].txt,"ФИО")
                    grf[i+1].isPart = True
                # ИОФ - И.О. Фамилия | И. Фамилия| Имя Отчество Фамилия
                if i < lnn-3 and ll==3 and ir(s[0]) and s[1]=="." and ir(s[2]) and grf[i+1].txt=="." and (grf[i+2].tip[0]=="Лек" or grf[i+2].tip[0]=="Lex") and not part:
                    adC(i,g.txt+grf[i+1].txt+" "+grf[i+2].txt,"ИОФ")
                    grf[i+1].isPart = True
                    grf[i+2].isPart = True
                # слова в р а з р я д к у
                if i<lnn-3 and il(g.txt) and ln(g.txt)==1 and il(grf[i+1].txt) and ln(grf[i+1].txt)==1 and il(grf[i+2].txt) and ln(grf[i+2].txt)==1:
                    ss=""
                    for ii in range(i,lnn):
                        if il(grf[ii].txt) and ln(grf[ii].txt)==1:
                            ss+=grf[ii].txt
                            grf[ii].isPart = True
                        else: break
                    adG(i,ss,"вразр")
                if i<lnn-3 and iU(g.txt) and ln(g.txt)==1 and iU(grf[i+1].txt) and ln(grf[i+1].txt)==1 and iU(grf[i+2].txt) and ln(grf[i+2].txt)==1:
                    st=""
                    for ii in range(i+1,lnn):
                        if iU(grf[ii].txt) and ln(grf[ii].txt)==1:
                            st+=grf[ii].txt
                            grf[ii].isPart = True
                        else: break
                    adG(i,st,"ВРАЗР")
            # - время: 6 час 12 мин
            #   -- если g = "чис" и после него идёт "час"...
            # - гео адреса: ул. Прямая, д. 20, кв. 46, ком. 2
            # - многословные топонимы: Набережные Челны
            # - наименования - после сокращений
            # - названия
            #    -- Слова С Большой Буквы
            #    -- ООО "Стройбат" | ОАО Забугор | Lochi Ltd. | gmbh. Arcon
            # - имя файла с параметрами командной строки:
            #   --   python.exe -o str.py
            #       -- за именем файла следуют латинские символы либо другие имена файлов

            # обработка одиночных нераспознанных графем:

                if sFin(":")>0 and g.isPart == False:
                    if isTime(s): adC(i,s,"TIME")
                    # если встретили точку, то
                    if s.find(".")>0:
                        tm = s.split(".")
                    # левая часть - время
                        if isTime(tm[0]) and iD(tm[1]) and ln(tm)==2: adC(i,s,"TIME_MSEC")
                    # если в строке есть "AM" или "PM",то
                    if sFin("AM")>0:
                        tim = s[0:sFin("AM")]
                        if isTime(tim): adC(i,s,"TIME_AM")
                    elif sFin("PM")>0:
                        tim = s[0:sFin("PM")]
                        if isTime(tim): adC(i,s,"TIME_PM")
            # - номера телефонов - 0-000-000-00-00   +7-953-354-99-61
            #   8(912)370-13-27     8 912 370 13 27     8 912 370-13-27
            #   если каждая часть "чис" и размер меньше 11

            # - однословные топонимы
            # - однословные наименования

            # - аббревиатуры - вуз, МУП, с.г.с., N.A.T.O.
            #   -- таблица стандартных аббревиатур
            #   -- если в слове есть "." после каждой буквы
            #   -- если все слова с большой буквы и содержится в таблице

            # - дата:  ДД/ММ/ГГ(ГГГГ)   ДД.ММ.ГГ(ГГГГ)
            #   -- поиск "/" в строке
            #   -- разбиение строки "/"
            #   -- первые две часть не более 2 символов и больше 0
            #   -- третья часть не менее 2-х и не более 4-х
            #   -- разделитель "." - далее тоже
                if iD(s[0]) and g.isPart == False:
                    date1 = isDate(s,".")
                    date2 = isDate(s,"/")
                    if date1 or date2: adC(i,s,"DATE")
                # IPv4 -         8.8.8.8
                if iD(s[0]) and g.isPart == False:
                    ip4 = False
                    ip6 = False
                    ss = s.split(".")
                    if ln(ss)==4:
                        for st in ss:
                            if iD(st) and ln(st)<4 and ln(st)>0:ip4=True
                            else:
                                ip4=False
                                break
                # IPv6 -         223.221.122.128.121
                    if ln(ss)==6:
                        for st in ss:
                            if iD(st) and ln(st)<4:ip6=True
                            else:
                                ip6=False
                                break
                    if ip4: adC(i,s,"IP4")
                    elif ip6: adC(i,s,"IP6")
                # электронные адреса
                # если в строке есть "/"
                #if s.find("/")>0 and not part:
                    #pass
                # адрес сайта -  http://ams.ru/    http2://ams.ru/
                if sFin("http")>0 and g.isPart == False:
                    adC(i,s,"FUL_SRV")
                # FTP адрес -    ftp://asd.de
                if sFin("ftp:")>0 and g.isPart == False:
                    adC(i,s,"FTP_ADR")
                # веб адрес -    www.dom.com   www2.dot.com
                if sFin(".")>0 and g.isPart == False:
                    web = s.split(".")
                    if web[0]=="www":adC(i,s,"WEB_ADR")
                # е-мэйл
                if sFin("@")>0 and g.isPart == False:
                    e_mail = s.split("@")
                    # левая часть имя пользователя, правая - почтовый сервер
                    if isE_name(e_mail[0]) and isAdress(e_mail[1]):
                        adC(i,s,"E_MAIL")
                # простой адрес сайта(сервера) - google.com
                if isAdress(s) and g.isPart == False:
                    adC(i,s,"ADR_SRV")

            #   -- отличие модификаторов доступа от доменов второго и др. уровней
            #       molotok.hh.ru   MyClass.property.set

                # имя файла -   doom.exe
                if isFile_name(s):
                    if g.isPart != True and g.tip[0]!="СОК": adC(i,s,"FILE")
                    else: g.tip.append("FILE")
                # полный путь -   C:\Directory\File.txt
                if findSlash(s) and not g.isPart:
                    path = s.split("\\")
                    if ln(path[0])>1:
                        if iS(path[0][0]) and path[0][1]==":":
                        # в конце либо директория, либо "имя_файла"
                            if isFile_name(path[-1]): adC(i,s,"FILE_PATH")
                            else: adC(i,s,"F_PATH")
                        else: adC(i,s,"PATH")

            # - цифры с буквами - 10h, 1997г, 1в
            # - если первый символ - цифра, то:
            #   -- если на конце "г" и слева 2-4 цифры, то это год
            #   -- если часть перед "г" - дата, то сохранить как "DATE"
            #   -- если последний символ "h" и перед ним только число, то
            #       пометить его как шестнадцатеричное - "HEX"
            # - цифры с окончаниями - 1-ый, 10го, 2-х
            #   -- сканируем слово с конца до "-", если есть
            #   -- берём левую часть - если это "чис", то тип графемы "чис","окон"
            #   -- если в слове нет "-" и окончание примыкает к числу, то
            #       сканируем с конца строки до первого числа
            #       копируем всё до этой позиции и если это "чис", то + "окон"

            # - формат записи числа:
            #   --    1000    - целочисленные
            #   --    -1      - отрицательные
            #   --    1.0     - дробные
            #   --    0.1+е8  - сокращённая запись - можно развернуть,
            #                   если после 'е' не более 32
            #   --    5i      - комплексные
            #   --    0x01    - шестнадцатеричные

            # - Латинские цифры: все XIX   XV   VL   CL
            #   -- если после лат символов идёт вв. или в.
            #   -- если перед символами идёт "век" в различных формах
            #   -- перевести в число
            #   -- однозначные: II  III  IV  VI  VII   VIII  IX  XI  XII  XIII
            #       XIV XV  XVI  XVII XVIII  XIX  XXI  XXII  ...
            #       XL  XLI  XLII  XC MXIX  MCIX  MCXLII ...
            #   -- неоднозначные: X  XX  XXX  XV  XC  CX  CV  CLX CXX  MC  MMCV ...

            # разделение слитных графем

                elif not part: app(g)
            elif not part: app(g)
        self.Grafems = gf

    def findPoints(self):
        i = 0
        ln = len
        grf = self.Grafems
        gf = []
        app = gf.append
        cG = self.createGrafem
        gZ = self.getZnakTip
        lnn = ln(grf)
        for i in range(lnn):
            g = grf[i]
            s = g.txt
            part = g.isPart
            if i+2 < lnn and not part:
                ds = s+grf[i+1].txt+grf[i+2].txt
                if ds == "...":
                    grf[i+2].isPart = True
                    grf[i+1].isPart = True
                    g.isPart = True
                    if g.tip[0] == "E_DEL": app(cG(ds,"E_DEL","МТЧ"))
                    elif g.tip[0] == "B_DEL": app(cG(ds,"B_DEL","МТЧ"))
                    else: app(cG(ds,"DEL","МТЧ"))
                elif not part:app(g)
            elif not part:app(g)
        self.Grafems = gf

    def findPromt(self):
        """
        алгоритм поиска границ предложений:
            - предложение всегда начинается с большой буквы
            - предложение не больше абзаца
            - не может состоять из одних знаков препинания
        """
        i = 0
        ii = 0
        ln = len
        grf = self.Grafems
        prmt = self.Promts
        Gr = self.createGrafem
        gG = self.getGraf
        isup = self.isUP
        isZ = self.isZnak
        soc = self.Sokr
        gf = []
        prm = []
        appr = prm.append
        cop = prm.copy
        appen = gf.append
        lnn = ln(grf)
        lnl = lnn-1
        EN = False
        for i in range(lnn):
            g = grf[i]
            part = g.isPart
            if g.tip[0] == "E_DEL" or g.tip[0]=="DEL" and not part:
                if ln(g.tip)>1 and self.isEndPromt(g.tip[1]):
                    # если после точки [через пробел] не идёт другой знак и слово с маленькой буквы
                    if i>0 and i<lnn-3 and isZ(grf[i+1].txt) and not isup(grf[i+2].txt):
                    # иначе точка - часть составной графемы (ФИО, аббревиатура, адрес ...)
                        appr(g)
                        appr(grf[i+1])
                        g.isPart = True
                        grf[i+1].isPart = True
                    # если далее запятая(ТЗП, ДВТ), то это не конец
                    elif i>0 and i<lnn-2 and ln(grf[i+1].tip)>1:
                        appr(g)
                        if grf[i+1].tip[1]=="ЗПТ" or grf[i+1].tip[1]=="ТЗП" or grf[i+1].tip[1]=="ДВТ":
                            appr(grf[i+1])
                            g.isPart = True
                            grf[i+1].isPart = True
                        elif isup(grf[i+1].txt):
                            if i<lnl and grf[i+1].tip[0]=="EOS":
                                appr(grf[i+1])
                                grf[i+1].isPart = True
                            pr = promt()
                            pr.Grafems = cop()
                            appen(pr)
                            prm.clear()
                    # если слово с точкой не является сокращением
                    # и после точки слово с большой буквы
                    # или после него едёт конец текста
                    elif i>0 and grf[i-1].tip[0] != "СОК" or i == lnl:
                        appr(g)
                        # любой знак включается в предложение
                        # может стоять несколько знаков: слово., - другая часть строки
                        if i<lnl and isZ(grf[i+1].txt):
                            appr(grf[i+1])
                            grf[i+1].isPart = True
                        pr = promt()
                        pr.Grafems = cop()
                        appen(pr)
                        prm.clear()
                    # либо слово с большой буквы - ЛЕК,Лек,ЛеК,LEX,Lex,LeX после сокращения
                    elif i>0 and i < lnn-2 and grf[i-1].tip[0] == "СОК" and isup(grf[i+1].txt):
                        # если сокращение не требует после себя слов:
                        if soc.needPost(grf[i-1].txt+".") == False:
                            appr(g)
                            if i < lnl and isZ(grf[i+1].txt):
                                appr(grf[i+1])
                                grf[i+1].isPart = True
                            pr = promt()
                            pr.Grafems = cop()
                            appen(pr)
                            prm.clear()
                        elif not part: appr(g)
                    elif not part: appr(g)
                elif not part: appr(g)
            # если не нашли границу предложения, а текст закончился, то пометить
            # конец текста как конец предложения
            elif i== lnl and not part:
                appr(g)
                pr = promt()
                pr.Grafems = cop()
                appen(pr)
                prm.clear()
            elif not part:
                appr(g)
        self.Promts = gf

    def postProcess(self):
        """
        правка списка графем - объединение, разбиение
        - поиск сокращений
        - обработка составных графем
        - выделение предложений
        """
        self.findSokr()
        self.findPoints()
        self.findSostav()
        self.findPromt()