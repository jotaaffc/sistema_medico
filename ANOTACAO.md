# PRINCIPAIS COMANDOS DO GIT 
## Enviando a primeira versão
1. git init -> Inicializar a pasta como repositório local
2. git branch -M main -> Altera a branch master para main
3. git add . -> Adiciona os arquivos para o repositório local 
4. git commit -m "Primeira versão do sistema"
5. git remote add origin https://github.com/jotaaffc/sistema_medico.git
6. git push -u origin main

## Enviando as próximas versões 
1. git add .
2. git commit -m "Segunda versão do sistema"
3. git push  



# CONFIGURAÇÃO DE USUÁRIO GIT
git config --global user.name "João almeida"
git config --global user.email "jjvictorcunha@gmail.com"

# COMANDOS DO AMBIENTE VIRTUAL
1. python -m venv venv -> Gera o ambiente virtual do tipo venv 
2. ./venv/Scripts/activate -> Ativa o ambiente virtual
3. pip install django - instala o django
4. django-admin startproject sistema . 
5. python manage.py runserver

# COMANDOS DO DJANGO
1. Criando um ambiente virtual -> python -m venv venv
2. Ativando o ambiente virtual -> .\venv\Scripts\activate 
3. Instalando o django -> pip install django
4. Criando o projeto django -> django-admin startproject nome_do_projeto.
5. Subindo o servidor -> python manage.py runserver
6. Criando um novo app -> python manage.py startapp nome_do_app
7. Criando um superusuario -> python manage.py createsuperuser 
8. Alterando a senha, caso voce esqueça -> python manage.py changepassword nome_do_usuario
9. Gerando o pacote de migração -> python manage.py makemigrations
10. Rodando as alterações do pacote de migração -> python manage.py migrate
11. comando para manipular imagens no django -> python -m pip install Pillow

## OBSERVAÇÕES 
1. Em python, podemos ter mais de uma classe por arquivo.

## Tipos de dados do framework ORM
``Charfield()`` -> é um campo de texto.
    - max_length -> é o tamanho maximo do campo.
    - choice -> é a possibilidade definida para aquele campo.
``Emailfield()``-> é um campo de email, ele valida se o email é valido.(@,.)
``DateTimefield()``-> é um campo de data e hora.
    - default -> é o valor padrão. 
    - timezone -> é a data e hora atual(local).
``Booleanfield `` -> é um campo booleano.
    - default=true -> é por padrão verdadeiro.
``Textfield`` -> é um campo de texto.
    - blank=true -> permite que o campo seja vazio. 
``Imagefield()`` -> é um campo de imagem.
    - uploud_to -> é o caminho onde a imagem será salva. 
    - %Y é o ano
    - %m é o mes
    - %d é o dia 
``Foreignkey()`` -> é um campo de chave estrangeira. 
    - on_delete=models.CASCADE -> significa que quando um paciente/medico for deletado, a consulta também será deletada.
    - verbose_name -> é o nome do campo que será exibido no admin.-
