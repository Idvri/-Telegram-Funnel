from datetime import datetime

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import mapped_column, Mapped

from sqlalchemy_utils import ChoiceType

from .config import Base

STATUS_CHOICES = (
    ('alive', 'Активно'),
    ('dead', 'Неактивно'),
    ('finished', 'Завершено'),
)


class Funnel(Base):
    """Класс воронки."""

    __tablename__ = 'funnel'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, nullable=False
    )
    created_at: Mapped[str] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    status: Mapped[str] = mapped_column(ChoiceType(STATUS_CHOICES), nullable=False)
    status_updated_at: Mapped[str] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
