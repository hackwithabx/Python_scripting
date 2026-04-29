import requests
import sys

required_headers =[
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "Referer-Policy"
]

with open("urls.txt","r") as f:
    urls = [line.strip() for line in f if line.strip()]

for url in urls:
    print("checking :"+ url)
    print("--------------------")

    try:
        response = requests.get(url, timeout=5)
        server_headers = response.headers
    except requests.exceptions.RequestException:
        print("[ERROR] Could not connect to " + url)
        print("----------------------------\n")
        continue

    results =[]
    for header in required_headers:
        if header in server_headers:
            results.append("[OK] " + header)
        else:
            results.append("[MISSING] " + header)

    for result in results:
        print(result)

    #print("----------------------------")                

    with open("report.txt","a") as f:
        f.write("URL: " + url + "\n")
        f.write("---------------------\n")
        for result in results:
            f.write(result + "\n")
        f.write("\n")

    print("----------------------------\n")

print("Report saved to report.txt")    