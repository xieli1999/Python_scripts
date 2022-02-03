#This module includes all functions that are related to MySQL

import os
import pymysql
from google.cloud.sql.connector import connector
import sqlalchemy
import Class_Definition
from Class_Definition import Person, ResponseDTO, Advisor, Address, ID

    
class DBBase(object):
    """description of class"""
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ai-financial-coop202112-6120926f2230.json"
        self.__Pool =sqlalchemy.create_engine("mysql+pymysql://", creator = self.__getconn,)


    def __getconn(self) -> pymysql.connections.Connection:
        # Set MySQL connection info
        _MySQL_connectionName = 'ai-financial-coop202112:us-central1:hengyi'
        _MySQL_host = '127.0.0.1'
        _MySQL_user = 'AIF0013'
        _MySQL_password = 'LiXie-AIF'
        _MySQL_database = 'aif_db_AIF0013'

        conn : pymysql.connections.Connection = connector.connect(
            _MySQL_connectionName,
            "pymysql",
            user= _MySQL_user,
            password = _MySQL_password,
            db = _MySQL_database,
            autocommit = True
            #cafile=MySQL_SSLPath,
            #validate_host=False,
        )
        return conn


# insert a new person, if this person was not in the database, it will return a string
# showing that it has been inserted, also it will return the personID of the new record. 
class AIFinanceDB(DBBase):
    def SaveApplicant(self, p: Person) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect() as db_conn:       
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_Applicant(
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
                    :Email,
                    :Bankruptcy,
                    :Discharge_Date)""",)

                result = db_conn.execute(SQL_Proc_text,
                    First_Name=p.First_Name,
                    Last_Name=p.Last_Name,
                    English_Name=p.English_Name,
                    Gender=p.Gender,
                    Date_of_Birth=p.Date_of_Birth,
                    Country_of_Birth=p.Country_of_Birth,
                    Province_of_Birth=p.Province_of_Birth,
                    Citizenship=p.Citizenship,
                    Tax_Status=p.Tax_Status,
                    Live_in_Canada_Since=p.Live_in_Canada_Since,
                    Marital_Status=p.Marital_Status,
                    Cellphone=p.Cellphone,
                    Email=p.Email,
                    Bankruptcy=p.Bankruptcy,
                    Discharge_Date=p.Discharge_Date).fetchone()
            
                p.PersonID=result[1]
                _resp.ErrorMsg=result[0]
                _resp.ErrorCode=result[2]
        except Exception as e:
            _resp.ErrorCode=99
            _resp.ErrorMsg=e
        return _resp

    def SaveTrustee(self, p: Person) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect() as db_conn:       
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_Trustee(
                    :First_Name,
                    :Last_Name)""",)

                result = db_conn.execute(SQL_Proc_text,
                    First_Name=p.First_Name,
                    Last_Name=p.Last_Name).fetchone()
            
                p.PersonID=result[1]
                _resp.ErrorMsg=result[0]
                _resp.ErrorCode=result[2]
        except Exception as e:
            _resp.ErrorCode=99
            _resp.ErrorMsg=e
        return _resp    
        
    def SaveSpouse(self, p: Person) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect() as db_conn:       
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_Spouse(
                    :First_Name,
                    :Last_Name,
                    :Date_of_Birth)""",)

                result = db_conn.execute(SQL_Proc_text,
                    First_Name=p.First_Name,
                    Last_Name=p.Last_Name,
                    Date_of_Birth=p.Date_of_Birth).fetchone()
            
                p.PersonID=result[1]
                _resp.ErrorMsg=result[0]
                _resp.ErrorCode=result[2]
        except Exception as e:
            _resp.ErrorCode=99
            _resp.ErrorMsg=e
        return _resp    
        
    def SaveBeneficiary(self, p: Person) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect() as db_conn:       
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_Beneficiary(
                    :First_Name,
                    :Last_Name,
                    :Gender,
                    :Date_of_Birth)""",)

                result = db_conn.execute(SQL_Proc_text,
                    First_Name=p.First_Name,
                    Last_Name=p.Last_Name,
                    Gender=p.Gender,
                    Date_of_Birth=p.Date_of_Birth).fetchone()
            
                p.PersonID=result[1]
                _resp.ErrorMsg=result[0]
                _resp.ErrorCode=result[2]
        except Exception as e:
            _resp.ErrorCode=99
            _resp.ErrorMsg=e
        return _resp
        
    def SaveAddress(self, a: Address) -> ResponseDTO:
        _resp = ResponseDTO()
        try:
            with self._DBBase__Pool.connect() as db_conn:       
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
                        :Homephone,
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
                    Homephone = a.Homephone,
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
            with self._DBBase__Pool.connect() as db_conn:       
                SQL_Proc_text = sqlalchemy.text(
                    """call Save_ID(
                        :PersonID,
                        :ID_Type,
                        :ID_Number,
                        :Issue_Date,
                        :Expiry_Date,
                        :Issue_Country,
                        :Issue_Province,
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
         
    
