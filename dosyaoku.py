import numpy
from matplotlib import pyplot as plt
from matplotlib import style
import datetime

f = open("tarihler.txt", "r")

saatler = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] # saatler

haftanin_günleri = ("Mon ", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    "Tue ", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    "Wed ", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    "Thu ", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    "Fri ", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    "Sat ", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    "Sun ", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    )

hafta_günü_tut = ""

for i in f:
    göz_kapama_saati = int(i[-3:-1])
    
    
    if(hafta_günü_tut != i[0:3]):
        hafta_günü_tut = i[0:3]
    
       
    for guntk in range(0,14,2):
        if(i == str(haftanin_günleri[guntk])+str(int(i[-3:-1]))+"\n"):  
            haftanin_günleri[guntk+1][göz_kapama_saati-1] = haftanin_günleri[guntk+1][göz_kapama_saati-1] + 1
                

gstr = False
style.use('ggplot')
renkler = ["red","green","blue","orange","black","purple","yellow"]

for n in range(0,14,2):
    mymodel = numpy.poly1d(numpy.polyfit(saatler, haftanin_günleri[n+1], 3))
    myline = numpy.linspace(1, 24, 100)
        
    line_x = saatler[90:]
    line_y = haftanin_günleri[n+1][90:] # eğitilmiş veriler
    plt.scatter(line_x, line_y)      # eğitilmiş verilerin rafiğini gösterir
        
    
    plt.plot(myline,mymodel(myline),renkler[int(n/2)],label=haftanin_günleri[n], linewidth=3)
     
    
    
if(gstr == False):
    print()
    
    print("---------Veriler---------")
    plt.title('Yorgunluk grafiği')
    plt.ylabel('Yorgunluk seviyesi')
    plt.xlabel('Saatler')
    plt.legend()
    plt.grid(True,color='k')
    plt.show()       
        



print("Veriler dahilinde olan sınır 150 dir bu eşik geçildiği durumlarda kullanıcının depreson seviyesi aşılmış durumdadır acil olarak destek alması gerekmektedir")


