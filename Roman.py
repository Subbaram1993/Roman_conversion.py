Roman = {1000 :"M",900 : "CM",500 :"D",400 : "CD",100 : "C",90 : "XC",50 : "L",40 : "XL",10 : "X",9 : "IX",5 : "V",4:"IV",1:"I"}

def sub(Num,Num2):
  Num1 = Num - Num2
  N = Num - Num1
  return N

def roman_convert(Num,roman) :
  #print(roman)
  while( Num > 0):
    if Num >= 1000:
       N = sub(Num,1000)
       roman.append(Roman.get(N))
       Num = Num - 1000
    elif Num >= 900:
       N = sub(Num,900)
       roman.append(Roman.get(N))
       Num = Num - 900
    elif Num >= 500:
        N = sub(Num,500)
        roman.append(Roman.get(N))
        Num = Num - 500
    elif Num >= 400:
       N = sub(Num,400)
       roman.append(Roman.get(N))
       Num = Num - 400
    elif Num >= 100:
       N = sub(Num,100)
       roman.append(Roman.get(N))
       Num = Num - 100
    elif Num >= 90:
       N = sub(Num,90)
       roman.append(Roman.get(N))
       Num = Num - 90
    elif Num >= 50:
       N = sub(Num,50)
       roman.append(Roman.get(N))
       Num = Num - 50 
    elif Num >= 40:
       N = sub(Num,40)
       roman.append(Roman.get(N))
       Num = Num - 40   
    elif Num >= 10:
       N = sub(Num,10)
       roman.append(Roman.get(N))
       Num = Num - 10        
    elif Num >= 9:
       N = sub(Num,9)
       roman.append(Roman.get(N))
       Num = Num - 9
    elif Num >= 4:
       N = sub(Num,4)
       roman.append(Roman.get(N))
       Num = Num - 4
    elif Num >= 1:
       N = sub(Num,1)
       roman.append(Roman.get(N))
       Num = Num - 1
    else :
       roman.append(0) 
  return roman
if __name__ == "__main__":
  print("Converting the Numbers into Roman:")
  Num = int(input("Enter the number :"))
  roman =[]
  R = roman_convert(Num,roman)
  Roman = "".join(str(x) for x in R)
  print(Roman)
