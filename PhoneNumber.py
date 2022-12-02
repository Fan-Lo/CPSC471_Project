class PhoneNumber:
    def __init__(self, *args):
        #optional attributes
        self.__countryCode = ''
        self.__extension = ''

        # only a single string is passed
        if len(args) == 1:
            charToRemove = " -()"
            phone = args[0]
            for i in charToRemove:
                phone = phone.replace(i, '')
        else:
            phone = ""
            for i in args:
                phone  += i

        length = len(phone)
        if length == 10: # i.e 4031112222
            self.__areaCode = phone[0:3]
            self.__telephonePrefix = phone[3:6]
            self.__lineNumber = phone[6:10]
        elif length == 11: #i.e. 14031112222
            self.__countryCode = phone[0]
            self.__areaCode = phone[1:4]
            self.__telephonePrefix = phone[4:7]
            self.__lineNumber = phone[7:11]
        elif length == 14: #i.e. 4031112222-3333 with extension
            self.__areaCode = phone[0:3]
            self.__telephonePrefix = phone[3:6]
            self.__lineNumber = phone[6:10]
            self.__extension = phone [10:14]
        elif length == 15: #i.e. has country code and extension
            self.__countryCode = phone[0]
            self.__areaCode = phone[1:4]
            self.__telephonePrefix = phone[4:7]
            self.__lineNumber = phone[7:11]
            self.__extension = phone [11:15]
 

    
    def display(self):
        return self.__countryCode + self.__areaCode + self.__telephonePrefix + self.__lineNumber + self.__extension

    def display2(self):
        return self.__countryCode + self.__areaCode + '-' + self.__telephonePrefix + '-' + self.__lineNumber + self.__extension
    
    def setCountryCode(self, code):
        self.__countryCode = code
    
    def setAreaCode(self, code):
        self.__areaCode = code
    
    def setTelephonePrefix(self, code):
        self.__telephonePrefix = code
    
    def setLineNumber(self, code):
        self.__lineNumber = code
    
    def setExtension(self, code):
        self.__extension = code