from flask_menu import current_menu
from invenio_i18n import lazy_gettext as _
from oarepo_ui.resources import BabelComponent
from oarepo_ui.resources.components import (
    # AllowedCommunitiesComponent,
    AllowedHtmlTagsComponent,
    EmptyRecordAccessComponent,
    FilesComponent,
    FilesLockedComponent,
    PermissionsComponent,
    RecordRestrictionComponent,
)
from oarepo_ui.resources.components.custom_fields import CustomFieldsComponent
from oarepo_ui.resources.records.config import RecordsUIResourceConfig
from oarepo_ui.resources.records.resource import RecordsUIResource
from oarepo_ui.utils import can_view_deposit_page


class DatasetsUIResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/datasets"
    blueprint_name = "datasets"
    model_name = "datasets"

    components = (
        AllowedHtmlTagsComponent,
        BabelComponent,
        PermissionsComponent,
        # FilesComponent,
        # AllowedCommunitiesComponent,
        CustomFieldsComponent,
        RecordRestrictionComponent,
        EmptyRecordAccessComponent,
        FilesLockedComponent,
    )

    try:
        from oarepo_vocabularies.ui.resources.components import (
            DepositVocabularyOptionsComponent,
        )

        components.append(DepositVocabularyOptionsComponent)
    except ImportError:
        pass

    application_id = "datasets"

    templates = {
        "detail": "datasets.Detail",
        "search": "datasets.Search",
        "edit": "datasets.Deposit",
        "create": "datasets.Deposit",
    }


class DatasetsUIResource(RecordsUIResource):
    pass


def init_menu(app):
    """Initialize menu before first request."""
    with app.app_context():
        current_menu.submenu("plus.create_datasets").register(
            "datasets.create",
            _("New Datasets"),
            order=1,
            visible_when=can_view_deposit_page,
        )


def create_blueprint(app):
    """Register blueprint for this resource."""
    blueprint = DatasetsUIResource(DatasetsUIResourceConfig()).as_blueprint()
    return blueprint
