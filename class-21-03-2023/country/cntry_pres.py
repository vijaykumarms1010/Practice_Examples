# country means cityname,areaname and pincode.

# 1. add a country information
# 2. change country information.. cityname and areaname..
# we can change cityname and areaname but not pincode.
# 3. if we give cityname. we should get all the area and pincodes..
# 4. if we give pincode, it should tell cityname and areaname.
# 5. sort 
# 	5.1 cityname
# 	5.2 areaname
# 	5.3 pincode
# 0. exit

from cntry_logic import addCountry,addInfo
def start():
    exit=False
    while not exit:
        print("1.Enter Country name\n0.Exit")
        c1=int(input("Enter ur choice:"))
        
        if c1==0:
            exit=True
        elif c1==1:
            country=input("Enter country name:")
            res=addCountry(country)
            print(res)
            print("1. Add Country Info\n2.Change Country Info\n3.Get Details based on cityname\n4.Get Details by Pincode")
            ch=int(input("Enter Your choice: "))
            if ch==1:
                cityname=input("Enter city name:")
                areaname=input("Enter areaname")
                pincode=int(input("Enter pincode:"))
                x=Info(cityname,areaname,pincode)
                res=addInfo(x)
                print(res)
