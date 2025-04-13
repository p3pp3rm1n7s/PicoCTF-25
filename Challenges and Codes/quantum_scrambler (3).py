# import ast

# def unscramble():
#     # Read the scrambled data from output.txt
#     with open(r'C:\Users\Shawf\Downloads\output.txt', 'r') as f:
#         scrambled_data = ast.literal_eval(f.read().strip())
    
#     # Initialize list to store the recovered hex values in order
#     hex_values = []
    
#     # We need to extract all hex strings from the nested structure
#     def extract_hex_values(data):
#         if isinstance(data, list):
#             for item in data:
#                 if isinstance(item, str) and item.startswith("0x"):
#                     hex_values.append(item)
#                 elif isinstance(item, list):
#                     extract_hex_values(item)
    
#     # Extract all hex values from the scrambled structure
#     extract_hex_values(scrambled_data)
    
#     # Convert hex values back to characters
#     flag = ""
#     for hex_val in hex_values:
#         flag += chr(int(hex_val, 16))
    
#     return flag

# # Example usage
# if __name__ == '__main__':
#     decrypted_flag = unscramble()
#     print(decrypted_flag)
# import ast

# def unscramble():
#     # Read the scrambled data from output.txt
#     with open(r'C:\Users\Shawf\Downloads\output.txt', 'r') as f:
#         scrambled_data = ast.literal_eval(f.read().strip())
    
#     # Print each item in the outer list on a separate line
#     print("Outer list items:")
#     for i, item in enumerate(scrambled_data):
#         print(f"Item {i}: {item}")
#     print("-------------------")
    
#     # Initialize list to store the recovered hex values in order
#     hex_values = []
    
#     # We need to extract all hex strings from the nested structure
#     def extract_hex_values(data):
#         if isinstance(data, list):
#             for item in data:
#                 if isinstance(item, str) and item.startswith("0x"):
#                     hex_values.append(item)
#                 elif isinstance(item, list):
#                     extract_hex_values(item)
    
#     # Extract all hex values from the scrambled structure
#     extract_hex_values(scrambled_data)
    
#     # Convert hex values back to characters
#     flag = ""
#     for hex_val in hex_values:
#         flag += chr(int(hex_val, 16))
    
#     return flag

# # Example usage
# if __name__ == '__main__':
#     decrypted_flag = unscramble()
#     print(decrypted_flag)
import ast

def unscramble():
    # Read the scrambled data from output.txt
    with open(r'C:\Users\Shawf\Downloads\output.txt', 'r') as f:
        scrambled_data = ast.literal_eval(f.read().strip())
    
    # Print each item in the outer list on a separate line
    print("Outer list items:")
    for i, item in enumerate(scrambled_data):
        print(f"Item {i}: {item}")
    print("-------------------")
    
    # Initialize list to store the recovered hex values in order
    hex_values = []
    
    # We need to extract all hex strings from the nested structure
    def extract_hex_values(data):
        if isinstance(data, list):
            for item in data:
                if isinstance(item, str) and item.startswith("0x"):
                    hex_values.append(item)
                elif isinstance(item, list):
                    extract_hex_values(item)
    
    # Extract all hex values from the scrambled structure
    extract_hex_values(scrambled_data)
    
    # Convert hex values back to characters
    flag = ""
    for hex_val in hex_values:
        flag += chr(int(hex_val, 16))
    
    return flag

# Example usage
if __name__ == '__main__':
    decrypted_flag = unscramble()
    
    # Print the full decrypted flag
    print("Full flag:", decrypted_flag)
    
    # Filter out characters from "picoCTF" (case sensitive)
    filter_chars = "picoCTF{}"
    filtered_content = ''.join(char for char in decrypted_flag if char not in filter_chars)
    
    # Print only the characters not in "picoCTF"
    print("Content not in picoCTF:", filtered_content)