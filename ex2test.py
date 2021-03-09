from ex2 import velocidade, posicao

eps = 1.19209e-07

def test1_velocidade():
    assert velocidade(0, 0, 0.1, 1) == 0.0
    assert abs(velocidade(0, 0, 0.1, 2) - 0.06) < eps
    assert abs(velocidade(0, 0, 0.1, 20) - 62913.3) < eps

def test2_posicao():
    assert posicao(0, 0, 0, 0.1, 1) == 0.0
    assert abs(posicao(0, 0, 0, 0.1, 2) - 0.06) < eps
    assert abs(posicao(0, 0, 0, 0.1, 20) - 1069548.9) < eps
