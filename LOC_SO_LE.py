value = input("NHAP DI: ")
numbers = [x for x in value.split(",") if int(x)%2!= 0]
print("ket qua ma may muon day: ",",".join(numbers))
print("\n\nNhan Gi do DI")