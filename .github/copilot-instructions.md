# Copilot Instructions for AI Agents

## Visão Geral do Projeto
Este repositório implementa funções para converter relatórios do linter `flake8` em formatos específicos para consumo automatizado. O foco é transformar a saída padrão do flake8 em estruturas de dados Python padronizadas, facilitando integração e análise.

## Estrutura Principal
- `app/main.py`: Local esperado para implementação das funções principais (`format_linter_error`, `format_single_linter_file`, `format_linter_report`).
- `tests/`: Contém testes automatizados para as funções principais.
- `README.md`: Documentação detalhada com exemplos de entrada e saída para cada função.
- `checklist.md`: Lista de verificação para submissão de código.

## Convenções e Padrões
- Todas as funções devem conter apenas a instrução `return` (sem lógica extra, prints ou side effects).
- O formato de saída deve seguir exatamente os exemplos do `README.md`.
- Utilize nomes de funções e argumentos exatamente como especificado.
- Não adicione validações, prints ou comentários extras nas funções principais.
- O código deve ser compatível com Python 3.8+.

## Fluxo de Trabalho
- Implemente as funções em `app/main.py`.
- Execute os testes em `tests/test_main.py` para validar a implementação.
- Utilize o checklist antes de submeter alterações.

## Dependências
- O projeto utiliza apenas dependências padrão do Python. Não adicione bibliotecas externas.

## Exemplos Importantes
Veja o `README.md` para exemplos detalhados de entrada e saída esperada das funções. Siga fielmente o formato apresentado.

## Observações
- O projeto não utiliza frameworks web, banco de dados ou integração externa.
- O foco é a transformação de dados e padronização de relatórios de linter.

---

Se alguma instrução estiver ambígua ou faltar contexto, consulte o `README.md` ou peça esclarecimentos ao mantenedor.
