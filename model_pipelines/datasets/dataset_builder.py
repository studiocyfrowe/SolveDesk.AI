from sentence_transformers import InputExample

class DatasetBuilder:
    def build_from_issues(self, issues: list[dict]) -> list[InputExample]:
        examples = []

        for row in issues:
            issue_name = str(row["issueName"])
            issue_symptoms = str(row["issueSympthoms"])

            examples.append(
                InputExample(
                    texts=[issue_name, issue_symptoms],
                    label=1.0
                )
            )

        return examples