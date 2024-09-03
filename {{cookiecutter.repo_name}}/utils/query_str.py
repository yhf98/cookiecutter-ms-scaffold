from typing import Dict, Optional
from urllib.parse import parse_qs

class QueryStringParser:
    def __init__(self, query_string: str):
        self.query_string = query_string
        self.parsed_data = self._parse_query_string()

    def _parse_query_string(self) -> Dict[str, str]:
        parsed = parse_qs(self.query_string)
        return {k: v[0] for k, v in parsed.items()}

    def get_value(self, key: str) -> Optional[str]:
        return self.parsed_data.get(key)

if __name__ == "__main__":
    # 使用示例
    query_string = "apikey=123e&name=angular"
    parser = QueryStringParser(query_string)

    apikey_value = parser.get_value("apikey")
    name_value = parser.get_value("name")

    print(f"apikey: {apikey_value}")  # 输出: apikey: 123e
    print(f"name: {name_value}")  # 输出: name: angular
