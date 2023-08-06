class CuentaBancaria:

    def __init__(self, numero_cuenta, propietarios, balance):
        self.__numero_cuenta = numero_cuenta
        self.__propietarios = propietarios
        self.balance = balance

    def depositar(self, valor_a_depositar):
        self.balance = self.balance + valor_a_depositar

    def retirar(self, valor_a_retirar):
        self.balance = self.balance - valor_a_retirar

    def aplicar_cuota_manejo(self):
        self.balance = self.balance - (self.balance*0.02)

    def obtener_num_cuenta(self):
        return(self.__numero_cuenta)
    
    def obtener_propietarios(self):
        return(self.__propietarios)
    
    def mostrar_detalles(self):
        print("Numero de cuenta: ", self.obtener_num_cuenta())
        print("Propietarios: ", self.obtener_propietarios())
        print("Balance: ", self.balance)