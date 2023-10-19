def card_menu():
    print('\n\n')
    print("*"*50)
    print("--------------!!!欢迎使用这个好东西!!!---------------")
    print("1、 新建")
    print("2、 显示全部")
    print("3、 查询")
    print("0、 退出")
    print("*" * 50)


card_list = []


def card_add():
    """
    添加人员时，先判断是否存在
    :return:
    """
    nd = {}
    for key in ("name", "phone", "qq", "email"):
        values = input("请输入{}:".format(key))
        nd[key] = values
        name_exists = False
    for item in card_list:
        if item["name"] == nd["name"]:
            name_exists = True
            print('\n\n',"！！！！有相同的名字了,请重新添加！！！！")
            break
    if not name_exists:
        card_list.append(nd)
    # TODO 没能明白为什么我这个代码和老师的不一样 数据没存会重置。。


def card_all():
    if len(card_list) <= 0:
        return print('\n\n',"！！！！还没人呢，赶紧去添加吧。。。！！！！")

    print("显示所有名片:")
    print("_" * 50)
    print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮箱".ljust(10),sep='\t\t')
    print("_" * 50)
    for item in card_list:
        print(item.get("name").ljust(10), item.get("phone").ljust(10), item.get("qq").ljust(10), item.get("email").ljust(10),sep='\t\t')
        print("_" * 50)


def card_sel():
    """
    查找人员，
    :return:
    """
    name = input("请输入你要查询人的名字")
    for item in card_list:
        if name == item.get("name"):
            print("{}的信息是：".format(name))
            print("_" * 50)
            print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮箱".ljust(10),sep='\t\t')
            print("_" * 50)
            print(item.get("name").ljust(10), item.get("phone").ljust(10), item.get("qq").ljust(10), item.get("email").ljust(10),sep='\t\t')
            print("_" * 50)
            print("")
            card_deal(item)
            break

    else:print('\n\n', "！！！！查无此人！！！！")


def card_deal(find_dict):
    """

    :param find_dict:
    :return:
    """
    op = input("请输入你要干嘛：【1、修改   2、删除    0、返回上级】")
    if op == "1":
        print("【功能】：修改名片")
        find_dict["name"] = input_no_enter(find_dict["name"], input("请输入修改后的姓名：[不修改直接回车]"))
        find_dict["phone"] = input_no_enter(find_dict["phone"], input("请输入修改后的电话：[不修改直接回车]"))
        find_dict["qq"] = input_no_enter(find_dict["qq"], input("请输入修改后的QQ号：[不修改直接回车]"))
        find_dict["email"] = input_no_enter(find_dict["email"], input("请输入修改后的邮箱：[不修改直接回车]"))
        card_all()

    elif op == "2":
        op1 = input("确定要删除 {} 的信息？,确定输入‘1’,取消输入‘0 ’： ".format(find_dict["name"]))
        if op1 == "1":
            card_list.remove(find_dict)
            print('\n\n',"!!! 删除成功  !!!")
        elif op1 == "0":
            return
        else:print("输入有误，重新输入")
    elif op == "0":
        print("【功能】：返回上级")
        return
    else:
        print("输入有误，重新输入")

def input_no_enter(dict_value,msg):
    """

    :param dict_value: 所在键的值
    :param msg: 输入的信息
    :return: 输入的有内容就返回输入的msg，没内容就返回原来的dict_value
    """

    info = input(msg)
    if len(info) > 0:
        return msg
    else:
        return dict_value