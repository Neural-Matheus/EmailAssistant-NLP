# -*- coding: utf-8 -*-

import imaplib
import email
from email.header import decode_header
import time
import nltk
from nltk.corpus import stopwords

# Baixar as stopwords do NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))

# Função para verificar novos e-mails
def check_email():
    # Credenciais de login
    username = "exemplo@gmail.com"
    password = "12345Exemplo@"  # Use a senha de aplicativo aqui

    # Conectar ao servidor de e-mail
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    # Buscar e-mails não lidos
    status, messages = mail.search(None, 'UNSEEN')

    # Converter a lista de IDs de e-mails em uma lista
    email_ids = messages[0].split()

    return mail, email_ids

# Função para extrair o conteúdo do e-mail
def extract_email_content(mail, email_id):
    res, msg = mail.fetch(email_id, "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
            else:
                content_type = msg.get_content_type()
                if content_type == "text/plain":
                    body = msg.get_payload(decode=True).decode()

            return subject, body

def enviar_email(remetente, destinatario, assunto, corpo_email, senha):
    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(remetente, senha)
    s.sendmail(remetente, [destinatario], msg.as_string().encode('utf-8'))
    print('Email enviado')

def check_email():
    # Credenciais de login
    username = "exemplo@gmail.com"
    password = "12345Exemplo@"  # Use a senha de aplicativo aqui

    # Conectar ao servidor de e-mail
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    # Buscar e-mails não lidos
    status, messages = mail.search(None, 'UNSEEN')

    # Converter a lista de IDs de e-mails em uma lista
    email_ids = messages[0].split()

    return mail, email_ids

def extract_email_content(mail, email_id):
    res, msg = mail.fetch(email_id, "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
            else:
                content_type = msg.get_content_type()
                if content_type == "text/plain":
                    body = msg.get_payload(decode=True).decode()

            return subject, body

def is_important(subject, body):
    keywords = ["projeto", "reunião", "importante", "urgente", "prazo", "chamada"]
    important_senders = ["chefe@example.com", "colega@example.com"]

    # Verificar palavras-chave no assunto ou corpo
    for keyword in keywords:
        if keyword in subject.lower() or keyword in body.lower():
            return True

    # Verificar se o remetente é importante
    for sender in important_senders:
        if sender in body.lower():
            return True

    return False

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

# Baixar recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('portuguese'))

# Função para resumir o texto
def summarize_text(text):
    # Dividir o texto em sentenças
    sentences = sent_tokenize(text, language='portuguese')

    # Dividir o texto em palavras
    words = word_tokenize(text, language='portuguese')

    # Filtrar stopwords e caracteres não alfabéticos
    words = [word for word in words if word.isalpha() and word.lower() not in stop_words]

    # Calcular a frequência das palavras
    word_freq = Counter(words)

    # Calcular a importância de cada sentença
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence, language='portuguese'):
            if word.lower() in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word.lower()]
                else:
                    sentence_scores[sentence] += word_freq[word.lower()]

    # Selecionar as sentenças mais importantes
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]

    # Juntar as sentenças selecionadas
    summary = ' '.join(summary_sentences)
    return summary

def main_loop():
    while True:
        mail, email_ids = check_email()

        important_emails = []
        # Processar apenas os três e-mails mais recentes
        for email_id in email_ids[-3:]:
            subject, body = extract_email_content(mail, email_id)
            if is_important(subject, body):
                summary = summarize_text(body)
                important_emails.append((subject, summary))

        if important_emails:
            print("E-mails importantes:")
            for subject, summary in important_emails:
                print(f"Assunto: {subject}")
                print(f"Resumo: {summary}\n")
        else:
            print("Últimos 3 e-mails:")
            for email_id in email_ids[-3:]:
                subject, body = extract_email_content(mail, email_id)
                summary = summarize_text(body)
                print(f"Assunto: {subject}")
                print(f"Resumo: {summary}\n")

        break  # Remove o loop infinito para apenas uma verificação

        # Verificar novos e-mails a cada 60 segundos
        time.sleep(60)

def main():
    print("Digite a Opção 1 para Enviar um e-mail e a Opção 2 para validar e-mails importantes!")
    opcao = int(input())

    if opcao == 1:
        remetente = input("Digite o seu e-mail: ")
        senha = input("Digite a sua senha: ")
        destinatario = input("Digite o e-mail do destinatário: ")
        assunto = input("Digite o assunto do e-mail: ")
        corpo_email = input("Digite o corpo do e-mail (pode usar HTML): ")
        enviar_email(remetente, destinatario, assunto, corpo_email, senha)
    elif opcao == 2:
        main_loop()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()