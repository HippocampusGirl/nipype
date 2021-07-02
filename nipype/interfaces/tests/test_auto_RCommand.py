# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..r import RCommand


def test_RCommand_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        rfile=dict(
            usedefault=True,
        ),
        script=dict(
            argstr='-e "%s"',
            mandatory=True,
            position=-1,
        ),
        script_file=dict(
            extensions=None,
            usedefault=True,
        ),
    )
    inputs = RCommand.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
