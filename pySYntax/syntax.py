# fName = input("Enter Your FirstName ")
# lName = input("Enter Your Last Name ")

# print(fName + " " +  lName)


# age = input("Enter Your Age ")

# age = int(age)
# if( age >= 18):
#     print("You are Eligible to Vote")
# else:
#     print("You Are Not Eligible to Vote")


# studentScore = input("Enter Your Score ")


# initNumber = 0

# while initNumber <= 10:
#     print(initNumber)
#     initNumber += 1

studentScore = input("Enter Your Score ")


while type(studentScore) is not int:
    try:
        studentScore = int(studentScore)
    except ValueError:
        print("Invalid input. Please enter a number.")
        studentScore = input("Enter Your Score: ")
    
if(studentScore >= 70):
    print("Score " + str(studentScore) + " Grade => A")
elif(studentScore >= 60):
    print("Score " + str(studentScore) + " Grade => B")
elif(studentScore >= 50):
    print("Score " + str(studentScore) + " Grade => C") 
elif(studentScore < 50):
    print("Score " + str(studentScore) + " Grade => F")



# studentScore = input("Enter Your Score: ")

# if(type(studentScore) is str):
#     studentScore = int(studentScore)
#     input("Enter a Valid number")
# else:
#     studentScore = int(studentScore)

# if(studentScore >= 70):
#     print("Score {} Grade => A".format(studentScore))
# elif(studentScore >= 60):
#     print("Score {} Grade => B".format(studentScore))
# elif(studentScore >= 50):
#     print("Score {} Grade => C".format(studentScore))
# else:
#     print("Score {} Grade => F".format(studentScore))


def add(a,b):
    return (a + b)

# list DATA TYPE  -- Javscript Array
studentAge = [12,14,16,18]


studentAge.__doc__

print(studentAge)

# studentAge.append(19)

# print(studentAge)

# dictionary = {"name" : "Eni" , "age" : 23}

# print(dictionary['age'])

sum_list = [2,4,6,8]

def sum_maker(sum_list):
    sum = 0
    for x in sum_list:
        sum = sum + x
        print(sum)    


sum_maker(sum_list)



def calculate():
    return 2 + 3 + 4 + 5

result =  calculate()
print(result)

# Default Arguments
def greet(name = "John Doe"):
    print("Hello how re you doing " + name)

greet("Shade")    

# Variable Length
name = "Sahde"
print(len(name))


words = [2,3,4,5,6]
sorted_words = filter(lambda y : y % 2 == 0, words  )

# res =  words.filter((y)=> y % 2 == 0)

# sortedoutList = list(sorted_words)





