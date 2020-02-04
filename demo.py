from jsonpath_rw import parse
import json

def read_petstore_openapi():
    with open("petstore.json", "r") as f:
        return json.load(f)

petstore = read_petstore_openapi()

def _get_match(jsonpath: str, obj):
    expr = parse(jsonpath)
    return expr.find(obj)

def get_multiple(jsonpath: str, obj):
    parse_result = _get_match(jsonpath, obj)
    return [match.value for match in parse_result]

def get_single_value(jsonpath: str, obj):
    return get_multiple(jsonpath, obj)[0]

def main():
    title = get_single_value("info.title", petstore)
    server_urls = get_multiple("servers[*].url", petstore)
    summaries = get_multiple("paths.'/pets'..summary", petstore)

    print("Title: {title}".format(title=title))
    print("Server URLs: {urls}".format(urls=', '.join(server_urls)))
    print("Summaries of operations in /pets: {ops}".format(ops=', '.join(summaries)))



if __name__ == '__main__':
    main()