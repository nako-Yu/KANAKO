import card_tool

while True:
    card_tool.card_menu()
    op = (input("请输入你的选择："))
    if op in["1","2","3"]:
        if op == "1":
            card_tool.card_add()
        elif op == "2":
            card_tool.card_all()
        else:
            card_tool.card_sel()


    elif op == "0":
        break
    else:
        print("输入有错，重新来")
print("！！！拜拜！！！")