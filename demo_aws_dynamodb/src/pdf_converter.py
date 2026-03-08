import base64

def convert_pdf_to_binary(file_path):
    """
    Convert a PDF file to binary data.
    
    :param file_path: Path to the PDF file.
    :return: Binary data of the PDF file.
    """
    with open(file_path, "rb") as pdf_file:
        binary_data = pdf_file.read()

    return binary_data



if __name__ == "__main__":
    # Example usage
    file_path = "../data/artifact_001.pdf"
    binary_data = convert_pdf_to_binary(file_path)

    # print(binary_data)
    # Encode binary data to base64
    base64_encoded_data = base64.b64encode(binary_data)
    

    print(base64_encoded_data)
    
    # Decode base64 data back to binary
    # decoded_data = base64.b64decode(base64_encoded_data)
    
    # # Save the decoded data to a new PDF file
    # with open("../test_files/decoded_test_2.pdf", "wb") as pdf_file:
    #     pdf_file.write(decoded_data)