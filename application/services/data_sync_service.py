class DataSyncService:
    def __init__(self, source, embedder, vector_store):
        self.source = source
        self.embedder = embedder
        self.vector_store = vector_store

    def sync(self):
        issues = self.source.fetch()

        for issue in issues:
            text = issue.get("ticketBody") or ""

            emb = self.embedder.embed(text)

            metadata = {
                "ticketId": issue.get("ticketId"),
                "ticketName": issue.get("ticketName") or "",
                "ticketBody": text,
                "ticketAnswer": issue.get("ticketAnswer") or ""
            }

            self.vector_store.add_new(
                doc_id=str(issue.get("ticketId")),
                embedding=emb,
                document=text,
                metadata=metadata
            )

        return len(issues)