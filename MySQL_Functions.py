#This module includes all functions that are related to MySQL

import os
from re import S
import pymysql
from google.cloud.sql.connector import connector
import sqlalchemy
import Class_Definition
from Class_Definition import Beneficiary, Person, ResponseDTO, Advisor, Address, ID, Employment, Asset, Liability, Spouse, Trustee, KYC, Income


    
class DBBase(object):
    """description of class"""
    def __init__(self):
        self.__Database = "cloud"
        if self.__Database == "cloud":
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "atomic-producer-342016-6c7dfb4be3fc.json"
            self.__Pool = sqlalchemy.create_engine("mysql+pymysql://", creator = self.__getconn,)
        else:
            self.__Pool = sqlalchemy.create_engine("mysql+pymysql://root:xieli3015@127.0.0.1:3306/aif_db_duplicate")


    def __getconn(self) -> pymysql.connections.Connection:
        # Set MySQL connection info
        _MySQL_connectionName = 'atomic-producer-342016:northamerica-northeast2:aif'
        _MySQL_host = '34.130.217.109'
        _MySQL_user = 'xieli'
        _MySQL_password = 'aifinancial'
        _MySQL_database = 'aif_db_duplicate'

        conn : pymysql.connections.Connection = connector.connect(
            _MySQL_connectionName,
            "pymysql",
            user= _MySQL_user,
            password = _MySQL_password,
            db = _MySQL_database,
        )
        return conn

