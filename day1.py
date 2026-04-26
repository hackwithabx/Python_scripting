headers = ["Content-Security-Policy", "X-Frame-Options","Strict-Transport-Security","X-Content-Type-Options","Referer-Policy"]

#for header in headers:
   # print("checking-headers:",header)


server_response = {
    "Content-Security-Policy": "default-src 'self'",
    "X-Frame-Options": "DENY",
    "Strict-Transport-Security": "max-age=31536000"

}

for header in headers:
    if header in server_response:
        print("[OK] " + header)
    else:
        print("[MISSING] " + header )

with open("headers_audit.txt","w") as f:
    for header in headers:
        if header in server_response:
            f.write("[OK] " +header + "\n")
        else:
            f.write("[MISSING] " +header + "\n")            