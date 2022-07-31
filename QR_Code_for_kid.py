print("***QR Code for kids***"'\n')

import qrcode

kid_months= " Months"
kid_years =" years"
kid_age_inf =True

#Fill out personal information
    
def qr_code_kid():
    kid_age_inf = "-"
    
    while kid_age_inf:
        
          kid_age_inf = input("Pick an option = Kids less than 2 year old = M, Kids over 2 year old = Y :"'\n').upper()
 
          #kids less than 2 years old
          if kid_age_inf == "M":              
             kid_age = int(input("Please enter how many months is the baby: "))
             if kid_age == 1:
                return str(kid_age) + kid_months[:-1]          
             if kid_age<24:
                return str(kid_age) + kid_months
             else:
                    print('\n'"Value should be less than 24 months"'\n')
                    
          #kids over 2 years old
          elif kid_age_inf == "Y":
                kid_age = int(input('\n'"Please enter how many years is the kid: "))
                if kid_age>=2:
                     return str(kid_age) + kid_years
                else:
                    print('\n'"Value should be minimum 2 years old"'\n')
                    
          kid_age_inf: False
          print("Please try again!! enter the correct value."'\n')
                                   
age = qr_code_kid()

kid_name =input("Please enter full child's name: ")
adress =(input("Please enter child's adress :"))
mother_name = input("Please enter mother's name: ")
mother_phone_number= int(input("Please enter mother's phone number: "))
father_name = input("Please enter father's name: ")
father_phone_number = int(input("Please enter father's phone number: "))
          
data = (f"I'm {kid_name},and i'm {age} old and  my parents are: {mother_name} and {father_name}, Phones: Mother - {mother_phone_number},\
Father - {father_phone_number} and my Adress is :{adress}.")
      
# Encoding data using make() function
img = qrcode.make(data)
   
# Saving as an image in my desktop with the kid's name.
img.save(f"C://Users/lorel/Desktop/{kid_name}.png")    
print('\n'"*** QR CODE GENERATED ***")

