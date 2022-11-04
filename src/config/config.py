class ConfigSingleton:

    __single = None 
    
    def __init__(self, input_scheme_path: str = "./input_schema.json", output_scheme_path: str = "./output_schema.json"):
        if not ConfigSingleton.__single:
            self.input_scheme: Dict = self.load_scheme_file(input_scheme_path, "input scheme file")
            self.output_scheme: Dict = self.load_scheme_file(output_scheme_path, "output scheme file")
        
    @staticmethod()
    def load_scheme_file(scheme_path: str, error_message: str | null = "") -> dict:
        try:
            with open(scheme_path, 'r') as f:
                return json.loads(f.read())
        except:
            raise Exception(f"[ERROR] {error_message} not found")
