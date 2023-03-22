# -*- coding: utf-8 -*-
"""Week 8 Practice Notebook: Deleting data from Redis - Breakout 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FyWZCbsJGwPiVgYHKnkh61YLK8w1R4-6

# Practice Notebook: Deleting data from Redis
"""

!pip install redis

"""## Challenge 1

Write a Python function that deletes a given key from a Redis instance on Redis Lab. The function should take two arguments: the Redis instance URL and the key to be deleted. The function should use the delete() method to delete the key from the Redis instance.

Hints:

* You will need to use the Redis library for Python. You can install it using pip by running pip install redis.
* You will need to create a Redis client object using the Redis URL provided in the function argument.
* You can then use the delete() method of the Redis client object to delete the key.
"""

# Your code goes here
#import librarie

import redis

#connect to redis
r = redis.Redis(
  host='redis-15919.c91.us-east-1-3.ec2.cloud.redislabs.com',
  port=15919,
  password='nVmHZlngfY9h61SwlkrcIsk8VF4ukWe4')
  

#function
def delete_key(redis_instance, key):
  #add strings
  redis_instance.set('key1', "value1")
  redis_instance.set('key2', "value2")
  redis_instance.set('key3', "value3")
  #delete record
  redis_instance.delete(key)

  values = redis_instance.get(key)

  return(values)

delete_key(r,'key1')

def delete_keys(redis_instance, keys):
  # Add key-value pairs
  redis_instance.set('key1', 'value1')
  redis_instance.set('key2', 'value2')
  redis_instance.set('key3', 'value3')

  # Delete keys
  redis_instance.delete(keys)

  # Retrieve all remaining keys
  remaining_keys = redis_instance.keys('*')

  # Retrieve values of remaining keys
  values = [redis_instance.mget(key) for key in remaining_keys]

  return values

delete_keys(r,'key1')

def delete_key(redis_instance, key):
  # add some keys
  redis_instance.set('key1', "value1")
  redis_instance.set('key2', "value2")
  redis_instance.set('key3', "value3")
  
  # delete the key
  redis_instance.delete(key)
  
  # get all the values in the Redis database
  all_values = redis_instance.mget(redis_instance.keys('*'))
  
  # return the values
  return all_values

result = delete_key(r, 'key1')
print(result)  # prints the list of all values in the Redis database

"""### Sample Solution"""

import redis

def delete_key(redis_url, key):
    client = redis.from_url(redis_url)
    client.delete(key)

# Example usage
redis_url = 'redis://localhost:6379/0'
key_to_delete = 'mykey'
delete_key(redis_url, key_to_delete)

"""## Challenge 2

Write a Python function that deletes a given field from a Redis hash on Redis Lab. The function should take three arguments: the Redis instance URL, the name of the hash, and the name of the field to be deleted. The function should use the hdel() method to delete the field from the Redis hash.

Hints:

* You will need to use the Redis library for Python. You can install it using pip by running pip install redis.
* You will need to create a Redis client object using the Redis URL provided in the function argument.
* You can then use the hdel() method of the Redis client object to delete the field from the Redis hash.
"""

# Your code goes here

def delete_from_hash(redis_instance, hash_name, field):
  #add some records
  redis_instance.hset("EK1200", "name","Anyira")
  redis_instance.hset("EK1200", "age","12")
  redis_instance.hset("EK1200", "dept","Big Data")
  redis_instance.hset("EK1200", "mobile","0722000000")

  redis_instance.hset("EK1270", "name","Mumbo")
  redis_instance.hset("EK1270", "age","120")
  redis_instance.hset("EK1270", "dept","Fixed Data")
  redis_instance.hset("EK1270", "mobile","0722000001")
  
  #delete
  redis_instance.hdel(hash_name, field)

  #get all the records
  remaining_data = redis_instance.hgetall('EK1200')
  return(remaining_data)

#call the function
delete_from_hash(r, 'EK1200', 'age')

def add_person(redis_instance, person_id, name, age, occupation):
  # Create a dictionary with the field-value pairs for the person
  person_data = {
    'name': name,
    'age': age,
    'occupation': occupation
  }

  # Set the field-value pairs in the hash for the specified person_id
  redis_instance.hmset(f'person:{person_id}', person_data)

  return True

r = redis.Redis(
  host='redis-15919.c91.us-east-1-3.ec2.cloud.redislabs.com',
  port=15919,
  password='nVmHZlngfY9h61SwlkrcIsk8VF4ukWe4')
  
# r = redis.Redis(host='localhost', port=6379, db=0)
add_person(r, 1, 'Alice', 25, 'Software Engineer')
add_person(r, 2, 'Bob', 30, 'Data Analyst')
add_person(r, 3, 'Charlie', 40, 'Marketing Manager')

"""### Sample solution"""

import redis

def delete_field(redis_url, hash_name, field_name):
    client = redis.from_url(redis_url)
    client.hdel(hash_name, field_name)

# Example usage
redis_url = 'redis://localhost:6379/0'
hash_name = 'myhash'
field_to_delete = 'field1'
delete_field(redis_url, hash_name, field_to_delete)