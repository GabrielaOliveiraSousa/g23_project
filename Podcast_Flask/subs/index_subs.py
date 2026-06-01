from flask import render_template, request, session
from classes.podcast import Podcast  
import datetime

# Inicializa a variável global que controla a opção anterior
prev_option = ""

def index(path):
    global prev_option
    
    # Garante que a BD é lida se a lista estiver vazia
    if len(Podcast.lst) == 0:
        Podcast.read(path)
        
    # Controla o estado dos botões no formulário
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")
    
    if option == "edit":
        butshow, butedit = "disabled", "enabled"
        
    elif option == "delete":
        obj = Podcast.current()
        Podcast.remove(obj.id)
        if not Podcast.previous():
            Podcast.first()
            
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
        
    elif option == "cancel":
        pass
        
    elif prev_option == 'insert' and option == 'save':
        strobj = str(Podcast.get_id(0))
        strobj = strobj + ';' + request.form["title"] + ';' + \
                 request.form["category"] + ';' + request.form["date"]
        
        obj = Podcast.from_string(strobj)
        Podcast.insert(obj.id)
        Podcast.last()
        
    elif prev_option == 'edit' and option == 'save':
        obj = Podcast.current()
        obj.title = request.form["title"]
        obj.category = request.form["category"]
        obj.date = request.form["date"]
        Podcast.update(obj.id)
        
    # Botões de Navegação
    elif option == "first":
        Podcast.first()
    elif option == "previous":
        Podcast.previous()
    elif option == "next":
        Podcast.nextrec()
    elif option == "last":
        Podcast.last()
    elif option == "exit":
        return "<h1>Thank you for using this app</h1>"
        
    prev_option = option
    
    # Procura o podcast selecionado
    obj = Podcast.current()
    
    if option == 'insert' or len(Podcast.lst) == 0:
        id = 0
        id = Podcast.get_id(id)
        title = category = date = ""
    else:
        id = obj.id
        title = obj.title
        category = obj.category
        date = str(obj.date)
        
    return render_template("index.html", 
                           butshow=butshow, 
                           butedit=butedit,
                           id=id, 
                           title=title, 
                           category=category, 
                           date=date,
                           ulogin=session.get("user"))