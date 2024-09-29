from django.shortcuts import render

def renderTemplate(request):
    data = {"id" : "123456",
            "nombre" : "Victoria Saldaña", 
            "email": "victoria.saldana@inacapmail.cl"}
    return render(request, 'templateApp/index.html', data)