import sys
randomList = ['a',0,2]

for nhap in randomList:
    try:
        print("Phan tu: ",nhap)
        r = 1/int(nhap)
        break
    except:
        print("cos ngoaij leej ",sys.exc_info()[0],"xaayr ra.")
        print("Nhaapj phaanf tuwr tieeps theo")
        print()
print("Keets quar phaanf tuwr ",nhap,"laf: ",r)

