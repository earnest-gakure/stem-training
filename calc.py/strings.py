from ast import Num
from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
from posixpath import supports_unicode_filenames


f_num = int(input("enter first number"))
s_num = int(input("enter second number"))
sum_of_numbers = f_num + s_num
print("sum is",sum_of_numbers)