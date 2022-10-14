def maximum(tal1,tal2):
    if (tal1<tal2):
          print("talet som ar storts ar", tal2)

    elif (tal2<tal1):
        print("talet som ar storts ar:", tal1)

    else:
        print("talen ar lika stora")

a = int(input("det ena talet ar:"))
b = int(input("det andra talet ar:"))

maximum(a,b)