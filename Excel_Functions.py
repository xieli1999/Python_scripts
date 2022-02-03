import re
import datetime
from datetime import datetime

# get province of birth and country of birth separately
#if "China" or "USA" or "Canada" was found in place of country&province, 
# "China" or "USA" or "Canada" will be filled into Country of Birth
# otherwise, this information will be filled into province of birth
def CN_Prov_of_birth(place_of_birth):
    if "China" in place_of_birth:
        Country_of_Birth = "China"
        ProvinceOB = place_of_birth.replace("China", "")
        ProvinceOB = (re.sub('[,&]', '', ProvinceOB)).strip()
        Province_of_Birth = ProvinceOB
    elif "USA" in place_of_birth or "United States" in place_of_birth:
        Country_of_Birth = "USA"
        ProvinceOB = place_of_birth.replace('USA', '').replace('United States', '')
        ProvinceOB = (re.sub('[,&]', '', ProvinceOB)).strip()
        Province_of_Birth = ProvinceOB
    elif "Canada" in place_of_birth or "CAN" in place_of_birth:
        Country_of_Birth = "CANADA"
        ProvinceOB = place_of_birth.replace('CANADA', '').replace('CAN', '')
        ProvinceOB = (re.sub('[,&]', '', ProvinceOB)).strip()
        Province_of_Birth = ProvinceOB
    else:
        Country_of_Birth = ""
        Province_of_Birth = place_of_birth
    return Country_of_Birth, Province_of_Birth
    
#comibnation of Date of Birth
 

def Date_of_Birth(Y_of_Birth,M_of_Birth,D_of_Birth):
    
    if isinstance(M_of_Birth, datetime):
        month_of_birth=int(datetime.strftime(M_of_Birth,"%m"))
    else:
        month_of_birth = int(datetime.strptime(M_of_Birth, "%b").strftime("%m"))
    
    return datetime(Y_of_Birth,month_of_birth,D_of_Birth)


def Validate_SIN(SINNo):
        nDigits = len(SINNo)
        nSum = 0
        isSecond = False

        # if len(SINNo) != 9 or SINNo[0] == '8' or SINNo[0] == '0':
        if SINNo[0] == '8' or SINNo[0] == '0':
            # print("This is not a valid SIN")
            return False
        elif nDigits != 9 :
            return False
        else:
            for i in range(nDigits - 1, -1, -1):
                d = ord(SINNo[i]) - ord('0')

                if (isSecond == True):
                    d = d * 2

                nSum += d // 10
                nSum += d % 10

                isSecond = not isSecond

            if (nSum % 10 == 0):
                return True
            else:
                return False

        if (checkLuhn(SINNo)):
            return True
        else:
            return False