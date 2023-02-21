#create customer class

class Customer:
    def __init__(self, custid, name, address, email, phone, mem_status)
        self.__custid = custid
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone 
        self.__mem_status = mem_status

    def get_custid(self):
        return self.__custid

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_mem_status(self):
        return self.__mem_status

#create transaction class

class Transaction:
    def __init__(self, date, item_name1, item_name2, cost1, cost2, custid, total_cost)
        self.__date = date
        self.__item_name1 = item_name1
        self.__item_name2 = item_name2
        self.__cost1 = cost1
        self.__cost2 = cost2
        self.__custid = custid
        self.__total_cost = total_cost

    def get_date(self):
        return self.__date

    def get_item_name1(self):
        return self.__item_name1

    def get_item_name2(self):
        return self.__item_name2

    def get_cost1(self):
        return self.__cost1

    def get_cost2(self):
        return self.__cost2

    def get_custid(self):
        return self.__custid

    def get_total_cost(self):
        return self.__total_cost