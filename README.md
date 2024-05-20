# 📂 CSV File Chunker

This Python script reads a large CSV file and splits it into smaller chunks. Each chunk retains the header from the original CSV file. 📈➡️📉

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### 🛠️ Prerequisites

- **Python**: Ensure Python is installed on your system. Download it from the official [Python website](https://www.python.org/).
- **Pandas**: Install the Pandas library using pip:

    ```
    pip install pandas
    ```

### 📥 Installing

1. **Clone the repository** to your local machine:

    ```
    git clone https://github.com/ufumzy/CSV-File-Chunker.git
    ```

2. **Navigate to the project directory**:

    ```
    cd CSV-File-Chunker
    ```

### ▶️ Usage

1. **Specify the path to your large CSV file**: Open the script `test.py` and set the `csv_file_path` variable to the path of your large CSV file.

    ```
    def main():
        # Specify the path to the CSV file
        csv_file_path = "path/to/your/large.csv"
    
        print("Processing CSV file and splitting into chunks...")
        process_csv_file(csv_file_path)
        print("Processing completed.")
    ```

2. **Run the script**:

    ```
    python test.py
    ```

### 🔍 Example

If your large CSV file is located at `/data/largefile.csv`, modify the `csv_file_path` variable in `test.py`:

```
def main():
    # Specify the path to the CSV file
    csv_file_path = "/data/largefile.csv"

    print("Processing CSV file and splitting into chunks...")
    process_csv_file(csv_file_path)
    print("Processing completed.")
```

Then run the script:

```
python test.py
```

This will create smaller chunk files in the same directory, each retaining the header from the original CSV file.

### 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### ✨ Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

---

Happy chunking! 🍰✨

---

## 🧑‍💻 Code Overview

Here's a brief overview of the code used in this project:
python
```
import pandas as pd

# Function to process the CSV file and split it into chunks
def process_csv_file(file_path):
    try:
        # Initialize variables
        chunk_size = 1000
        header = None
        
        # Read the CSV file in chunks
        reader = pd.read_csv(file_path, chunksize=chunk_size)
        
        # Read the first chunk to get the header
        first_chunk = next(reader)
        header = first_chunk.columns.tolist()
        first_chunk.to_csv('first_chunk.csv', index=False)  # Save the first chunk
            
        # Iterate through the remaining chunks
        chunk_number = 2
        for chunk in reader:
            # Save each chunk with the header
            chunk.to_csv(f'chunk_{chunk_number}.csv', index=False, header=header)
            chunk_number += 1
        
        print("CSV file split into chunks successfully.")
            
    except Exception as e:
        print("An error occurred:", e)

def main():
    # Specify the path to the CSV file
    csv_file_path = "data.csv"

    print("Processing CSV file and splitting into chunks...")
    process_csv_file(csv_file_path)
    print("Processing completed.")

if __name__ == "__main__":
    main()
```

### 📝 Explanation

1. **Imports**: The script uses the Pandas library for reading and writing CSV files.
2. **process_csv_file(file_path)**: This function processes the CSV file specified by `file_path` and splits it into chunks of 1000 rows each.
3. **Main Function**: The `main()` function sets the path to the CSV file and calls `process_csv_file()`.
4. **Execution**: When the script is run, it processes the CSV file and creates smaller chunk files with the same header.

