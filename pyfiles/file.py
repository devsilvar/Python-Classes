# //create a file called datat.txt
myfile = open('data.txt' , 'w')

# # //wrote something to the file
myfile.write("I just wrote osmething donw")

# # closed the file
myfile.close()


# # METHOD2
# with open("lotti.txt" , 'w' ) as newfile:
#     newfile.write("I am a new style to creating file")

students = ["Lotti" , "uthman" , "Daniel" , "Great" , "Emmanuel" , "Success"]

# for x in students:
#     print(x)




with open('student.txt'  ,  'a' ) as studentList:
    for name in students:
        studentList.write(name + "\n")

        

    












