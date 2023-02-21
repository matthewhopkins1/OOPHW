import FoodClass as fc
# this dictionary represents transactions. The key of the dictionary is the 
transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]
dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}
order_total = 0

custid = 570
name = 'Danni Sellyar'
address = '97 Mitchell Way Hewitt Texas 76712'
email = 'dsellyarft@gmpg.org'
phone = '254-555-9362'
mem_status = 'False'
date = dict['trans3'][0]
item_name1 = dict['trans3'][1]
item_name2 = dict['trans4'][1]
cost1 = dict['trans3'][2]
cost2 = dict['trans4'][2]
total_cost = cost1 + cost2

custid = 569
name = 'Aubree Himsworth'
address = '1172 Moulton Hill Waco Texas 76710'
email = 'ahimsworthfs@list-manage.com'
phone = '254-555-2273'
mem_status = 'True'
date = dict['trans1'][0]
item_name1 = dict['trans1'][1]
item_name2 = dict['trans2'][1]
cost1 = dict['trans1'][2]
cost2 = dict['trans2'][2]
total_cost = cost1 + cost2

customer = fc.Customer(custid, name, address, email, phone, mem_status)
transaction = fc.Transaction(date, item_name1, item_name2, cost1, cost2, custid, total_cost)

print('Customer Name:', name)
print('Phone:', phone)
print('Order Item:', item_name1,  'Price:', cost1)
print('Order Item:', item_name2,  'Price:', cost2)
print('Total Cost', total_cost)
if mem_status == 'True'
    print('Member Discount:', total_cost * .2)
    print('Total Cost after discount:', total_cost * .8)
