"""create-roles

Revision ID: 70178deedcc6
Revises: a70417660f36
Create Date: 2024-07-31 20:01:13.151669

"""
import os
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70178deedcc6'
down_revision: Union[str, None] = 'a70417660f36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Reading the POSTGREST config from environment variable
pgrst_db_username = os.getenv('PGRST_DB_USERNAME', 'authenticator')
pgrst_db_schema = os.getenv('PGRST_DB_SCHEMA', 'api')
pgrst_db_anon_role = os.getenv('PGRST_DB_ANON_ROLE', 'web_anon')
pgrst_db_password = os.getenv('PGRST_DB_PASSWORD')

def upgrade() -> None:
    pass
    # Create the web_anon role
    op.execute(f"CREATE ROLE {pgrst_db_anon_role} NOLOGIN;")

    # Grant usage on the schema api to web_anon
    op.execute(f"GRANT USAGE ON SCHEMA {pgrst_db_schema} TO {pgrst_db_anon_role};")

    # Grant select on the table api.todos to web_anon
    op.execute(f"GRANT SELECT ON {pgrst_db_schema}.todos TO {pgrst_db_anon_role};")

    # Create the authenticator role with a password and NOINHERIT attribute
    op.execute(f"CREATE ROLE {pgrst_db_username} NOINHERIT LOGIN PASSWORD '{pgrst_db_password}';")

    # Grant the web_anon role to the authenticator role
    op.execute(f"GRANT {pgrst_db_anon_role} TO {pgrst_db_username};")


def downgrade() -> None:
    # Revoke the web_anon role from the authenticator role
    op.execute(f"REVOKE {pgrst_db_anon_role} FROM {pgrst_db_username};")

    # Drop the authenticator role
    op.execute(f"DROP ROLE {pgrst_db_username};")

    # Revoke permissions granted to the web_anon role
    op.execute(f"REVOKE SELECT ON {pgrst_db_schema}.todos FROM {pgrst_db_anon_role};")
    op.execute(f"REVOKE USAGE ON SCHEMA {pgrst_db_schema} FROM {pgrst_db_anon_role};")

    # Drop the web_anon role
    op.execute(f"DROP ROLE {pgrst_db_anon_role};")