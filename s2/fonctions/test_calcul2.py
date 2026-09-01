from Calcul import addition

def test_addition():
    # Arrange
    a = 5
    b = 15

    # Act
    resultat = addition(a, b)

    # Assert
    assert  resultat == 20

def test_addition2():
    # Arrange
    a = 5
    b = 20

    # Act
    resultat = addition(a, b)

    # Assert
    assert  resultat == 25

def test_addition3():
    # Arrange
    a = 5
    b = 25

    # Act
    resultat = addition(a, b)

    # Assert
    assert  resultat == 30

def test_addition4():
    # Arrange
    a = 5
    b = 35

    # Act
    resultat = addition(a, b)

    # Assert
    assert  resultat == 40