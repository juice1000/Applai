from custom_types import ColumnInfo, TableSchema
from libs.db.init_db import engine
from libs.logger.init_logger import logger
from sqlalchemy import text
from sqlmodel import Session, text


def add_field_to_table(field_name: str, field_type: str):
    """
    Add a new nullable field to the Jobs table
    Args:
        field_name (str): Name of the new field
        field_type (str): SQL type of the field (e.g., 'TEXT', 'INTEGER', 'BOOLEAN')
    """
    logger.info(
        f"Adding nullable field {field_name} of type {field_type} to Jobs table..."
    )

    if not engine:
        raise Exception("No Engine for DB found")

    try:
        with Session(engine) as session:
            # Create the ALTER TABLE statement with NULL constraint
            alter_statement = text(
                f"ALTER TABLE job ADD COLUMN {field_name} {field_type} NULL"
            )
            session.exec(alter_statement)
            session.commit()
            logger.info(f"Successfully added nullable field {field_name} to Jobs table")
    except Exception as e:
        logger.error(f"Error adding field to table: {str(e)}")
        raise Exception(f"Failed to add field: {str(e)}")


def get_table_schema():
    """Get the schema of the jobs table"""
    if not engine:
        raise Exception("No Engine for DB found")

    with Session(engine) as session:
        result = session.execute(text("PRAGMA table_info(job)")).fetchall()

        columns = [
            ColumnInfo(
                name=row[1],
                type=row[2],
                notnull=bool(row[3]),
            )
            for row in result
        ]

        return TableSchema(columns=columns)
