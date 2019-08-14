# -*-coding:utf-8-*-
# Author: key
# Email: admin@gh0st.cn
# Blog: gh0st.cn
# Team: Mystery Security Team

import random
from districtcode import area_dict
from datetime import timedelta, date

# 生成手机号
def genMobile():
    prelist = {"133":"电信","149":"电信","153":"电信","173":"电信","177":"电信","180":"电信","181":"电信","189":"电信","199":"电信","130":"联通","131":"联通","132":"联通","145":"联通","155":"联通","156":"联通","166":"联通","171":"联通","175":"联通","176":"联通","185":"联通","186":"联通","166":"联通","134":"移动","135":"移动","136":"移动","137":"移动","138":"移动","139":"移动","147":"移动","150":"移动","151":"移动","152":"移动","157":"移动","158":"移动","159":"移动","172":"移动","178":"移动","182":"移动","183":"移动","184":"移动","187":"移动","188":"移动","198":"移动"}
    three = list(prelist.keys())[random.randint(0,len(prelist)-1)]
    mobile = three + "".join(random.choice("0123456789") for i in range(8))
    op = prelist[three]
    return {mobile:op}

def first_name():
    first_name_list = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
                '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
                '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
                '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    n = random.randint(0, len(first_name_list) - 1)
    f_name = first_name_list[n]
    return f_name

def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st

def second_name():
    second_name_list = [GBK2312(), '']
    n = random.randint(0, 1)
    s_name = second_name_list[n]
    return s_name

def last_name():
    return GBK2312()

# 生成姓名
def genName():
    name = first_name() + second_name() + last_name()
    return name

# 生成身份证
def genIdCard(age,gender):
    area_code = ('%s' % random.choice(list(area_dict.keys())))
    id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    if str(area_code) not in area_dict.keys():
        return None
    datestring = str(date(date.today().year - age, 1, 1) + timedelta(days=random.randint(0, 364))).replace("-", "")
    rd = random.randint(0, 999)
    if gender == 0:
        gender_num = rd if rd % 2 == 0 else rd + 1
    else:
        gender_num = rd if rd % 2 == 1 else rd - 1
    result = str(area_code) + datestring + str(gender_num).zfill(3)
    b = result + str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in result])]) % 11])
    return b

# 生成组织机构代码
def genOrgCode():
    max = 99999999
    min = 10000000
    num = int((random.random() * (max-min)) + min)
    ws = [3, 7, 9, 10, 5, 8, 4, 2]
    sum = 0
    for i in range(len(ws)):
        sum += int(str(num)[i]) * ws[i]

    C9 = 11 - (sum % 11)
    if (C9 == 11):
        C9 = '0'
    elif (C9 == 10):
        C9 = 'X'
    else:
        C9 = str(C9)
    return str(num) + "-" + C9

# 生成统一社会信用代码
def genCreditCode():
    orgCode = {"1":"机构编制","2":"外交","3":"教育","4":"公安","5":"民政","6":"司法","7":"交通运输","8":"文化","9":"工商","A":"中央军委改革和编制办公室","N":"农业","Y":"其他"}

    icCode = {"1":{"1":"机关","2":"事业单位","3":"中央编办直接管理机构编制的群众团体","9":"其他"},"2":{"1":"外国常驻新闻机构","9":"其他"},"3":{"1":"律师执业机构","2":"公证处","3":"基层法律服务所","4":"司法鉴定机构","5":"仲裁委员会","9":"其他"},"4":{"1":"外国在华文化中心","9":"其他"},"5":{"1":"社会团体","2":"民办非企业单位","3":"基金会","9":"其他"},"6":{"1":"外国旅游部门常驻机构代表机构","2":"港澳台地区旅游部门常驻内地（大陆）代表机构","9":"其他"},"7":{"1":"宗教活动场所","2":"宗教院校","9":"其他"},"8":{"1":"基层工会","9":"其他"},"9":{"1":"企业","2":"个体工商户","3":"农民专业社"},"A":{"1":"军队事业单位","9":"其他"},"N":{"1":"组级集体经济组织","2":"村级集体经济组织","3":"乡镇集体经济组织","9":"其他"},"Y":{"1":"其他"}}
    areas = ['110000', '110101', '110102', '110103', '110104', '110105', '110106', '110107', '110108', '110109', '110111', '110112', '110113', '110114', '110115', '110116', '110117', '110228', '110229', '120000', '120101', '120102', '120103', '120104', '120105', '120106', '120107', '120108', '120109', '120110', '120111', '120112', '120113', '120114', '120115', '120221', '120223', '120225', '130000', '130100', '130102', '130103', '130104', '130105', '130107', '130108', '130121', '130123', '130124', '130125', '130126', '130127', '130128', '130129', '130130', '130131', '130132', '130133', '130181', '130182', '130183', '130184', '130185', '130200', '130202', '130203', '130204', '130205', '130207', '130208', '130223', '130224', '130225', '130227', '130229', '130230', '130281', '130283', '130300', '130302', '130303', '130304', '130321', '130322', '130323', '130324', '130400', '130402', '130403', '130404', '130406', '130421', '130423', '130424', '130425', '130426', '130427', '130428', '130429', '130430']
    regOrg = list(orgCode.keys())[random.randint(0,len(orgCode)-1)]
    orgtype = list(icCode[regOrg].keys())[random.randint(0,len(icCode[regOrg].keys())-1)]
    ot = icCode[regOrg][orgtype]
    num = int(random.random() * 99)
    area = areas[num]
    num = int(((random.random() * (99999999 - 10000000)) + 10000000))
    ws = [3, 7, 9, 10, 5, 8, 4, 2]
    sum = 0
    for i in range(len(ws)):
        sum += int(str(num)[i]) * ws[i]
    
    C9 = 11 - (sum % 11)
    if (C9 == 11):
        C9 = '0'
    elif (C9 == 10):
        C9 = 'X'
    else:
        C9 = str(C9)
    orgCode = str(num) + C9
    code = regOrg + orgtype + area + orgCode
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wi = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]
    sum = 0
    for i in range(len(wi)):
        sum += s.find(code[i]) * wi[i]
    C18 = 31 - (sum % 31)
    if (C18 == 31):
        C18 = '0'
    else:
        C18 = s[C18:C18+1]
    return {code+C18:ot}

if __name__ == '__main__':
    age = random.randint(16,60) #可调整生成的年龄范围（身份证），这边是16-60岁
    gender = random.randint(0,1)
    sex = u"男" if gender == 1 else u"女"
    print("姓名: {0}\n年龄: {1}\n性别: {2}\n身份证: {3}\n手机号: {4} {5}\n组织机构代码: {6}\n统一社会信用代码: {7}\n单位性质: {8}".format(genName(), age, sex, genIdCard(age, gender), list(genMobile().keys())[0], list(genMobile().values())[0], genOrgCode(), list(genCreditCode().keys())[0], list(genCreditCode().values())[0]))