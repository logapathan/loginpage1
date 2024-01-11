#saving students data in dictionary according to the department

#by directly saving in dictionary
mechanical={"student1":{"name":"ram","year":2004,"email_id":"ram@gmail.com"},#including details of students in mechanical using dictionary
            "student2":{"name":"ramesh","year":2003,"email_id":"ramesh@gmail.com"},
            "student3":{"name":"pathan","year":2002,"email_id":"pathan@gmail.com"},
            "student4":{"name":"rahul","year":2004,"email_id":"rahul@gmail.com"},
            "student5":{"name":"jithesh","year":2003,"email_id":"jithesh@gmail.com"}}
electrical={"student1":{"name":"vinith","year":2003,"email_id":"vinith@gmail.com"},#including details of students in electrical using dictionary
            "student2":{"name":"naveen","year":2003,"email_id":"naveen@gmail.com"},
            "student3":{"name":"abilash","year":2006,"email_id":"abilash@gmail.com"},
            "student4":{"name":"abdul","year":2005,"email_id":"abdul@gmail.com"},
            "student5":{"name":"varma","year":2003,"email_id":"varma@gmail.com"}}
civil={"student1":{"name":"gokul","year":2007,"email_id":"gokul@gmail.com"},#including details of students in civil using dictionary
            "student2":{"name":"aravinth","year":2001,"email_id":"aravinth@gmail.com"},
            "student3":{"name":"aswath","year":2004,"email_id":"aswath@gmail.com"},
            "student4":{"name":"yash","year":2004,"email_id":"yash@gmail.com"},
            "student5":{"name":"omen","year":2006,"email_id":"omen@gmail.com"}}
#indirectly saving in dictionary by creating variables ouside the dictionary and inserting the values in the dictionary
student1={"name":"rahul","year":2005,"email_id":"rahul12@gmail.com"}
student2={"name":"phonix","year":2001,"email_id":"phonix@gmail.com"}
student3={"name":"reyna","year":2002,"email_id":"reyna@gmail.com"}
student4={"name":"yaswanth","year":2004,"email_id":"yashwanth@gmail.com"}
student5={"name":"mathur","year":2006,"email_id":"mathur@gmail.com"}

cse={"student1":student1,
     "student2":student2,
     "student3":student3,
     "student4":student4,
     "student5":student5}

student6={"name":"naveen","year":2003,"email_id":"naveen@gmail.com"}
student7={"name":"ramesh","year":2001,"email_id":"ramesh@gmail.com"}
student8={"name":"thrishan","year":2006,"email_id":"thrishan@gmail.com"}
student9={"name":"varman","year":2008,"email_id":"varman123@gmail.com"}
student10={"name":"bala","year":2002,"email_id":"bala@gmail.com"}

aids={"student1":student10,
     "student2":student9,
     "student3":student8,
     "student4":student7,
     "student5":student6}

print(mechanical)
print(electrical)
print(civil)
print(cse)
print(aids)




