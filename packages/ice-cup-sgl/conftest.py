import pytest

def pytest_addoption(parser):
    parser.addoption("--weights", action="store", help="Path to model weights")

def pytest_generate_tests(metafunc): 
    if "model_weights_path" in metafunc.fixturenames:
        option_value = metafunc.config.getoption("weights")
        
        if option_value:
            metafunc.parametrize("model_weights_path", [option_value])
        else:
            metafunc.parametrize("model_weights_path", [None])