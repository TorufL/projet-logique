from Calcul import addition

def test_addition():
    # Arrange
    a = 5
    b = 15

    # Act
    resultat = addition(a, b)

    # Assert
    assert  resultat == 20