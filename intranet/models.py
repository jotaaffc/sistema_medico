from django.utils import timezone

from django.db import models

# criar um modelo do médico, com nome, email, telefone, crm, especialidade
class Medico(models.Model):
    # Atributos = caracteristicas = variáveis 
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    criacao_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=15)
    crm = models.CharField(max_length=6)
    especialidade = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    mensagem = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)


    # Métodos = Ações = Funções 
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Paciente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    criacao_data = models.DateTimeField(default=timezone.now)
    cpf = models.CharField(max_length=11)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)


    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    

class Consulta(models.Model):
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE)
    horario =  models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)
    status = models.CharField(
        default= 'A', 
        max_length=1,
        choices=(
            ('A','Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada')
        )
    )

    def __str__(self):
        return f'Consulta {self.status} com sucesso.'
    