# define a class person

class Person:
    Applicant_PID = ""
    PersonID = ""
    First_Name = ""
    Last_Name = ""
    English_Name = ""
    Gender = ""
    Date_of_Birth = None
    Country_of_Birth = ""
    Province_of_Birth = ""
    Citizenship = ""
    Tax_Status = ""
    Live_in_Canada_Since = None
    Marital_Status = ""
    Cellphone = ""
    Homephone = ""
    Workphone = ""
    SIN = ""
    Email = ""
    Postcode = ""
    PersonType = ""
    Bankruptcy = 0
    Discharge_Date = None
    AdvisorPID = ""
    Start_date = None
    End_date = None
    Current_Flag = 0
    Verify_date = None
    Notes = ""
        
    @classmethod
    def New_person(
        cls, 
        Applicant_PID,
        PersonID,
        First_Name,
        Last_Name,
        English_Name,
        Gender,
        Date_of_Birth,
        Country_of_Birth,
        Province_of_Birth,
        Citizenship,
        Tax_Status,
        Live_in_Canada_Since,
        Marital_Status,
        Cellphone,
        Homephone,
        Workphone,
        SIN,
        Email,
        Postcode,
        PersonType,
        Bankruptcy,
        Discharge_Date,
        AdvisorPID,
        Start_date,
        End_date,
        Current_Flag,
        Verify_date,
        Notes):
        
        p=cls()
        p.Applicant_PID = Applicant_PID
        p.PersonID = PersonID
        p.First_Name = First_Name
        p.Last_Name = Last_Name
        p.English_Name = English_Name
        p.Gender = Gender
        p.Date_of_Birth = Date_of_Birth
        p.Country_of_Birth = Country_of_Birth
        p.Province_of_Birth = Province_of_Birth
        p.Citizenship = Citizenship
        p.Tax_Status = Tax_Status
        p.Live_in_Canada_Since = Live_in_Canada_Since
        p.Marital_Status = Marital_Status
        p.Cellphone = Cellphone
        p.Homephone = Homephone
        p.Workphone = Workphone
        p.SIN = SIN
        p.Email = Email
        p.Postcode = Postcode
        p.PersonType = PersonType
        p.Bankruptcy = Bankruptcy
        p.Discharge_Date = Discharge_Date
        p.AdvisorPID = AdvisorPID
        p.Start_date = Start_date
        p.End_date = End_date
        p.Current_Flag = Current_Flag
        p.Verify_date = Verify_date
        p.Notes = Notes
        return p
  
    @property
    def Full_Name(self):
        #print("Getting value...")
        return self.First_Name + ' ' + self.Last_Name
# the end of Person class definition        

class Beneficiary(Person):
    Applicant_PID = ''
    AIF_Invest_No = ''
    B_Relationship = ''
    B_Percentage = 0
    Revokable = 0 
    
# the end of Beneficiary class definition

class Spouse(Person):
    Applicant_PID = ''
    S_Relationship = 'Spouse'
    
# the end of Spouse class definition

class Trustee(Person):
    Applicant_PID = ''
    T_Relationship = ''

    
# the end of Trustee class definition

class Advisor(Person):
    AdvisorID = None
# the end of Advisor class definition


class Address:
    PersonID = None
    Apt_No = ''
    Street_No = ''
    Street_Name = ''
    City = ''
    Province = ''
    Country = ''
    Postcode = ''
    Homephone = ''
    Living_Status = ''
    Start_Date = None
    End_Date = None
    Current_Flag = ''
    Verify_Date = None
    Notes = ''
        
    @classmethod
    def New_address(
        cls,
        PersonID,
        Apt_No,
        Street_No,
        Street_Name,
        City,
        Province,
        Country,
        Postcode,
        Homephone,
        Living_Status,
        Start_Date,
        End_Date,
        Current_Flag,
        Verify_Date,
        Notes):
        
        a=cls()
        a.PersonID = PersonID,
        a.Apt_No = Apt_No,
        a.Street_No = Street_No,
        a.Street_Name = Street_Name,
        a.City = City,
        a.Province = Province,
        a.Country = Country,
        a.Postcode = Postcode,
        a.Homephone = Homephone,
        a.Living_Status = Living_Status,
        a.Start_Date = Start_Date,
        a.End_Date = End_Date,
        a.Current_Flag = Current_Flag,
        a.Verify_Date = Verify_Date,
        a.Notes = Notes
        return a
  
    @property
    def Full_Adress(self):
        #print("Getting value...")
        return self.Apt_No + ', ' + self.Street_No + ' ' + self.Street_Name + ', ' + self.City + ', ' + self.Province + ', ' + self.Country + ', ' + self.Postcode
