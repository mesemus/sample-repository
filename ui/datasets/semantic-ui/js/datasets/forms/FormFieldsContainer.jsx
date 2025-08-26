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

const FormFieldsContainer = () => {
  const { allowed_file_extensions: allowedFileExtensions } = useFormConfig();

  return (
    <React.Fragment>
      {/* <CommunitySelector /> */}
      <AccordionField
        includesPaths={["metadata.title", "metadata.languages"]}
        active
        label={i18next.t("Basic information")}
      >
        <TextField fieldPath="metadata.title" />
        {/* <VocabularyField
          fieldPath="metadata.languages"
          multiple
          vocabularyName="languages"
        /> */}
      </AccordionField>
      <AccordionField
        includesPaths={["files.enabled"]}
        active
        label={
          <label htmlFor="files.enabled">{i18next.t("Files upload")}</label>
        }
        data-testid="filesupload-button"
      >
        <FilesField allowedFileTypes={allowedFileExtensions} />
      </AccordionField>
      {process.env.NODE_ENV === "development" && <FormikStateLogger />}
    </React.Fragment>
  );
};

export default FormFieldsContainer;
