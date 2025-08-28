import * as React from "react";
import {
  useFormConfig,
  FormikStateLogger,
  FilesField,
  TextField,
} from "@js/oarepo_ui/forms";
// import { CommunitySelector } from "@js/communities_components/CommunitySelector/CommunitySelector";
// import { VocabularyField } from "@js/oarepo_vocabularies";
import { AccordionField } from "react-invenio-forms";
import { i18next } from "@translations/i18next";
import { UppyUploader } from "@js/invenio_rdm_records";
import { connect } from "react-redux";
import PropTypes from "prop-types";

const FormFieldsContainerComponent = ({ record }) => {
  const { filesLocked } = useFormConfig();
  return (
    <React.Fragment>
      <AccordionField
        includesPaths={["metadata.title"]}
        active
        label={i18next.t("Basic information")}
      >
        <TextField fieldPath="metadata.title" />
      </AccordionField>
      <AccordionField
        includesPaths={["files.enabled"]}
        active
        label={
          <label htmlFor="files.enabled">{i18next.t("Files upload")}</label>
        }
        data-testid="filesupload-button"
      >
        <UppyUploader
          isDraftRecord={!record.is_published}
          // TODO: implement following being sent from BE? They are sending some parameters in separate
          // hidden inputs and some in config? Not clear based on what they are arranging this
          // quota={this.config.quota}
          // decimalSizeDisplay={this.config.decimal_size_display}
          // allowEmptyFiles={allowEmptyFiles}
          // fileUploadConcurrency={config.fileUploadConcurrency}

          showMetadataOnlyToggle={false}
          filesLocked={filesLocked}
        />
      </AccordionField>
      {process.env.NODE_ENV === "development" && <FormikStateLogger />}
    </React.Fragment>
  );
};

FormFieldsContainerComponent.propTypes = {
  record: PropTypes.object.isRequired,
};

const mapStateToProps = (state) => {
  return {
    record: state.deposit.record,
  };
};

export default connect(mapStateToProps)(FormFieldsContainerComponent);
