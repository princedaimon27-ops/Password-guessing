#simple password check
correct_password="Golden"
attempts =0
max_attempts =3
password=""

while attempts <max_attempts and password != correct_password:
  password=input("enter your password:")
  if password == correct_password:
       print("access granted")
  if password != correct_password:
      attempts +=1    
      print(f"wrong password X({attempts}/{max_attempts})")
     
  elif attempts >= max_attempts:
        print("Too many attempts.Access denied")