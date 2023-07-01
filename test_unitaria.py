import pytest
from unitaria import numeros_amigos,main
    
def test_numero_amigos_pass1():
    numeros_amigos_passes=numeros_amigos(12285,14595)
    assert numeros_amigos_passes
    print("las funcion parametrizada funcioina correctamente")
def test_numero_amigos_pass2():
    numeros_amigos_passes=numeros_amigos(1184,1210)
    assert numeros_amigos_passes
    print("las funcion parametrizada funcioina correctamente")
def test_numero_amigos_pass3():
    numeros_amigos_passes=numeros_amigos(2620,2924)
    assert numeros_amigos_passes
    print("las funcion parametrizada funcioina correctamente")
def test_numero_amigos_pass4():
    numeros_amigos_passes=numeros_amigos(66928,66992)
    assert numeros_amigos_passes
    print("las funcion parametrizada funcioina correctamente")
def test_numero_amigos_pass5():
    numeros_amigos_passes=numeros_amigos(63020,76084)
    assert numeros_amigos_passes
    print("las funcion parametrizada funcioina correctamente")

def test_numero_amigos_fail1():
    numeros_amigos_fails=numeros_amigos(112,99)
    assert not numeros_amigos_fails
    print("las funcion parametrizada funcioina correctamente")

def test_numero_amigos_fail2():
    numeros_amigos_fails=numeros_amigos(779,56)
    assert not numeros_amigos_fails
    print("las funcion parametrizada funcioina correctamente")
def test_numero_amigos_fail3():
    numeros_amigos_fails=numeros_amigos(419,33)
    assert not numeros_amigos_fails
    print("las funcion parametrizada funcioina correctamente")
def test_numero_amigos_fail4():
    numeros_amigos_fails=numeros_amigos(584,679)
    assert not numeros_amigos_fails
    print("las funcion parametrizada funcioina correctamente")
def test_numero_amigos_fail5():
    numeros_amigos_fails=numeros_amigos(10023,45)
    assert not numeros_amigos_fails
    print("las funcion parametrizada funcioina correctamente")
    


if __name__ == '__main__':
    test_numero_amigos_pass1()
    test_numero_amigos_pass2()
    test_numero_amigos_pass3()
    test_numero_amigos_pass4()
    test_numero_amigos_pass5()
    test_numero_amigos_fail1()
    test_numero_amigos_fail2()
    test_numero_amigos_fail3()
    test_numero_amigos_fail4()
    test_numero_amigos_fail5()
