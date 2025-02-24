# a class for DFAs
# modify as needed
class DFA :

    # init the DFA
    def __init__(self, Q, Sigma, delta, q0, F) : 
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function
        self.q0 = q0 # initial state
        self.F = F # final states
   
   # print the data of the DFA
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the DFA on the word w
    # return if the word is accepted or not
    # modify as needed
    
    def run(self, w):
        #Simulate the DFA on the input word w
        current_state = self.q0  # Start at the initial state
        for symbol in w:
            if symbol not in self.Sigma:
                return False  # Reject if input contains an invalid symbol
            current_state = self.delta.get((current_state, symbol), None)
            if current_state is None:
                return False  # Reject if no transition exists
        
        return current_state in self.F  # Accept if ending in a final state
        