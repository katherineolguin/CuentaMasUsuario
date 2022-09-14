
class Cuenta:

    # nombre_banco = "Primer Dojo Nacional"
    devolver_cuenta = []

    def __init__ (self, balance, tasa_interés, numerocuenta): 
        #self.nombreBanco= nombreBanco
        # self.apellido = apellido
        self.balance = balance
        # self.tasa_interés = 0.05
        self.tasa_interés = tasa_interés
        self.numerocuenta = numerocuenta
        Cuenta.devolver_cuenta.append(self)
        

    def depósito(self, amount_increase):
        self.balance += amount_increase
        if self.balance + 1:
            print(f"Tienes un deposito de $+{amount_increase}")
            return self
            
        
    def retiro(self, amount_decrease, Usuario_balance):
        self.balance -= 5
        self.balance -= amount_decrease
        if self.balance < amount_decrease:
            self.balance = Usuario_balance
            print(f"Saldo insuficiente, intente otro monto menor a ${Usuario_balance}.- "  )
            return self
        else:
            print(f"Has echo un retiro de: $-{amount_decrease}, con un cobro de retiro de $5")
            return self

    def transf_dinero(self, amount_decrease, otro_usuario):
        self.balance -= 5
        self.balance -= amount_decrease
        if self.balance < amount_decrease:
            self.balance = otro_usuario
            print(f"Saldo insuficiente, intente otro monto menor a ${otro_usuario}.- "  )
            return self
        else:
            print(f"Has echo un retiro de: $-{amount_decrease}, con un cobro de retiro de $5")
            return self


    def mostrar_info_cuenta(self): 
        print(f"Tu balance es de: ${self.balance} ")
        return self


    def generar_interés(self):
        self.balance += self.balance * self.tasa_interés 
        print(f"Tu balance más tu tasa de interes es de: ${self.balance}")
        return self


    @classmethod
    def import_inst(cls):
        print(f"\n ------------ \nTotal de usuarios que tienen cuenta y sus balances: {len(cls.devolver_cuenta)} cuentas \n")
       
        for ussers in cls.devolver_cuenta:
            # print(f"Nombre Usuario: {ussers.nombre} Apellido: {ussers.apellido} Balance: {ussers.balance})Tasa interes: {ussers.tasa_interés}\n")
            print(f" N° Cuenta: {ussers.numerocuenta} \n Balance: {ussers.balance} \n Tasa interes: {ussers.tasa_interés}\n -----------\n")

   
    def recibir_transf(self, cantidad, otro_Usuario):
        self.balance += cantidad
        otro_Usuario = otro_Usuario
        
        if self.balance > 1:
            print(f"Recibiste un monto de: ${cantidad} de -{otro_Usuario}- ")
            
        return self



    
   
   
    # @classmethod
    # def import_inst(cls):
    #     print(f"Total de usuarios que tienen cuenta y sus balances: {len(cls.devolver_cuenta)} cuentas")

    #     for ussers in cls.devolver_cuenta:
    #         print(f"Nombre Usuario: {ussers.Usuario.nombre}")
    #         print(f"Apellido: {ussers.Usuario.apellido}")
    #         print(f"Balance: {ussers.balance}")
    #         print(f"Tasa interes: {ussers.tasa_interés}\n")
    
