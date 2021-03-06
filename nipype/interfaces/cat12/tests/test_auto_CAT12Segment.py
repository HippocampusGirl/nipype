# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import CAT12Segment


def test_CAT12Segment_inputs():
    input_map = dict(
        affine_preprocessing=dict(
            field="extopts.APP",
            usedefault=True,
        ),
        affine_regularization=dict(
            field="opts.affreg",
            usedefault=True,
        ),
        cobra=dict(
            field="output.ROImenu.atlases.hammers",
            usedefault=True,
        ),
        csf_output_dartel=dict(
            field="output.CSF.dartel",
            usedefault=True,
        ),
        csf_output_modulated=dict(
            field="output.CSF.mod",
            usedefault=True,
        ),
        csf_output_native=dict(
            field="output.CSF.native",
            usedefault=True,
        ),
        gm_output_dartel=dict(
            field="output.GM.dartel",
            usedefault=True,
        ),
        gm_output_modulated=dict(
            field="output.GM.mod",
            usedefault=True,
        ),
        gm_output_native=dict(
            field="output.GM.native",
            usedefault=True,
        ),
        hammers=dict(
            field="output.ROImenu.atlases.cobra",
            usedefault=True,
        ),
        ignore_errors=dict(
            field="extopts.ignoreErrors",
            usedefault=True,
        ),
        in_files=dict(
            copyfile=False,
            field="data",
            mandatory=True,
        ),
        initial_segmentation=dict(
            field="extopts.spm_kamap",
            usedefault=True,
        ),
        internal_resampling_process=dict(
            field="extopts.restypes.optimal",
            maxlen=2,
            minlen=2,
            usedefault=True,
        ),
        jacobianwarped=dict(
            field="output.jacobianwarped",
            usedefault=True,
        ),
        label_dartel=dict(
            field="output.label.dartel",
            usedefault=True,
        ),
        label_native=dict(
            field="output.label.native",
            usedefault=True,
        ),
        label_warped=dict(
            field="output.label.warped",
            usedefault=True,
        ),
        las_dartel=dict(
            field="output.las.dartel",
            usedefault=True,
        ),
        las_native=dict(
            field="output.las.native",
            usedefault=True,
        ),
        las_warped=dict(
            field="output.las.warped",
            usedefault=True,
        ),
        local_adaptive_seg=dict(
            field="extopts.LASstr",
            usedefault=True,
        ),
        lpba40=dict(
            field="output.ROImenu.atlases.lpba40",
            usedefault=True,
        ),
        matlab_cmd=dict(),
        mfile=dict(
            usedefault=True,
        ),
        n_jobs=dict(
            field="nproc",
            mandatory=True,
            usedefault=True,
        ),
        neuromorphometrics=dict(
            field="output.ROImenu.atlases.neuromorphometrics",
            usedefault=True,
        ),
        output_labelnative=dict(
            field="output.labelnative",
            usedefault=True,
        ),
        own_atlas=dict(
            copyfile=False,
            field="output.ROImenu.atlases.ownatlas",
            mandatory=False,
        ),
        paths=dict(),
        power_spm_inhomogeneity_correction=dict(
            field="opts.biasacc",
            usedefault=True,
        ),
        save_bias_corrected=dict(
            field="output.bias.warped",
            usedefault=True,
        ),
        shooting_tpm=dict(
            copyfile=False,
            extensions=[".hdr", ".img", ".img.gz", ".nii"],
            field="extopts.registration.shooting.shootingtpm",
            mandatory=False,
        ),
        shooting_tpm_template_1=dict(
            copyfile=False,
            extensions=[".hdr", ".img", ".img.gz", ".nii"],
            mandatory=False,
        ),
        shooting_tpm_template_2=dict(
            copyfile=False,
            extensions=[".hdr", ".img", ".img.gz", ".nii"],
            mandatory=False,
        ),
        shooting_tpm_template_3=dict(
            copyfile=False,
            extensions=[".hdr", ".img", ".img.gz", ".nii"],
            mandatory=False,
        ),
        shooting_tpm_template_4=dict(
            copyfile=False,
            extensions=[".hdr", ".img", ".img.gz", ".nii"],
            mandatory=False,
        ),
        skull_strip=dict(
            field="extopts.gcutstr",
            usedefault=True,
        ),
        surface_and_thickness_estimation=dict(
            field="surface",
            usedefault=True,
        ),
        surface_measures=dict(
            field="output.surf_measures",
            usedefault=True,
        ),
        tpm=dict(
            copyfile=False,
            field="tpm",
            mandatory=False,
        ),
        use_mcr=dict(),
        use_v8struct=dict(
            min_ver="8",
            usedefault=True,
        ),
        voxel_size=dict(
            field="extopts.vox",
            usedefault=True,
        ),
        warps=dict(
            field="output.warps",
            maxlen=2,
            minlen=2,
            usedefault=True,
        ),
        wm_hyper_intensity_correction=dict(
            field="extopts.WMHC",
            usedefault=True,
        ),
        wm_output_dartel=dict(
            field="output.WM.dartel",
            usedefault=True,
        ),
        wm_output_modulated=dict(
            field="output.WM.mod",
            usedefault=True,
        ),
        wm_output_native=dict(
            field="output.WM.native",
            usedefault=True,
        ),
    )
    inputs = CAT12Segment.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CAT12Segment_outputs():
    output_map = dict(
        bias_corrected_image=dict(
            extensions=None,
        ),
        csf_dartel_image=dict(
            extensions=None,
        ),
        csf_modulated_image=dict(
            extensions=None,
        ),
        csf_native_image=dict(
            extensions=None,
        ),
        gm_dartel_image=dict(
            extensions=None,
        ),
        gm_modulated_image=dict(
            extensions=None,
        ),
        gm_native_image=dict(
            extensions=None,
        ),
        label_files=dict(),
        label_roi=dict(
            extensions=None,
        ),
        label_rois=dict(
            extensions=None,
        ),
        lh_central_surface=dict(
            extensions=None,
        ),
        lh_sphere_surface=dict(
            extensions=None,
        ),
        mri_images=dict(),
        report=dict(
            extensions=None,
        ),
        report_files=dict(),
        rh_central_surface=dict(
            extensions=None,
        ),
        rh_sphere_surface=dict(
            extensions=None,
        ),
        surface_files=dict(),
        wm_dartel_image=dict(
            extensions=None,
        ),
        wm_modulated_image=dict(
            extensions=None,
        ),
        wm_native_image=dict(
            extensions=None,
        ),
    )
    outputs = CAT12Segment.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
