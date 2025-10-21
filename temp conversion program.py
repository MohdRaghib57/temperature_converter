# converting temperature from celsius to fahrenheit and vice  versa


unit = input("Chose an unit (C/F): ").strip()


temp = float(input("Enter temperature:"))

if unit == "C" :
    temp = round((temp * 9)/5 + 32 , 2 )
    print(f"Temperature is: {temp} °F")
elif unit == "F":
    temp = round((temp - 32 ) * 5 / 9 , 2 )
    print(f"Temperature is: {temp} °C")
else :
    print(f"Sorry! {unit} is not valid unit for this program!")
    


