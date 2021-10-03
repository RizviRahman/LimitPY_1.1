
# Import Required Library 
from tkinter import *
from tkcalendar import Calendar 
from datetime import date
import os 
import xml.etree.ElementTree as ET

# Create Object 
page = Tk() 

#get current date
today = date.today()



## csv file read to import limit data
import csv

dailyLimit = {}
mobileLimit = {}

with open('LimitFile/dailyLimit.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        dailyLimit[row[0]] = row[1]
        
# print(dailyLimit)


with open('LimitFile/mobileLimit.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if(int(row[1])<0):
            row[1] = '0'
        mobileLimit[row[0]] = row[1]
       
# print(mobileLimit)

## end of csv file read to import limit data



#dictionary to store all limit
# dailyLimit = {
#             'DN2485':'100000',
#             'DN2638':'500000',
#             'DN2024':'1500000',
#             'DN1515':'500000',
#             'DN2070':'400000',
#             'D2000':'10000000',
#             'DN3000':'2000000',
#             'DN2009':'400000',
#             'DN2004':'600000',
#             'DN2005':'500000',
#             'DN2622':'1000000',
#             'DN2012':'1000000',
#             'N633':'500000',
#             'N188':'500000',
#             'DN2444':'500000',
#             'N134':'500000',
#             'DN1780':'500000',
#             'DN1781':'500000',
#             'DN1922':'500000',
#             'N4036':'300000',
#             'DN2959':'200000',
#             'DN3066':'10000000',
#             'DN3056':'2000000',
#             'DN3128':'10000000',
#             'DN1729':'500000',
#             'DN2375':'500000',
#             'DN3062':'100000',
#             'DN3078':'50000',
#             'DN3075':'1000000',
#             'DN3084':'50000',
#             'DN3090':'1000000',
#             'DN3246':'1000000',
#             'DN3293':'2000000',
#             'DN3294':'100000',
#             'DN3276':'500000',
#             'DN1970':'700000',
#             'N191':'50000',
#             'D1838':'300000',
#             'D1938':'300000',
#             'NK1184':'700000',
#             'NK1136':'11000000',
#             'NK1169':'1000000',
#             'NK1191':'10000000',
#             'NK1101':'600000',
#             'NK1072':'300000',
#             'NK1123':'200000',
#             'NK1171':'200000',
#             'NK1118':'700000',
#             'NK1094':'2000000',
#             'NK1068':'1000000',
#             'NK1173':'150000',
#             'NK1194':'1000000',
#             'NK1067':'300000',
#             'NK1032':'1000000',
#             'NK1259':'400000',
#             'NK1052':'85500',
#             'NK1053':'600000',
#             'NK1054':'427000',
#             'NC125':'400000',
#             'NC545':'1000000',
#             'DN2999':'200000',
#             'DN2681':'300000',
#             'DN2682':'1000000',
#             'DN3052':'500000',
#             'DN2882':'300000',
#             'NK1234':'250000',
#             'D1986':'100000',
#             'DN2627':'100000',
#             'DN3136':'1000000',
#             'D1033':'600000',
#             'NK1168':'1500000',
#             'NK1271':'400000',
#             'NK1261':'70000',
#             'DN2454':'1500000',
#             'NC547':'200000',
#             'DN1499':'200000',
#             'DN2000':'3000000',
#             'DN2222':'5000000',
#             'DN3403':'500000',
#             'DN3058':'5000000',
#             'NK95':'7000000',
#             'N97':'500000',
#             'DN3070':'1000000',
#             'DN3287':'200000',
#             'DN3278':'100000',
#             'NK1024':'100000',
#             'NK1188':'300000',
#             'NK1317':'500000',
#             'NC418':'500000',
#             'NK1257':'500000',
#             'DN3280':'2000000',
#             'DN3294':'200000'
#             #'N183':'1000000',
#          }

# #dictionary to store mobile code
# mobileLimit = {
#             'C1781':'677',
#             'D716':'46584',
#             'D420':'0',
#             'C2880':'0',
#             'C2927':'0',
#             'D1827':'4',
#             'D1842':'694',
#             'C3021':'556',
#             'C3023':'0',
#             'D1876':'2484',
#             'C3091':'9585',
#             'D1889':'11793',
#             'C3118':'29623',
#             'C3119':'10782',
#             'C3149':'9137',
#             'D1910':'8705',
#             'D1911':'27984',
#             'D1920':'29',
#             'K214':'1671',
#             'C3182':'103218',
#             'C3200':'31387',
#             'C3264':'467182'
            
#             #daily limit          'D1986':'0',
#         }



y = int(today.strftime("%Y"))
m = int(today.strftime("%m"))
d = int(today.strftime("%d"))
# Set geometry 
page.geometry("400x400") 
  
# Add Calender 
cal = Calendar(page, selectmode = 'day', 
               year = y, month = m, day = d, 
               firstweekday = 'sunday', weekenddays = [6,7], 
               date_pattern = "dd.mm.yy", showweeknumbers = False, 
               weekendbackground = 'Light Green') 
  
cal.pack(pady = 5) 
  
def grad_date(): 
    date.config(text = "Selected Date is: " + cal.get_date()) 
    date_c = cal.get_date()
    date_list = date_c.split(".")
    month = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

    file_start = str(y) + date_list[1] + date_list[0]
    file_end = "*.xml"


    ch_dir = '\\\\150.1.62.26\\'+str(y)+'\\'+ month[int(date_list[1])-1] + '-' + date_list[2]

    #creating month folder in required destination using date format
    if not os.path.exists(ch_dir):
        os.mkdir(ch_dir) 
    
    os.chdir(ch_dir)
    

    #creating date folder in required destination using date format
    if not os.path.exists(date_c):
        os.mkdir(date_c) 


    src = "\\\\150.1.62.2\MottaiXML\\"
    
    #src = "E:\Projects\LimitPY\FinalProjectBefore_run\src\\"
    #dst = "E:\Projects\LimitPY\FinalProjectBefore_run\dst"

    dst = ch_dir + "\\" + date_c
    #dst = "\\\\150.1.62.26\\2021\MAR-21\\" + "test"

    cmd = "copy " + src + file_start + file_end +' '+ dst
    os.system(cmd)

    os.chdir(dst)

    cli_files = os.listdir('.')

    for cl_file in cli_files:
        if cl_file.endswith("-clients-RBS.xml"):
            xml_to_read = cl_file
            break

    tree = ET.parse(xml_to_read)
    root = tree.getroot()
    print('Client Code', '\t\t[Old]', '\t\t[New]')
    for limit in root.findall('Limits'):            # using root.findall() to avoid removal during traversal
        client = str(limit.find('ClientCode').text)
        cash = limit.find('Cash').text

        new_cash = dailyLimit.get(client,'noNeed')  #collecting cash limit if required to change
        #print(client,': ',new_cash)

        mobile_limit = mobileLimit.get(client,'noNeed') #collecting mobile limit 
        
        if new_cash !='noNeed' and int(new_cash) > int(cash):
            limit.find('Cash').text = new_cash
            print(client, '\t\t',cash, '\t\t',new_cash)

        if mobile_limit != 'noNeed':
            limit.find('Cash').text = mobile_limit
            print(client, '\t\t',cash, '\t\t',mobile_limit, '\tMobile code')

        
    tree.write('new.xml')

    toFormatXML = open("new.xml", "r")
    content = toFormatXML.read()
    toFormatXML.close()
    os.remove("new.xml")
    os.remove(xml_to_read)
    firstLine = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n\n"

    formatXML = open(xml_to_read, "w")
    formatXML.write(firstLine)
    formatXML.write(content)
    formatXML.close()
    print("Done")



# Add Button and Label 
Button(page, text = "Generate", command = grad_date).pack(pady = 20) 


date = Label(page, text = "") 
date.pack(pady = 5) 


Button(page, text = "Exit", command = exit).pack(pady = 10)    
# Excecute Tkinter 
page.mainloop()
