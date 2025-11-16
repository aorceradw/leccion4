vocales = "aeiouAEIOU"

while True:
    caracter = input("Carácter: ")
    
    if caracter == " ":
        break
    
    if caracter in vocales:
        print("VOCAL")
    else:
        print("NO VOCAL")
