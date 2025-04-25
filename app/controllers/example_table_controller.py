from sqlalchemy.orm import Session
from ..models import ExampleTable

def get_all_example_table_entries(session: Session):
    return session.execute(
        session.query(ExampleTable)
    ).scalars().all()

def update_first_entry():
    first_entry_id = ExampleTable.query.fetchone