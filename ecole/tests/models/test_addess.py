import pytest

from ecole.models.address import Address

def test_address_str_should_return_correct_format():
    sut = Address(street="Street", postal_code="1234", city="City")
    assert str(sut) == "Street, 1234 City"