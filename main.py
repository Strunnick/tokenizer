#-------------------------------------------------------------------------------
# Name:        Основной модуль парсинга
# Author:      ash-911
# Created:     19.06.2016
# Copyright:   (c) ash-911 2016
#-------------------------------------------------------------------------------

from g_analiser import Grafem_Analiser
import time

GRF = Grafem_Analiser()

def main():
    i = 0
    ln = len
    # строка текста для анализа
    st = """В русский ЯЗЫК слово пришло в конце XVII – начале XVIII вв., во времена Петровских реформ. Однако настоящую популярность оно приобрело лишь в начале XIX в.
 В буквальном переводе с французского «абажур» обозначает «то, что отражает свет». Но в России первым его значением было «косое окошко, сообщающее свет сверху».
 Именно с таким значением оно впервые вошло и в словарь русского языка 1803 г. выпуска.
 Производные: абажурный, абажурчик."""
    ss = "А Именно – StrOka 1, . о, адм.-терр. \" («со скобками.») и т. д."
    s = """128.168.128.100 ash-911@yandex.ru google.com И.М. Иванов; 12.03.2016 - зам. нач. 12:00AM 12:24:32.953 C:\Dir\Con MyFile123.exe C:\Os\Dir\File.txt."""
##    clc = time.time()
##    i = 0
##    for i in range(280):
    GRF.process_(st)
    GRF.postProcess()
##    clc = time.time() - clc
##    print( "время обработки: {0:.2f} секунд".format(clc))
    #print("результаты: %s" % GRF.Tokens)
    print ("число графем: %s" % len(GRF.Grafems))
    print ("число предложений: %s" % len(GRF.Promts))
    #for i in range(ln(GRF.Grafems)):
        #print("{}={}".format(GRF.Grafems[i].tip,GRF.Grafems[i].txt))
    for i in range(ln(GRF.Promts)):
        print("Предложение №%s" % i)
        for ii in range (ln(GRF.Promts[i].Grafems)):
            print("{}={}".format(GRF.Promts[i].Grafems[ii].tip,GRF.Promts[i].Grafems[ii].txt))

if __name__ == '__main__':
    main()
    #с = input()