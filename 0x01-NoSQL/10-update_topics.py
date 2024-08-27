#!/usr/bin/env python3
"""
This module conatines a function that updates a document in a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates a document in a collection based on kwargs
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
