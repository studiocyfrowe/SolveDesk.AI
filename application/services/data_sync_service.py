class DataSyncService:
    def __init__(self, source, embedder, vector_store):
        self.source = source
        self.embedder = embedder
        self.vector_store = vector_store

    def sync(self):
        issues = self.source.fetch()
        processed = 0

        for issue in issues:
            raw_id = issue.get("ticketId")

            if raw_id is None:
                print(f"Pominięto rekord bez ticketId: {issue}")
                continue

            doc_id = str(raw_id)

            text = issue.get("ticketBody") or ""

            if not text.strip():
                print(f"Pusty ticketBody dla ID: {doc_id}")
                continue

            emb = self.embedder.embed(text)

            metadata = {
                "ticketId": raw_id,
                "ticketName": issue.get("ticketName") or "",
                "ticketBody": text,
                "ticketAnswer": issue.get("ticketAnswer") or ""
            }

            self.vector_store.add_new(
                doc_id=doc_id,
                embedding=emb,
                document=text,
                metadata=metadata
            )

            processed += 1

        return processed