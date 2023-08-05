# desafio-sistema-bancario

Este é um desafio da DIO de um sistema bancario em Python, de um programa simples que simula um sistema bancário básico, permitindo que o usuário realize algumas operações com sua conta.

Modo de uso:

Depositar (d): Ao selecionar essa opção, você poderá depositar dinheiro na sua conta. O programa pedirá que você informe o valor que deseja depositar e, em seguida, o valor será adicionado ao saldo da sua conta. Caso informe um valor inválido (não positivo), o programa mostrará uma mensagem de erro.

Sacar (s): Nessa opção, você pode realizar saques da sua conta. O programa solicitará o valor que você deseja sacar. Antes de efetuar o saque, algumas verificações serão feitas: se há saldo suficiente na conta, se o valor do saque não excede o limite diário e se você não excedeu o número máximo de saques permitidos. Se alguma dessas condições não for atendida, o programa mostrará uma mensagem de erro. Caso o saque seja realizado com sucesso, o valor será deduzido do saldo da sua conta.

Extrato (e): Ao escolher essa opção, o programa mostrará um extrato com todas as movimentações que foram realizadas na sua conta, incluindo depósitos e saques. O extrato também exibirá o saldo atual da conta.

Histórico de transações (h): Aqui, você poderá visualizar um histórico detalhado de todas as transações realizadas na sua conta, incluindo a data, a hora, o tipo de transação (depósito ou saque) e o valor.

Sair (q): Se você escolher essa opção, o programa será encerrado e você sairá do sistema bancário.
