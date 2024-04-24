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
