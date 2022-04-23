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
        
    def test_nulInt(self):
        assert MF.div(0,1) == 0
        
    def test_nulFloat(self):
        assert MF.div(0,1.125) == 0
        
    def test_nul(self):
        assert MF.div(0,0) == False
        
    def test_intNul(self):
        assert MF.div(1,0) == False
        
    def test_floatNul(self):
        assert MF.div(1.125,0) == False
        
class TestFactorial:
    
    def test_intPos(self):
        assert MF.factorial(3) == 6
        
    def test_posDot(self):
        assert MF.factorial(5.0) == 120
    
    def test_nul(self):
        assert MF.factorial(0) == 1
        
    #todo -5!
        
    def test_floatPos(self):
        assert MF.factorial(1.125) == False

    def test_floatNeg(self):
        assert MF.factorial(-1.125) == False

    def test_neg(self):
        assert MF.factorial(-5) == False
        
    #todo ostatni
    

class TestPow_n:
    
    def test_posPos(self):
        assert MF.pow_n(2,2) == 4
        
    def test_posNeg(self):
        assert MF.pow_n(2,-2) == False
    
    def test_negPos(self):
        assert MF.pow_n(-2,2) == 4
    
    def test_negNeg(self):
        assert MF.pow_n(-2,-2) == False
        
    def test_negOdd(self):
        assert MF.pow_n(-2,3) == -8
        
    def test_intNul(self):
        assert MF.pow_n(2,0) == 1
    
    def test_intNul(self):
        assert MF.pow_n(2,-0) == 1
        
    def test_floatPos(self):
        assert MF.pow_n(2.5,2) == 6.25
    
    def test_floatNeg(self):
        assert MF.pow_n(2.5,-2) == False 
        
    def test_floatNegPos(self):
        assert MF.pow_n(-2.5,2) == 6.25
    
    def test_floatNegNeg(self):
        assert MF.pow_n(-2.5,-2) == False 

    def test_floatNegOdd(self):
        assert MF.pow_n(-2.5,3) == -15.625
        
    def test_intNul(self):
        assert MF.pow_n(2.5,0) == 1
    
    def test_intNul(self):
        assert MF.pow_n(2.5,-0) == 1
    
    def test_nulNul(self):
        assert MF.pow_n(0,0) == 1
        
    def test_nulPos(self):
        assert MF.pow_n(0,5) == 0
        
    #todo ^
    
    
class TestLogx:
        #b>0 b!=1 x>0
        #todo names
        #todo errors

        
    def test_intPosPos(self):
        assert MF.logx(4,2) == 2
        
    def test_floatPosPos(self):
        assert MF.logx(0.25,0.5) == 2
        
    def test_why(self):
        assert MF.logx(0.16,0.2) == 1.138646883853214
        
    def test_intFloatPosPos(self):
        assert MF.logx(4,0.2) == -0.8613531161467861
        
    def test_floatIntPosPos(self):
        assert MF.logx(0.25, 4) == -1
        
    def test_baseOne(self):
        assert MF.logx(4,1) == False
    
    def test_baseNul(self):
        assert MF.logx(4,0) == False
        
    def test_baseNeg(self):
        assert MF.logx(4,-2) == False
        
    def test_argNul(self):
        assert MF.logx(0,2) == False
        
    def test_argNeg(self):
        assert MF.logx(-2,2) == False
