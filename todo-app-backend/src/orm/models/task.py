from sqlalchemy.orm import Mapped, mapped_column
from orm import Base
from orm.mixins.uuid_str_pk import UidStrPKMixin

class Task(UidStrPKMixin, Base):
    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)