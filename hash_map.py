class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashTable = [[] for _ in range(self.size)]

    def setValue(self, key, value):
        hashedKey = hash(key)%self.size
        bucket = self.hashTable[hashedKey]

        for index , record in enumerate(bucket):
            recordKey, recordValue = record
            if recordKey == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))

    def getValue(self, key):
        hashedKey = hash(key)%self.size
        bucket = self.hashTable[hashedKey]
        for index, record in  enumerate(bucket):
            recordKey, recordValue = record
            if recordKey == key:
                return record

        return "Record Not found"
    
    def __str__(self):
        return str(self.hashTable)

    def deleteValue(self, key):
        hashedKey = hash(key)%self.size
        self.hashTable[hashedKey] = []


hashTable = HashTable(10)
hashTable.setValue("tomdf@mail.com","Tom Avetisyan, 1993, Armenia")
hashTable.setValue("jhondgtr@mail.com","Jhon Frye, 2000, Russian Republic")
print(hashTable)
hashTable.deleteValue("tomdf@mail.com",)
print(hashTable)
