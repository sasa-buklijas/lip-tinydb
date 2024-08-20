from random import randint
from tinydb import TinyDB

#
# same as 2.py, but with different abroach
# do not get all db, just record with ID 1
#

def main():
    db = TinyDB('./db_3.json', sort_keys=True, indent=4, separators=(',', ': '))
    data = db.get(doc_id=1)
    print(f'{data=} {type(data)=}')

    if not data:    # if empty
        data = {}   # must make it, because it is None
        data['rn'] = randint(1, 5)
        data['count'] = 0
        db.insert(data)

        data = db.get(doc_id=1) 
        print(f'{data=} {type(data)=}')
    else:
        rn = randint(1, 5)
        print(f'{rn=}')
        
        if rn == data['rn']:
            print(f'We have winner {rn=} after {data['count']} attempts !!!')

            data['rn'] = randint(1, 5)
            data['count'] = 0
            db.update(data, doc_ids=[1])

        else:
            data['count'] += 1
            db.update(data, doc_ids=[1])

if __name__ == "__main__":
    main()