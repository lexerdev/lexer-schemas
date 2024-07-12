from lexer_schemas.all import all_api_names

if __name__ == "__main__":
    for api_name, schema_class in all_api_names.items():
        with open(f"jsonschema/{api_name}.json", "w") as out:
            out.write(schema_class.schema_json(indent=2))
