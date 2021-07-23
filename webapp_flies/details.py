#!/usr/bin/python3

import cgi

print("content-type: text/html")
print()

recieve = cgi.FieldStorage()
plate_number=recieve.getvalue("y")




if plate_number == "MH 20 TC 1107E":
    print("<body style='padding: 40px;'>")
    print('<h2> Number Plate Detected: MH 20 TC 1107E </h2>')
    print('<h1 style="color:Blue;" >VECHICLE DETAILS</h1>')
    print('''<pre>
    Registration Name : ARYAN SHARMA
    License No : 12345677889
    Make / Model : BMW X4
    Registration Date : 11/12/2015
    Registering Authority : DELHI , INDIA
    Vehicle Class : MCWG
    Fuel Type : DIESEL
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 15/03/2030
    Fitness Upto : 14/08/2035
    </pre>''')
    print("</body>")

elif plate_number == "DL 11 FW 5120":
    print("<body style='padding: 40px;'>")
    print('<h2> Number Plate Detected: DL 11 FW 5120 </h2>')
    
    print('<h1 style="color:Blue;" >VECHICLE DETAILS</h1>')
    print('''<pre>
    Registration Name : ANIKET KUMAR
    License No : 098363357292
    Make / Model : MARUTI SUZUKI / SWIFT
    Registration Date : 1/12/2014
    Registering Authority : DELHI, INDIA
    Vehicle Class : MCWG
    Fuel Type : PETROL
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

elif plate_number == "HP 12 HZ 0148":
    print("<body style='padding: 40px;'>")
    print('<h2> Number Plate Detected: HP 12 HZ 8148 </h2>')
    
    print('<h1 style="color:Blue;" >VEHICLE DETAILS</h1>')
    print('''<pre>
    Registration Name : PIYUSH THAKUR
    License No : 735382528936
    Make / Model : HYUNDAI / I20  
    Registration Date : 1/12/2014
    Registering Authority : HIMACHAL PRADESH, INDIA
    Vehicle Class : MCWG
    Fuel Type : PETROL
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("This vehicle number is not registered in our database.")
    print("</body>")


