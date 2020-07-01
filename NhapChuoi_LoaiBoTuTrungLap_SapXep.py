s= input("Nhap chuoi cua ban: ")
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))