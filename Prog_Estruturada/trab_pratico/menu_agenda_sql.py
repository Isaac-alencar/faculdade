import modulo_agenda_sql as agenda

print('-'*30)
print('     Agendar de Contatos')
print('-'*30)

while True:
  print('1 - Cadastrar contato;')
  print('2 - Listar contato;')
  print('3 - Listar todos os contatos;')
  print('4 - Apagar contato;')
  print('5 - Apagar todos os contatos;')
  print('6 - Sair.')

  op = int(input('Entre com a opção desejada: '))

  if op == 1:
    nome = input('Digite o nome:')
    nome = agenda.toLower(nome)
    tel = int(input('Digite o telefone:'))
    agenda.adiciona(nome,tel)
  elif op == 2:
    nome = input('Digite o nome para a pesquisa:')
    nome = agenda.toLower(nome)
    print('-'*30)
    agenda.mostraContato(nome)
    print('-'*30)
  elif op == 3:
    print('-'*30)
    print('     Todos os contatos')
    agenda.mostraLista()
    print('-'*30)
  elif op == 4:
    nome = input('Digite o id para a pesquisa:')
    nome = agenda.toLower(nome)
    agenda.apagaContato(nome)
  elif op == 5:
    agenda.apagaTodosContatos()
    print("Todos contatos foram deletados!")
  elif op == 6:
    break
  else:
    print('Digite a opção correta!')

print('-'*30)
print('Obrigado por usar a agenda!!!')
print('-'*30)
