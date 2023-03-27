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

class country:
    def __init__(self,cityname,areaname,pincode):
        self.cityname=cityname
        self.areaname=areaname
        self.pincode=pincode
    def __repr__(self):
        return f"CityNamet:{self.cityname},\nname:{self.areaname},\npincode:{self.pincode}"
class countrystatus():
    def __init__(self,statuscode,message,countryobj):
        self.statuscode=statuscode
        self.message=message
        self.countryobj=countryobj
    def __repr__(self):
        return f"{self.statuscode},{self.message},{self.countryobj}"


# def /check1():
