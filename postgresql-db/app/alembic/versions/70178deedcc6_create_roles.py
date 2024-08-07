"""create-roles

Revision ID: 70178deedcc6
Revises: a70417660f36
Create Date: 2024-07-31 20:01:13.151669

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70178deedcc6'
down_revision: Union[str, None] = 'a70417660f36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass
    # Create the web_anon role
    op.execute("CREATE ROLE web_anon NOLOGIN;")

    # Grant usage on the schema api to web_anon
    op.execute("GRANT USAGE ON SCHEMA api TO web_anon;")

    # Grant select on the table api.todos to web_anon
    op.execute("GRANT SELECT ON api.todos TO web_anon;")

    # Create the authenticator role with a password and NOINHERIT attribute
    op.execute("CREATE ROLE authenticator NOINHERIT LOGIN PASSWORD 'mysecretpassword';")

    # Grant the web_anon role to the authenticator role
    op.execute("GRANT web_anon TO authenticator;")


def downgrade() -> None:
    # Revoke the web_anon role from the authenticator role
    op.execute("REVOKE web_anon FROM authenticator;")

    # Drop the authenticator role
    op.execute("DROP ROLE authenticator;")

    # Revoke permissions granted to the web_anon role
    op.execute("REVOKE SELECT ON api.todos FROM web_anon;")
    op.execute("REVOKE USAGE ON SCHEMA api FROM web_anon;")

    # Drop the web_anon role
    op.execute("DROP ROLE web_anon;")