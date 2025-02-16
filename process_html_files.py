import pandas as pd
from typing import List, Tuple

# List to store extracted tables
dfs: List[pd.DataFrame] = []

def get_table_data(file_path: str, approx_start: int = 862, approx_end: int = 10683) -> str:
    """
    Extracts the HTML table section from a file.

    Args:
        file_path (str): Path to the file containing the HTML content.
        approx_start (int): Approximate starting line to search for the <table> tag.
        approx_end (int): Approximate ending line to search for the </table> tag.

    Returns:
        str: Extracted HTML table as a string.
    """
    table_start_line = 0
    table_end_line = 0

    # Read the file contents
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.readlines()

    # Ensure start and end positions are within bounds
    approx_start = min(approx_start, len(data) - 1)
    approx_end = min(approx_end, len(data) - 1)

    # Find the actual start of the table
    for line_no in range(approx_start, len(data)):
        if "<table" in data[line_no]:
            table_start_line = line_no
            break

    # Find the actual end of the table
    for line_no in range(approx_end, 0, -1):
        if "</table" in data[line_no]:
            table_end_line = line_no
            break

    # Extract table data
    table_data = data[table_start_line : table_end_line + 1]
    
    return "\n".join(table_data)

def process_files(input_dir: str, output_csv: str, file_count: int = 101) -> None:
    """
    Processes multiple files, extracts tables, and combines them into a single CSV.

    Args:
        input_dir (str): Directory containing the input files.
        output_csv (str): Path where the combined CSV should be saved.
        file_count (int): Number of files to process.
    """
    for file_num in range(1, file_count + 1):
        file_path = f"{input_dir}/page_{file_num}.html"
        print(f"Processing file {file_num}...")

        try:
            # Extract table HTML
            table_data = get_table_data(file_path)

            # Read table into DataFrame
            tables = pd.read_html(table_data)
            if tables:
                dfs.append(tables[0])

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    if not dfs:
        print("No tables were extracted. Exiting.")
        return

    # Combine all tables into one DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # Rename columns
    combined_df.rename(columns={"Unnamed: 0": "Time Control"}, inplace=True)

    # Remove unwanted column if it exists
    combined_df.drop(columns=["Unnamed: 6"], errors="ignore", inplace=True)

    # Save to CSV
    combined_df.to_csv(output_csv, index=False)
    print(f"Data successfully saved to {output_csv}")

if __name__ == "__main__":
    # Define paths (modify as needed before running)
    INPUT_DIRECTORY = "path/to/chess_games"
    OUTPUT_CSV = "path/to/output/combined_tables.csv"

    # Process files
    process_files(INPUT_DIRECTORY, OUTPUT_CSV)
