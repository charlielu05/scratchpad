from functools import partial

fname = 'input1.stream'

# order added message, message type = 'A', total byte size is 32
order_added = {'symbol': 3,
               'order_id': 8,
               'side': 1,
               'spaces': 3,
               'size': 8,
               'price': 4,
               'spaces_2': 4}

# order updated, message type = 'U', total byte size is 32
order_updated = {'symbol': 3,
                 'order_id': 8,
                 'side': 1,
                 'spaces': 3,
                 'size': 8,
                 'price': 4,
                 'spaces_2': 4}

# order deleted, message type = 'D', total byte size is 16
order_deleted = {'symbol': 3,
                 'order_id': 8,
                 'side': 1,
                 'spaces': 3}

# order executed, message type = 'E', total byte size is 24
order_executed = {'symbol': 3,
                  'order_id': 8,
                  'side': 1,
                  'spaces': 3,
                  'trade_qty': 8}

# map msg type to order length dictionary
msg_mapping = {'A': order_added,
               'U': order_updated,
               'D': order_deleted,
               'E': order_executed}

def byte_to_int(input_byte, signed=False)->int:
    return int.from_bytes(input_byte, byteorder='little', signed=signed)

def byte_to_string(input_byte)->str:
    return input_byte.decode('utf-8')

# decoder mapping for field type
decoder_mapping = {'msg_type': byte_to_string,
                   'symbol': byte_to_string,
                   'order_id': byte_to_int,
                   'side': byte_to_string,
                   'size': byte_to_int,
                   'spaces': byte_to_string,
                   'spaces_2': byte_to_string,
                   'price': partial(byte_to_int, signed=True),
                   'trade_qty': byte_to_int}

def process_message(message_size:int, data:object)->dict:
    # always read first one to determine type of message
    msg_type = data.read(1).decode('utf-8')
    print(f"message type: {msg_type}")
    print(f"message size: {message_size}")

    message_decoder = msg_mapping.get(msg_type)
    
    return {k: decoder_mapping.get(k)(data.read(v)) for k,v in message_decoder.items()} 
    
with open(fname, "rb") as stream:
    message = []
    while True:
        sequence_num = byte_to_int(stream.read(4))
        if sequence_num == 0:
            break
        message_size = byte_to_int(stream.read(4))
        message.append({'sequence': sequence_num,
                        'message_size' : message_size})
        
        message.append(process_message(message_size, stream))
        
