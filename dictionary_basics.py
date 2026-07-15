student = { "name" : "Archit", 
           "age" : 20, 
           "course" : "B.tech"
          }
student.update({"city" : "Ghaziabad"})
student["age"] = 21
student.pop("city")
print(student)