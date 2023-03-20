from logic import plustwo,falldist,areaOfCir,intrest
class presentation:
    out2=falldist(10)
    out1=plustwo(2)
    out3=areaOfCir(10, 3.14)
    p=int(input("Enter principal amount:"))
    r=int(input("Enter rate of Intrest:"))
    n=int(input("Enter num of years:"))
    print('The sum of num:',out1)
    print('The fallDist is:',out2)
    print('The area of circle is:',out3)
    print('The rate of intrest is:',intrest(p, r, n))

