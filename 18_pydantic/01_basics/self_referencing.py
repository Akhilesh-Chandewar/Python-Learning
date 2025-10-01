from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None  # Self-referencing field

Comment.model_rebuild()  # Required to resolve forward references

comment = Comment(
    id=1,
    content="This is a comment",
    replies=[
        Comment(id=2, content="This is a reply"),
        Comment(id=3, content="This is another reply", replies=[
            Comment(id=4, content="Nested reply")
        ])
    ]
)

print(comment.model_dump_json(indent=2))