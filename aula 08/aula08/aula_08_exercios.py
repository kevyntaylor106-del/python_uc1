
def soma(a, b):
   return a + b

def subtracao(a, b):
   return a - b

#def main():
   resultado_soma = soma(10, 5)
   resultado_subtracao = subtracao(10, 5)
   #print(f"\n\n\tSoma\n\n: {resultado_soma}")
  # print(f"\n\n\tSubtração\n\n: {resultado_subtracao}")

if __name__ == "__main__":
  # main() 

 def main () :
      for i in range(1, 11) :
       #  print(i)
         if __name__ == "\n\n\t__main__\n\n" :
             main()
      

     



def fatorial(n):
   if n == 0 or n == 1:
       return 1
   else:
       return n * fatorial(n - 1)

def main():
   num = int(input("\n\n\tDigite um número\n\n: "))
   print(f"\n\n\tO fatorial de\n\n {num} é {fatorial(num)}")

if __name__ == "__main__":
   main()