# DESAFIO TECNICO - SICREDI

# Explicação breve da solução

A solução foi separada da seguinte forma:
- reader:
responsável por tocar a fonte dos dados de adapta-los para uso do resto do programa
- normalizer:
normalizar os dados dos campos passados para o parser
- processor:
reponsável por aplicar filtros e regra de negócio nos dados já tratados
- main:
constrói o artefato a partir dos dados filtrados
- models:
restringe e tipifica os dados trabalhados
- log:
recebe uma mensagem de log, concatena com o momento exato e documenta a informação

Ao executar o main.py, o programa limpa o processamento.log da execução anterior e registra o início do processamento. Em seguida, o reader carrega o solicitacoes.json e confere se o conteúdo é uma lista de registros. Cada registro passa pelo normalizer, que valida a estrutura e os tipos dos campos e os converte para o formato esperado (por exemplo, id como texto e status como enum). Registros malformados são ignorados e registrados no log com o motivo. Os registros válidos viram objetos Request e seguem para o processor, que mantém apenas os de status APROVADO com CPF preenchido e registra no log o motivo de cada descarte. Por fim, o main gera o aprovados.csv com as colunas id, nome e cpf e registra os totais de registros lidos, exportados e ignorados. Se ocorrer um erro que impeça o processamento (arquivo não encontrado, JSON inválido, estrutura inesperada ou falha ao ler ou gravar arquivos), o erro é registrado no log e o programa encerra com código de saída 1; em caso de sucesso, encerra com código 0.



# pré-requisitos

# instruções para executar o projeto

# premissas adotadas

# ferramentas de consulta ou IA utilizadas
Foram usadas as seguintes ferramentas:
- Documentação oficial da linguagem Python para:
    - a fim conferir e entender melhor o funcionamento das ferramentas nativas da linguagem que não me recordava exatamente(função open() por exemplo)

- Claude: 
    - Discussões sobre abordagens de solução
    - Validação estrutural do projeto principalmente relacionadas à divisão de responsabilidades
    - "Traduzir" minha experiência profissional usando Typescript para o que faz sentido ser aplicado em Python(conceitos mais profundos de POO por exemplo, que costumo prezar por seguir visando um código escalável)
    - Expandir a cobertura de testes do projeto, me ajudando a entender quais possibilidades ainda não foram cobertas
    - implemenatação de mensagens de alguns logs
    
Como você adaptaria essa solução para um processo de BPM, no qual os registros fossem
recebidos por um formulário e o arquivo CSV fosse gerado após uma etapa de
aprovação?