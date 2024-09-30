from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'victoria_saldana_EVA1/index.html')

def user(request):
    data = {"usuario": "1234567",
            "nombre": "Victoria",
            "apellido_pat": "Saldaña",
            "correo_elec": "victoria.saldana@inacapmail.cl",
            "ciudad": "Temuco",
    }
    return render(request, 'victoria_saldana_EVA1/user.html', data)

def terror(request):
    data = {"titulo":"Terror",
            "producto1": "Legado de sangre",
            "producto2": "La Chica gris",
            "producto3": "El baile de los muertos",
            "foto1": "terror1.jpg",
            "foto2": "terror2.jpg",
            "foto3": "terror3.jpg",
            }
    return render(request, 'victoria_saldana_EVA1/productos.html', data)

def fantasia(request):
    data = {"titulo":"Fantasía",
            "producto1": "Juego de tronos",
            "producto2": "Los jardines de la luna",
            "producto3": "El señor de los anillos",
            "foto1": "fantasia1.jpg",
            "foto2": "fantasia2.jpg",
            "foto3": "fantasia3.jpg",
            }
    return render(request, 'victoria_saldana_EVA1/productos.html', data)

def aventura(request):
    data = {"titulo":"Aventura",
            "producto1": "Viaje al centro de la tierra",
            "producto2": "Sherlocks Holmes",
            "producto3": "Donde los áboles cantan",
            "foto1": "aventura1.jpg",
            "foto2": "aventura2.jpg",
            "foto3": "aventura3.jpg",
            }
    return render(request, 'victoria_saldana_EVA1/productos.html', data)


def descripcion(request):   
    data_desc = { 
        "Terror": {
            "Legado de sangre": "Una oscura historia de herencias malditas", 
            
            "La Chica gris": "Donde el miedo acecha en cada sombra",

            "El baile de los muertos": "Una danza macabra que te atrapará hasta el último suspiro."},

        "Fantasía": {
            "Juego de Tronos": "Una lucha por el poder en un reino lleno de intrigas",

            "Los jardines de la luna": "Donde la magia y las conspiraciones se entrelazan en un vasto universo",

            "El señor de los anillos": """La legendaria aventura que definió el género, 
            con héroes enfrentándose a la oscuridad. Cada historia te transportará a mundos 
            extraordinarios donde lo imposible se convierte en realidad.
            """},

        "Aventura": {
            "Viaje al centro de la Tierra": "Una expedición épica hacia lo desconocido",

            "Sherlock Holmes": "Donde el famoso detective enfrenta misterios llenos de peligros",

            "Donde los árboles cantan": """ una aventura mágica que te transportará a un mundo 
            lleno de secretos y maravillas. Cada relato promete llevarte al límite de lo imaginable."""}
    }   

    # descripcion =  data_desc.get(categoria, {}).get(producto, "descripcion no se encuentra")
    
    # data = {"titulo": "descripcion",
    #        "categoria": categoria,
    #        "producto": producto,
    #        "descripcion": descripcion
    #}

    return render(request, 'victoria_saldana_EVA1/descripcion.html', data_desc)