# the end of Address class definition        

class ID:
    PersonID = None
    ID_Type = None
    ID_Number = None
    Issue_Date = None
    Expiry_Date = None
    Issue_Country = None
    Issue_Province = None
    Start_Date = None
    End_Date = None
    Current_Flag = None
    Verify_Date = None
    Notes = None
        
    @classmethod
    def New_ID(
        cls,
        PersonID,
        ID_Type,
        ID_Number,
        Issue_Date,
        Expiry_Date,
        Issue_Country,
        Issue_Province,
        Current_Flag,
        Verify_Date,
        Notes):
        
        i=cls()
        i.PersonID = PersonID,
        i.ID_Type = ID_Type,
        i.ID_Number = ID_Number,
        i.Issue_Date = Issue_Date,
        i.Expiry_Date = Expiry_Date,
        i.Issue_Country = Issue_Country,
        i.Issue_Province = Issue_Province,
        i.Current_Flag = Current_Flag,
        i.Verify_Date = Verify_Date,
        i.Notes = Notes
        return i
  
# the end of ID class definition 

class Asset:
    PersonID = None
    Assets_Type = None
    Market_Value = None
    Institution = None
    Address = None
    Current_Flag = 1
    Verify_Date = None
    Notes = None
        
    @classmethod
    def New_Asset(
        cls,
        PersonID,
        Assets_Type,
		Market_Value,
		Institution,
		Address,
        Current_Flag,
		Verify_Date,
		Notes):
        
        ass=cls()
        ass.PersonID,
        ass.Assets_Type,
        ass.Market_Value,
        ass.Institution,
        ass.Address,
        ass.Current_Flag,
        ass.Verify_Date,
        ass.Notes
        return ass
  
# the end of Asset class definition 

class Liability:
    PersonID = None
    L_Type = None
    L_Balance = None
    L_Monthly_Payment = None
    Institution = None
    Address = None
    Current_Flag = 1
    Verify_Date = None
    Notes = None
        
    @classmethod
    def New_Asset(
        cls,
        PersonID,
        L_Type,
        L_Balance,
        L_Monthly_Payment,
        Institution,
		Address,
        Current_Flag,
		Verify_Date,
		Notes):
        
        liab=cls()
        liab.PersonID,
        liab.L_Type,
        liab.L_Balance,
        liab.L_Monthly_Payment,
        liab.Institution,
        liab.Address,
        Liab.Current_Flag,
        liab.Verify_Date,
        liab.Notes
        return liab
  
# the end of Liability class definition 

class Employment:
    PersonID = None
    Employment_Status = None
    Employer = None
    Industry = None
    Occupation = None
    Income = None
    Unit = None
    Street_No = None
    Street_Name = None
    City = None
    Province = None
    Country = None
    Postcode = None
    Workphone = None
    Start_Date = None
    End_Date = None
    Current_Flag = None
    Verify_Date = None
    Notes = None
        
    @classmethod
    def New_Employemnt(
        cls,
        PersonID,
        Employment_Status,
        Employer,
        Industry,
        Occupation,
        Unit,
        Street_No,
        Street_Name,
        City,
        Province,
        Country,
        Postcode,
        Workphone,
        Income,
        Start_Date,
        End_Date,
        Current_Flag,
        Verify_Date,
        Notes):
        
        e=cls()
        PersonID = PersonID,
        Employment_Status = Employment_Status,
        Employer = Employer,
        Industry = Industry,
        Occupation = Occupation,
        Unit = Unit,
        Street_No = Street_No,
        Street_Name = Street_Name,
        City = City,
        Province = Province,
        Country = Country,
        Postcode = Postcode,
        Workphone = Workphone,
        Income = Income,
        Start_Date = Start_Date,
        End_Date = End_Date,
        Current_Flag = Current_Flag,
        Verify_Date = Verify_Date,
        Notes = Notes
        return e
  
# the end of Asset class definition



class ResponseDTO(object):
    Succeeded = False
    __ErrCode = 0
    ErrorMsg = None

    @property
    def ErrorCode(self):
        #print("Getting value...")
        return self.__ErrCode

    @ErrorCode.setter
    def ErrorCode(self, value):
        #print("Setting value...")
        self.Succeeded = (value == 0)
        self.__ErrCode = value