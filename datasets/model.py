
#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-rdm (see https://github.com/oarepo/oarepo-rdm).
#
# oarepo-rdm is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
from __future__ import annotations

from invenio_i18n import lazy_gettext as _
from oarepo_model.api import model
from oarepo_model.presets.drafts import drafts_presets
from oarepo_model.presets.rdm import rdm_presets
from oarepo_model.presets.records_resources import records_resources_presets
from oarepo_model.datatypes.registry import from_yaml

datasets = model(
    "datasets",
    version="1.0.0",
    presets=[records_resources_presets, drafts_presets, rdm_presets],
    types=[
        from_yaml("metadata.yaml", __file__)
    ],
    metadata_type="Metadata",
    customizations=[],
)
