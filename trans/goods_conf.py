goods = [
    {
        'id': '0',
        'name': 'Dell Xps 13',
        'price': 5399
    },
    {
        'id': '1',
        'name': 'Apple Data Line',
        'price': 100
    },
    {
        'id': '2',
        'name': 'Iphone X',
        'price': 5899
    },
    {
        'id': '3',
        'name': 'Dog Xiao hua',
        'price': 3000
    },
    {
        'id': '4',
        'name': 'Dog Xiao Jin',
        'price': 4000
    },
    {
        'id': '5',
        'name': 'Cat Miao',
        'price': 2000
    },
    {
        'id': '6',
        'name': 'Cat Haha',
        'price': 1000
    },
    {
        'id': '7',
        'name': 'Diamond',
        'price': 4000
    },
    {
        'id': '8',
        'name': 'Huawei P20',
        'price': 4000
    },
    {
        'id': '9',
        'name': 'Glass Cup',
        'price': 30
    },
    {
        'id': '10',
        'name': 'PC',
        'price': 5000
    },
    {
        'id': '11',
        'name': 'Book A',
        'price': 50
    },
    {
        'id': '12',
        'name': 'Kindle',
        'price': 1200
    },
    {
        'id': '13',
        'name': 'VIP Account',
        'price': 360
    }
]


def encode_goods_idx(own_goods):
    goods_str = ""
    print(own_goods)
    for g in own_goods:
        goods_str += g + " "
    return goods_str

def decode_goods_idx(own_goods_str):
    goods_array = own_goods_str.split(' ')
    goods_array.pop()
    return goods_array
