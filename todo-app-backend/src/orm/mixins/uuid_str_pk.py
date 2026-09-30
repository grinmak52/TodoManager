from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column

class UidStrPKMixin:
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))