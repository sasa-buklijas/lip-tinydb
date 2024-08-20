from random import randint
from tinydb import TinyDB

#
# simulate program that needs to save state between runs
#

def main():
    db = TinyDB('./db_2.json', sort_keys=True, indent=4, separators=(',', ': '))
    data = db.all()
    print(f'{data=} {type(data)=}')

    if not data:    # if empty
        data = {}
        data['rn'] = randint(1, 5)
        data['count'] = 0
        db.insert(data)

        data =db.all()  # .all() always return list
        print(f'{data=}')
    else:
        rn = randint(1, 5)
        print(f'{rn=}')
        
        if rn == data[0]['rn']:
            print(f'We have winner {rn=} after {data[0]['count']} attempts !!!')

            db.truncate()   # remove data
            # generate fresh start
            data = {}
            data['rn'] = randint(1, 5)
            data['count'] = 0
            db.insert(data)

        else:
            data[0]['count'] += 1
            db.truncate()   # remove all
            db.insert(data[0])

if __name__ == "__main__":
    main()