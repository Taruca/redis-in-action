
import time
import unittest

'''
# <start id="simple-string-calls"/>
$ redis-cli                                 #A
redis 127.0.0.1:6379> set hello world       #D
OK                                          #E
redis 127.0.0.1:6379> get hello             #F
"world"                                     #G
redis 127.0.0.1:6379> del hello             #H
(integer) 1                                 #I
redis 127.0.0.1:6379> get hello             #J
(nil)
redis 127.0.0.1:6379> 
# <end id="simple-string-calls"/>
#A Start the redis-cli client up
#D Set the key 'hello' to the value 'world'
#E If a SET command succeeds, it returns 'OK', which turns into True on the Python side
#F Now get the value stored at the key 'hello'
#G It is still 'world', like we just set it
#H Let's delete the key/value pair
#I If there was a value to delete, DEL returns the number of items that were deleted
#J There is no more value, so trying to fetch the value returns nil, which turns into None on the Python side
#END
'''


'''
# <start id="simple-list-calls"/>
redis 127.0.0.1:6379> rpush list-key item   #A
(integer) 1                                 #A
redis 127.0.0.1:6379> rpush list-key item2  #A
(integer) 2                                 #A
redis 127.0.0.1:6379> rpush list-key item   #A
(integer) 3                                 #A
redis 127.0.0.1:6379> lrange list-key 0 -1  #B
1) "item"                                   #B
2) "item2"                                  #B
3) "item"                                   #B
redis 127.0.0.1:6379> lindex list-key 1     #C
"item2"                                     #C
redis 127.0.0.1:6379> lpop list-key         #D
"item"                                      #D
redis 127.0.0.1:6379> lrange list-key 0 -1  #D
1) "item2"                                  #D
2) "item"                                   #D
redis 127.0.0.1:6379> 
# <end id="simple-list-calls"/>
#A When we push items onto a LIST, the command returns the current length of the list
#B We can fetch the entire list by passing a range of 0 for the start index, and -1 for the last index
#C We can fetch individual items from the list with LINDEX
#D By popping an item from the list, it is no longer available
#END
'''


'''
# <start id="simple-set-calls"/>
redis 127.0.0.1:6379> sadd set-key item     #A
(integer) 1                                 #A
redis 127.0.0.1:6379> sadd set-key item2    #A
(integer) 1                                 #A
redis 127.0.0.1:6379> sadd set-key item3    #A
(integer) 1                                 #A
redis 127.0.0.1:6379> sadd set-key item     #A
(integer) 0                                 #A
redis 127.0.0.1:6379> smembers set-key      #B
1) "item"                                   #B
2) "item2"                                  #B
3) "item3"                                  #B
redis 127.0.0.1:6379> sismember set-key item4   #C
(integer) 0                                     #C
redis 127.0.0.1:6379> sismember set-key item    #C
(integer) 1                                     #C
redis 127.0.0.1:6379> srem set-key item2    #D
(integer) 1                                 #D
redis 127.0.0.1:6379> srem set-key item2    #D
(integer) 0                                 #D
redis 127.0.0.1:6379>  smembers set-key
1) "item"
2) "item3"
redis 127.0.0.1:6379> 
# <end id="simple-set-calls"/>
#A When adding an item to a SET, Redis will return a 1 if the item is new to the set and 0 if it was already in the SET
#B We can fetch all of the items in the SET, which returns them as a sequence of items, which is turned into a Python set from Python
#C We can also ask Redis whether an item is in the SET, which turns into a boolean in Python
#D When we attempt to remove items, our commands return the number of items that were removed
#END
'''


'''
# <start id="simple-hash-calls"/>
redis 127.0.0.1:6379> hset hash-key sub-key1 value1 #A
(integer) 1                                         #A
redis 127.0.0.1:6379> hset hash-key sub-key2 value2 #A
(integer) 1                                         #A
redis 127.0.0.1:6379> hset hash-key sub-key1 value1 #A
(integer) 0                                         #A
redis 127.0.0.1:6379> hgetall hash-key              #B
1) "sub-key1"                                       #B
2) "value1"                                         #B
3) "sub-key2"                                       #B
4) "value2"                                         #B
redis 127.0.0.1:6379> hdel hash-key sub-key2        #C
(integer) 1                                         #C
redis 127.0.0.1:6379> hdel hash-key sub-key2        #C
(integer) 0                                         #C
redis 127.0.0.1:6379> hget hash-key sub-key1        #D
"value1"                                            #D
redis 127.0.0.1:6379> hgetall hash-key
1) "sub-key1"
2) "value1"
# <end id="simple-hash-calls"/>
#A When we add items to a hash, again we get a return value that tells us whether the item is new in the hash
#B We can fetch all of the items in the HASH, which gets translated into a dictionary on the Python side of things
#C When we delete items from the hash, the command returns whether the item was there before we tried to remove it
#D We can also fetch individual fields from hashes
#END
'''


'''
# <start id="simple-zset-calls"/>
redis 127.0.0.1:6379> zadd zset-key 728 member1     #A
(integer) 1                                         #A
redis 127.0.0.1:6379> zadd zset-key 982 member0     #A
(integer) 1                                         #A
redis 127.0.0.1:6379> zadd zset-key 982 member0     #A
(integer) 0                                         #A
redis 127.0.0.1:6379> zrange zset-key 0 -1 withscores   #B
1) "member1"                                            #B
2) "728"                                                #B
3) "member0"                                            #B
4) "982"                                                #B
redis 127.0.0.1:6379> zrangebyscore zset-key 0 800 withscores   #C
1) "member1"                                                    #C
2) "728"                                                        #C
redis 127.0.0.1:6379> zrem zset-key member1     #D
(integer) 1                                     #D
redis 127.0.0.1:6379> zrem zset-key member1     #D
(integer) 0                                     #D
redis 127.0.0.1:6379> zrange zset-key 0 -1 withscores
1) "member0"
2) "982"
# <end id="simple-zset-calls"/>
#A When we add items to a ZSET, the the command returns the number of new items
#B We can fetch all of the items in the ZSET, which are ordered by the scores, and scores are turned into floats in Python
#C We can also fetch a subsequence of items based on their scores
#D When we remove items, we again find the number of items that were removed
#END
'''