from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from orm import Base
from orm.mixins.uuid_str_pk import UidStrPKMixin

class Category(UidStrPKMixin, Base):
    __tablename__ = 'categories'
    name: Mapped[str] = mapped_column(String(255))
