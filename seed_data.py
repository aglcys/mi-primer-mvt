from ejemplo.models import Familiar

Familiar(nombre="Angelica", direccion="Roma 800", numero_pasaporte=999999).save()
Familiar(nombre="Perseo", direccion="Roma 800", numero_pasaporte=777777).save()
Familiar(nombre="Andromeda", direccion="Roma 800", numero_pasaporte=888888).save()
Familiar(nombre="Michelle", direccion="Roma 800", numero_pasaporte=101010).save()

print("Tu Ohana está correctamente grabada")