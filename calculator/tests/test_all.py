import matlib.math_funcs as MF

class TestAdd:
    def test_intPos(self):
        assert MF.add(1,2) == 3
        
    def test_intNeg(self):
        assert MF.add(-1,-2) == -3
        
    def test_floatPos(self):
        assert MF.add(1.5,2.7) == 4.2
        
    def test_floatNeg(self):
        assert MF.add(1.5+2.7) == 4.2
    
    def test_intFloat(self):
        assert MF.add(1,2.5) == 3.5