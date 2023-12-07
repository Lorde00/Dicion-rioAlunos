while True:
        alunos = {'Lucas': 23876263,
                  'Maria': 29382738,
                  'Enzo': 93626145,
                  'João': 18765243}
       
        aluno = str(input('Digite o nome do aluno que quer adicionar: '))
        matricula = (input('Digite a matricula do aluno: '))
        
        alunos.update({ f'{aluno}' : f'{matricula} '})
        
        remover = str(input(f'Deseja remover algum aluno? {alunos} '))
        if remover in alunos:
                alunos.pop(remover)
                print(alunos)
                break
        else:
                print(f' Está é a lista final {alunos} ')
                print('Obrigado por utilizar o programa!')
                break
        
        
                
                  
                  
        







