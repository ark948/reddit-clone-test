class Profile(
    TimestampModel,
    SQLModel, 
    table=True
    ):
    id: int = Field(default=None, primary_key=True)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: str = Field(unique=True, nullable=False, max_length=64)
    owner_id: int = Field(foreign_key='users.id')
    owner: User = Relationship(back_populates="profile")

    def __repr__(self) -> str:
        return f'Profile -> {self.username}'

    def dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'created': self.created_at,
            'updated': self.updated_at,
            'owner_id': self.owner_id,
            'owner': self.owner # may cause error
        }
    


# for user model
profile: Optional["Profile"] = Relationship(back_populates="owner")