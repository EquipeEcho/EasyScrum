from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def sobrenome(nome):
    nome = nome.split(" ")
    iniciais = ""
    if len(nome) > 1:
        for i in nome:
            if i != nome[0] and i != nome[-1]:
                i = i[:1] + "."
                iniciais += i + " "
        return nome[0] + " " + iniciais + nome[-1]
    else:
        return nome[0]

def gerar_cert(nome):
    img = Image.open("./static/images/cert.png")
    d = ImageDraw.Draw(img)
    location = (330, 700)
    text_color = (0, 0, 0)
    font = ImageFont.truetype('./static/tff/FreeMonoBold.ttf', 115)
    d.text(location, nome, fill=text_color, font = font)
    current_date = datetime.now()
    date_string = current_date.strftime("%d/%m/%Y")
    date_location = (1500, 1100)
    font_size = 50
    d.text(date_location, date_string, fill=text_color, font_size=font_size)
    cert = "./static/generated/" + nome + ".pdf"
    img.save(cert)
    return cert