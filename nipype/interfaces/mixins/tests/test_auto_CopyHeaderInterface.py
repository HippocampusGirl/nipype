# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..fixheader import CopyHeaderInterface


def test_CopyHeaderInterface_inputs():
    input_map = dict()
    inputs = CopyHeaderInterface.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
