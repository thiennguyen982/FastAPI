import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    client.subscribe("Test/#")
    
def on_message(client, userdata, msg):
    print(str(msg.payload))
    
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("m14.cloudmqtt.com", 18410, 60)
client.username_pw_set("<<Username>>", "<<Password>>")

client.loop_forever()

import asyncio
import boto3
import json
import time
from asyncua import Client
from pydantic import BaseModel, Field
from typing import List

# OPC UA server endpoint with credentials embedded in the URI
uri_creds = "opc.tcp://foobar:hR%26yjjGhP%246%40nQ4e@127.0.0.1:48517/baz/server"
node_id = "ns=2;i=2"  # Update this with the correct Node ID

# AWS S3 Configuration
s3_bucket_name = "your-s3-bucket-name"
s3_file_name = "opcua_data.json"  # Update this with your desired file name

# Initialize S3 client
s3_client = boto3.client('s3')


# Pydantic model for individual data points
class DataPoint(BaseModel):
    timestamp: float = Field(..., description="The time the data was recorded")
    value: float = Field(..., description="The value read from the OPC UA server")


# Pydantic model for the payload
class DataPayload(BaseModel):
    start_time: float = Field(..., description="Start time of the data collection window")
    end_time: float = Field(..., description="End time of the data collection window")
    data: List[DataPoint] = Field(..., description="List of data points collected")


async def read_data_in_time_window():
    client = Client(uri_creds)
    try:
        await client.connect()
        print(f"Connected to OPC UA Server: {client.server_url.geturl()}")

        node = client.get_node(node_id)
        data_list = []

        while True:
            # Start time for the 10-second window
            start_time = time.time()

            # Collect data for 10 seconds
            while time.time() - start_time < 10:
                # Read the value from the node
                data_value = await node.read_value()
                timestamp = time.time()

                # Create a DataPoint instance
                data_point = DataPoint(timestamp=timestamp, value=data_value)
                data_list.append(data_point)

                # Sleep for a short time to avoid overwhelming the server
                await asyncio.sleep(0.5)

            # End time for the 10-second window
            end_time = time.time()

            # Create a DataPayload instance and push the data to S3
            payload = DataPayload(start_time=start_time, end_time=end_time, data=data_list)
            await push_data_to_s3(payload)

            # Clear the list for the next window
            data_list = []

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        await client.disconnect()
        print("Disconnected from OPC UA Server")


async def push_data_to_s3(payload: DataPayload):
    try:
        # Convert payload to JSON
        json_data = payload.json()

        # Upload to S3
        s3_client.put_object(Bucket=s3_bucket_name, Key=s3_file_name, Body=json_data)
        print(f"Data successfully pushed to S3 bucket {s3_bucket_name} as {s3_file_name}")

    except Exception as e:
        print(f"Failed to upload data to S3: {e}")


if __name__ == "__main__":
    asyncio.run(read_data_in_time_window())