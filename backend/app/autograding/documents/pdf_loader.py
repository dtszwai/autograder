import uuid
import requests
from typing import Optional
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def download_pdf(
    url: str,
    *,
    filename: str = str(uuid.uuid4()),
    sub_dirs: Optional[list[str]] = None,
) -> Path:
    """
    Downloads a PDF from the given URL and saves it in the 'downloads' directory.
    Optionally, additional subdirectories can be specified.

    Args:
        url (str): The URL of the PDF to download.
        filename (str): The name of the downloaded PDF file. Defaults to a random UUID.
        sub_dirs (Optional[str]): Additional subdirectories under 'downloads' to save the PDF.
                                  For example, 'reports/2024' will create 'downloads/reports/2024'.
                                  Defaults to None.
        apply_data_masking (bool): Whether to apply data masking to the PDF content.

    Returns:
        Path: The path to the downloaded PDF file.

    Raises:
        RuntimeError: If the download fails or the URL does not point to a PDF.
    """
    root_download_dir = Path("downloads")

    download_path = (
        root_download_dir / "/".join(sub_dirs) if sub_dirs else root_download_dir
    )
    download_path.mkdir(parents=True, exist_ok=True)

    file_name = filename if filename.endswith(".pdf") else f"{filename}.pdf"
    file_path = download_path / file_name

    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "").lower()
        if "application/pdf" not in content_type:
            raise ValueError("URL does not point to a PDF file")

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        return file_path

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to download PDF from {url}") from e
    except IOError as e:
        raise RuntimeError(f"Failed to write PDF to {file_path}") from e
    except Exception as e:
        raise RuntimeError(f"Invalid PDF file at {url}") from e


def load_pdf(pdf_path: Path, extract_text: bool = False):
    """
    Loads the PDF from the specified path.

    If `extract_text` is True, returns the concatenated text content.
    Otherwise, returns the PyPDFLoader instance for further processing.
    """
    loader = PyPDFLoader(str(pdf_path))
    if extract_text:
        documents = loader.load()
        full_text = "\n".join(doc.page_content for doc in documents)
        return full_text
    return loader
