from alembic import op
import sqlalchemy as sa
from models import Todo, SessionLocal

# Open a session to the database
session = SessionLocal()

# Example seed data
seed_data = [
    {"task": "Learn SQLAlchemy"},
    {"task": "Build an API with Flask"},
    {"task": "Write documentation"},
    {"task": "Test the API"}
]

try:
    # Check if there are any existing tasks in the database
    existing_task = session.query(Todo).first()

    # If no existing tasks found, proceed with seeding
    if existing_task is None:
        # Create Todo instances from the seed data
        todos = [Todo(**data) for data in seed_data]

        # Add new Todos to the session
        session.add_all(todos)

        # Commit the transaction
        session.commit()

        print("Seeding completed successfully!")
    else:
        print("Seeding is not needed!")
        pass
except Exception as e:
    # Roll back the session in case of an error
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    # Close the session
    session.close()