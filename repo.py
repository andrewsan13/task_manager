import abc
import models


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, batch: models.Project):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> models.Project:
        raise NotImplementedError


class PyMongoRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def add(self, project):
        self.session.add(project)

    def get(self, reference):
        return self.session.query(models.Project).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(models.Project).all()
