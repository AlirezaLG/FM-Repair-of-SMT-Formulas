from z3 import *

class UnsatCoreChecker:
    def __init__(self):
        self.s = Solver()
        self.s.set(unsat_core=True)

    def check_unsat_core(self, solver):
        # find unsat 
        # (assert (! (= 12 (+ (- doubleRainbow rainbow) rainbow)) :named a1))
        for i, assertion in enumerate(solver.assertions(), start=0):
            self.s.assert_and_track(assertion, str(i))
        
        # return unsat core index
        if self.s.check() == unsat:
            core = self.s.unsat_core()
            # print(core.sort())
            # print("sharks2")
            return [int(str(constraint)) for constraint in core]