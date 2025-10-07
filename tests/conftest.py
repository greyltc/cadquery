import pytest


def pytest_addoption(parser):
    parser.addoption("--tgui", action="store_true", default=False, help="run gui tests")


def pytest_configure(config):
    config.addinivalue_line("markers", "tgui: mark gui test")


def pytest_collection_modifyitems(config, items):

    # run gui tests --tgui option is proveded
    if config.getoption("--tgui"):
        return

    # skip gui tests otherwise
    skip_gui = pytest.mark.skip(reason="need --tgui option to run")
    for item in items:
        if "tgui" in item.keywords:
            item.add_marker(skip_gui)
