# Email Assistant com Processamento de Linguagem Natural (NLP)

Este é um assistente de e-mails desenvolvido em Python que utiliza técnicas de Processamento de Linguagem Natural (NLP) para extrair e sumarizar conteúdos importantes de mensagens de e-mail.

## Funcionalidades

- **Verificação de E-mails:** O assistente conecta-se à caixa de entrada do Gmail para verificar e-mails não lidos.
- **Extração de Conteúdo:** Extrai o assunto e o corpo dos e-mails utilizando a biblioteca `imaplib` e `email` do Python.
- **Identificação de E-mails Importantes:** Utiliza palavras-chave e remetentes pré-definidos para determinar se um e-mail é importante.
- **Sumarização de Texto:** Usa NLP para resumir o conteúdo dos e-mails em poucas sentenças significativas.
- **Envio de E-mails:** Capacidade de enviar e-mails utilizando SMTP, com suporte a conteúdo HTML.

## Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/Neural-Matheus/EmailAssistant-NLP
   cd EmailAssistant-NLP
   
2. Instale as dependências necessárias (se ainda não estiverem instaladas):
    
    ```bash
    pip install -r requirements.txt
    
3. Configure suas credenciais de e-mail no arquivo main.py:
    ```bash
    username = "seu-email@gmail.com"
    password = "sua-senha"

4. Execute o programa:
    ```bash
    python main.py
    
5. Escolha entre enviar um e-mail (Opção 1) ou verificar e-mails importantes (Opção 2) no menu interativo.

# Pré-requisitos
* Python 3.x
* Conta no Gmail (para utilização do Gmail API)

