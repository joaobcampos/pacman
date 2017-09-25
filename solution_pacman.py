import os
os.chdir('C://Users/jcampos/Desktop/search')
exec(open('pacman.py').read())
exec(open('searchAgents.py').read())
exec(open('search.py').read())
exec(open('layout.py').read())

aux_layout = Layout(["%%%%%%%","%..%.G%", "%.o%..%", "%%....%", "%..%%%%", "%.P....%", "%%%%%%%"])
aux = SearchAgent()
state_aux = GameState()
state_aux.initialize(aux_layout, 1)
aux.registerInitialState(state_aux)