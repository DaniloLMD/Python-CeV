n = int(input('Digite um número entre 0 e 9.999: '))
print(f"Unidade: {str(n)[int(len(str(n))) - 1]} \n Dezena: {n//10 - (n//100 * 10)} \n"
      f"Centena: {n//100 - (n//1000 * 10)} \n Milhar: {n // 1000}")

#Código acima usando variáveis
n = int(input('Digite um número entre 0 e 9.999: '))
milhar = n //1000
centena = n//100 - milhar*10
dezena = n //10 - (n//100 * 10)

x = str(n)
u = int(len(x)) - 1
unidade= n//1 - (n//10 * 10)

print(f'Unidade: {unidade}  \n Dezena: {dezena} \n Centena: {centena} \n Milhar: {milhar}  ')

