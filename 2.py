#Convert Temparature from Ceksius to farhenheit
def celsius_farhenheit (x):
    farhenhelit=(x*9/5)+32
    return farhenhelit
T=int(input("Enter Temparature in celsius"))
CelsiusTemparature = celsius_farhenheit(T)
print(CelsiusTemparature)
