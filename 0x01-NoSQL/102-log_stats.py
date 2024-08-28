#!/usr/bin/env python3
"""
A Python script that provides some stats about Nginx logs stored in MongoDB
and the top 10 of the most present IPs in the collection logs.nginx
"""


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    docs_count = logs.count_documents({})
    get_count = logs.count_documents({"method": "GET"})
    post_count = logs.count_documents({"method": "POST"})
    put_count = logs.count_documents({"method": "PUT"})
    patch_count = logs.count_documents({"method": "PATCH"})
    delete_count = logs.count_documents({"method": "DELETE"})
    status_check = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{docs_count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_count}")
    print(f"\tmethod POST: {post_count}")
    print(f"\tmethod PUT: {put_count}")
    print(f"\tmethod PATCH: {patch_count}")
    print(f"\tmethod DELETE: {delete_count}")
    print(f"{status_check} status check")
    print("IPs:")
    ips = logs.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
