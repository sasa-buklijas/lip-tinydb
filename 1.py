
from tinydb import TinyDB

#
# just save dict in DB
#

def main():
    db = TinyDB('./db_1.json')
    data = {'number': 5}
    document_id = db.insert(data)   # every time it will make new document ID
    print(f'{document_id=} {type(document_id)=}')

if __name__ == "__main__":
    main()