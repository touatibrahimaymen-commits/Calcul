from src.fuss import fuss


def test_fusses():
   assert fuss(5,4)>=1

def test_fusses02():
   assert fuss(7,4)>=1

def test_fusses03():
   assert fuss(10,4)>=1