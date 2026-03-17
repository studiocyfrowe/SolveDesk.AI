class DataSyncService:
    def __init__(self, source, embedder, vector_store):
        self.source = source
        self.embedder = embedder
        self.vector_store = vector_store

    def sync(self):
        issues = self.source.fetch()
        for issue in issues:
            text = issue["issueSympthoms"]
            emb = self.embedder.embed(text)

            self.vector_store.add_new(
                doc_id=str(issue["issueItemId"]),
                embedding=emb,
                document=text,
                metadata={
                    "issueItemId": issue["issueItemId"],
                    "issueName": issue["issueName"],
                    "issueSympthoms": issue["issueSympthoms"],
                    "issueSolution": issue["issueSolution"]
                }
            )
        
        return len(issues)