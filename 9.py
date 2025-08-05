from collections import defaultdict

def analyze_log(file_path):
    ip_count = defaultdict(int)
    url_count = defaultdict(int)
    response_count = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) < 9:
                continue
            ip = parts[0]
            url = parts[6]
            code = parts[8]

            ip_count[ip] += 1
            url_count[url] += 1
            response_count[code] += 1

    print("Top IPs:", sorted(ip_count.items(), key=lambda x: -x[1])[:5])
    print("Top URLs:", sorted(url_count.items(), key=lambda x: -x[1])[:5])
    print("Response Codes:", response_count)

