import json
import re
import sys

def validate_config(config):
    # 检查字段是否存在并且满足要求
    required_fields = ["name", "description", "type", "status", "id", "version"]
    
    for field in required_fields:
        if field not in config:
            return f"Missing required field: {field}"
    
    # 检查 `name` 和 `description`
    if not isinstance(config['name'], str) or not config['name']:
        return "Invalid 'name': should be a non-empty string"
    
    if not isinstance(config['description'], str):
        return "Invalid 'description': should be a string"
    
    # 检查 `type`
    if config['type'] not in ["OS", "CPU"]:
        return "Invalid 'type': should be either 'OS' or 'CPU'"
    
    # 检查 `status`
    if config['status'] not in ["open", "closed"]:
        return "Invalid 'status': should be either 'open' or 'closed'"
    
    # 检查 `id`
    if not isinstance(config['id'], str) or ' ' in config['id']:
        return "Invalid 'id': should be a string without spaces"
    
    # 检查 `version`
    if not isinstance(config['version'], int) or config['version'] <= 0:
        return "Invalid 'version': should be a positive integer"
    
    # TODO: 检查 `auto_grade` 字段
    
    return None

def main():
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading config.json: {e}")
        sys.exit(1)

    # 验证配置文件
    error = validate_config(config)
    if error:
        print(f"[!] Validation error: {error}")
        sys.exit(1)
    
    print("config.json is valid.")
    sys.exit(0)

if __name__ == "__main__":
    main()