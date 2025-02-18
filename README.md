# Exemplo de CRUD com AJAX no Django
Material de apoio da disciplina de [Programação de Sistemas para Internet](https://dvcirilo.github.io/psi-ifrn) do IFRN - Campus São Paulo do Potengi.

## Informações
- Sistema simples de lista de livros;
    - Usuários avulsos podem ver a lista e detalhes dos livros;
    - O usuário avulso pode se cadastrar;
    - O usuário comum logado pode adicionar livros aos seus favoritos;
    - O administrador pode gerenciar livros e usuários.
- O objetivo é demonstrar o uso do AJAX com [*jQuery*](https://jquery.com/) e [Django](https://www.djangoproject.com/);
- *Front-end* feito usando apenas blocos de exemplo do [Bootstrap 5](https://getbootstrap.com/);
- *Back-end* seguindo os exemplos da documentação do Django e usando FBVs (*Function Based Views*)

## Implementação
- Pastas de `templates` e `static` na raiz, com sub-pastas para cada *app*, evitando conflitos;
- 3 *apps*:
    - livraria: app principal
    - dashboard: páginas de gerenciamento do sistema
    - contas: gerenciamento de usuários
- Autenticação do Django;
- *Forms* com [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms);

## Rodando
- Clone o repositório;
- Dentro da pasta do repositório inicie e ative um `venv`;
- Instale as dependências:
    - `pip install -r requirements.txt`
- Inicie o BD:
    - `python manage.py migrate`
- Crie um *superuser*:
    - `python manage.py createsuperuser`
- Rode o servidor:
    - `python manage.py runserver`

## Contribuições
- O objetivo do sistema é apenas educacional;
- O código tenta ser simples;
- O código tenta seguir os exemplos das documentações:
    - Facilita o entendimento por iniciantes;
- O código tenta seguir boas práticas de estilo e segurança;
- São bem vindas contribuições no sentido de:
    - Simplificar o código;
    - Atualizar recomendações da documentação;
    - Atualizar as boas práticas.
- Crie seu *fork* e abra um PR para o *branch* `dev`!

