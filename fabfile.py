from fabric.api import run, local


def runlocal():
    """
    Runserver with local settings
    """
    local('./manage.py runserver --settings=tequio.settings.local')

def shelllocal():
    """
    django shell with local settings
    """
    local('./manage.py shell --settings=tequio.settings.local')

def test():
    """
    test with local settings
    """
    local('./manage.py test --settings=tequio.settings.local')
