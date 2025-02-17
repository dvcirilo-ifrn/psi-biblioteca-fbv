# Exemplo de CRUD com AJAX no Django
Material de apoio da disciplina de [Programação de Sistemas para Internet](https://dvcirilo.github.io/psi-ifrn) do IFRN - Campus São Paulo do Potengi.

## Informações
- Sistema simples de lista de livros;
- Usa AJAX para quase tudo;
- *Front-end* feito usando apenas blocos de exemplo do [Bootstrap](https://getbootstrap.com/);
- *Back-end* seguindo os exemplos da documentação do Django e usando FBV (*Function Based Views*)
- Pastas de `templates` e `static` na raiz, com sub-pastas para cada *app*, evitando conflitos;
- 3 *apps*:
    - site: páginas públicas do sistema
    - dashboard: páginas de gerenciamento do sistema
    - contas: gerenciamento de usuários

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
- O código tem que ser simples;
- O código tenta seguir os exemplos da documentação das dependências:
    - Facilita o entendimento por iniciantes;
- O código tenta seguir as boas práticas no momento da escrita;
- São bem vindas contribuições no sentido de:
    - Simplificar o código;
    - Atualizar recomendações da documentação;
    - Atualizar as boas práticas.

