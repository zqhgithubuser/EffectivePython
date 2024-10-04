from datetime import datetime, timedelta


class Bucket:

    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return (f"Bucket(max_quota={self.max_quota}, "
                f"quota_consumed={self.quota_consumed})")

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount  # 消费配额
        if amount == 0:  # 配额重置
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            self.max_quota = amount + self.quota_consumed
        else:
            self.quota_consumed = delta


def fill(bucket, amount):
    now = datetime.now()
    # 超时，配额重置
    if (now - bucket.reset_time) > bucket.period_delta:
        bucket.quota = 0
        bucket.resest_time = now
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    # 超时
    if (now - bucket.reset_time) > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True


bucket = Bucket(60)
print("Initial", bucket)
fill(bucket, 100)
print("Filled", bucket)

if deduct(bucket, 99):
    print("Had 99 quota")
else:
    print("Not enough for 99 quota")
print("Now", bucket)  # Now Bucket(max_quota=100, quota_consumed=99)

if deduct(bucket, 3):
    print("Had 3 quota")
else:
    print("Not enough for 3 quota")
print("Still", bucket)
