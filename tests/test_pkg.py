import molecularnodes as mn

def test_name_versions():
    for name in mn.pkg.get_pkgs().keys():
        assert mn.pkg.is_current(name)

def test_is_available():
    assert mn.pkg.is_current('biotite')

def test_get_pkgs():
    names = ['biotite', 'MDAnalysis', 'mrcfile', 'eulerangles', 'starfile']
    for name in mn.pkg.get_pkgs().keys():
        assert name in names