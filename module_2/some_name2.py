class FileManager:
    """Class responsible for file operations.
    
    SRP: This class has the single responsibility of handling file read/write
    operations.
    """
    
    @staticmethod
    def read_urls_from_file(file_path):
        """Read URLs from a file and return as a list.
        
        Args:
            file_path (str): The path to the file containing URLs.
        
        Returns:
            list: A list of URLs read from the file.
        """
        with open(file_path, 'r') as file:
            return file.readlines()
    
    @staticmethod
    def write_content_to_file(content, file_path):
        """Write content to a file.
        
        Args:
            content (str): The content to write to the file.
            file_path (str): The path to the file where content is to be written.
        """
        with open(file_path, 'w') as file:
            file.write(content)
