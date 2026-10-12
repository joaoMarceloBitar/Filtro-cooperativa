# DESAFIO TECNICO - SICREDI

## Link do repositório:
https://github.com/joaoMarceloBitar/Filtro-cooperativa

## Explicação breve da solução

A solução foi separada da seguinte forma:
- reader:
responsável por ler a fonte dos dados e adaptá-los para uso do resto do programa
- normalizer:
normalizar os dados dos campos passados para o parser, validando e convertendo os dados, rejeitando os registros inválidos
- processor:
responsável por aplicar filtros e regra de negócio nos dados já tratados
- main:
constrói o artefato a partir dos dados filtrados, orquestra o fluxo de execução modular e trata os erros
- models:
restringe e tipifica os dados trabalhados
- log:
recebe uma mensagem de log, concatena com o momento exato e documenta a informação

Ao executar o main.py, o programa limpa o processamento.log da execução anterior e registra o início do processamento. Em seguida, o reader carrega o solicitacoes.json e confere se o conteúdo é uma lista de registros. Cada registro passa pelo normalizer, que valida a estrutura e os tipos dos campos e os converte para o formato esperado (por exemplo, id como texto e status como enum). Registros malformados são ignorados e registrados no log com o motivo. Os registros válidos viram objetos Request e seguem para o processor, que mantém apenas os de status APROVADO com CPF preenchido e registra no log o motivo de cada descarte. Por fim, o main gera o aprovados.csv com as colunas id, nome e cpf e registra os totais de registros lidos, exportados e ignorados. Se ocorrer um erro que impeça o processamento (arquivo não encontrado, JSON inválido, estrutura inesperada ou falha ao ler ou gravar arquivos), o erro é registrado no log e o programa encerra com código de saída 1; em caso de sucesso, encerra com código 0.

## Decisões relevantes
- O separador usado no arquivo csv consolidado foi a vírgula
- A arquitetura do projeto foi pensada de forma modular, seguindo o princípio da responsabilidade única: cada módulo e cada função tem um único motivo para mudar. O pipeline de operações foi dividido em arquivos: reader lê os dados de entrada -> normalizer valida e converte cada registro -> processor aplica as regras de negócio -> main orquestra a operação como um todo e constrói o csv completo
- A validação foi dividida em duas camadas: o normalizer valida o formato do dado (tipos, campos obrigatórios, CPF com 11 dígitos) e o processor aplica as regras de negócio (status APROVADO e CPF preenchido). Assim o log diferencia um registro inválido de um registro válido, mas que não atende aos critérios de exportação
- Erros de registro e erros estruturais são tratados de forma diferente: um registro inválido é ignorado e registrado no log, sem interromper o processamento dos demais. Já arquivo inexistente, JSON inválido ou conteúdo que não seja uma lista de registros interrompem a execução, pois não há dados para processar
- O filtro confere o status antes do CPF, então cada registro descartado aparece no log com um único motivo
- Priorizei bibliotecas nativas do python para que o projeto rode sem instalar dependências. Para validação de dados e typesafety, por exemplo, poderia ser utilizado pydantic, que já utilizei em outros projetos.

## Pré-requisitos
Python 3.11 ou superior

## Instruções para executar o projeto
1. Abra um terminal na pasta do projeto. Os caminhos dos arquivos são relativos, então o programa deve ser executado a partir dela.
2. Confirme que o arquivo solicitacoes.json está na pasta.
3. Execute: python main.py

Ao final da execução, são gerados na mesma pasta:
- aprovados.csv: registros aprovados com CPF preenchido, com as colunas id, nome e cpf
- processamento.log: registro da execução (também exibido no terminal)

