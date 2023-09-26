def parse_encoded_string(encoded_string):
    parts = encoded_string.split('0')  
    parts = [part for part in parts if part]
    
    if len(parts) >= 2:
        
        first_name = parts[0]
        
        
        id_str = parts[-1]
        
        
        last_name_parts = parts[1:-1]
        
        
        last_name = ' '.join(last_name_parts)
        
        return {
            "first_name": first_name,
            "last_name": last_name,
            "id": id_str
        }
    else:
        
        return None


encoded_string = input("Enter the encoded string: ")
result = parse_encoded_string(encoded_string)
if result:
    print(result)
else:
    print("Invalid encoded string format.")
