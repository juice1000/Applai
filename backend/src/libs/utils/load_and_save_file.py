from os import makedirs
from os.path import abspath, dirname, exists, join

from langchain_chroma import Chroma
from libs.llm.init_llm import init_embedding_function

CUR_DIR = dirname(abspath(__file__))
ROOT_DIR = abspath(join(CUR_DIR, "..", "..", ".."))
CHROMA_PATH = join(ROOT_DIR, "chroma")
CHROMA_PATH_DE = join(ROOT_DIR, "chroma_de")
DATA_PATH = join(ROOT_DIR, "data")
INPUT_PATH = join(DATA_PATH, "input")
COVER_LETTERS_PATH = join(DATA_PATH, "cover_letters")


# LOAD FILES
def check_file_exists(file_path: str) -> bool:
    if not exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return True


def get_data_file_path(file_path: str) -> str:
    # Construct the absolute path to the file
    absolute_path = join(DATA_PATH, file_path)
    check_file_exists(absolute_path)
    return absolute_path


def get_input_file_path(file_path: str) -> str:
    # Construct the absolute path to the file
    absolute_path = join(INPUT_PATH, file_path)
    check_file_exists(absolute_path)
    return absolute_path


def get_cover_letters_file_path(file_path: str) -> str:
    # Construct the absolute path to the file
    absolute_path = join(COVER_LETTERS_PATH, file_path)

    check_file_exists(absolute_path)
    return absolute_path


def get_vector_db_path(language: str = "en") -> str:
    if language == "de":
        db_path = CHROMA_PATH_DE
    else:
        db_path = CHROMA_PATH

    check_file_exists(db_path)
    return db_path


def load_vector_db(language: str = "en"):
    db_path = get_vector_db_path(language)
    return Chroma(
        persist_directory=db_path,
        embedding_function=init_embedding_function(),
    )


##################
# SAVE FILES


def save_file_to_data(file_path: str, content: str) -> None:
    """
    Save the given content to a file in the data directory.
    """
    # Construct the absolute path to the file
    absolute_path = join(DATA_PATH, file_path)

    # Create the directory if it doesn't exist
    makedirs(dirname(absolute_path), exist_ok=True)

    # Write the content to the file
    with open(absolute_path, "wb") as f:
        f.write(content)
