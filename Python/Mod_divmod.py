# Enter your code here. Read input from STDIN. Print output to STDOUT

def main():
   num = int(input())
   div = int(input())

   rem = num % div
   quo = num // div
   print(quo)
   print(rem)

   print('('+str(quo)+', '+str(rem)+')')




main()
