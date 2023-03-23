from urllib.parse import urlparse
import os

def get_name(raw_input):
    # The parser requires a scheme
    if "://" not in raw_input:
        raw_input = 'http://' + raw_input

    input_arg = urlparse(raw_input)
    domain = input_arg.netloc
    domain_without_www = domain.replace('www.', '')
    segments = domain_without_www.split('.')
    return segments[0] if len(segments) == 1 else '.'.join(segments[0:-1])

if __name__ == "__main__":
    print(get_name(os.environ['URL']))
