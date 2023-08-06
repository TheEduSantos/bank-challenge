
# Banking-System-Challenge

This is a DIO challenge for a banking system in Python, a simple program that simulates a basic banking system, allowing the user to perform some operations with their account.

How to use:

Deposit (d): By selecting this option, you can deposit money into your account. The program will prompt you to enter the amount you want to deposit, and then the amount will be added to your account balance. If you enter an invalid value (non-positive), the program will display an error message.

Withdraw (s): In this option, you can make withdrawals from your account. The program will ask for the amount you want to withdraw. Before processing the withdrawal, some checks will be made: if there is sufficient balance in the account, if the withdrawal amount does not exceed the daily limit, and if you have not exceeded the maximum number of allowed withdrawals. If any of these conditions are not met, the program will display an error message. If the withdrawal is successful, the amount will be deducted from your account balance.

Statement (e): By choosing this option, the program will display a statement with all the transactions that have been made in your account, including deposits and withdrawals. The statement will also show the current account balance.

Transaction History (h): Here, you can view a detailed history of all transactions made in your account, including the date, time, type of transaction (deposit or withdrawal), and the amount.

New Account (nc):
This option allows you to create a new bank account. When you choose this option, the system will ask you for some information, like your CPF (a unique identification number), your full name, date of birth, and address. Once you provide this information, the bank will create a new account for you, and you'll receive an account number and other details. 

List Accounts (lc):
When you select this option, the system will show you a list of all the bank accounts you have created. It will display the account number, the agency it belongs to, and the name of the account holder.

New User (nu):
This option allows you to add a new user to the system. You need to provide the person's CPF (identification number), full name, date of birth, and address. Once you enter this information, the system will register the new user.

Quit (q): If you choose this option, the program will be terminated, and you will exit the banking system.


# desafio-sistema-bancario

Este é um desafio da DIO de um sistema bancário em Python, de um programa simples que simula um sistema bancário básico, permitindo que o usuário realize algumas operações com sua conta.

Modo de uso:

Depositar (d): Ao selecionar essa opção, você poderá depositar dinheiro na sua conta. O programa pedirá que você informe o valor que deseja depositar e, em seguida, o valor será adicionado ao saldo da sua conta. Caso informe um valor inválido (não positivo), o programa mostrará uma mensagem de erro.

Sacar (s): Nessa opção, você pode realizar saques da sua conta. O programa solicitará o valor que você deseja sacar. Antes de efetuar o saque, algumas verificações serão feitas: se há saldo suficiente na conta, se o valor do saque não excede o limite diário e se você não excedeu o número máximo de saques permitidos. Se alguma dessas condições não for atendida, o programa mostrará uma mensagem de erro. Caso o saque seja realizado com sucesso, o valor será deduzido do saldo da sua conta.

Extrato (e): Ao escolher essa opção, o programa mostrará um extrato com todas as movimentações que foram realizadas na sua conta, incluindo depósitos e saques. O extrato também exibirá o saldo atual da conta.

Histórico de transações (h): Aqui, você poderá visualizar um histórico detalhado de todas as transações realizadas na sua conta, incluindo a data, a hora, o tipo de transação (depósito ou saque) e o valor.

Nova Conta(nc):
Essa opção permite criar uma nova conta bancária. Ao selecioná-la, o sistema irá solicitar algumas informações, como seu CPF, nome completo, data de nascimento e endereço. Depois de fornecer essas informações, o banco irá criar uma nova conta, e você receberá um número de conta e outros detalhes. 

Listar Contas(lc):
Ao escolher esta opção, o sistema irá mostrar uma lista de todas as contas bancárias que você criou. Serão exibidos o número da conta, a agência a que pertence e o nome do titular da conta. 

Novo Usuário(nu):
Essa opção permite adicionar um novo usuário ao sistema. Você precisará fornecer o CPF (número de identificação), nome completo, data de nascimento e endereço da pessoa. Depois de inserir essas informações, o sistema registrará o novo usuário. 

Sair (q): Se você escolher essa opção, o programa será encerrado e você sairá do sistema bancário.
