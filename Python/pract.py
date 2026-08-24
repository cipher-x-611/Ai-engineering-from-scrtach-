#name="rehan"
#age=32
#height=5.5
#student=True
#print(age)
#print(height)
#print(student)
#print(type(student))
#print(type(age))
#print(type(height))
#print(type(name))


#new=["apple","banana","orange","watermelon","melon"]
#print(new)
#print(new[3])
#new.append("grapes")
#new.append("mullbery")
#new.append("melon")
#print(new)
#new.remove("melon")
#print(new)

#dicttionary 
#car = {
 #   "brand": "Mercedes",
  #  "model": "c-class",
   # "year": "2024"
#}
#print(car)
#print("the brand of acr is:",car["brand"])
#car.update({"color":"red"})
#print(car)


#/set prctise 
#numbers = {1, 2, 2, 3, 3, 3, 4}
#print(numbers)
#print(3 in numbers)
#numbers.add(10)
#print(numbers)
#set_a = {1, 2, 3, 4}
#set_b = {3, 4, 5, 6}
#print(set_a & set_b) 
#numbers.remove(2)
#print(numbers)


#practise 
#
#marks=int(input("enter your marks:"))
#if marks>=85:
#    print("Grade A")
#elif marks>100:
#    print("Invalid Number")
#elif marks>=70:
#    print("Grade B")
#elif marks>=60:
#    print("Grade C")
#elif marks>=50:
#    print("Grade D")
#elif marks<100:
#    print("Invalid Number")
#else:
#    print("Fail")



# ATM PROGRAM practise 
#amount=int(input("please enter your account balance "))
#withdraw_amount=int(input("please enter the withdrawl amount"))
#if amount<=0:
#    print("you have zero balance") 
#    print("thnkyou for using atm")
#elif withdraw_amount<=0:
#    print("invalid aamount")
#    print("thnkyou for using atm")
#elif withdraw_amount>amount:
#    print("insufficient balance")
#    print("thnkyou for using atm")
#elif withdraw_amount<=amount:
#    amount=amount-withdraw_amount
#    print("Withdrwal Successfull")
#    print("Remaining amount is ", amount)    
#    print("thnkyou for using atm")

#numbers = [3, 8, 15, 22, 6, 19, 4]
#for num in range(1,10):
#    if num==5:
#        continue
#    print("Number list is as following: ",num )





#numbers = [10, 20, 30, 40, 50]
#a=0
#for num in numbers:
#    a=num+a
#    print("sum is:",a)
#avg=a/len(numbers)
#print("average numbers are:",avg)




#functions practise


#def welcome():
 #   print("welcome to python")

#name=str(input("please enter your name: "))
#age=int(input("please enter your age: "))

#def student_info(name,age,department_name):
#    print("name is: ",name)
#    print("Age is: ",age) 
#    print("department name is: ", department_name)
#student_info("rehan",20,"softwre engineering")
#
#student_info("ali", 21, "computer science")
#student_info("ahmed", 19, "information technology")


#return function 
#def mul(a,b):
#    return(a*b)
#result=mul(4,5)
#print("Multipication of the value is ",result)
#print(result + 10)
#print(result * 2)
#

#def calculator(a,b):
#    return(a+b,a-b,a*b)
#add,sub,mul=calculator(6,4)
#print("addittion of two numbrs is ",add)
#print("addittion of two numbrs is ",sub)
#print("addittion of two numbrs is ",mul)
#
#"\n"
#
#add, sub,mul=calculator(5,1)
#print("addittion of two numbrs is ",add)
#print("addittion of two numbrs is ",sub)
#print("addittion of two numbrs is ",mul)

#marks=int(input("Enter your marks: "))
#def student_marks(marks):
#    return(marks)
#result=student_marks(marks)
#if marks>80:
#    print("Student Secured A grade marks",result)
#elif marks>70:
#    print("Student Secured B grade marks ",result)
#elif marks>60:
#    print("Student Secured C grade marks ",result)
#elif marks >50:
#    print ("Student Secured D grade Marks ", result)
#else:
#    print("UNFORTUNATELY! TRY AGAIN IN NEXT TIME ")


#Recursion 
#def recursion(n):
#    if n==0:
#        return
#    print(n)
#    recursion(n-1)
#recursion(5)

#add= lambda x:x*x
#print(add(9))

#Final Practise 
#def calculator (a,b):
#    return(a+b,a-b,a*b,a/b)
#add,sub,mul,div=calculator(10,5)
#print("Addition of two values is: ",add)
#print(" Subtraction of two numbers is: ",sub)
#print("Multiplication of two numbers is: ",mul)
#print("Division of two numbers is: ",div)

#n=0
#def series(num):
#    if num==10:
#        return n+series
#    print(num)
#    series(num+1)
#print(series(3))


file=open("file.txt","w")
file.write("hello world")
file.write("\n" \
"class is going to start from 10:00 am")  
file.close()
file=open("file.txt","r")
print(file.read())
file.close()
file=open("file.txt","a")
file.write("\n" \
"this is appended text")  
file.close()
file=open("file.txt","r")
print(file.read())
file.close()