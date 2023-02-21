import phonenumbers
from phonenumbers import timezone,carrier,geocoder
number = input("Enter the number starting with +91:")
phone = phonenumbers.parse(number)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print(phone)
print(car)
print(reg)
