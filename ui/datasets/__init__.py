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
    FilesQuotaAndTransferComponent,
)
from oarepo_ui.resources.components.custom_fields import CustomFieldsComponent
from oarepo_ui.resources.records.config import RecordsUIResourceConfig
from oarepo_ui.resources.records.resource import RecordsUIResource
from oarepo_ui.utils import can_view_deposit_page
from oarepo_ui.ui.components import UIComponent, UIComponentImportMode, UIComponentOverride
from oarepo_ui.proxies import current_oarepo_ui, current_ui_overrides


class DatasetsUIResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/datasets"
    blueprint_name = "datasets_ui"
    model_name = "datasets"

    components = (
        AllowedHtmlTagsComponent,
        BabelComponent,
        PermissionsComponent,
        FilesComponent,
        # AllowedCommunitiesComponent,
        CustomFieldsComponent,
        RecordRestrictionComponent,
        EmptyRecordAccessComponent,
        FilesLockedComponent,
        FilesQuotaAndTransferComponent,
    )

    try:
        from oarepo_vocabularies.ui.resources.components import (
            DepositVocabularyOptionsComponent,
        )

        components.append(DepositVocabularyOptionsComponent)
    except ImportError:
        pass

    application_id = "datasets"

    search_component = UIComponent("DatasetsResultsListItem", "@js/datasets/search/ResultsListItem", UIComponentImportMode.DEFAULT)


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

    config = DatasetsUIResourceConfig()
    resource = DatasetsUIResource(config)
    app.config["OAREPO_UI_RESULT_LIST_ITEM_REGISTRATION_CALLBACK"] = [_register_result_item_to_my_ui]
    print(app.config["OAREPO_UI_RESULT_LIST_ITEM_REGISTRATION_CALLBACKS"], "dwadwadwadawddddd", flush=True)
    # with app.app_context():
    if current_oarepo_ui is not None and resource.api_config.schema and config.search_component:
        component = UIComponent("DynamicResultsListItem", "@js/oarepo_ui/search/DynamicResultsListItem", UIComponentImportMode.DEFAULT)

        override = UIComponentOverride("invenio_app_rdm_users.uploads",f"InvenioAppRdm.DashboardUploads.ResultsList.item", component)
        if override not in current_ui_overrides:
            current_ui_overrides.add(override)
    if current_oarepo_ui is not None and resource.api_config.schema and config.search_component:
        bla=config.model
        current_oarepo_ui.register_result_list_item(config.model.record_json_schema, config.search_component)

         

def _register_result_item_to_my_ui(
        ui_overrides: set[UIComponentOverride], schema: str, component: UIComponent
    ) -> None:
        print("Registering result list item for schema", schema, flush=True)
        component_override = UIComponentOverride("invenio_app_rdm_users.uploads", f"InvenioAppRdm.DashboardUploads.ResultsList.item.{schema}", component)
        if component_override not in ui_overrides:
            ui_overrides.add(component_override)

def create_blueprint(app):
    """Register blueprint for this resource."""
    config = DatasetsUIResourceConfig()
    resource = DatasetsUIResource(config)
    # with app.app_context():
        # if current_oarepo_ui is not None and resource.api_config.schema and config.search_component:
        #     current_oarepo_ui.register_result_list_item(resource.api_config.schema, config.search_component)


    # blueprint = DatasetsUIResource(DatasetsUIResourceConfig()).as_blueprint()
    return resource.as_blueprint()
