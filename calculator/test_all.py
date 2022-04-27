import pytest
import mathlib.math_funcs as MF

#refactoring needed 
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
        
    def test_floatNegIntPos(self):
        assert MF.pow_n(-2.5,2) == 6.25
    
    def test_floatNegIntNeg(self):
        assert MF.pow_n(-2.5,-2) == False 

    def test_floatNegOdd(self):
        assert MF.pow_n(-2.5,3) == -15.625
        
    def test_floatNul(self):
        assert MF.pow_n(2.5,0) == 1
    
    def test_floatNulNeg(self):
        assert MF.pow_n(2.5,-0) == 1
    
    def test_nulNul(self):
        assert MF.pow_n(0,0) == 1
        
    def test_nulPos(self):
        assert MF.pow_n(0,5) == 0

    def test_intPosfloatPos(self):
        assert MF.pow_n(2,2.5) == False

    def test_intNegfloatPos(self):
        assert MF.pow_n(-2,2.5) == False

    def test_intPosfloatNeg(self):
        assert MF.pow_n(2,-2.5) == False

    def test_intNegfloatNeg(self):
        assert MF.pow_n(-2,-2.5) == False

    def test_floatPosfloatPos(self):
        assert MF.pow_n(2.5,2.5) == False
    
    def test_floatNegfloatPos(self):
        assert MF.pow_n(-2.5,2.5) == False

    def test_floatPosfloatNeg(self):
        assert MF.pow_n(2.5,-2.5) == False
    
    def test_floatNegfloatNeg(self):
        assert MF.pow_n(-2.5,-2.5) == False
        
class TestNrh_root:

    def test_intPosIntPos(self):
        assert MF.nth_root(4,2) == 2

    def test_intPosIntNeg(self):
        assert MF.nth_root(4,-2) == False

    def test_intPosNul(self):
        assert MF.nth_root(4,0) == False

    def test_intPosfloatPos(self):
        assert MF.nth_root(4,3.375) == 1.5079541804033867

    def test_intPosfloatNeg(self):
        assert MF.nth_root(4,-3.375) == False

    def test_intNegIntOdd(self):
        assert MF.nth_root(-8,3) == -2

    def test_intNegIntEven(self):
        assert MF.nth_root(-8,2) == False

    def test_intNegIntNeg(self):
        assert MF.nth_root(-2,-2) == False

    def test_IntNegNul(self):
        assert MF.nth_root(-2,0) == False

    def test_intNegfloatPos(self):
        assert MF.nth_root(-2,3.375) == False

    def test_intNegfloatNeg(self):
        assert MF.nth_root(-2,-3.375) == False

    def test_nulIntPos(self):
        assert MF.nth_root(0,43) == 0

    def test_nulIntNeg(self):
        assert MF.nth_root(0,-43) == False

    def test_nulNul(self):
        assert MF.nth_root(0,0) == False

    def test_nulFloatPos(self):
        assert MF.nth_root(0,3.375) == 0

    def test_nulFloatNeg(self):
        assert MF.nth_root(0,-3.375) == False

    def test_floatPosIntPos(self):
        assert MF.nth_root(3.375,3) == 1.5

    def test_floatNegOdd(self):
        assert MF.nth_root(-3.375,3) == -1.5

    def test_floatNegEven(self):
        assert MF.nth_root(-3.375,2) == False

    def test_floatPosIntNeg(self):
        assert MF.nth_root(3.375,-3) == False

    def test_floatPosNul(self):
        assert MF.nth_root(3.375,0) == False

    def test_floatPosfloatPos(self):
        assert MF.nth_root(3.375,3.375) == 1.4339221176344628

    def test_floatPosfloatNeg(self):
        assert MF.nth_root(3.375,-3.375) == False

class TestLogx:

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
