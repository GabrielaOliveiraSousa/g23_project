from flask import Flask, render_template, request, session
from classes.podcast import Podcast

prev_option = ""

def apps_podcast():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
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
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Podcast.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["dob"] + ';' + request.form["salary"]
            obj = Podcast.from_string(strobj)
            Podcast.insert(obj.id)
            Podcast.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Podcast.current()
            obj.name = request.form["name"]
            obj.dob = request.form["dob"]
            obj.salary = float(request.form["salary"])
            Podcast.update(obj.id)
        elif option == "first":
            Podcast.first()
        elif option == "previous":
            Podcast.previous()
        elif option == "next":
            Podcast.nextrec()
        elif option == "last":
            Podcast.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Podcast.current()
        if option == 'insert' or len(Podcast.lst) == 0:
            id = 0
            id = Podcast.get_id(id)
            name = dob = salary = ""
        else:
            id = obj.id
            name = obj.name
            dob = obj.dob
            salary = obj.salary
        return render_template("podcast.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,dob=dob,salary=salary, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-
