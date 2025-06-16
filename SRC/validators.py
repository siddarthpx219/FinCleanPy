import pandera as pa

def validate_schema(df, schema):
    schema.validate(df)
    return True