## Premissas adotadas
- O arquivo de entrada deve conter uma lista de registros; qualquer outro conteúdo (objeto, número, null) interrompe a execução
- Cada registro deve ser um objeto com exatamente os campos id, nome, cpf e status. Registros com campos faltando ou com campos extras são considerados inválidos
- Espaços no início e no fim de id, nome, cpf e status são desconsiderados
- id: tratado como identificador textual, e não numérico. É aceito como número ou texto e gravado como texto. Valores null, booleanos ou vazios tornam o registro inválido
- nome: deve ser um texto não vazio; caso contrário, o registro é inválido
- status: a comparação não diferencia maiúsculas de minúsculas ("aprovado" equivale a "APROVADO"). Valores diferentes de APROVADO, PENDENTE e REPROVADO tornam o registro inválido
- cpf:
    - null, texto vazio ou apenas espaços são tratados como CPF vazio: o registro é válido, mas não é exportado
    - é aceito com ou sem pontuação (123.456.789-00 ou 12345678900) e gravado no csv apenas com os dígitos
    - deve conter 11 dígitos; os dígitos verificadores não são validados, conforme o enunciado
    - CPF informado como número, e não como texto, torna o registro inválido, pois zeros à esquerda seriam perdidos na leitura do JSON
- Totais do log: "lidos" considera todos os itens do arquivo, inclusive os inválidos; "ignorados" corresponde a lidos menos exportados

## Ferramentas de consulta ou IA utilizadas
Foram usadas as seguintes ferramentas:
- Documentação oficial da linguagem Python:
    - Conferir e entender melhor o funcionamento das ferramentas nativas da linguagem que não me recordava (função open() por exemplo)

- Claude: 
    - Discussões sobre abordagens de solução
    - Validação estrutural do projeto principalmente relacionadas à divisão de responsabilidades
    - "Traduzir" minha experiência profissional usando Typescript para o que faz sentido ser aplicado em Python(conceitos mais profundos de POO por exemplo, que costumo prezar por seguir visando um código escalável)
    - Expandir a cobertura de exceções capturadas e testes do projeto, me ajudando a entender quais possibilidades ainda não foram cobertas
    - implementação e correção dos logs(sob minha revisão)
    - verificação de bugs silenciosos
    - Auxílio de redação e revisão ortográfica e gramatical do readme
    
## Transparência de ferramentas
Conceitos do projeto que não são autorais ou resultado de discussões de arquitetura, mas sim, propostas geradas pelo claude que foram acatadas no projeto:
- Retorno booleano de build_approved_requests_csv que possibilita encerrar a execução do programa com um código de erro
- Exceção de erros de estrutura de dados carregados

## Integração com processos
Como você adaptaria essa solução para um processo de BPM, no qual os registros fossem
recebidos por um formulário e o arquivo CSV fosse gerado após uma etapa de
aprovação?

Grande parte do projeto pode ser reaproveitada, por conta da abordagem modular: como cada módulo tem um único motivo para mudar, trocar a origem dos dados afeta principalmente o reader. Sobre a implementação, o programa seria executado como uma etapa automática do processo, acionada após a aprovação e recebendo apenas as solicitações aprovadas.
- reader: A fonte dos dados deixa de ser um arquivo e passa a ser o formulário, provavelmente por meio de uma requisição. Seria necessário entender o contrato de dados enviado (lista de objetos, dicionário de objetos...) e adaptar a leitura.
- normalizer: Pode ser totalmente reaproveitado. Mesmo com validações no formulário, o serviço não deve confiar apenas nos dados vindos da interface.
- processor: Como a aprovação passa a ser uma etapa do processo, o filtro de status pode ser removido ou mantido apenas como verificação de segurança. A verificação do CPF poderia ser antecipada para o formulário, evitando que solicitações sem CPF cheguem à etapa de aprovação.
- Geração do CSV: O CSV seria gerado periodicamente (por exemplo, uma vez por dia) com todas as solicitações aprovadas no período, mantendo o formato de arquivo diário que as outras áreas já consomem. Uma geração manual, acionada por um botão no sistema interno, poderia complementar esse fluxo.