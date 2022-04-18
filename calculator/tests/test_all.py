import pytest
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
        

class TestMul:
    
    def test_intPos(self):
        assert MF.mul(1,2) == 2
        
    def test_intNeg(self):
        assert MF.mul(-1,-2) == 2
        
    def test_intNegPos(self):
        assert MF.mul(-2,1) == -2
        
    def test_floatPos(self):
        assert round(MF.mul(1.5,2.8),1) == 4.2
        
    def test_floatNeg(self):
        assert round(MF.mul(-1.5,-2.8),1) == 4.2
        
    def test_floatNegPos(self):
        assert round(MF.mul(-1.2,2.325),2) == -2.79
    
    def test_intFloat(self):
        assert MF.mul(1,2.5) == 2.5
        
    def test_nul(self):
        assert MF.mul(0,0) == 0
        
    def test_nulInt(self):
        assert MF.mul(0,1) == 0
        
    def test_nulFloat(self):
        assert MF.mul(0,1.125) == 0
        
class TestDiv:
    
    def test_intPos(self):
        assert MF.div(1,2) == 0.5
        
    def test_intNeg(self):
        assert MF.div(-1,-2) == 0.5
        
    def test_intNegPos(self):
        assert MF.div(-2,1) == -2
        
    def test_floatPos(self):
        assert MF.div(1.5,0.75) == 2
        
    def test_floatNeg(self):
        assert MF.div(-1.5,-0.75) == 2
        
    def test_floatNegPos(self):
        assert MF.div(1.5,-0.75) == -2
    
    def test_intFloat(self):
        assert MF.div(2.5,1) == 2.5
        
    def test_nul(self):
        MF.div(0,0)
        assert "Division by zero" 
        
    def test_nulInt(self):
        assert MF.div(0,1) == 0
        
    def test_nulFloat(self):
        assert MF.div(0,1.125) == 0
        
    def test_nul(self):
        MF.div(0,0)
        assert "Division by zero" 
        
    def test_intNul(self):
        MF.div(1,0)
        assert "Division by zero" 
        
    def test_floatNul(self):
        MF.div(1.125,0)
        assert "Division by zero" 
        
class TestFactorial:
    
    def test_pos(self):
        assert MF.factorial(3) == 6
    
    def test_nul(self):
        assert MF.factorial(0) == 1
        
    def test_float(self):
        MF.factorial(1.125)
        assert "Param is not an integer"