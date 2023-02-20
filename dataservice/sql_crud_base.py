

from datastore.sql_datastore import SqlDataStore


class SqlCrudBaseClass:
    def __init__(self, datastore: SqlDataStore, model) -> None:
        self.datastore = datastore
        self.model = model
        return

    def get(self, id: str) -> None:
        self.datastore.session.query(self.model).filter(self.model.id == id).first()
        return

    def create(self) -> None:
        return

    def update(self) -> None:
        return

    def delete(self) -> None:
        return
