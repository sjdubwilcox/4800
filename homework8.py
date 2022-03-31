




from scapy.all import DNS, DNSQR, IP, sr1, UDP import argparse  parser = argparse.ArgumentParser(description='DNS Query Example') parser.add_argument('query', help="Name to resolve", action="store") args= parser.parse_args()  dnsRequest = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=args.query))
dnsResponse= sr1(dnsRequest)
print(dnsResponse[DNS].summary())




















