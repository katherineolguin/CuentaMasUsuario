from multiprocessing.sharedctypes import Value
from Cuenta import Cuenta

class Usuario():
   

    def __init__ (self, nombre, apellido, email, cuentas): 
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.cuentas = cuentas
        # self.cuenta = Cuenta (balance = balance, tasa_interés = 0.05)
        # Usuario.cantidad +=1


    def depósito(self, amount_increase):
        self.cuentas.balance += amount_increase
        if self.cuentas.balance + 1:
            print(f"Tienes un deposito de $+{amount_increase}")
            return self
            
        
    def retiro(self, amount_decrease, Usuario_balance):
        self.cuentas.balance -= 5
        self.cuentas.balance -= amount_decrease
        if self.cuentas.balance < amount_decrease:
            self.cuentas.balance = Usuario_balance
            print(f"Saldo insuficiente, intente otro monto menor a ${Usuario_balance}.- "  )
            return self
        else:
            print(f"Has echo un retiro de: $-{amount_decrease}, con un cobro de retiro de $5")
            return self


    def mostrar_info_cuenta(self): 
        print(f"Tu balance es de: ${self.cuentas.balance} ")
        return self


    def generar_interés(self):
        self.cuentas.balance += self.cuentas.balance * self.cuentas.tasa_interés 
        print(f"Tu balance más tu tasa de interes es de: ${self.cuentas.balance}")
        return self

        

    def recibir_transf(self, nombrecuenta, cantidad , otro_Usuario, nombre_cuenta_usuario):
        self.cuentas[nombrecuenta].transf_dinero(otro_Usuario.cuentas[nombre_cuenta_usuario], cantidad)
        return self
