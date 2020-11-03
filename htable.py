"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    return [[] for i in range(nbuckets)]

def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    if isinstance(o, int):
        return o
    elif isinstance(o, str):
        h = 0
        for c in o:
            h = h * 31 + ord(c)
        return h
    else:
        return None


def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    return hashcode(key) % len(table)


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """

    """
    why replace? because everytime the input value will be a new set of values
    don't care about waht was the old value, just replace it.
    that's what I think what does Parrt think about

    Plus, those associations (key-value pairs) are tuples, so you can't modify
    the values in any associations, so that's why the prompt said "replce" it!

    It's not a conept of "adding up", it's more like an "updating whole thing
    with new one"
    """
    # bucket_index = bucket_indexof(table, key)
    # if (key, value) in table[bucket_index]:
    #     table[bucket_index].remove((key, value))
    # table[bucket_index].append((key, value))
    bucket_index = bucket_indexof(table, key)
    print("key=", key, 'index=', bucket_index)
    for idx,asso in enumerate(table[bucket_index]):
        if asso[0] == key:
            asso_remove = table[bucket_index][idx]
            table[bucket_index].remove(asso_remove)
    table[bucket_index].append((key, value))


def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    bucket_index = bucket_indexof(table, key)
    bucket = table[bucket_index]
    for asso in bucket:
        if asso[0] == key:
            return asso[1]
    return None


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    s = ''
    for idx,bucket in enumerate(table):
        s += f"{idx:04}->"
        # {c:015,d}
        if bucket == []: # Edge case: empty bucket (empty list)
            s += "\n"
        else:
            for idx,asso in enumerate(bucket):
                if idx != len(bucket) - 1:
                    s += f"{asso[0]}:{asso[1]}, "
                else:
                    s += f"{asso[0]}:{asso[1]}\n"
    # print(s)
    return s


def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    s = '{'
    for bucket in table:
        for asso in bucket:
            s += f'{asso[0]}:{asso[1]}, '
    s = s.rstrip(', ') + '}'
    print(s)
    return s

if __name__ == '__main__':
    # # Test htable()
    #print(htable(5))

    # # Test hashcode()
    #print(hashcode('a'))

    # # Test htable_put()
    # table = htable(5)
    # print(table)
    # htable_put(table, 'parrt', [99])
    # print(table)
    # htable_put(table, 'parrt', [100])
    # print(table)
    # htable_put(table, 'parrt', [99])
    # print(table)


    # # Test htable_get()
    # table = htable(5)
    # print(table)
    # htable_put(table, 'ronald', {9, 3})
    # print(table)
    # htable_put(table, 'reagan', {17})
    # print(table)
    # print(htable_get(table, 'ronald'))
    # print(htable_get(table, 'kevin'))

    # # Test htable_buckets_str()
    # table = htable(5)
    # htable_buckets_str(table)
    # htable_put(table, 'ronald', {9, 3})
    # htable_buckets_str(table)
    # htable_put(table, 'reagan', {17})
    # htable_buckets_str(table)

    # Test htable_str()
    table = htable(5)
    htable_put(table, 'ronald', {9, 3})
    htable_put(table, 'reagan', {17})
    print(htable_str(table))
