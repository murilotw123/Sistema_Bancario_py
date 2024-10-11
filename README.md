# Sistema Bancário em Python - Versão 1.0

## Descrição

Este é um sistema bancário simples desenvolvido em Python que permite aos usuários realizar operações básicas como **depósitos**, **saques** e consultar o **extrato**. O sistema controla um limite de saque diário e um número máximo de saques por dia.

## Funcionalidades

- **Depositar**: O usuário pode adicionar fundos à sua conta.
- **Sacar**: O usuário pode realizar saques, com um limite de valor por transação e um limite de três saques diários.
- **Extrato**: Mostra todas as transações realizadas e o saldo atual.
- **Sair**: Encerra o sistema.

## Regras do Sistema

O limite de saque é de R$ 500,00 por transação. O número máximo de saques diários é 3. O sistema só aceita valores positivos tanto para depósitos quanto para saques. O saldo atual é exibido ao consultar o extrato.

## Exemplo de Uso

O menu principal apresenta as seguintes opções:

[D] - Depositar [S] - Sacar [E] - Extrato [Q] - Sair

### Exemplo de Depósito

=> D Quanto deseja depositar? 100.00

### Exemplo de Saque

=> S Quanto deseja sacar? 200.00

### Exemplo de Extrato

=> E

================ EXTRATO ================ Depósito: R$ 100.00 Saque: R$ 50.00 ========================================= Saldo Atual: R$ 50.00 =========================================

## Como Executar

1. Certifique-se de que você tenha o Python instalado na sua máquina. 2. Baixe o código deste repositório. 3. Execute o script `sistema_bancario.py` em seu terminal ou IDE preferida:

python sistema_bancario.py

## Melhorias Futuras

- Implementar autenticação de usuário. - Adicionar funcionalidade para transferências entre contas. - Criar uma interface gráfica para melhorar a interação do usuário.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto é licenciado sob a MIT License.
