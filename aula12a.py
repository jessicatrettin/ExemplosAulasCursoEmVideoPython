nome = str(input('Qual o seu nome? ')).title()
if nome == 'Jéssica':
    print('Que nome bonito.')
elif nome == 'João' or nome == 'Maria':
    print('Seu nome é bem comum no Brasil.')
else:
    print('Que nome normal.')
print('Tenha um bom dia, {}!'.format(nome))
