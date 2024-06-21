import math
import numpy as np
from numba import cuda

# Função que será executada na GPU
@cuda.jit
def is_prime_kernel(number, result):
    idx = cuda.grid(1)
    if idx < result.size:
        if number % (idx + 2) == 0:
            result[idx] = False

def is_prime(number):
    # Assumimos inicialmente que o número é primo
    primo = "é"
    
    # Um número primo é maior que 1
    if number <= 1:
        primo = "não é"
        return primo
    
    # Verificamos os divisores possíveis do número, até a raiz quadrada de number
    limit = int(math.sqrt(number)) + 1
    result = cuda.to_device(np.full(limit - 2, True))  # Array para armazenar os resultados dos testes de divisibilidade

    # Configuração da execução na GPU
    threads_per_block = 256
    blocks_per_grid = (result.size + (threads_per_block - 2)) // threads_per_block
    
    # Chamada da função que roda na GPU
    is_prime_kernel[blocks_per_grid, threads_per_block](number, result)
    
    # Transferindo os resultados de volta para a CPU
    result_host = result.copy_to_host()

    # Se algum valor no array result for False, o número não é primo
    if not result_host.all():
        primo = "não é"
    
    return primo

# Solicita o número ao usuário
number = int(input("Digite um número inteiro positivo: "))
primo = is_prime(number)

print("O número {} {} primo!".format(number, primo))
