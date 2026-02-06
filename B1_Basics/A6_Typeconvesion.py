num_int=3
num_float=4.6
num_new=num_int+num_float
print("num_new= ", num_new)
print(type(num_new))
num_str="5" #string
print("num_str= ", num_str)     
print(type(num_str))
num_str_int=int(num_str)    
print("num_str_int= ", num_str_int)
print(type(num_str_int))
num_str_float=float(num_str)    
print("num_str_float= ", num_str_float) 
print(type(num_str_float))
num_int_str=str(num_int)
print("num_int_str= ", num_int_str)
print(type(num_int_str))    
num_float_str=str(num_float)
print("num_float_str= ", num_float_str)

# error=num_int+num_str #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print("error= ", error)

print(type(num_float_str))
num_new_str=str(num_new)
print("num_new_str= ", num_new_str)
print(type(num_new_str))
num_str_float2=float(num_str)+0.4
print("num_str_float2= ", num_str_float2)
print(type(num_str_float2))
num_str_int2=int(num_str)+2
print("num_str_int2= ", num_str_int2)
print(type(num_str_int2))
#num_str_int3=int("3.5") #ValueError: invalid literal for int() with base 10: '3.5'
num_str_float3=float("3.5")
print("num_str_float3= ", num_str_float3)
print(type(num_str_float3))
num_str_float4=int(float("3.5"))
print("num_str_float4= ", num_str_float4)
print(type(num_str_float4))
#num_str_int4=float(int("3.5")) #ValueError: invalid literal for int() with base 10: '3.5'
num_str_float5=float("3")
print("num_str_float5= ", num_str_float5)

print(type(num_str_float5))
num_str_int5=int("3")
print("num_str_int5= ", num_str_int5)
print(type(num_str_int5))
#num_str_float6=int("3.5abc") #ValueError: invalid literal for int() with base 10: '3.5abc'
#num_str_int6=float("3.5abc") #ValueError: could not convert string to float: '3.5abc'
num_str_float7=float("3abc".strip('abc'))       
print("num_str_float7= ", num_str_float7)
print(type(num_str_float7))
c=5+3j
print("c= ", c) 
print(type(c))
c_str=str(c)    
print("c_str= ", c_str)
print(type(c_str))  

