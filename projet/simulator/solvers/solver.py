class SolverError(Exception):
    pass


class ISolver:

    # NOTE: our systems do not depend on time,
    # so the input t0 will never be used by the
    # the derivatives function f
    # However, removing it will not simplify
    # our functions so we might as well keep it
    # and build a more general library that
    # we will be able to reuse some day

    def __init__(self, f, t0, y0, max_step_size=0.01):
        self.f = f
        self.t0 = t0
        self.y0 = y0
        self.max_step_size = max_step_size



class DummySolver(ISolver):
    def integrate(self, t):
        """ Compute the solution of the system at t
            The input `t` given to this method should be increasing
            throughout the execution of the program.
            Return the new state at time t.
        """

        h = self.max_step_size
        y = self.y0
        
        while(self.t0 - h <t):     
            y += h * self.f( self.t0 , y)
            self.t0 += h
            
        y_t0 = y 
        y_t1 = y + h*self.f(self.t0, y)
        
        
        self.y0 = ((y_t1-y_t0)/h)*(t-self.t0) + y_t0
        
        return self.y0