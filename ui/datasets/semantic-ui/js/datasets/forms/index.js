import { DepositFormApp, parseFormAppConfig } from "@js/oarepo_ui/forms";
import React from "react";
import ReactDOM from "react-dom";
import { OARepoDepositSerializer } from "@js/oarepo_ui/api";
import FormFieldsContainer from "./FormFieldsContainer";
import FormActionsContainer from "./FormActionsContainer";

const recordSerializer = new OARepoDepositSerializer(
  ["errors", "expanded"],
  ["__key"]
);

const config = parseFormAppConfig();
config.formConfig.transfer_types = {
  LOCAL: "L",
  FETCH: "F",
  REMOTE: "R",
  MULTIPART: "M",
};
config.formConfig.enabled_transfer_types = ["L"];

const overridableIdPrefix = config.formConfig.overridableIdPrefix;

export const componentOverrides = {
  [`${overridableIdPrefix}.FormFields.container`]: FormFieldsContainer,
  [`${overridableIdPrefix}.FormActions.container`]: FormActionsContainer,
};

ReactDOM.render(
  <DepositFormApp
    config={config.formConfig}
    record={config.record}
    files={config.files}
    recordSerializer={recordSerializer}
    componentOverrides={componentOverrides}
  />,
  config.rootEl
);
