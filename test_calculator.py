import calculator

class TestCalculator:
  def test_calculator(self):
    assert 4 == calculator.add(2, 2)
    
  def test_calculator(self):
    assert 2 == calculator.subtract(4, 2)
