from sqlalchemy import Column, String, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import db
from app.model.user import User


class UserCredential(db.Model):
    __tablename__ = 'user_credential'

    # Using with_variant enables auto_increment in sqlite
    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    name = Column(String)
    base64 = Column(String)
    user_id = Column(String, ForeignKey(User.id, ondelete='CASCADE'), nullable=False, index=True)

    user = relationship('User', back_populates='credentials')
