import json


def trim_string(input_string):
    return input_string[7:].strip()


def replace_pipe_with_line_break(input_string):
    return input_string.replace("|", "\n")


def parser_json(response):
    datas = json.loads(response)

    if datas["response"]["body"]["items"] is None:
        return []

    data = datas["response"]["body"]["items"]["item"]
    return_data = []

    for item in data:
        title = item.get("title", "N/A")
        description = item.get("description", "N/A")
        tel = item.get("tel", "N/A")
        address = item.get("address", "N/A")
        charge = item.get("charge", "N/A")
        # 'category1': '반려의료', 'category2': '동물약국', 'category3': None / 3개의 카테고리를 category로 합쳐서 보여줌
        category1 = item.get("category1", " ")
        category2 = item.get("category2", " ")
        category3 = item.get("category3", " ")

        # None을 제외한 문자열만 합치기 "category1, category2"이렇게
        categorys = ""
        if category1 != None and category2 != None:
            categorys += f"{category1}, "
        elif category1 != None and category2 == None:
            categorys += f"{category1}"
        if category2 != None and category3 != None:
            categorys += f"{category2}, "
        elif category2 != None and category3 == None:
            categorys += f"{category2}"
        if category3 != None:
            categorys += f"{category3}"

        return_data.append(
            {
                "title": title,
                "category": categorys,
                "description": replace_pipe_with_line_break(description),
                "tel": tel,
                "address": trim_string(address),
                "charge": charge,
            }
        )

    return return_data
