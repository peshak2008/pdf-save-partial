from PyPDF2 import PdfReader, PdfWriter

def main():
    def save_selected_pages(source_file, pages):
        """
        Extracts selected pages from the source PDF and saves them into a new PDF file.
        
        Args:
        source_file (str): The path to the source PDF file.
        pages (list of int): The list of pages to include in the new PDF.
        """
        # Create a PDF reader object
        reader = PdfReader(source_file)

        # Check if any selected pages are out of range
        num_pages = len(reader.pages)
        if any(page < 1 or page > num_pages for page in pages):
            print(f"Error: Some pages are out of range. The PDF has {num_pages} pages.")
            return
        
        # Determine the target file name
        target_file = source_file.replace('.pdf', '_partial.pdf')
        
        # Create a PDF writer object
        writer = PdfWriter()
        
        # Add the selected pages to the writer
        for page_number in pages:
            writer.add_page(reader.pages[page_number-1])
        
        # Write out the new PDF
        with open(target_file, "wb") as f:
            writer.write(f)
        print(f"Selected pages have been saved to {target_file}")

    # Ask user for the source PDF location
    source_pdf = input("Enter the path to the source PDF file: ")
    
    # Ask user for the page numbers
    page_numbers_input = input("Enter the page numbers to include (e.g., 1,3,5 or 1-5): ")
    
    # Process the input to handle ranges and individual numbers
    selected_pages = []
    for part in page_numbers_input.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            selected_pages.extend(range(start, end + 1))
        else:
            selected_pages.append(int(part))
    
    # Remove duplicates and sort the pages
    selected_pages = sorted(set(selected_pages))
    
    # Call the function with user inputs
    save_selected_pages(source_pdf, selected_pages)


if __name__ == "__main__":
    main()