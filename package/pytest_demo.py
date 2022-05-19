import pytest
import logging as logger

def test_set_comparison():
    set1 = set("1308")
    set2 = set("1308")
    assert set1 == set2
    print("<<<<<<<>>>>>>>>>>>>>>>>>><<<Success<<<<<<<<<<<>>>>>")


#@pytest.mark.tcid29
def test_create_user():
    logger.info("<<<<<<<Name is logger>>>>>>>>")
    print("test123")