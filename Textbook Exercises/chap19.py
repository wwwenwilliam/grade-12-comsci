
class BasePostAddress:
    
    def __init__(self, country, name):
        self.country = country
        self.name = name
        
    def validate(self):
        return self.name != '' and self.country != ''
    
    def isInState(self, state):
        return False
    
    def getINTequ(self):
        raise CannotConvertToINTException
        
class CannotConvertToINTException(Exception):
    
    def  __init__(self, message="Could not get INT equivalent"):
        super().__init__(message)
        

##taken from chapter -------------------------------------------
class IrishPostAddress(BasePostAddress):
    
    def __init__(self, name, postalCode):
        super().__init__("IRELAND", name)
        self.postalCode = postalCode

    def display(self):
        print(self.name)
        print(self.postalCode)
        print(self.country)

    def validate(self):
        return super().validate() and len(self.postalCode) == 7


class USPostAddress(BasePostAddress):
    
    def __init__(self, name, street, city, state, zipcode):
        super().__init__("USA", name)
        self.street = street
        self.city = city
        self.state = state
        self.zip = zipcode

    def display(self):
        print(self.name)
        print(self.street)
        print(self.city + ", " + self.state + "  " + self.zip)
        print(self.country)

    def validate(self):
        return (super().validate() and self.city != '' and
            len(self.state) == 2 and
            (len(self.zip) == 5 or len(self.zip) == 9))
    
    ##added myself -------------
    def isInState(self, state):
        ##added myself
        if self.state == state: return True
        return False
    
    def getINTequ(self):
        return INTPostAddress(self.name, self.street, self.city, self.state, self.zip, "USA")
    #-------------------------
##----------------------------------------------------------------

##Guidelines taken from canada post website

class INTPostAddress(BasePostAddress):
    
    #international address
    def __init__(self, name, street, city, state, postCode, country):
        super().__init__(country, name)
        self.street = street
        self.city = city
        self.state = state
        self.postCode = postCode
        
    def display(self):
        print(self.name)
        print(self.street)
        print(self.postCode + " " + self.state + " " + self.city)
        print(self.country)
        
    def validate(self):
        return (super().validate() and self.street != "" and 
                self.state != "" and self.city != "" and 
                self.postCode != ""
                )
    
    def getINTequ(self):
        #returns self, maybe should return copy of self
        return self
    
    
class CADPostAddress(BasePostAddress):
    
    def __init__(self, name, street, postCode, province, city):
        super().__init__("CANADA", name)
        self.street = street
        self.city = city
        self.province = province
        self.postCode = postCode
        
    def display(self):
        print(self.name)
        print(self.street)
        print(self.city + " " + self.province + " " + self.postCode)
        print(self.country)
        
    def validate(self):
        return (super().validate() and self.street != "" and 
                len(self.province) == 2 and self.city != "" and 
                len(self.postCode) == 7
                )
    
    def isInState(self, state):
        if self.province == state: return True
        return False
    
    def getINTequ(self):
        return INTPostAddress(self.name, self.street, self.city, self.province, self.postCode, "CANADA")
    
test = [CADPostAddress("JOHN JONES", "10-123 1/2 MAIN ST SE", "MONTREAL", "QC", "H3Z 2Y7"),
        USPostAddress("Abe Jones", "103 Anywhere Ln", "Greenville", "SC", "29609"),
        USPostAddress("JOHN JONES", "101 MAIN ST", "WASHINGTON", "DC", "20019"),
        IrishPostAddress("Alf Jones", "A26F4G9"),
        INTPostAddress("JOHN JONES", "RODODENDRONPIEIN 7B", "3053", "ES", "ROTTERDAM", "NETHERLANDS")
       ]

print("Display addresses ---------------------")
for adr in test:
    print("Valid? " + str(adr.validate()))
    adr.display()
    print("------------------")
   
print("filter by province: QC ------------------")
for adr in test:
    if adr.isInState("QC"):
        adr.display()
        print("------------------")

print("International equivalents ----------------")
for adr in test:
    try:
        adr.getINTequ().display()
    except CannotConvertToINTException:
        print("could not get INT equivalent, displaying as country-specific")
        adr.display()
    print("------------------")

    
    
    
    