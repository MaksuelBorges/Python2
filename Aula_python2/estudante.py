class Estudade():
    def __init__(self):
        self.nome = None
        self.email = None
        self.semestre = 1
        
    def avancar_semestre(self):
        self.semestre += 1
        
class EstudadeDeGraduacao(Estudade):
    def __init__(self, curso):
        super().__init__()
        self.curso = curso
        self.modalidade = None
    
    def exibir(self):
        print("Nome:", self.nome)
        print("Curso:", self.curso)
        print("Modalidade:", self.modalidade)

if __name__ == '__main__':
    aluno = EstudadeDeGraduacao('Computação')
    aluno.exibir()
    print(isinstance(aluno, EstudadeDeGraduacao))
    print(isinstance(aluno, Exception))
    print(isinstance(aluno, Estudade))
    