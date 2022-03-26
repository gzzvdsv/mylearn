import os
# import MySQLdb
with open ('1.txt','r') as f:
     print(f.read())
     value_='123'
     sql_="INSERT      INTO `mynote`. `new_table`(`idnew_table`, `new_tablecol`, `new_tablecol2`) VALUES('" +value_ + "', '132', '13');"
     print(sql_)