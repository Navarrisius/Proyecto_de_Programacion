class GameStateManager:
    def __init__(self, estado_actual):
        self.estado_actual = estado_actual


    def get_estado(self):
        return self.estado_actual
    
    
    def set_estado(self, estado):
        self.estado_actual = estado
