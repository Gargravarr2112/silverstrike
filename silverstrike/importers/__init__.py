from . import dkb, dkb_visa, halifax, pc_mastercard, volksbank

IMPORTERS = [
    dkb,
    dkb_visa,
    halifax,
    pc_mastercard,
    volksbank,
]

IMPORTER_NAMES = [
    'DKB Giro',
    'DKB Visa',
    'Halifax',
    'PC MasterCard',
    'Volksbank',
]

try:
    from . import ofx
    IMPORTERS.append(ofx)
    IMPORTER_NAMES.append('OFX Importer')
except ImportError:
    pass
