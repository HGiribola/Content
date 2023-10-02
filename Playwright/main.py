from playwright.sync_api import sync_playwright
from time import sleep
# import hidden


def bemdormido():
    aux = int('3')       # mudar número de 'aux' de acordo com o seu processamento
    while aux > 0:
        print(".")
        sleep(1)
        aux -= 1


def login():        # faz login no google para acessar o bard
    login_link = "https://accounts.google.com/signin/v2/identifier?hl=ja&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    with sync_playwright() as play:
        browser_login = play.chromium.launch(headless=True)
        context_login = browser_login.new_context()
        bemdormido()

        page_login = context_login.new_page()
        page_login.goto(login_link)     # encaminha para a tela de login do google
        bemdormido()

        page_login.fill('#identifierId',userinfo['id'])

        context_login.close()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)     # abrir navegador
    bemdormido()

    login()

    page = browser.new_page()       # abrir bard
    page.goto("https://bard.google.com/chat")
    print(page.title())
    bemdormido()

    browser.close()     # fecha tudo
