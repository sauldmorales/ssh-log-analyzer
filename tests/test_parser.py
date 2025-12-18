import os
import sys

# Import desde ../src sin instalar paquete
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from ssh_analyzer import FAILED_PATTERN

def test_detecta_ataque_invalid_user():
    linea = "Failed password for invalid user admin from 192.168.1.66 port 22 ssh2"
    m = FAILED_PATTERN.search(linea)
    assert m is not None
    assert m.group("ip") == "192.168.1.66"
    assert m.group("user") == "admin"

def test_detecta_failed_sin_invalid_user():
    linea = "Failed password for root from 8.8.8.8 port 2222 ssh2"
    m = FAILED_PATTERN.search(linea)
    assert m is not None
    assert m.group("ip") == "8.8.8.8"
    assert m.group("user") == "root"

def test_ignora_trafico_seguro():
    linea = "Accepted password for saul from 10.0.0.1 port 22 ssh2"
    m = FAILED_PATTERN.search(linea)
    assert m is None

def test_no_revienta_con_linea_basura():
    linea = "\xff\xfe\x00BADLINE"
    m = FAILED_PATTERN.search(linea)
    assert m is None