# insert a new person, if this person was not in the database, it will return a string
# showing that it has been inserted, also it will return the personID of the new record. 
class AIFinanceDB(DBBase):
    def SaveApplicant(self, p: Person) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_Applicant(
                    :Person_ID,
                    :First_Name,
                    :Last_Name,
                    :English_Name,
                    :Gender,
                    :Date_of_Birth,
                    :Country_of_Birth,
                    :Province_of_Birth,
                    :Citizenship,
                    :Tax_Status,
                    :Live_in_Canada_Since,
                    :Marital_Status,
                    :Cellphone,
                    :Homephone,
			        :Workphone,
			        :SIN,
			        :Email,
			        :Postcode,
			        :PersonType,
			        :Bankruptcy,
                    :Discharge_Date,
                    :AdvisorPID,
			        :Start_date,
			        :End_date,
			        :Current_Flag,
			        :Verify_date,
			        :Notes)""",)


                result = db_conn.execute(SQL_Proc_text,
                    Person_ID = p.PersonID,
                    First_Name = p.First_Name,
                    Last_Name = p.Last_Name,
                    English_Name = p.English_Name,
                    Gender = p.Gender,
                    Date_of_Birth = p.Date_of_Birth,
                    Country_of_Birth = p.Country_of_Birth,
                    Province_of_Birth = p.Province_of_Birth,
                    Citizenship = p.Citizenship,
                    Tax_Status = p.Tax_Status,
                    Live_in_Canada_Since = p.Live_in_Canada_Since,
                    Marital_Status = p.Marital_Status,
                    Cellphone = p.Cellphone,
                    Homephone = p.Homephone,
			        Workphone = p.Workphone,
			        SIN = p.SIN,
			        Email = p.Email,
                    Postcode = p.Postcode,
			        PersonType = p.PersonType,
			        Bankruptcy = p.Bankruptcy,
                    Discharge_Date = p.Discharge_Date,
                    AdvisorPID = p.AdvisorPID,
			        Start_date = p.Start_date,
			        End_date = p.End_date,
			        Current_Flag = p.Current_Flag,
			        Verify_date = p.Verify_date,
			        Notes = p.Notes).fetchone()
            
                p.PersonID = result[1]
                _resp.ErrorMsg = result[0]
                _resp.ErrorCode = result[2]
        except Exception as e:
            _resp.ErrorCode = 99
            _resp.ErrorMsg = e
        return _resp

    def SaveTrustee(self, t: Trustee) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_Trustee(
                    :Applicant_PID,
                    :Person_ID,
                    :First_Name,
                    :Last_Name,
                    :T_Relationship,
                    :AdvisorPID)""",)

                result = db_conn.execute(SQL_Proc_text,
                    Applicant_PID = t.Applicant_PID,
                    Person_ID = t.PersonID,
                    First_Name = t.First_Name,
                    Last_Name = t.Last_Name,
                    T_Relationship = t.T_Relationship,
                    AdvisorPID =t.AdvisorPID).fetchone()
                
                _resp.ErrorMsg = result[0]
                _resp.ErrorCode = result[2]
        except Exception as e:
            _resp.ErrorCode=99
            _resp.ErrorMsg=e
        return _resp    
        
    def SaveSpouse(self, s: Spouse) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_Spouse(
                    :Applicant_PID,
                    :Person_ID,
                    :First_Name,
                    :Last_Name,
                    :Date_of_Birth,
                    :AdvisorPID)""",)

                result = db_conn.execute(SQL_Proc_text,
                    Applicant_PID = s.Applicant_PID,
                    Person_ID = s.PersonID,
                    First_Name = s.First_Name,
                    Last_Name = s.Last_Name,
                    Date_of_Birth = s.Date_of_Birth,
                    AdvisorPID = s.AdvisorPID).fetchone()
            
                s.PersonID = result[1]
                _resp.ErrorMsg = result[0]
                _resp.ErrorCode = result[2]
        except Exception as e:
            _resp.ErrorCode=99
            _resp.ErrorMsg=e
        return _resp    
        
    def SaveBeneficiary(self, b: Beneficiary) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_Beneficiary(
                    :Applicant_PID,
                    :Person_ID,
                    :First_Name,
                    :Last_Name,
                    :Relationship,
                    :Gender,
                    :Date_of_Birth,
                    :AdvisorPID)""",)

                result = db_conn.execute(SQL_Proc_text,
                    Applicant_PID = b.Applicant_PID,
                    Person_ID = b.PersonID,
                    First_Name = b.First_Name,
                    Last_Name = b.Last_Name,
                    Relationship = b.B_Relationship,
                    Gender = b.Gender,
                    Date_of_Birth = b.Date_of_Birth,
                    AdvisorPID = b.AdvisorPID).fetchone()
            
                b.PersonID = result[1]
                _resp.ErrorMsg = result[0]
                _resp.ErrorCode = result[2]
        except Exception as e:
            _resp.ErrorCode = 99
            _resp.ErrorMsg = e
        return _resp
        
    def SaveAddress(self, a: Address) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_Address(
                        :PersonID,  
                        :Apt_No,
                        :Street_No,
                        :Street_Name,
                        :City,
                        :Province,
                        :Country,
                        :Postcode,
                        :Living_Status,
                        :Start_Date,
                        :End_Date,
                        :Current_Flag,
                        :Verify_Date,
                        :Notes)""",)

                result = db_conn.execute(SQL_Proc_text,
                    PersonID = a.PersonID,
                    Apt_No = a.Apt_No,
                    Street_No = a.Street_No,
                    Street_Name = a.Street_Name,
                    City = a.City,
                    Province = a.Province,
                    Country = a.Country,
                    Postcode = a.Postcode,
                    Living_Status = a.Living_Status,
                    Start_Date = a.Start_Date,
                    End_Date = a.End_Date,
                    Current_Flag = a.Current_Flag,
                    Verify_Date = a.Verify_Date,
                    Notes = a.Notes).fetchone()
            
                _resp.ErrorMsg=result[0]
                _resp.ErrorCode=result[1]
        except Exception as e:
            _resp.ErrorCode=99
            _resp.ErrorMsg=e
        return _resp    
    
    def SaveID(self, i: ID) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_ID(
                        :PersonID,
                        :ID_Type,
                        :ID_Number,
                        :Issue_Date,
                        :Expiry_Date,
                        :Issue_Country,
                        :Issue_Province,
                        :Start_Date,
                        :End_Date,
                        :Current_Flag,
                        :Verify_Date,
                        :Notes)""",)

                result = db_conn.execute(SQL_Proc_text,
                    PersonID = i.PersonID,
                    ID_Type = i.ID_Type,
                    ID_Number = i.ID_Number,
                    Issue_Date = i.Issue_Date,
                    Expiry_Date = i.Expiry_Date,
                    Issue_Country = i.Issue_Country,
                    Issue_Province = i.Issue_Province,
                    Start_Date = i.Start_Date,
                    End_Date = i.End_Date,
                    Current_Flag = i.Current_Flag,
                    Verify_Date = i.Verify_Date,
                    Notes = i.Notes).fetchone()
            
                _resp.ErrorMsg=result[0]
                _resp.ErrorCode=result[1]
        except Exception as e:
            _resp.ErrorCode=99
            _resp.ErrorMsg=e
        return _resp    
        # _resp.ErrorCode = 0 means successful; = 1 means something wrong with Insert statment of MySQL;
        #  = 2 means something wrong with Update statement of MySQL 
         
    def SaveEmployment(self, E: Employment) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_Employment(
                        :PersonID,
                        :Employment_Status,
                        :Employer,
                        :Industry,
                        :Occupation,
                        :Income,
                        :Unit,
                        :Street_No,
                        :Street_Name,
                        :City,
                        :Province,
                        :Country,
                        :Postcode,
                        :Workphone,
                        :Start_Date,
                        :End_Date,
                        :Current_Flag,
                        :Verify_Date,
                        :Notes)""",)

                result = db_conn.execute(SQL_Proc_text,
                    PersonID = E.PersonID,
                    Employment_Status = E.Employment_Status,
                    Employer = E.Employer,
                    Industry = E.Industry,
                    Occupation = E.Occupation,
                    Unit = E.Unit,
                    Street_No = E.Street_No,
                    Street_Name = E.Street_Name,
                    City = E.City,
                    Province = E.Province,
                    Country = E.Country,
                    Postcode = E.Postcode,
                    Workphone = E.Workphone,
                    Income = E.Income,
                    Start_Date = E.Start_Date,
                    End_Date = E.End_Date,
                    Current_Flag = E.Current_Flag,
                    Verify_Date = E.Verify_Date,
                    Notes = E.Notes).fetchone()
            
                _resp.ErrorMsg=result[0]
                _resp.ErrorCode=result[1]
        except Exception as e:
            _resp.ErrorCode=99
            _resp.ErrorMsg=e
        return _resp    
        # _resp.ErrorCode = 0 means successful; = 1 means something wrong with Insert statment of MySQL;
        #  = 2 means something wrong with Update statement of MySQL


    def SaveAsset(self, ass: Asset) -> ResponseDTO:
            _resp = ResponseDTO()
            try:
                with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                    SQL_Proc_text = sqlalchemy.text(
                        """call Save_Asset(
                        :PersonID,
                        :Assets_Type,
                        :Market_Value,
                        :Institution,
                        :A_Address,
                        :Current_Flag,
                        :Verify_Date,
                        :Notes)""",)

                    result = db_conn.execute(SQL_Proc_text,
                        PersonID = ass.PersonID,
                        Assets_Type = ass.Assets_Type,
                        Market_Value = ass.Market_Value,
                        Institution = ass.Institution,
                        A_Address = ass.Address,
                        Current_Flag = 1,
                        Verify_Date = ass.Verify_Date,
                        Notes = ass.Notes).fetchone()
                
                    
                    _resp.ErrorMsg=result[0]
                    _resp.ErrorCode=result[1]
            except Exception as e:
                _resp.ErrorCode=99
                _resp.ErrorMsg=e
            return _resp


    def SaveKYC(self, k: KYC) -> ResponseDTO:
            _resp = ResponseDTO()
            try:
                with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                    SQL_Proc_text = sqlalchemy.text(
                        """call Save_KYC(
                        :PersonID,
                        :VersionNo,
                        :Score,
                        :Verify_Date,
                        :Notes)""",)

                    result = db_conn.execute(SQL_Proc_text,
                        PersonID = k.PersonID,
                        VersionNo = k.VersionNo,
                        Score= ",".join(k.Score),
                        Verify_Date = k.Verify_Date,
                        Notes = k.Notes).fetchone()
                
                    _resp.ErrorMsg=result[0]
                    _resp.ErrorCode=result[1]
            except Exception as e:
                _resp.ErrorCode=99
                _resp.ErrorMsg=e
            return _resp
    

    def SaveLiability(self, liab: Liability) -> ResponseDTO:
            _resp = ResponseDTO()
            try:
                with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                    SQL_Proc_text = sqlalchemy.text(
                        """call Save_Liability(
                        :PersonID,
                        :L_Type,
                        :L_Balance,
                        :L_Monthly_Payment,
                        :Institution,
                        :Address,
                        :Current_Flag,
                        :Verify_Date,
                        :Notes)""",)

                    result = db_conn.execute(SQL_Proc_text,
                        PersonID = liab.PersonID,
                        L_Type=liab.L_Type,
                        L_Balance=liab.L_Balance,
                        L_Monthly_Payment=liab.L_Monthly_Payment,
                        Institution = liab.Institution,
                        Address = liab.Address,
                        Current_Flag = liab.Current_Flag,
                        Verify_Date = liab.Verify_Date,
                        Notes = liab.Notes).fetchone()
                
                    
                    _resp.ErrorMsg=result[0]
                    _resp.ErrorCode=result[1]
            except Exception as e:
                _resp.ErrorCode=99
                _resp.ErrorMsg=e
            return _resp


    def SaveIncome(self, i: Income) -> ResponseDTO:
            _resp = ResponseDTO()
            try:
                with self._DBBase__Pool.connect().execution_options(autocommit=True) as db_conn:
                    SQL_Proc_text = sqlalchemy.text(
                        """call Save_Income(
                        :PersonID,
                        :I_Type,
                        :I_Frequency,
                        :Income,
                        :Start_Date,
                        :End_Date,
                        :Notes,
                        :Current_Flag
                        )""",)

                    result = db_conn.execute(SQL_Proc_text,
                        PersonID = i.PersonID,
                        I_Type = i.I_Type,
                        I_Frequency = i.I_Frequency,
                        Income = i.Income,
                        Start_Date = i.Start_Date,
                        End_Date = i.End_Date,
                        Notes = i.Notes,
                        Current_Flag = i.Current_Flag).fetchone()
                
                    _resp.ErrorMsg=result[0]
                    _resp.ErrorCode=result[1]
            except Exception as e:
                _resp.ErrorCode=99
                _resp.ErrorMsg=e
            return _resp        