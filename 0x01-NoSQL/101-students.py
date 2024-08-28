#!/usr/bin/env python3
"""
This module containes a Python function that
returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    studens = [
        {
            "$project":
            {
                "name": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort":
            {"averageScore": -1}
        }
    ]
    return mongo_collection.aggregate(studens)
