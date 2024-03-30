import hashlib
import uuid


def get_random_str():
    """获取UUID"""
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()
