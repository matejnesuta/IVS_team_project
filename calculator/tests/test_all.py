import matlib.math_funcs as MF

class TestAdd:
    def test_intPos(self):
        assert MF.add(1,2) == 3
        
    def test_intNeg(self):
        assert MF.add(-1,-2) == -3
        
    def test_intNegPos(self):
        assert MF.add(-2,1) == -1
        
    def test_floatPos(self):
        assert MF.add(1.5,2.7) == 4.2
        
    def test_floatNeg(self):
        assert MF.add(-1.5,-2.7) == -4.2
        
    def test_floatNegPos(self):
        assert round(MF.add(-1.2,2.325),3) == 1.125
    
    def test_intFloat(self):
        assert MF.add(1,2.5) == 3.5
        
        
    def test_nul(self):
        assert MF.add(0,0) == 0
        
    def test_nulInt(self):
        assert MF.add(0,1) == 1
        
    def test_nulFloat(self):
        assert MF.add(0,1.125) == 1.125
        

class TestSub:
    def test_intPos(self):
        assert MF.sub(1,2) == -1
        
    def test_intNeg(self):
        assert MF.sub(-1,-2) == 1
        
    def test_intNegPos(self):
        assert MF.sub(-2,1) == -3
        
    def test_floatPos(self):
        assert round(MF.sub(1.5,2.8),1) == -1.3
        
    def test_floatNeg(self):
        assert round(MF.sub(-1.5,-2.7),1) == 1.2
        
    def test_floatNegPos(self):
        assert round(MF.sub(-1.2,2.325),3) == -3.525
    
    def test_intFloat(self):
        assert MF.sub(1,2.5) == -1.5
        
        
    def test_nul(self):
        assert MF.sub(0,0) == 0
        
    def test_nulInt(self):
        assert MF.sub(0,1) == -1
        
    def test_nulFloat(self):
        assert MF.sub(0,1.125) == -1.125