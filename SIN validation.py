
    

    #### convert K8 integer to string:
    SINNo = list(input("type your SIN here:"))
   
    
    def checkLuhn(SINNo):
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
        print("This is a valid SIN")
    else:
        print("This is not a valid SIN")