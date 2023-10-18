import os

# Cloud api details
KAFKA_API_KEY = os.getenv('KAFKA_API_KEY',None)
KAFKA_API_SECRET_KEY = os.getenv('KAFKA_API_SECRET_KEY',None)
KAFKA_BOOTSTRAP_SERVER = os.getenv('KAFKA_BOOTSTRAP_SERVER',None)

# Authenticatio related variables
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL','SASL_SSL')
SSL_MECHANISM = os.getenv('SSL_MECHANISM','PLAIN')

# Schema related variables
KAFKA_SCHEMA_URL = os.getenv('KAFKA_SCHEMA_URL','None')
KAFKA_SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY','None')
KAFKA_SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET','None')

def sasl_conf():
    sasl_conf = {
        'sasl_mechanism': SSL_MECHANISM,
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVER,
        'security.protocol': SECURITY_PROTOCOL,
        'sasl.username': KAFKA_API_KEY,
        'sasl.password': KAFKA_API_SECRET_KEY
    }
    print(sasl_conf)
    return sasl_conf

def schema_config():
    schema_conf =  {
        'url':KAFKA_SCHEMA_URL,
        'basic.auth.user.info': f'{KAFKA_SCHEMA_REGISTRY_API_KEY}:{KAFKA_SCHEMA_REGISTRY_API_SECRET}'
    }
    print(schema_conf)
    return schema_conf

if __name__ == '__main__':
    sasl_conf()
    schema_config()