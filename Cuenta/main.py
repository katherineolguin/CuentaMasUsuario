from Cuenta import Cuenta
from Usuario import Usuario



Cuenta1 = Cuenta(50000, 0.05, 0.1)
Cuenta2 = Cuenta(50000, 0.05, 0.2 )
# Marie = Cuenta ("Marie", "Curie", 50000)
# Nicolas = Cuenta ("Nicolas", "Tesla", 50000) 


# print(Marie.Usuario.nombre)
# Marie.mostrar_info_cuenta().depósito(5000).depósito(10000).depósito(6000).retiro(72000, (Marie.balance)).mostrar_info_cuenta()

# print("\n")

# print(Nicolas.nombre)
# Nicolas.mostrar_info_cuenta().depósito(15000).depósito(6000).retiro(5000, (Nicolas.balance)).retiro(5000, (Nicolas.balance)).retiro(5000, (Nicolas.balance)).retiro(4000, (Nicolas.balance)).generar_interés().mostrar_info_cuenta()


print("\n")
Cuenta.import_inst()




Marie = Usuario("Marie", "Curie", "marie.curie@coding.com",{Cuenta1})

print(Marie.nombre)
Cuenta1.mostrar_info_cuenta().depósito(5000).depósito(10000).depósito(6000).retiro(7000, {Cuenta1}).mostrar_info_cuenta()
print("\n")

Nicolas = Usuario("Nicolas", "Tesla", "nicola.t@coding.com",{Cuenta2})

print(Nicolas.nombre)
Cuenta2.mostrar_info_cuenta().depósito(15000).depósito(6000).retiro(5000, {Cuenta2}).retiro(5000, {Cuenta2}).retiro(5000, {Cuenta2}).retiro(4000, {Cuenta2}).generar_interés().mostrar_info_cuenta()



print("\n")

Cuenta.import_inst()

print(f"Usurio: {Marie.nombre}")
Cuenta1.recibir_transf(20000, (Nicolas.nombre + ' ' + Nicolas.apellido))


print("\n")

Cuenta.import_inst()