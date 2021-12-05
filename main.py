import phonenumbers
from test import numbers
if len(numbers) < 16 :
    print("the number is  available")
    from phonenumbers import geocoder
    place= phonenumbers.parse(numbers)
    print("this number is found in : ")
    print((geocoder.description_for_number(place,"fr")))

    from phonenumbers import carrier
    company_name=phonenumbers.parse(numbers)
    print("the Telecom Company is ")
    print(carrier.name_for_number(company_name,"fr"))
    print("welcome !")
else:
 print("the number is not available")

